#!/usr/bin/env python3
"""Deterministic one-sided permutation tests against the TP53 DBD background."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


CANONICAL = [175, 245, 248, 249, 273, 282]


def empirical_test(
    query_positions: list[int],
    conservation: pd.DataFrame,
    iterations: int,
    seed: int,
) -> dict[str, float | int]:
    indexed = conservation.set_index("human_position")
    dbd = conservation[conservation["domain"] == "DNA_binding_domain"]
    dbd_positions = set(dbd["human_position"].astype(int))
    query = [
        position
        for position in query_positions
        if position in indexed.index and position in dbd_positions
    ]
    values = dbd["human_residue_conservation"].dropna().to_numpy(float)

    if not query:
        raise ValueError("No query positions were present in the conservation table")
    if len(query) > len(values):
        raise ValueError("Query is larger than the DBD sampling background")

    observed = float(indexed.loc[query, "human_residue_conservation"].mean())
    rng = np.random.default_rng(seed)
    null = np.empty(iterations, dtype=float)
    for index in range(iterations):
        null[index] = rng.choice(values, size=len(query), replace=False).mean()

    exceedances = int(np.count_nonzero(null >= observed))
    return {
        "n_query": len(query),
        "observed_mean_conservation": observed,
        "null_mean_conservation": float(null.mean()),
        "null_2.5_percentile": float(np.quantile(null, 0.025)),
        "null_97.5_percentile": float(np.quantile(null, 0.975)),
        "empirical_p_one_sided": (exceedances + 1) / (iterations + 1),
        "iterations": iterations,
        "seed": seed,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--conservation", type=Path, default=Path("data/processed/residue_conservation.csv"))
    parser.add_argument("--mutations", type=Path, default=Path("data/raw/cbioportal_mutation_frequency_by_codon.csv"))
    parser.add_argument("--output", type=Path, default=Path("results/statistics/permutation_hotspot_statistics.csv"))
    parser.add_argument("--iterations", type=int, default=100000)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.iterations < 1000:
        raise ValueError("Use at least 1,000 iterations")

    conservation = pd.read_csv(args.conservation)
    mutations = pd.read_csv(args.mutations)
    mutations["codon"] = pd.to_numeric(mutations["codon"], errors="coerce")
    mutations = mutations.dropna(subset=["codon"]).sort_values("hotspot_rank")
    ranked = mutations["codon"].astype(int).tolist()

    comparisons = {
        "canonical_6_vs_DBD_permutation": CANONICAL,
        "top10_mutated_codons_vs_DBD_permutation": ranked[:10],
        "top20_mutated_codons_vs_DBD_permutation": ranked[:20],
        "top30_mutated_codons_vs_DBD_permutation": ranked[:30],
    }

    rows = []
    for offset, (name, positions) in enumerate(comparisons.items()):
        row = empirical_test(positions, conservation, args.iterations, args.seed + offset)
        rows.append({"comparison": name, **row})

    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(args.output, index=False)
    print(pd.DataFrame(rows).to_string(index=False))
    print(f"Output: {args.output}")


if __name__ == "__main__":
    main()
