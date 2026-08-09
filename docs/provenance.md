# 🔎 Data Provenance & Dataset Curation

> **A traceable record of the biological resources, accession-level information, curation decisions, and external datasets used in the mammalian TP53 evolutionary-conservation analysis.**

---

## 🧭 1. Purpose

This document describes the provenance of the datasets used throughout the **TP53 Evolutionary Conservation Across Mammals** project.

The purpose of maintaining an explicit provenance record is to ensure that every major computational input can be traced from:

```text
Public biological resource
        ↓
Source record / accession
        ↓
Sequence or dataset retrieval
        ↓
Curation
        ↓
Analysis-ready dataset
        ↓
Computational analysis
        ↓
Results
        ↓
Figures / manuscript
````

The repository therefore treats provenance as part of the scientific evidence rather than as administrative metadata.

---

# 🧬 2. Study Data Architecture

The repository separates biological inputs into three principal layers:

```text
┌─────────────────────────────────────────────┐
│                 RAW SOURCES                 │
│                                             │
│ Public databases, reference structures,     │
│ cancer mutation resources and metadata      │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              PROCESSED DATA                 │
│                                             │
│ Curated sequences, accession audits,        │
│ conservation tables and derived datasets    │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│                  RESULTS                    │
│                                             │
│ Statistical outputs, hotspot analyses,      │
│ mutation analyses and phylogenetic files    │
└─────────────────────────────────────────────┘
```

This distinction is intentional:

> **Raw data are inputs. Processed data are transformed analytical resources. Results are outputs generated from those resources.**

---

# 🧬 3. Human TP53 Reference

The human TP53 protein is the reference coordinate system for the comparative analysis.

| Property          | Reference                   |
| ----------------- | --------------------------- |
| Gene              | **TP53**                    |
| Protein           | Cellular tumour antigen p53 |
| Species           | *Homo sapiens*              |
| UniProt accession | **P04637**                  |
| Protein length    | **393 amino acids**         |

The human reference sequence establishes the residue numbering used throughout the hotspot and conservation analyses.

This is particularly important for recurrent cancer-associated positions such as:

```text
R175
G245
R248
R249
R273
R282
```

These positions are interpreted according to the human TP53 reference sequence rather than raw alignment-column numbers.

---

# 🗃️ 4. Primary Sequence Resource

The comparative analysis uses a curated mammalian TP53 protein dataset containing:

> **56 mammalian TP53 sequences**

The analysis-ready FASTA resource is stored at:

```text
data/processed/TP53_curated.fasta
```

This file represents the curated sequence collection used for downstream comparative analysis.

The corresponding accession-level audit is stored at:

```text
data/processed/TP53_sequence_accession_audit.csv
```

The audit provides a traceable relationship between the analyzed sequences and their source identifiers.

---

# 🌍 5. Sequence Database Sources

Mammalian TP53 sequence information was obtained from publicly accessible biological sequence resources.

The principal source used for sequence accession and genomic/protein information is:

### 🧬 NCBI

[NCBI](https://www.ncbi.nlm.nih.gov/)

NCBI provides:

* nucleotide and protein sequence records;
* accession identifiers;
* organism information;
* RefSeq records;
* assembly information;
* and associated annotation.

The repository retains accession information rather than treating downloaded sequences as anonymous files.

---

# 🧬 6. Protein Reference Annotation

The human TP53 reference is anchored to:

### UniProt

[UniProt](https://www.uniprot.org/)

Reference:

```text
P04637
```

UniProt provides the standardized protein-level reference used for:

* human TP53 sequence definition;
* residue numbering;
* protein annotation;
* functional interpretation;
* and cross-reference information.

---

# 🐘 7. Mammalian Sequence Selection

The final comparative dataset contains **56 mammalian TP53 sequences**.

The purpose of the dataset is not simply to maximize the number of sequences.

Instead, the dataset is intended to provide a comparative mammalian framework in which:

* TP53 homologues can be aligned;
* homologous residue positions can be identified;
* conservation can be quantified;
* cancer-associated human residues can be mapped;
* and phylogenetic relationships can be considered.

The final dataset should therefore be interpreted as a **curated comparative sampling of mammalian TP53**, rather than a complete catalogue of all available mammalian TP53 sequences.

---

# 🧹 8. Sequence Curation Principles

Sequence curation was performed before downstream comparative analysis.

The curation process was designed around the following principles:

### 8.1 Correct biological identity

Sequences should correspond to TP53 or an appropriate TP53 orthologue.

### 8.2 Species traceability

Each sequence should retain information identifying its species of origin.

### 8.3 Accession traceability

Where available, accession identifiers are retained so that source records can be independently located.

### 8.4 Protein-level consistency

Sequences are represented as protein sequences because the primary analysis concerns conservation of amino-acid residues.

### 8.5 Analytical suitability

Sequences included in the final dataset should be suitable for multiple sequence alignment and residue-level comparative analysis.

---

# 🧾 9. Accession-Level Audit

The accession audit is one of the principal reproducibility resources in the repository.

Location:

```text
data/processed/TP53_sequence_accession_audit.csv
```

The audit is intended to provide a structured record connecting:

```text
Species
   ↓
