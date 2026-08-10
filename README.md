# 🧬 Evolutionary Conservation and Functional Constraint of TP53 Mutation Hotspots Across Mammalian Species

<p align="center">

**A reproducible comparative-bioinformatics framework for investigating why recurrent human cancer-associated TP53 residues remain evolutionarily constrained across mammals.**

</p>

<p align="center">

[![Research](https://img.shields.io/badge/Research-Comparative%20Genomics-blue)](https://github.com/Rita1791/TP53-Evolutionary-Conservation-Mammals)
[![Bioinformatics](https://img.shields.io/badge/Field-Bioinformatics-purple)](https://github.com/Rita1791/TP53-Evolutionary-Conservation-Mammals)
[![Python](https://img.shields.io/badge/Code-Python-3776AB)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Preprint](https://img.shields.io/badge/Preprint-Research%20Square-orange)](https://doi.org/10.21203/rs.3.rs-9299199/v1)

</p>

---

## 🔬 Research in One Sentence

This project investigates whether recurrent human **TP53 cancer mutation hotspots** occur at amino-acid positions that are unusually constrained across mammalian evolution, integrating comparative sequence analysis, residue-level conservation, mutation recurrence, statistical testing, phylogenetics, and structural context.

---

# 🧠 Why This Research?

TP53 encodes the tumour-suppressor protein p53, a central regulator of genomic stability and one of the most frequently altered genes in human cancer.

Human cancer datasets repeatedly identify a small number of recurrent TP53 mutation hotspots, including:

```text
R175
G245
R248
R249
R273
R282
```

The central evolutionary question is:

> **Are these recurrently mutated human residues also evolutionarily constrained across mammals?**

This project approaches that question computationally by placing human cancer-associated residues onto a comparative mammalian TP53 sequence framework.

The aim is not to claim that evolutionary conservation causes cancer mutation.

Instead, the study asks whether **mutation recurrence and evolutionary constraint converge at the same residue-level positions**, potentially highlighting functionally important sites for further structural and experimental investigation.

---

## For PIs / Reviewers

Start here if you are reviewing this repository for academic, PhD, or computational biology evaluation:

1. [`docs/reviewer_summary.md`](docs/reviewer_summary.md)
2. [`docs/reviewer_quickstart.md`](docs/reviewer_quickstart.md)
3. [`docs/statistical_analysis.md`](docs/statistical_analysis.md)
4. [`docs/provenance.md`](docs/provenance.md)
5. [`docs/interpretation_and_limitations.md`](docs/interpretation_and_limitations.md)
6. [`docs/result_interpretation_for_non_specialists.md`](docs/result_interpretation_for_non_specialists.md)

---

# 🧬 Research Framework

```text
                     HUMAN TP53
                         │
                         ▼
              Recurrent cancer hotspots
                         │
                         ▼
             Human residue coordinates
                         │
                         ▼
          Mammalian TP53 sequence dataset
                         │
                         ▼
              Multiple sequence alignment
                         │
                         ▼
             Residue-level conservation
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       Hotspots       Controls       Mutations
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                Statistical analysis
                         │
                         ▼
                  Phylogenetic context
                         │
                         ▼
                  Structural context
                         │
                         ▼
               Integrated interpretation
                         │
                         ▼
             Testable biological hypotheses
```

---

# 🎯 Core Research Questions

### Question 1 — Evolutionary constraint

Are recurrent human TP53 cancer hotspots highly conserved across mammals?

### Question 2 — Comparative enrichment

Is hotspot conservation greater than expected relative to an appropriate background/control set?

### Question 3 — Mutation–conservation relationship

Do recurrently mutated human TP53 residues preferentially occur at evolutionarily constrained positions?

### Question 4 — Evolutionary robustness

Are the observed patterns stable when the taxonomic composition of the mammalian dataset is changed?

### Question 5 — Functional context

Do conserved hotspot positions correspond to known structural or functional regions of TP53?

---

# 🧪 Analytical Strategy

The repository separates the evidence into independent analytical layers:

| Layer | Purpose |
|---|---|
| 🧬 Comparative sequences | Establish mammalian TP53 evolutionary context |
| 🎯 Hotspot mapping | Define and map canonical human TP53 cancer-associated positions |
| 📊 Conservation | Quantify residue-level evolutionary constraint |
| 🧪 Mutation analysis | Integrate human cancer mutation recurrence |
| 📈 Statistics | Evaluate hotspot enrichment against empirical null models |
| 🌳 Phylogeny | Provide evolutionary context and sensitivity analysis |
| 🧩 Structure | Interpret conserved residues in structural context |
| ♻️ Reproducibility | Preserve provenance, code, outputs, and documentation |

---

# 📊 Key Computational Result

The repository contains permutation-based statistical outputs comparing observed conservation of recurrently mutated TP53 positions with matched background distributions.

For the canonical six-hotspot comparison, the current result table reports:

| Analysis | Observed mean | Null mean | Empirical one-sided P |
|---|---:|---:|---:|
| Canonical 6 vs DBD | 1.000 | 0.936 | 0.02359 |
| Top 10 mutated codons | 1.000 | 0.936 | 0.00182 |
| Top 20 mutated codons | 0.992 | 0.936 | 0.00139 |
| Top 30 mutated codons | 0.994 | 0.936 | 0.00003 |

These results indicate that recurrently mutated TP53 positions show strong conservation under the specified permutation framework.

**Important:** these statistics do not establish causality, mechanism, or experimental functional equivalence.

See:

[`results/statistics/permutation_hotspot_statistics.csv`](results/statistics/permutation_hotspot_statistics.csv)

and:

[`docs/statistical_analysis.md`](docs/statistical_analysis.md)

---

# 🧬 Canonical TP53 Hotspots

The primary hotspot set is:

| Human TP53 residue | Role in analysis |
|---|---|
| **R175** | Recurrent cancer-associated hotspot |
| **G245** | Recurrent cancer-associated hotspot |
| **R248** | Recurrent cancer-associated hotspot |
| **R249** | Recurrent cancer-associated hotspot |
| **R273** | Recurrent cancer-associated hotspot |
| **R282** | Recurrent cancer-associated hotspot |

The positions are defined using the human TP53 reference coordinate system.

Human reference:

**UniProt P04637**

---

# 🌍 Comparative Genomics

The project uses mammalian TP53 protein sequences to establish an evolutionary comparison framework.

The repository distinguishes:

```text
RAW DATA
   ↓
CURATED DATA
   ↓
ALIGNMENT
   ↓
RESIDUE-LEVEL ANALYSIS
   ↓
STATISTICS
   ↓
INTERPRETATION
```

The exact accession-level provenance is documented in:

[`docs/provenance.md`](docs/provenance.md)

---

# 🔬 Methodological Components

## 1. Sequence Curation

Publicly available TP53 protein sequences are curated with accession-level traceability.

## 2. Multiple Sequence Alignment

Protein sequences are aligned to establish homologous residue positions across mammals.

## 3. Conservation Scoring

Residue-level conservation is calculated from the comparative alignment.

## 4. Hotspot Mapping

Human cancer-associated hotspot positions are mapped onto the comparative framework.

## 5. Statistical Testing

Permutation-based null models are used to evaluate whether hotspot conservation is greater than expected under matched sampling.

## 6. Phylogenetic Reconstruction

Phylogenetic reconstruction provides evolutionary context for the comparative sequence dataset.

## 7. Structural Interpretation

Structural information is used as supporting context for conserved TP53 residues.

---

# 📁 Repository Architecture

```text
TP53-Evolutionary-Conservation-Mammals/
│
├── 📄 README.md
├── 📄 CITATION.cff
├── 📄 LICENSE
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── 🧬 data/
│   ├── raw/
│   └── processed/
│
├── 📚 docs/
│   ├── methodology.md
│   ├── provenance.md
│   ├── reproducibility.md
│   ├── statistical_analysis.md
│   └── interpretation_and_limitations.md
│
├── 💻 scripts/
│   ├── conservation_analysis.py
│   ├── hotspot_analysis.py
│   ├── mutation_analysis.py
│   ├── phylogenetic_analysis.py
│   ├── statistical_analysis.py
│   └── tp53_evolutionary_functional_analysis.py
│
├── 📓 notebooks/
│
├── 📊 results/
│   ├── conservation/
│   ├── hotspot_analysis/
│   ├── mutation_analysis/
│   ├── phylogeny/
│   └── statistics/
│
├── 🖼️ figures/
│   ├── main/
│   └── supplementary/
│
├── 📄 publication/
│   └── manuscript_source/
│
└── 🌍 eccb2026/
```

---

# 🧭 Researcher / PI Reading Path

If you are reviewing this repository for the first time:

### 01 — Understand the research

Start here.

### 02 — Understand the methodology

[`docs/methodology.md`](docs/methodology.md)

### 03 — Verify data provenance

[`docs/provenance.md`](docs/provenance.md)

### 04 — Inspect reproducibility

[`docs/reproducibility.md`](docs/reproducibility.md)

### 05 — Examine statistical framework

[`docs/statistical_analysis.md`](docs/statistical_analysis.md)

### 06 — Inspect computational implementation

[`scripts/`](scripts/)

### 07 — Examine derived outputs

[`results/`](results/)

### 08 — Examine figures

[`figures/`](figures/)

### 09 — Read interpretation and limitations

[`docs/interpretation_and_limitations.md`](docs/interpretation_and_limitations.md)

### 10 — Examine the associated research

[`publication/`](publication/)

---

# 📚 Research Outputs

## 📄 Research Square Preprint

**Evolutionary Conservation and Functional Constraint of TP53 Mutation Hotspots Across Mammalian Species**

Ritika Rajendra Rawat, Sermarani Nadar, Gursimran Kaur Uppal.

**DOI:**  
https://doi.org/10.21203/rs.3.rs-9299199/v1

[Read the preprint](https://doi.org/10.21203/rs.3.rs-9299199/v1)

---

## 🔎 ResearchGate

[View research profile and associated research](https://www.researchgate.net/profile/Ritika-Rawat-10)

[View the TP53 preprint on ResearchGate](https://www.researchgate.net/publication/403476498_Evolutionary_Conservation_and_Functional_Constraint_of_TP53_Mutation_Hotspots_Across_Mammalian_Species)

---

# 🏆 Conference / Research Presentation

The research is being developed for scientific dissemination through conference presentation and research communication.

Conference materials are maintained separately under:

[`eccb2026/`](eccb2026/)

This separation keeps:

```text
Research code
     +
Research data
     +
Research results
     +
Conference communication
```

as distinct but connected components.

---

# 👩‍🔬 About the Researcher

## Ritika Rajendra Rawat

**MSc Bioinformatics | Computational Biology | Comparative Genomics | Cancer Bioinformatics**

My research interests lie at the intersection of:

```text
🧬 Comparative Genomics
        +
🧪 Cancer Biology
        +
🌳 Evolutionary Biology
        +
💻 Bioinformatics
        +
📊 Sequence Analysis
        +
🧠 Computational Modelling
        +
♻️ Reproducible Research
```

I am particularly interested in using computational approaches to investigate how evolutionary constraint, sequence variation, and disease-associated mutations intersect across biological systems.

My current research direction includes:

- cancer genomics;
- evolutionary bioinformatics;
- comparative genomics;
- TP53 biology;
- sequence conservation;
- mutation analysis;
- computational biomarker discovery;
- and reproducible computational research.

---

# 🔗 Connect With Me

| Platform | Link |
|---|---|
| 💼 LinkedIn | [Ritika Rawat](https://in.linkedin.com/in/ritika-rawat-551107219) |
| 🔬 ResearchGate | [Ritika Rawat](https://www.researchgate.net/profile/Ritika-Rawat-10) |
| 📧 Email | [ritika.rawat27@outlook.com](mailto:ritika.rawat27@outlook.com) |
| 💻 GitHub | [Rita1791](https://github.com/Rita1791) |

### Interested in collaboration, computational biology, or PhD research?

📧 **Email:** [ritika.rawat27@outlook.com](mailto:ritika.rawat27@outlook.com)

💼 **Connect on LinkedIn:** [Ritika Rawat](https://in.linkedin.com/in/ritika-rawat-551107219)

---

# 🧰 Technologies & Methods

### Programming

`Python`

### Bioinformatics

`Biopython` · `Multiple Sequence Alignment` · `Residue Mapping`

### Statistics

`SciPy` · `Mann–Whitney U` · `Permutation Testing` · `Empirical Null Models`

### Evolutionary Analysis

`Phylogenetics` · `Sequence Conservation` · `Comparative Genomics`

### Structural Analysis

`PDB/mmCIF` · `BLOSUM62` · `Structural Context`

### Scientific Computing

`NumPy` · `Pandas` · `Matplotlib`

### Reproducibility

`Git` · `GitHub` · `Jupyter` · `CITATION.cff`

---

# ♻️ Reproducibility

The repository is structured so that the analytical path can be inspected from biological source material to final interpretation.

```text
Public database
      ↓
Accession-level provenance
      ↓
Curated sequence dataset
      ↓
Alignment
      ↓
Residue-level analysis
      ↓
Statistical evaluation
      ↓
Phylogenetic context
      ↓
Structural interpretation
      ↓
Figures
      ↓
Manuscript
```

See:

- [`docs/provenance.md`](docs/provenance.md)
- [`docs/reproducibility.md`](docs/reproducibility.md)

---

# ⚠️ Interpretation Boundary

This is a computational evolutionary-bioinformatics study.

The results should **not** be interpreted as direct experimental evidence for:

- cancer resistance;
- clinical prediction;
- causal mutation mechanisms;
- identical TP53 function across species;
- or therapeutic efficacy.

Instead, the analysis identifies evolutionary and sequence-level patterns that can generate hypotheses for future structural, functional, and experimental investigation.

Full discussion:

[`docs/interpretation_and_limitations.md`](docs/interpretation_and_limitations.md)

---

# 📖 Citation

If you use this repository, its methodology, computational framework, derived results, or figures, please cite the associated research.

### Associated research

**Rawat, R. R., Nadar, S., & Uppal, G. K. (2026).**

*Evolutionary Conservation and Functional Constraint of TP53 Mutation Hotspots Across Mammalian Species.*

Research Square.

**DOI:** https://doi.org/10.21203/rs.3.rs-9299199/v1

### Machine-readable citation

[`CITATION.cff`](CITATION.cff)

---

# 📜 License

This repository is released under the **MIT License**.

See [`LICENSE`](LICENSE).

---

# 🌐 External Resources

| Resource | Link |
|---|---|
| 🧬 Human TP53 — UniProt P04637 | [UniProt](https://www.uniprot.org/uniprotkb/P04637) |
| 🧬 NCBI | [NCBI](https://www.ncbi.nlm.nih.gov/) |
| 🧪 cBioPortal | [cBioPortal](https://www.cbioportal.org/) |
| 📄 Research Square | [Preprint](https://doi.org/10.21203/rs.3.rs-9299199/v1) |
| 🔬 ResearchGate | [Research profile](https://www.researchgate.net/profile/Ritika-Rawat-10) |

---

# 🧭 Research Philosophy

The central principle of this project is:

> **Use computational evidence to identify evolutionary patterns, preserve the analytical path behind those observations, and translate those observations into testable biological hypotheses.**

```text
DATA
 ↓
EVIDENCE
 ↓
ANALYSIS
 ↓
VALIDATION
 ↓
INTERPRETATION
 ↓
HYPOTHESIS
```

The repository is therefore designed not merely as a collection of code and figures, but as a **traceable computational research record**.

---

<p align="center">

### 🧬 Comparative Genomics · Evolutionary Cancer Biology · Computational Biology

**Ritika Rajendra Rawat · MSc Bioinformatics**

💻 GitHub · 💼 LinkedIn · 🔬 ResearchGate · 📧 Email

</p>
