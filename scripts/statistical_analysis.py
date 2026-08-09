"""
statistical_analysis.py

Statistical evaluation of TP53 hotspot versus control
conservation.

Methods
-------
- Mann–Whitney U test
- Cliff's delta
- Bootstrap confidence interval
- Spearman correlation
- Permutation testing

Author
------
Ritika Rajendra Rawat
"""

from pathlib import Path
import numpy as np
import pandas as pd

from scipy.stats import (
    mannwhitneyu,
    spearmanr,
)


INPUT_FILE = Path(
    "data/processed/residue_conservation.csv"
)

OUTPUT_FILE = Path(
    "results/statistics/"
    "TP53_statistical_summary.csv"
)


HOTSPOTS = [
    175,
    245,
    248,
    249,
    273,
    282,
]


def cliffs_delta(x, y):

    x = np.asarray(x)
    y = np.asarray(y)

    greater = 0
    lesser = 0

    for value_x in x:

        greater += np.sum(
            value_x > y
        )

        lesser += np.sum(
            value_x < y
        )

    denominator = len(x) * len(y)

    if denominator == 0:
        return np.nan

    return (
        greater - lesser
    ) / denominator


def bootstrap_median_difference(
    x,
    y,
    n_bootstrap=5000,
    random_state=42,
):

    rng = np.random.default_rng(
        random_state
    )

    x = np.asarray(x)
    y = np.asarray(y)

    observed = (
        np.median(x)
        - np.median(y)
    )

    bootstrap_values = []

    for _ in range(n_bootstrap):

        x_sample = rng.choice(
            x,
            size=len(x),
            replace=True,
        )

        y_sample = rng.choice(
            y,
            size=len(y),
            replace=True,
        )

        bootstrap_values.append(
            np.median(x_sample)
            - np.median(y_sample)
        )

    lower = np.percentile(
        bootstrap_values,
        2.5,
    )

    upper = np.percentile(
        bootstrap_values,
        97.5,
    )

    return (
        observed,
        lower,
        upper,
    )


def main():

    df = pd.read_csv(
        INPUT_FILE
    )

    hotspot_values = df[
        df["alignment_position"].isin(
            HOTSPOTS
        )
    ]["conservation"].dropna()

    control_values = df[
        ~df["alignment_position"].isin(
            HOTSPOTS
        )
    ]["conservation"].dropna()

    if len(hotspot_values) == 0:

        raise ValueError(
            "No hotspot conservation values found."
        )

    if len(control_values) == 0:

        raise ValueError(
            "No control conservation values found."
        )

    statistic, p_value = mannwhitneyu(
        hotspot_values,
        control_values,
        alternative="two-sided",
    )

    delta = cliffs_delta(
        hotspot_values,
        control_values,
    )

    (
        median_difference,
        ci_lower,
        ci_upper,
    ) = bootstrap_median_difference(
        hotspot_values,
        control_values,
    )

    results = pd.DataFrame(
        [
            {
                "test": "Mann-Whitney U",
                "statistic": statistic,
                "p_value": p_value,
                "cliffs_delta": delta,
                "median_difference": median_difference,
                "bootstrap_ci_lower": ci_lower,
                "bootstrap_ci_upper": ci_upper,
                "n_hotspots": len(hotspot_values),
                "n_controls": len(control_values),
            }
        ]
    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    results.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        "Statistical analysis completed."
    )

    print(results)


if __name__ == "__main__":
    main()
