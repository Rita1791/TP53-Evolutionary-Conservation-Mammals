# Reviewer summary

## Question

Are recurrent human TP53 cancer-mutation hotspots unusually conserved across a
curated mammalian sequence dataset relative to a DNA-binding-domain background?

## Dataset and coordinate system

- Expanded repository analysis: 56 mammalian TP53 sequences.
- Canonical human reference: `NP_001394193` (393 amino acids).
- Human positions are mapped through the multiple-sequence alignment.
- Canonical hotspots: R175, G245, R248, R249, R273 and R282.

## Canonical execution path

```bash
conda env create -f environment.yml
conda activate tp53_mammals
bash scripts/run_pipeline.sh
pytest -q
```

The run creates a committed MAFFT alignment, residue-level conservation table,
hotspot table, mutation-conservation join and seeded permutation results.

## Main evidence

- `data/processed/TP53_aligned.fasta`
- `data/processed/residue_conservation.csv`
- `results/hotspot_analysis/canonical_hotspot_conservation.csv`
- `results/statistics/permutation_hotspot_statistics.csv`
- `results/phylogeny/TP53_mammals.treefile`

## Statistical interpretation

The permutation tests ask whether the mean conservation of specified recurrent
mutation sets is at least as high as size-matched samples from the TP53
DNA-binding-domain background. The seed and iteration count are stored with
every result. P-values are empirical and one-sided.

## Critical limitations

- Species are phylogenetically related and therefore not independent samples.
- The result depends on sequence and isoform selection, alignment, human
  coordinate mapping, gap handling and background definition.
- High conservation does not establish a causal reason for mutation recurrence.
- Sequence conservation is not clinical, therapeutic or experimental evidence.

## Associated outputs

The associated Research Square preprint is a narrower study version. The
expanded repository analysis must not silently replace the data or results of
that preprint. See `docs/analysis_versions.md`.

