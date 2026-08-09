# Methodology

> **Computational framework for investigating evolutionary conservation, mutation hotspots, and functional constraint in mammalian TP53.**

---

## 🧬 1. Study Overview

This repository contains the computational framework developed to investigate the evolutionary conservation of **TP53** across mammalian species and to examine whether recurrent human cancer-associated mutation sites occur within evolutionarily constrained regions of the protein.

The central hypothesis is:

> **If recurrent human TP53 mutation hotspots occur at functionally important residues, those residues may exhibit stronger evolutionary conservation across mammals than surrounding non-hotspot positions.**

The analysis therefore connects three complementary biological dimensions:

```text
                 🧬 MAMMALIAN TP53 SEQUENCES
                            │
                            ▼
                  🔎 SEQUENCE CURATION
                            │
                            ▼
                  🧩 MULTIPLE SEQUENCE
                      ALIGNMENT
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
       Conservation      Mutation       Phylogenetic
         Analysis         Mapping          Analysis
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                  🔬 INTEGRATED ANALYSIS
                            │
                            ▼
                🧠 FUNCTIONAL INTERPRETATION