Accession
   ↓
TP53 sequence
   ↓
Curated dataset
```

This is preferable to relying solely on a FASTA file because a FASTA sequence by itself does not necessarily communicate sufficient biological provenance.

---

# 🔬 10. Why Accession-Level Provenance Matters

Sequence-based evolutionary conclusions depend directly on the biological sequences entering the alignment.

If the source sequence changes, the downstream analysis can change.

Therefore:

```text
Different sequence
       ↓
Different alignment
       ↓
Different residue correspondence
       ↓
Different conservation estimate
       ↓
Potentially different biological interpretation
```

For this reason, accession-level provenance is treated as an integral component of the computational workflow.

---

# 🧬 11. Processed Sequence Dataset

The curated dataset is stored separately from the original source information.

### Analysis-ready sequence

```text
data/processed/TP53_curated.fasta
```

This file is used as the sequence-level input for the comparative workflow.

The processing stage establishes a stable analysis resource while retaining the source audit required to understand where the sequences originated.

---

# 📊 12. Species Metadata

Species-level metadata are retained in:

```text
data/raw/species_metadata.csv
```

This resource supports interpretation of the comparative dataset and helps distinguish biological identity from sequence-level information.

The metadata layer is particularly important for phylogenetic sensitivity analyses because taxonomic composition can influence evolutionary comparisons.

---

# 🧬 13. Sequence Accession Audit and Reproducibility

The repository contains two related provenance concepts:

### Biological provenance

Where did the sequence originate?

### Computational provenance

How did that sequence become part of the final analysis?

These should not be conflated.

The provenance chain is:

```text
NCBI / reference database
        ↓
Accession record
        ↓
Retrieved protein sequence
        ↓
Curated sequence
        ↓
TP53_curated.fasta
        ↓
Multiple sequence alignment
        ↓
Residue-level conservation
```

---

# 🧪 14. Cancer Mutation Data

Evolutionary conservation is integrated with human cancer mutation information.

The repository contains the mutation-frequency resource:

```text
data/raw/cbioportal_mutation_frequency_by_codon.csv
```

This dataset provides the cancer-genomics layer of the analysis.

The purpose is to evaluate the relationship between:

```text
Human cancer mutation recurrence
              +
Mammalian evolutionary conservation
```

rather than deriving evolutionary conservation from the cancer dataset itself.

---

# 🧬 15. Cancer Mutation Data Source

The mutation analysis uses publicly available cancer-genomics information associated with:

### cBioPortal

[cBioPortal](https://www.cbioportal.org/)

and TCGA-derived cancer datasets.

cBioPortal provides a standardized interface for exploring cancer genomic alterations across studies.

The mutation dataset is treated as an independent evidence layer from the mammalian sequence dataset.

This distinction is important because:

> **Cancer mutation recurrence and evolutionary conservation represent different biological processes.**

The analysis brings them together only after each has been independently represented.

---

# 🔗 16. Separation of Evidence Layers

The repository intentionally maintains separate data streams:

```text
             MAMMALIAN EVOLUTION
                    │
                    ▼
             TP53 sequences
                    │
                    ▼
              Conservation
                    │
                    │
                    ├───────────────┐
                    │               │
                    ▼               ▼
             Human cancer      Structural
              mutations         context
                    │               │
                    └───────┬───────┘
                            ▼
                    Integrated analysis
