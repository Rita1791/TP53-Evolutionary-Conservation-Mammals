# 🧬 Processed Data

> **Analysis-ready datasets generated from the curated TP53 sequence, mutation, species, and structural resources used in this study.**

The `processed/` directory contains **derived computational resources** produced after data curation and preprocessing. These files form the bridge between the raw biological inputs in [`data/raw/`](../raw/) and the statistical analyses, visualizations, phylogenetic analyses, and biological interpretations reported in the repository.

---

## 🧭 Role in the Research Workflow

```text
                    🌐 PUBLIC RESOURCES
                           │
                           ▼
                     📥 data/raw/
                           │
                           ▼
                  🧹 CURATION & QC
                           │
                           ▼
                  🧬 data/processed/
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Conservation      Hotspot/control   Structural
      datasets            mapping         annotation
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    📊 STATISTICAL
                       ANALYSIS
                           │
                           ▼
                    🌳 PHYLOGENETIC
                       ANALYSIS
                           │
                           ▼
                       RESULTS
