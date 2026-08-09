"""
conservation_analysis.py

Residue-level evolutionary conservation analysis for mammalian TP53.

Purpose
-------
Calculates residue-level conservation metrics from a multiple sequence
alignment and produces an analysis-ready conservation table.

Inputs
------
- Protein multiple sequence alignment in FASTA format.

Outputs
-------
- Residue-level conservation table.

Author
------
Ritika Rajendra Rawat
"""

from pathlib import Path
from collections import Counter
import math
import pandas as pd


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

ALIGNMENT_FILE = Path(
    "data/processed/TP53_curated.fasta"
)

OUTPUT_FILE = Path(
    "data/processed/residue_conservation.csv"
)


# ---------------------------------------------------------------------
# FASTA parser
# ---------------------------------------------------------------------

def read_fasta(path):
    """
    Read a protein FASTA file.

    Returns
    -------
    dict
        Mapping of sequence identifiers to sequences.
    """

    sequences = {}
    current_id = None
    current_sequence = []

    with open(path, "r", encoding="utf-8") as handle:

        for line in handle:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):

                if current_id is not None:
                    sequences[current_id] = "".join(current_sequence)

                current_id = line[1:].split()[0]
                current_sequence = []

            else:
                current_sequence.append(line)

    if current_id is not None:
        sequences[current_id] = "".join(current_sequence)

    return sequences


# ---------------------------------------------------------------------
# Conservation functions
# ---------------------------------------------------------------------

def calculate_entropy(residues):
    """
    Calculate Shannon entropy for a residue column.

    Gap characters are excluded.

    Returns
    -------
    float
        Shannon entropy.
    """

    residues = [
        residue
        for residue in residues
        if residue not in {"-", "."}
    ]

    if not residues:
        return float("nan")

    counts = Counter(residues)
    total = len(residues)

    entropy = 0.0

    for count in counts.values():

        probability = count / total

        entropy -= probability * math.log2(probability)

    return entropy


def calculate_conservation(sequences):
    """
    Calculate residue-level conservation metrics.

    Returns
    -------
    pandas.DataFrame
    """

    sequence_ids = list(sequences.keys())

    sequence_lengths = {
        sequence_id: len(sequence)
        for sequence_id, sequence in sequences.items()
    }

    alignment_length = max(sequence_lengths.values())

    rows = []

    for position in range(alignment_length):

        residues = []

        for sequence_id in sequence_ids:

            sequence = sequences[sequence_id]

            if position < len(sequence):
                residue = sequence[position]
            else:
                residue = "-"

            residues.append(residue)

        ungapped = [
            residue
            for residue in residues
            if residue not in {"-", "."}
        ]

        if not ungapped:
            continue

        counts = Counter(ungapped)

        majority_residue, majority_count = counts.most_common(1)[0]

        conservation = majority_count / len(ungapped)

        entropy = calculate_entropy(residues)

        human_residue = residues[0]

        human_residue_frequency = (
            counts.get(human_residue, 0) / len(ungapped)
            if human_residue not in {"-", "."}
            else float("nan")
        )

        rows.append(
            {
                "alignment_position": position + 1,
                "human_residue": human_residue,
                "majority_residue": majority_residue,
                "conservation": conservation,
                "human_residue_frequency": human_residue_frequency,
                "entropy": entropy,
                "n_sequences": len(ungapped),
            }
        )

    return pd.DataFrame(rows)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main():

    print("Loading TP53 alignment...")

    sequences = read_fasta(ALIGNMENT_FILE)

    if not sequences:
        raise ValueError(
            "No sequences were found in the alignment."
        )

    print(f"Loaded {len(sequences)} sequences.")

    results = calculate_conservation(sequences)

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    results.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Conservation analysis completed: "
        f"{OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