```

This architecture reduces the risk of circular interpretation.

The cancer mutation data are not used to define the evolutionary conservation signal.

---

# 🧩 17. Structural Reference

Structural context is provided through:

```text
data/raw/1tup.cif
```

This structural resource is used as supporting information for interpretation of TP53 residue positions and structural/functional classes.

Structural information is therefore treated as a contextual evidence layer rather than as an input to the primary conservation calculation.

---

# 🧬 18. Structural Classification

The processed structural classification is stored at:

```text
data/processed/structural_class_summary.csv
```

This resource supports interpretation of residue classes and their structural context.

The purpose is to ask whether conservation patterns correspond to known structural or functional regions of TP53.

---

# 🎯 19. Hotspot Definition

The human cancer hotspot analysis focuses on six recurrent TP53 residues:

| Hotspot | Human TP53 residue |
| ------: | :----------------: |
|     175 |      **R175**      |
|     245 |      **G245**      |
|     248 |      **R248**      |
|     249 |      **R249**      |
|     273 |      **R273**      |
|     282 |      **R282**      |

These positions are defined from the human TP53 reference coordinate system.

They are therefore independent of the observed mammalian conservation results.

---

# 🧠 20. Avoiding Circularity

A key methodological principle is:

> **The hotspot definition is established before evaluating whether the hotspots are conserved.**

This means the workflow does not:

```text
Find highly conserved residues
        ↓
Call them hotspots
```

Instead, it follows:

```text
Define biologically established human hotspots
        ↓
Map them to the mammalian alignment
        ↓
Measure their conservation
        ↓
Compare against controls
```

This preserves the distinction between hypothesis definition and hypothesis testing.

---

# 🧬 21. Control Dataset Provenance

The hotspot analysis uses DNA-binding-domain-matched control residues.

The reason for this design is that the DNA-binding domain itself is evolutionarily constrained.

A comparison between:

```text
Hotspots
     vs
Every other residue in TP53
```

could therefore mix hotspot-specific conservation with broad domain-level conservation.

The matched-control strategy provides a more biologically appropriate comparison.

---

# 📊 22. Conservation Dataset

The residue-level conservation dataset is stored at:

```text
data/processed/residue_conservation.csv
```

This dataset represents the processed conservation measurements derived from the mammalian TP53 alignment.

It provides the analytical bridge between:

```text
Sequence alignment
       ↓
Residue-level conservation
       ↓
Hotspot/control comparison
```

---

# 🔄 23. Permutation Statistics

Permutation-based hotspot statistics are stored at:

```text
data/processed/permutation_hotspot_statistics.csv
```

The permutation analysis provides an empirical null-model framework for evaluating whether the observed hotspot conservation is greater than expected under matched random sampling.

The corresponding result outputs are retained under:

```text
results/statistics/
```

---

# 🌳 24. Phylogenetic Data

Phylogenetic analysis is performed on the mammalian TP53 sequence dataset.

The principal phylogenetic output files are:

```text
results/phylogeny/
├── TP53_mammals.iqtree
└── TP53_mammals.treefile
```

The phylogenetic analysis provides evolutionary context for the sequence comparisons.

It is not used to claim that phylogenetic proximity alone explains residue conservation.

---

# 🌿 25. Phylogenetic Sensitivity Dataset Provenance

Because mammalian sequences are evolutionarily related, conservation estimates are not necessarily independent across species.

The study therefore evaluates alternative taxonomic sampling strategies.

The sensitivity framework includes:

```text
1. Full mammalian dataset
2. Excluding primates
3. Excluding rodents
4. Excluding primates and rodents
5. One representative species per mammalian order
```

The purpose is to determine whether the principal conservation pattern remains directionally stable when influential taxonomic groups are removed or down-sampled.

This is an important distinction between:

> **observing conservation**

and

> **demonstrating robustness of the conservation signal.**

---

# 🧪 26. Data Transformation Map

The complete transformation pathway is:

```text
                PUBLIC SOURCES
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
      NCBI        UniProt     cBioPortal
        │            │            │
        ▼            ▼            ▼
 Mammalian       Human TP53    Cancer
 sequences       reference    mutations
        │            │            │
        └────────────┼────────────┘
                     ▼
               DATA CURATION
                     │
                     ▼
           ANALYSIS-READY DATA
                     │
       ┌─────────────┼─────────────┐
       │             │             │
       ▼             ▼             ▼
 Conservation     Mutation      Phylogeny
       │             │             │
       └─────────────┼─────────────┘
                     ▼
              Statistical analysis
                     │
                     ▼
               Final results
