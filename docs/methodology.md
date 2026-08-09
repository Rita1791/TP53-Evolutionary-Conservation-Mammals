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
