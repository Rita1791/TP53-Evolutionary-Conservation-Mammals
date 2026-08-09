# 💻 Computational Scripts

> **Analysis modules implementing the computational workflow for evaluating TP53 evolutionary conservation, recurrent cancer-associated hotspots, mutation patterns, and phylogenetic context across mammals.**

The `scripts/` directory contains the computational layer of the repository.

The overall philosophy is:

```text
                 Biological Question
                         │
                         ▼
                  Input Datasets
                         │
                         ▼
                Computational Scripts
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     Conservation     Hotspots       Mutation
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                    Statistics
                         │
                         ▼
                    Phylogeny
                         │
                         ▼
                  Derived Results
                         │
                         ▼
                 Figures / Manuscript