```

---

# 📁 27. Provenance-to-Repository Map

| Data / Resource           | Repository location                                   | Role                                 |
| ------------------------- | ----------------------------------------------------- | ------------------------------------ |
| Human TP53 reference      | UniProt P04637                                        | Reference coordinate system          |
| Mammalian TP53 sequences  | `data/processed/TP53_curated.fasta`                   | Comparative sequence dataset         |
| Sequence accession audit  | `data/processed/TP53_sequence_accession_audit.csv`    | Sequence provenance                  |
| Species metadata          | `data/raw/species_metadata.csv`                       | Taxonomic metadata                   |
| Cancer mutation data      | `data/raw/cbioportal_mutation_frequency_by_codon.csv` | Mutation recurrence                  |
| Structural reference      | `data/raw/1tup.cif`                                   | Structural context                   |
| Structural classification | `data/processed/structural_class_summary.csv`         | Functional/structural interpretation |
| Conservation data         | `data/processed/residue_conservation.csv`             | Residue-level conservation           |
| Permutation statistics    | `data/processed/permutation_hotspot_statistics.csv`   | Null-model analysis                  |
| Hotspot analysis          | `results/hotspot_analysis/`                           | Hotspot-specific outputs             |
| Phylogenetic outputs      | `results/phylogeny/`                                  | Evolutionary relationships           |
| Main analysis script      | `scripts/`                                            | Computational implementation         |
| Analysis notebook         | `notebooks/`                                          | Interactive analysis                 |

---

# 🔬 28. Provenance of the Analytical Coordinate System

A critical component of the study is the maintenance of a consistent coordinate relationship between human TP53 and mammalian homologues.

The coordinate hierarchy is:

```text
Human TP53 residue number
            │
            ▼
Multiple sequence alignment
            │
            ▼
Homologous mammalian position
            │
            ▼
Conservation measurement
            │
            ▼
Hotspot / control classification
```

This prevents the common error of treating an alignment column as automatically equivalent to a biological residue number.

---

# 🧾 29. Data Versioning Principle

Public biological databases are dynamic.

Sequence records, annotations, mutation datasets, and database interfaces may change over time.

For this reason, the repository preserves the actual analysis resources used in the study rather than relying exclusively on live database queries.

The combination of:

```text
Source database
+
Accession
+
Stored analysis resource
+
Processing documentation
```

provides a more stable provenance record.

---

# ♻️ 30. Reproducibility Boundary

This repository aims to make the analytical inputs inspectable and traceable.

However, reproducibility has several levels:

### Level 1 — Data reproducibility

Can another researcher identify the biological records used?

### Level 2 — Computational reproducibility

Can another researcher inspect the code and analytical transformations?

### Level 3 — Result reproducibility

Can the reported outputs be regenerated from the documented inputs?

### Level 4 — Biological reproducibility

Would an independent biological experiment reproduce the observed biological phenomenon?

This repository primarily addresses **Levels 1–3**.

It does not claim experimental reproducibility of the biological findings.

---

# ⚠️ 31. Provenance Limitations

Several limitations should be considered when interpreting the provenance of the study.

### Database availability

Public databases may change after the original analysis.

### Annotation differences

Protein annotations can differ among species and database records.

### Taxonomic availability

Not every mammalian species has an equally well-characterized TP53 sequence.

### Sequence quality

Publicly available records can differ in completeness and annotation quality.

### Mutation database evolution

Cancer mutation datasets can be updated as additional samples and studies become available.

These limitations are reasons for preserving the actual analysis resources and accession-level metadata.

---

# 🔍 32. What a Researcher Can Verify

A researcher inspecting this repository can independently examine:

### 🧬 Sequence inputs

```text
data/processed/TP53_curated.fasta
```

### 🔎 Accession provenance

```text
data/processed/TP53_sequence_accession_audit.csv
```

### 🐭 Species metadata

```text
data/raw/species_metadata.csv
```

### 🧪 Cancer mutation resource

```text
data/raw/cbioportal_mutation_frequency_by_codon.csv
```

### 🧩 Structural reference

```text
data/raw/1tup.cif
```

### 📊 Conservation measurements

```text
data/processed/residue_conservation.csv
```

### 🔄 Permutation analysis

```text
data/processed/permutation_hotspot_statistics.csv
```

### 🌳 Phylogenetic outputs

```text
results/phylogeny/
```

### 💻 Computational implementation

```text
scripts/
```

---

# 🧭 33. Recommended Provenance Audit Path

For a researcher reviewing this project:

```text
START
  │
  ▼
Human TP53 reference
  │
  ▼
56 mammalian sequences
  │
  ▼
