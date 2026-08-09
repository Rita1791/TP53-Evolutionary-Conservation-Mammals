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
```

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
│               PROCESSED DATA                │
│                                             │
│ Curated sequences, accession audits,        │
│ conservation tables and derived datasets    │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│                   RESULTS                   │
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

| Property | Reference |
| :--- | :--- |
| Gene | **TP53** |
| Protein | Cellular tumour antigen p53 |
| Species | *Homo sapiens* |
| UniProt accession | **P04637** |
| Protein length | **393 amino acids** |

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
* Nucleotide and protein sequence records;
* Accession identifiers;
* Organism information;
* RefSeq records;
* Assembly information;
* Associated annotation.

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
* Human TP53 sequence definition;
* Residue numbering;
* Protein annotation;
* Functional interpretation;
* Cross-reference information.

---

# 🐘 7. Mammalian Sequence Selection

The final comparative dataset contains **56 mammalian TP53 sequences**.

The purpose of the dataset is not simply to maximize the number of sequences.

Instead, the dataset is intended to provide a comparative mammalian framework in which:
* TP53 homologues can be aligned;
* Homologous residue positions can be identified;
* Conservation can be quantified;
* Cancer-associated human residues can be mapped;
* Phylogenetic relationships can be considered.

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
```text
[The original text cut off here]
```
