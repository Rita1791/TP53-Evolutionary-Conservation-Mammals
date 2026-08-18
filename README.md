# TP53 Evolutionary Conservation Across Mammals

### Comparative genomics of recurrent human TP53 cancer mutation hotspots

**Ritika Rajendra Rawat · Sermarani Nadar · Gursimran Kaur Uppal**

This repository contains the computational work behind our study of recurrent **TP53 cancer mutation hotspots** and their conservation across mammalian evolution.

The project started from a fairly simple question:

> **Are the TP53 residues that repeatedly mutate in human cancers also residues that evolution has strongly conserved across mammals?**

The answer turned out to be more interesting than simply saying that the hotspots are conserved.

All six canonical hotspots are highly constrained, but the important part of the study is that they remain unusually conserved even when I compare them against other residues from the **same TP53 DNA-binding domain**, which is itself already strongly conserved.

That distinction became central to how I interpret the work.

---

## Start here

If you are reviewing the repository for the first time, I recommend this order:

1. Read the [final manuscript](publication/MAIN_MANUSCRIPT_FINAL_SUBMISSION_READY.pdf).
2. Look at the six [main figures](figures/main/).
3. Inspect the processed [residue-level conservation table](data/processed/residue_conservation.csv).
4. Check the [permutation-test output](results/statistics/permutation_hotspot_statistics.csv).
5. Read the [analysis-version note](docs/analysis_versions.md).
6. Look through the scripts if you want to inspect how the calculations were implemented.

The repository also contains the material prepared for my **ECCB 2026 poster presentation** in [`eccb2026/`](eccb2026/).

---

## The biological question

TP53 is one of the most frequently mutated genes in human cancer.

What interested me was that TP53 mutations are not distributed uniformly across the protein. Certain residues appear again and again across tumour datasets.

The six canonical hotspots used in this study are:

```text
R175
G245
R248
R249
R273
R282
```

All six occur within the TP53 DNA-binding domain.

At first, it is tempting to ask only:

> Are these residues conserved across mammals?

But that comparison is too easy.

The DNA-binding domain itself is already highly constrained, so a hotspot could look impressive simply because it belongs to a conserved functional region.

The stronger question is therefore:

> **Are the hotspots more conserved than other non-hotspot residues from the same DNA-binding domain?**

That became the primary comparison in the study.

---

## The dataset I finally used

The expanded analysis represented in the current repository contains:

| Component | Dataset |
|---|---:|
| Mammalian TP53 protein sequences | **56** |
| Human TP53 reference length | **393 aa** |
| Canonical hotspots | **6** |
| TP53 mutations in the PanCancer dataset | **4,225** |
| Mutated TP53 codons represented | **300** |

The curated mammalian protein set is available here:

[`data/processed/TP53_curated.fasta`](data/processed/TP53_curated.fasta)

I also kept an accession-level audit rather than only the FASTA file:

[`data/processed/TP53_sequence_accession_audit.csv`](data/processed/TP53_sequence_accession_audit.csv)

That file is important to me because the result depends on exactly which TP53 sequence and isoform represents each species.

---

# What I found

## 1. All six canonical hotspots were invariant

In the expanded 56-sequence analysis:

```text
R175   1.000
G245   1.000
R248   1.000
R249   1.000
R273   1.000
R282   1.000
```

All six canonical hotspots showed:

- majority-residue conservation = **1.000**
- human-residue conservation = **1.000**
- Shannon entropy = **0.000**
- no gaps at the hotspot alignment positions

This was the first result, but I do not consider it the strongest result of the study.

The DNA-binding domain is already highly conserved, so complete hotspot conservation alone does not answer whether the hotspots are unusual within their own functional background.

<p align="center">
  <a href="figures/main/Figure_1_Conservation_Profile.png">
    <img src="figures/main/Figure_1_Conservation_Profile.png"
         alt="Residue-level mammalian TP53 conservation profile"
         width="90%" />
  </a>
</p>

---

## 2. The domain-matched comparison was more informative

The primary comparison was therefore:

```text
canonical hotspots
        versus
DNA-binding-domain non-hotspot residues
```

The mean majority-residue conservation was:

| Group | Mean conservation |
|---|---:|
| Canonical hotspots | **1.000** |
| DBD non-hotspots | **0.934** |

The reported statistical comparison was:

```text
Mann–Whitney U = 819.0
one-sided p    = 0.0156
Cliff's δ      = 0.476
```

