"""
mutation_analysis.py

Integrates human TP53 cancer mutation-frequency data
with residue-level evolutionary conservation.

Author
------
Ritika Rajendra Rawat
"""

from pathlib import Path
import pandas as pd


MUTATION_FILE = Path(
    "data/raw/cbioportal_mutation_frequency_by_codon.csv"
)

CONSERVATION_FILE = Path(
    "data/processed/residue_conservation.csv"
)

OUTPUT_FILE = Path(
    "results/mutation_analysis/"
    "TP53_mutation_conservation_integrated.csv"
)


def load_data():

    if not MUTATION_FILE.exists():

        raise FileNotFoundError(
            f"Mutation dataset not found: "
            f"{MUTATION_FILE}"
        )

    if not CONSERVATION_FILE.exists():

        raise FileNotFoundError(
            f"Conservation dataset not found: "
            f"{CONSERVATION_FILE}"
        )

    mutation_data = pd.read_csv(
        MUTATION_FILE
    )

    conservation_data = pd.read_csv(
        CONSERVATION_FILE
    )

    return mutation_data, conservation_data


def identify_position_column(df):

    possible_columns = [
        "position",
        "codon",
        "residue_position",
        "aa_position",
        "alignment_position",
    ]

    for column in possible_columns:

        if column in df.columns:
            return column

    raise ValueError(
        "Could not identify a residue-position "
        "column in the mutation dataset."
    )


def integrate_data(
    mutation_data,
    conservation_data
):

    mutation_position = identify_position_column(
        mutation_data
    )

    mutation_data = mutation_data.copy()

    mutation_data[
        "analysis_position"
    ] = pd.to_numeric(
        mutation_data[mutation_position],
        errors="coerce"
    )

    conservation_data = conservation_data.copy()

    conservation_data[
        "analysis_position"
    ] = pd.to_numeric(
        conservation_data[
            "alignment_position"
        ],
        errors="coerce"
    )

    merged = conservation_data.merge(
        mutation_data,
        on="analysis_position",
        how="left",
        suffixes=(
            "_conservation",
            "_mutation"
        ),
    )

    return merged


def main():

    mutation_data, conservation_data = load_data()

    integrated = integrate_data(
        mutation_data,
        conservation_data
    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    integrated.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        "Mutation/conservation integration completed."
    )

    print(
        f"Output: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
