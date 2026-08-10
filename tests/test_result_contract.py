from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
CONSERVATION = ROOT / "data" / "processed" / "residue_conservation.csv"
PERMUTATION = ROOT / "results" / "statistics" / "permutation_hotspot_statistics.csv"
HOTSPOTS = {175: "R", 245: "G", 248: "R", 249: "R", 273: "R", 282: "R"}


def test_conservation_table_uses_unique_human_coordinates():
    frame = pd.read_csv(CONSERVATION)
    required = {
        "human_position",
        "human_residue",
        "human_residue_conservation",
        "shannon_entropy",
        "domain",
    }
    assert required <= set(frame.columns)
    assert not frame["human_position"].duplicated().any()
    assert frame["human_residue_conservation"].between(0, 1).all()


def test_canonical_hotspot_residues_match_human_reference():
    frame = pd.read_csv(CONSERVATION).set_index("human_position")
    observed = {position: frame.loc[position, "human_residue"] for position in HOTSPOTS}
    assert observed == HOTSPOTS


def test_permutation_output_records_seed_and_iterations():
    frame = pd.read_csv(PERMUTATION)
    assert set(frame["comparison"]) == {
        "canonical_6_vs_DBD_permutation",
        "top10_mutated_codons_vs_DBD_permutation",
        "top20_mutated_codons_vs_DBD_permutation",
        "top30_mutated_codons_vs_DBD_permutation",
    }
    assert (frame["iterations"] >= 1000).all()
    assert frame["seed"].notna().all()
    assert frame["empirical_p_one_sided"].between(0, 1).all()