The same direction was also observed when I used human-residue conservation and entropy rather than only majority-residue conservation.

For me, this is the main evolutionary result:

> **The hotspots are not only conserved. They are unusually constrained even relative to an already-conserved DNA-binding-domain background.**

<p align="center">
  <a href="figures/main/Figure_2_Hotspot_vs_Control_Boxplot.png">
    <img src="figures/main/Figure_2_Hotspot_vs_Control_Boxplot.png"
         alt="Canonical TP53 hotspot conservation compared with domain-matched controls"
         width="82%" />
  </a>
</p>

---

## 3. I used permutation testing as a second check

With only six canonical hotspots, I did not want to rely only on a rank-based group comparison.

I therefore asked another question:

> If I randomly sample six residues from the TP53 DNA-binding domain, how often do I obtain a mean conservation at least as high as the six actual hotspots?

For the canonical hotspot set:

```text
Observed hotspot mean = 1.000
DBD-matched null mean = 0.935845368
Empirical one-sided p = 0.023589764
Iterations            = 100,000
Seed                  = 42
```

The committed output is:

[`results/statistics/permutation_hotspot_statistics.csv`](results/statistics/permutation_hotspot_statistics.csv)

I like this test because its interpretation is fairly intuitive: the observed hotspot set sits toward the extreme end of conservation values obtainable from size-matched sets of DBD residues.

The same file also contains permutation analyses for the most recurrent mutation sets:

| Query | Observed mean | Empirical p |
|---|---:|---:|
| Canonical 6 | 1.000 | 0.02359 |
| Top recurrent 10 | 1.000 | 0.00182 |
| Top recurrent 20* | 0.99248 | 0.00139 |
| Top recurrent 30* | 0.99426 | 0.00003 |

\*Only codons present in the DBD/background and conservation table enter the corresponding test, which is why the recorded `n_query` values can be smaller than the nominal top-20 or top-30 labels.

---

## 4. I wanted to know whether taxonomic sampling was driving the result

A comparative mammalian dataset is not a set of 56 independent observations.

Some taxonomic groups are represented by several closely related species, so I repeated the comparison after changing the composition of the dataset.

The hotspot-minus-DBD conservation difference remained positive in each sensitivity analysis:

```text
Full dataset                +0.066   p = 0.0156
Without primates            +0.067   p = 0.0196
Without rodents             +0.063   p = 0.0245
Without primates/rodents    +0.064   p = 0.0316
One species per order       +0.082   p = 0.0355
```

This does **not** make the sequences phylogenetically independent.

What it tells me is narrower:

> the hotspot-versus-background signal is not obviously being created by one overrepresented mammalian lineage.

<p align="center">
  <a href="figures/main/Figure_3_Phylogenetic_Sensitivity.png">
    <img src="figures/main/Figure_3_Phylogenetic_Sensitivity.png"
         alt="Phylogenetic sensitivity analysis"
         width="82%" />
  </a>
</p>

---

## 5. Conservation and human cancer recurrence are related

I then joined the mammalian conservation measurements with human TP53 mutation recurrence from TCGA PanCancer/cBioPortal.

Across all 393 human TP53 positions:

```text
Spearman ρ = 0.430
p = 4.49 × 10⁻¹⁹
```

Within the DNA-binding domain:

```text
Spearman ρ = 0.368
p = 1.68 × 10⁻⁷
```

So, in this dataset, residues with stronger mammalian conservation tend to show greater recurrence in human cancer.

That is an association.

I do **not** interpret it as evidence that evolutionary conservation causes mutation recurrence.

<p align="center">
  <a href="figures/main/Figure_4_Mutation_Count_vs_Conservation.png">
    <img src="figures/main/Figure_4_Mutation_Count_vs_Conservation.png"
         alt="Human TP53 mutation recurrence versus mammalian conservation"
         width="82%" />
  </a>
</p>

---

# The result that stopped me from oversimplifying the story: R249

One residue is especially useful when interpreting the study.

### R249

```text
Mammalian conservation     = 1.000
PanCancer mutation count   = 47
Recurrence rank            = 19
```

R249 is completely conserved in the mammalian alignment, but it is not one of the very highest-frequency TP53 codons in the PanCancer dataset.

By comparison:

```text
R273  → rank 1
R248  → rank 2
R175  → rank 3
R282  → rank 5
G245  → rank 6
R249  → rank 19
```

