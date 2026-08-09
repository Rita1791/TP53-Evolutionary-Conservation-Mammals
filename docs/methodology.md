# 🔬 Methodology

> **A reproducible computational framework for evaluating evolutionary conservation and functional constraint at recurrent human TP53 cancer mutation hotspots across mammalian species.**

---

## 🧭 1. Methodological Overview

This repository implements a comparative evolutionary bioinformatics workflow designed to investigate whether recurrent human TP53 cancer mutation hotspots occur at residues that are unusually constrained across mammalian evolution.

The study integrates four complementary evidence layers:

1. 🧬 **Mammalian TP53 sequence conservation**
2. 🎯 **Recurrent human TP53 cancer mutation positions**
3. 📊 **Statistical comparison of hotspot and matched control residues**
4. 🌳 **Phylogenetic and structural context**

The central analytical question is:

> **Do recurrent human TP53 cancer mutation hotspots occupy evolutionarily constrained residues across mammals?**

Rather than treating mutation recurrence and evolutionary conservation as independent observations, the workflow places both on the same residue-level coordinate system.

---

# 🧠 2. Conceptual Framework

The complete analytical logic can be summarized as:

```text
                    HUMAN TP53
                        │
                        ▼
             Recurrent cancer hotspots
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
      Mammalian TP53          Human cancer
        sequences             mutation data
             │                     │
             ▼                     ▼
       Sequence curation      Mutation mapping
             │                     │
             └──────────┬──────────┘
                        ▼
              Multiple sequence
                   alignment
                        │
                        ▼
              Residue-level mapping
                        │
             ┌──────────┼──────────┐
             │          │          │
             ▼          ▼          ▼
        Conservation  Statistics  Phylogeny
             │          │          │
             └──────────┼──────────┘
                        ▼
               Structural context
                        │
                        ▼
             Integrated interpretation
                        │
                        ▼
              Evolutionary constraint


# 🧠 3. Complete Workflow

The complete analytical logic can be summarized as:

```text

                     ┌─────────────────────┐
                     │  PUBLIC RESOURCES   │
                     │ NCBI / UniProt /    │
                     │ cBioPortal / TCGA   │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │  DATA CURATION      │
                     │  56 mammalian TP53  │
                     │      sequences       │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │       MAFFT         │
                     │ Multiple Sequence   │
                     │      Alignment      │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ RESIDUE-LEVEL       │
                     │ CONSERVATION        │
                     └──────────┬──────────┘
                                │
             ┌──────────────────┼──────────────────┐
             │                  │                  │
             ▼                  ▼                  ▼
      Canonical hotspots   DBD controls      Mutation data
       R175/G245/R248       matched set      TCGA/cBioPortal
       R249/R273/R282
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ▼
                     ┌─────────────────────┐
                     │ STATISTICAL TESTING │
                     │ Mann–Whitney        │
                     │ Cliff's delta       │
                     │ Bootstrap           │
                     │ Permutation         │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ MUTATION–           │
                     │ CONSERVATION        │
                     │ ASSOCIATION         │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │     IQ-TREE         │
                     │ Phylogenetic        │
                     │ reconstruction      │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ PHYLOGENETIC        │
                     │ SENSITIVITY         │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ STRUCTURAL CONTEXT  │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │ BIOLOGICAL          │
                     │ INTERPRETATION      │
                     └─────────────────────┘

🧬 4. From Sequence → Constraint → Mutation → Evolution → Hypothesis

Mammalian TP53 sequences
          ↓
      Alignment
          ↓
Residue conservation
          ↓
Human cancer hotspots
          ↓
Domain-matched comparison
          ↓
Statistical validation
          ↓
Mutation recurrence
          ↓
Phylogenetic robustness
          ↓
Structural interpretation
          ↓
Reproducible biological hypothesis
