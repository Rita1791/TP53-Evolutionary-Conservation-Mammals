from scripts.conservation_analysis import (
    calculate_conservation,
    identify_human,
    shannon_entropy,
)


def test_human_coordinates_ignore_human_alignment_gaps():
    records = {
        "NP_001394193|Homo_sapiens": "AR-G",
        "example_mammal": "AKTG",
    }
    frame = calculate_conservation(
        records,
        "NP_001394193|Homo_sapiens",
        validate_hotspots=False,
    )

    assert frame["human_position"].tolist() == [1, 2, 3]
    assert frame["alignment_position"].tolist() == [1, 2, 4]
    assert frame["human_residue"].tolist() == ["A", "R", "G"]


def test_human_record_is_identified_by_accession():
    records = {
        "other": "AAAA",
        "NP_001394193|Homo_sapiens": "AAAA",
    }
    assert identify_human(records) == "NP_001394193|Homo_sapiens"


def test_entropy_is_zero_for_invariant_column():
    assert shannon_entropy(["R", "R", "R", "-"]) == 0.0