This was an important check on the interpretation.

If conservation directly determined cancer recurrence, R249 would be difficult to explain.

Instead, I interpret the result this way:

> **Evolutionary conservation marks functional sensitivity, but it does not determine recurrence frequency.**

Mutation recurrence also reflects biology that is not contained in a protein conservation score: mutational processes, nucleotide context, tumour type, selection, exposure, tissue environment, cohort composition and other factors.

That is why I use conservation as a **prioritisation signal**, not as a causal explanation.

---

# My analysis workflow

The broad workflow was:

```text
Mammalian TP53 proteins
        │
        ▼
Sequence curation
        │
        ▼
Multiple sequence alignment
        │
        ▼
Human-coordinate mapping
        │
        ▼
Residue-level conservation
        │
        ├───────────────┐
        │               │
        ▼               ▼
Canonical hotspots    DBD background
        │               │
        └──────┬────────┘
               ▼
      Statistical comparison
               │
               ▼
        Permutation testing
               │
               ▼
      Taxonomic sensitivity
               │
               ▼
        Cancer recurrence
               │
               ▼
     Biological interpretation
```

The main implementation files are:

| Analysis step | File |
|---|---|
| Sequence alignment | [`scripts/01_align_sequences.sh`](scripts/01_align_sequences.sh) |
| Conservation analysis | [`scripts/conservation_analysis.py`](scripts/conservation_analysis.py) |
| Hotspot extraction | [`scripts/hotspot_analysis.py`](scripts/hotspot_analysis.py) |
| Mutation analysis | [`scripts/mutation_analysis.py`](scripts/mutation_analysis.py) |
| Permutation analysis | [`scripts/permutation_analysis.py`](scripts/permutation_analysis.py) |
| Phylogenetic analysis | [`scripts/phylogenetic_analysis.py`](scripts/phylogenetic_analysis.py) |
| Pipeline wrapper | [`scripts/run_pipeline.sh`](scripts/run_pipeline.sh) |

The statistical and methodological notes are in:

- [`docs/methodology.md`](docs/methodology.md)
- [`docs/statistical_analysis.md`](docs/statistical_analysis.md)
- [`docs/provenance.md`](docs/provenance.md)
- [`docs/reproducibility.md`](docs/reproducibility.md)

---

# Conservation metrics

I did not want to represent residue conservation using only one number.

The processed residue table contains:

```text
human_position
human_residue
domain
is_canonical_hotspot
total_species
non_gap_count
gap_count
gap_fraction
majority_residue
majority_count
majority_conservation
human_residue_conservation
shannon_entropy
normalized_entropy
unique_residue_count
```

The table can be inspected directly here:

[`data/processed/residue_conservation.csv`](data/processed/residue_conservation.csv)

For example, the first position is represented as:

```text
human_position            1
human_residue             M
total_species             56
majority_residue           M
majority_conservation      1
human_residue_conservation 1
shannon_entropy            0
```

Using both majority-residue and human-residue conservation helped me avoid treating “most common residue” and “retention of the human residue” as identical concepts.

Entropy provides a separate view of column diversity.

---

# Phylogenetic context

The repository also contains a maximum-likelihood TP53 protein phylogeny for the mammalian dataset.

<p align="center">
  <a href="figures/main/Figure_6_Mammalian_TP53_Phylogeny_CLEAN.png">
    <img src="figures/main/Figure_6_Mammalian_TP53_Phylogeny_CLEAN.png"
         alt="Maximum-likelihood phylogeny of mammalian TP53 protein sequences"
         width="62%" />
  </a>
</p>

The tree file is available at:

[`results/phylogeny/TP53_mammals.treefile`](results/phylogeny/TP53_mammals.treefile)

I use the phylogeny mainly as evolutionary context and as a reminder that a multi-species alignment does not automatically provide statistically independent observations.

That limitation matters throughout the interpretation of this project.

---

# Structural context

The six hotspots do not all affect TP53 in the same way.

A simple functional grouping used in the study is:

### DNA-contact hotspots

```text
R248
R273
```

These residues directly participate in DNA-contact-related functions.

### Structural-core hotspots

```text
R175
G245
R249
R282
```

These are generally interpreted in relation to structural stability and integrity of the DNA-binding domain.

The domain-level recurrence map is shown below.