Accession audit
  │
  ▼
Curated FASTA
  │
  ▼
Multiple sequence alignment
  │
  ▼
Residue conservation
  │
  ├───────────────┐
  ▼               ▼
Hotspots       Mutation data
  │               │
  └───────┬───────┘
          ▼
     Statistics
          │
          ▼
      Phylogeny
          │
          ▼
     Interpretation
```

This provides a direct path from biological source material to the scientific interpretation.

---

# 🧠 34. Why This Provenance Architecture Matters

The scientific value of a comparative bioinformatics study does not depend only on the sophistication of its algorithms.

It also depends on whether another researcher can determine:

> **What data were used?**

> **Where did those data originate?**

> **How were they transformed?**

> **Which observations came from the original data and which were computationally derived?**

> **Can the analytical path be independently inspected?**

The repository therefore treats provenance as part of the scientific methodology.

---

# 🔬 35. Provenance Principle

The guiding principle of this project is:

> **Every major computational conclusion should have a traceable relationship to a documented biological input.**

In practical terms:

```text
No anonymous sequence
        ↓
No undocumented transformation
        ↓
No unexplained dataset
        ↓
No untraceable result
```

Instead:

```text
Source
  ↓
Accession
  ↓
Curated input
  ↓
Analysis
  ↓
Output
  ↓
Figure
  ↓
Interpretation
```

---

# 📚 36. External Resources

### NCBI

[https://www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/)

Primary resource for sequence records, accession identifiers, and genomic/protein information.

### UniProt

[https://www.uniprot.org/](https://www.uniprot.org/)

Reference protein annotation and human TP53 reference sequence.

### cBioPortal

[https://www.cbioportal.org/](https://www.cbioportal.org/)

Cancer genomic alteration and mutation-frequency resource.

### TCGA

[https://www.cancer.gov/tcga](https://www.cancer.gov/tcga)

Cancer genomics resource underlying many of the mutation datasets accessible through cBioPortal.

---

# 🔗 37. Related Repository Documentation

Continue the computational audit through:

### Methodology

👉 [`methodology.md`](methodology.md)

### Statistical analysis

👉 [`statistical_analysis.md`](statistical_analysis.md)

### Reproducibility

👉 [`reproducibility.md`](reproducibility.md)

### Interpretation and limitations

👉 [`interpretation_and_limitations.md`](interpretation_and_limitations.md)

### Data architecture

👉 [`../data/README.md`](../data/README.md)

---

# 🧬 38. Final Provenance Summary

The final dataset and analysis can be represented as:

```text
                 PUBLIC BIOLOGICAL RESOURCES
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
          NCBI             UniProt         cBioPortal
            │                 │                 │
            ▼                 ▼                 ▼
      Mammalian TP53      Human TP53       Cancer mutation
         records            reference          data
            │                 │                 │
            └─────────────────┼─────────────────┘
                              ▼
                       CURATED DATASETS
                              │
                 ┌────────────┼────────────┐
                 │            │            │
                 ▼            ▼            ▼
             Sequences    Mutations    Structure
                 │            │            │
                 └────────────┼────────────┘
                              ▼
                       COMPUTATIONAL
                          ANALYSIS
                              │
                              ▼
                         STATISTICS
                              │
                              ▼
                       INTERPRETATION
```

---

## ♻️ Provenance in One Sentence

> **The repository preserves a traceable path from publicly accessible biological records and cancer-genomics resources through sequence curation and computational analysis to the evolutionary, statistical, and structural evidence used to interpret recurrent human TP53 cancer mutation hotspots across mammals.**

````

### Why this is the right next file

This is deliberately **not just documentation for the sake of documentation**. It establishes the chain a serious PI will care about:

**source → accession → curated sequence → analysis → result.**

It also explicitly separates **what your repository can reproduce from what it cannot claim to reproduce experimentally**. That distinction matters.

One thing I am **not** doing is inventing exact accession numbers, download dates, database versions, or sequence-selection decisions that aren't explicitly established in the material you've provided. Those should come from your actual `TP53_sequence_accession_audit.csv` and source records. If we fabricate them just to make the README look polished, we'd be making the repository *look* more rigorous while actually making it less trustworthy.

### After you paste this

The next three files should be completed in this order:

```text
docs/
├── provenance.md                    ← NOW
├── statistical_analysis.md          ← NEXT
├── reproducibility.md               ← THEN
└── interpretation_and_limitations.md
````
