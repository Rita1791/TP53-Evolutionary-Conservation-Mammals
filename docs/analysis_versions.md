# Analysis versions and manuscript reconciliation

## Why this file exists

The associated preprint and the current repository do not represent an
identical analytical snapshot. Without an explicit version record, a reviewer
cannot determine which dataset generated which claim.

## Version map

| Version | Dataset | Purpose | Status |
|---|---|---|---|
| Preprint v1 | 10-species analysis described in the submitted manuscript | Published research communication | Frozen; do not overwrite |
| Repository v1.0 | Expanded 56-sequence mammalian analysis | Reproducible extension and sensitivity work | Canonical repository release after CI passes |

## Interpretation rule

Results from the 56-sequence analysis are an extension, not retroactive
evidence for every number in preprint v1. When the two versions differ, report
both and explain the methodological or dataset reason.

## Required provenance for repository v1.0

- input FASTA checksum;
- full accession/species table;
- MAFFT version and command;
- human reference accession and length;
- gap-handling and conservation formulas;
- canonical hotspot definition;
- cBioPortal query/export provenance;
- permutation seed, iterations and background definition;
- IQ-TREE version, model and command;
- tested Git commit and release tag.

## Release checklist

Before tagging v1.0.0:

1. Regenerate alignment and all dependent tables.
2. Confirm the six human reference residues.
3. Confirm README values match the regenerated CSV.
4. Confirm `git diff --exit-code -- data/processed results` passes after a
   second clean run.
5. Record any difference from preprint v1 in the release notes.