<p align="center">
  <a href="figures/main/Figure_5_TP53_Domain_Lollipop_Map.png">
    <img src="figures/main/Figure_5_TP53_Domain_Lollipop_Map.png"
         alt="TP53 recurrent mutation map"
         width="90%" />
  </a>
</p>

I consider this classification useful context, but not a substitute for residue-specific structural or experimental validation.

---

# What this study supports — and what it does not

I try to keep this distinction explicit because it is very easy to overstate comparative-genomics results.

| Supported by this analysis | Not established by this analysis |
|---|---|
| Canonical TP53 hotspots occupy strongly constrained residues | Conservation causes cancer recurrence |
| Hotspots are unusually conserved relative to DBD controls | Conservation alone predicts recurrence frequency |
| Conservation and PanCancer recurrence are positively associated | Personal cancer risk |
| The signal remains positive across sampling sensitivity analyses | Statistical independence of mammalian species |
| Conservation can help prioritise functionally sensitive residues | Clinical diagnosis |
| R249 shows that constraint and recurrence are not equivalent | Treatment response or prognosis |
| Evolution provides independent biological evidence | Experimental mechanism |

The sentence I use to summarise the interpretation is:

> **Conservation supports prioritisation, not causation.**

---

# An important note about analysis versions

This repository is also a record of how the project developed, and not every file belongs to exactly the same analytical snapshot.

The associated Research Square preprint and the expanded repository analysis are not identical.

| Version | Scope | How I treat it |
|---|---|---|
| **Preprint v1** | Earlier, narrower analysis | Frozen publication record |
| **Expanded repository analysis** | 56 mammalian TP53 sequences | Current comparative extension |

I do not think these versions should be silently mixed.

The version-reconciliation note is here:

[`docs/analysis_versions.md`](docs/analysis_versions.md)

This matters especially when comparing older intermediate result tables with the expanded residue-level analysis.

---

## A repository inconsistency I am keeping visible

While reviewing the repository for reproducibility, I found that:

[`results/hotspot_analysis/TP53_hotspot_analysis.csv`](results/hotspot_analysis/TP53_hotspot_analysis.csv)

contains hotspot conservation values such as:

```text
R175 = 0.909090909
R248 = 0.909090909
R282 = 0.909090909
```

Those values do **not** match the expanded 56-sequence residue-level table used for the final analysis, where all six canonical hotspots are represented as fully conserved.

I therefore do **not** use that older hotspot CSV as the source for the final 56-sequence hotspot result.

For the expanded analysis, I refer instead to:

- [`data/processed/residue_conservation.csv`](data/processed/residue_conservation.csv)
- [`results/statistics/permutation_hotspot_statistics.csv`](results/statistics/permutation_hotspot_statistics.csv)
- the main figures
- and the final manuscript

I am leaving the mismatch documented rather than quietly deleting it because it records an earlier stage of the analysis and because reproducibility requires knowing which result belongs to which version.

---

# Current reproducibility status

This repository contains the data, scripts and result files needed to inspect the analysis, but I would not currently describe it as a completely verified **one-command rebuild**.

There is one implementation issue that still needs cleanup.

The committed `data/processed/residue_conservation.csv` uses the expanded schema:

```text
human_position
majority_conservation
human_residue_conservation
domain
...
```

while the current [`scripts/conservation_analysis.py`](scripts/conservation_analysis.py) still writes an earlier, simpler schema using fields such as:

```text
alignment_position
conservation
human_residue_frequency
```

Downstream scripts such as [`scripts/hotspot_analysis.py`](scripts/hotspot_analysis.py) and [`scripts/permutation_analysis.py`](scripts/permutation_analysis.py) expect the expanded human-coordinate schema.

So although [`scripts/run_pipeline.sh`](scripts/run_pipeline.sh) records the intended execution order, I currently treat it as a **workflow record that still needs schema reconciliation**, not as a production-ready pipeline command.

I think this is worth stating directly rather than presenting the repository as more polished than it is.

The scientific outputs are preserved; the next software task is to make the computational route to those outputs cleaner and fully reproducible from a fresh checkout.

---

# What I would improve next

If I continue developing this repository, my priorities are not additional figures or visual polish.

They are:

### 1. Consolidate the conservation pipeline

There should be one script that reproduces the exact committed `residue_conservation.csv` schema from the curated alignment.

### 2. Lock the alignment provenance

I want the final pipeline to record:

```text
input FASTA checksum
MAFFT version
MAFFT command
human reference accession
alignment checksum
```

