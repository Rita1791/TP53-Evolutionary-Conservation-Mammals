# 🧬 Data

> **Data architecture for the comparative evolutionary analysis of TP53 across mammals.**

This directory separates the biological resources used as **inputs** from datasets produced through **curation and computational processing**.

```text
                         DATA LAYER
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
          data/raw/                   data/processed/
        Source resources             Analysis-ready data
              │                             │
              └──────────────┬──────────────┘
                             ▼
                    Comparative analysis
                             │
                             ▼
                         results/
