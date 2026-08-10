#!/usr/bin/env python3
"""Extract and validate canonical human TP53 hotspot conservation values."""

from pathlib import Path

import pandas as pd


INPUT = Path("data/processed/residue_conservation.csv")
OUTPUT = Path("results/hotspot_analysis/canonical_hotspot_conservation.csv")
HOTSPOTS = {175: "R", 245: "G", 248: "R", 249: "R", 273: "R", 282: "R"}


def extract_hotspots(frame: pd.DataFrame) -> pd.DataFrame:
    required = {"human_position", "human_residue", "human_residue_conservation"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    result = frame[frame["human_position"].isin(HOTSPOTS)].copy()
    result = result.sort_values("human_position")

    observed = dict(zip(result["human_position"].astype(int), result["human_residue"]))
    if observed != HOTSPOTS:
        raise ValueError(f"Hotspot residue mismatch: expected {HOTSPOTS}, got {observed}")
    if len(result) != len(HOTSPOTS):
        raise ValueError("Not all canonical hotspots were found exactly once")

    result.insert(0, "hotspot_label", [f"{HOTSPOTS[p]}{p}" for p in result["human_position"]])
    return result


def main() -> None:
    result = extract_hotspots(pd.read_csv(INPUT))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(OUTPUT, index=False)
    print(result[["hotspot_label", "human_residue_conservation"]].to_string(index=False))
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()