### 3. Regenerate hotspot outputs from the same table

The hotspot CSV should be generated directly from the expanded human-coordinate conservation table so that there is no ambiguity between analysis versions.

### 4. Add automated checks

At minimum, I would like tests asserting that:

```text
human reference length == 393
number of curated sequences == 56
R175 == R
G245 == G
R248 == R
R249 == R
R273 == R
R282 == R
canonical hotspot count == 6
```

and that all final output files can be regenerated without manual editing.

### 5. Move beyond simple residue conservation

The current study uses protein-level conservation.

A deeper evolutionary extension would include:

- codon-aware models,
- lineage-specific selection,
- ancestral reconstruction,
- phylogenetically informed statistical models,
- residue-level structural context,
- stability effects,
- and functional experimental evidence.

That is the direction I find most interesting scientifically.

---

# Repository structure

```text
TP53-Evolutionary-Conservation-Mammals/
│
├── data/
│   ├── raw/
│   └── processed/
│       ├── TP53_curated.fasta
│       ├── TP53_sequence_accession_audit.csv
│       ├── residue_conservation.csv
│       ├── permutation_hotspot_statistics.csv
│       └── structural_class_summary.csv
│
├── scripts/
│   ├── 01_align_sequences.sh
│   ├── conservation_analysis.py
│   ├── hotspot_analysis.py
│   ├── mutation_analysis.py
│   ├── permutation_analysis.py
│   ├── phylogenetic_analysis.py
│   └── run_pipeline.sh
│
├── results/
│   ├── conservation/
│   ├── hotspot_analysis/
│   ├── mutation_analysis/
│   ├── phylogeny/
│   └── statistics/
│
├── figures/
│   ├── main/
│   └── supplementary/
│
├── notebooks/
│
├── docs/
│   ├── methodology.md
│   ├── statistical_analysis.md
│   ├── interpretation_and_limitations.md
│   ├── analysis_versions.md
│   ├── provenance.md
│   └── reproducibility.md
│
├── publication/
│
├── eccb2026/
│
├── quality/
│
├── CITATION.cff
├── requirement.txt
├── LICENSE
└── README.md
```

---

# Main figures

I kept the publication figures in one place so the analysis can be read visually without opening the manuscript first.

<table>
<tr>
<td width="50%" align="center">

<a href="figures/main/Figure_1_Conservation_Profile.png">
<img src="figures/main/Figure_1_Conservation_Profile.png" width="100%" />
</a>

**Figure 1 — Residue-level conservation**

</td>
<td width="50%" align="center">

<a href="figures/main/Figure_2_Hotspot_vs_Control_Boxplot.png">
<img src="figures/main/Figure_2_Hotspot_vs_Control_Boxplot.png" width="100%" />
</a>

**Figure 2 — Hotspots vs DBD controls**

</td>
</tr>

<tr>
<td width="50%" align="center">

<a href="figures/main/Figure_3_Phylogenetic_Sensitivity.png">
<img src="figures/main/Figure_3_Phylogenetic_Sensitivity.png" width="100%" />
</a>

**Figure 3 — Sampling sensitivity**

</td>
<td width="50%" align="center">

<a href="figures/main/Figure_4_Mutation_Count_vs_Conservation.png">
<img src="figures/main/Figure_4_Mutation_Count_vs_Conservation.png" width="100%" />
</a>

**Figure 4 — Recurrence vs conservation**

</td>
</tr>

<tr>
<td width="50%" align="center">

<a href="figures/main/Figure_5_TP53_Domain_Lollipop_Map.png">
<img src="figures/main/Figure_5_TP53_Domain_Lollipop_Map.png" width="100%" />
</a>

**Figure 5 — TP53 recurrence map**

</td>
<td width="50%" align="center">

<a href="figures/main/Figure_6_Mammalian_TP53_Phylogeny_CLEAN.png">
<img src="figures/main/Figure_6_Mammalian_TP53_Phylogeny_CLEAN.png" width="80%" />
</a>

**Figure 6 — Mammalian TP53 phylogeny**

</td>
</tr>
</table>

---

# Installation for inspection

Clone the repository:

```bash
git clone https://github.com/Rita1791/TP53-Evolutionary-Conservation-Mammals.git
cd TP53-Evolutionary-Conservation-Mammals
```

Create a Python environment:

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

Install the Python dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirement.txt
```

MAFFT and IQ-TREE are external command-line dependencies and need to be installed separately for the corresponding alignment and phylogenetic steps.

Because of the schema issue described above, I recommend inspecting or running the scripts individually rather than assuming that `run_pipeline.sh` currently reproduces the final repository state without modification.

---

# Publication

Associated research work:

**Rawat RR, Nadar S, Uppal GK.**  
*Evolutionary Conservation and Functional Constraint of TP53 Mutation Hotspots Across Mammalian Species.*  
2026.

Research Square preprint:

**DOI:** `10.21203/rs.3.rs-9299199/v1`

Repository manuscript:

[`publication/MAIN_MANUSCRIPT_FINAL_SUBMISSION_READY.pdf`](publication/MAIN_MANUSCRIPT_FINAL_SUBMISSION_READY.pdf)

Machine-readable citation metadata:

[`CITATION.cff`](CITATION.cff)

---

# ECCB 2026

This work was selected for presentation at the **25th European Conference on Computational Biology (ECCB 2026)** in Geneva.

I keep conference-specific material separate from the analytical code:

[`eccb2026/`](eccb2026/)

That directory is intended for the poster/presentation version of the work rather than as another source of computational results.

---

# Research team

### Ritika Rajendra Rawat

Study conception, sequence curation, computational analysis, comparative genomics, phylogenetic analysis, cancer-mutation integration, visualisation, interpretation and manuscript preparation.

### Sermarani Nadar

Scientific discussion, interpretation and critical manuscript review.

### Gursimran Kaur Uppal

Scientific discussion, interpretation and critical manuscript review.

---

# How I currently describe this work

I would not describe the result as:

> “Cancer mutates TP53 hotspots because they are conserved.”

That is much stronger than the analysis supports.

The interpretation I am comfortable defending is:

> **Recurrent TP53 cancer hotspots preferentially occupy evolutionarily constrained residues, and this constraint remains detectable even against a domain-matched DNA-binding-domain background. Mammalian conservation therefore provides an independent prioritisation signal for functional sensitivity, but it does not by itself explain cancer mutation recurrence.**

That distinction is the main reason I kept R249 visible throughout the project rather than treating it as an inconvenient exception.

---

# For reviewers and potential collaborators

If you are looking at this repository because of an application, PhD discussion, conference conversation, or possible collaboration, the files that best represent the scientific work are:

- [`publication/MAIN_MANUSCRIPT_FINAL_SUBMISSION_READY.pdf`](publication/MAIN_MANUSCRIPT_FINAL_SUBMISSION_READY.pdf)
- [`data/processed/residue_conservation.csv`](data/processed/residue_conservation.csv)
- [`data/processed/TP53_sequence_accession_audit.csv`](data/processed/TP53_sequence_accession_audit.csv)
- [`results/statistics/permutation_hotspot_statistics.csv`](results/statistics/permutation_hotspot_statistics.csv)
- [`figures/main/`](figures/main/)
- [`docs/analysis_versions.md`](docs/analysis_versions.md)
- [`docs/reproducibility.md`](docs/reproducibility.md)

I am particularly interested in discussing extensions involving:

- comparative cancer genomics,
- evolutionary constraint,
- phylogenetically informed residue analysis,
- ancestral sequence reconstruction,
- protein structure and stability,
- genotype-to-phenotype interpretation,
- and evidence-aware computational genomics.

---

# Contact

**Ritika Rajendra Rawat**

GitHub: [Rita1791](https://github.com/Rita1791)  
LinkedIn: [Ritika Rawat](https://in.linkedin.com/in/ritika-rawat-551107219)  
ResearchGate: [Ritika Rawat](https://www.researchgate.net/profile/Ritika-Rawat-10)  
Email: [ritikarvl2627@gmail.com](mailto:ritikarvl2627@gmail.com)

---

# License

Code and repository-created material are provided under the [MIT License](LICENSE).

External biological datasets retain the terms and citation requirements of their original sources.

---

### Final note

This repository is not meant to look like a perfectly finished software product.

It is a record of a research question that went through dataset expansion, statistical checking, sensitivity analysis, interpretation changes and reproducibility cleanup.

There are parts I would now implement differently, and I have tried to leave those visible.

For me, the useful conclusion is not that conservation gives us a complete explanation of TP53 cancer recurrence.

It is that **evolution provides another independent line of evidence for identifying residues where change appears to be biologically costly — and that evidence becomes more useful when its limitations are kept in view.**
