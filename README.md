<a id="top"></a>

<div align="center">

<a href="figures/main/Figure_5_TP53_Domain_Lollipop_Map.png">
  <img src="figures/main/Figure_5_TP53_Domain_Lollipop_Map.png" alt="TP53 recurrent mutation map across protein domains" width="920">
</a>

TP53 Evolutionary Conservation Across Mammals

Why does cancer repeatedly alter residues that mammalian evolution refused to change?

Ritika Rajendra Rawat · Sermarani Nadar · Gursimran Kaur Uppal · 2026





Results · Research map · Figures · Methods · Code & data · Citation · Contact

</div>

TL;DR

🧬 This study maps recurrent human TP53 cancer hotspots onto an alignment of 56 mammalian TP53 protein sequences. All six canonical hotspots—R175, G245, R248, R249, R273 and R282—are invariant in the committed repository analysis. They are more conserved than non-hotspot residues from the same DNA-binding domain, and cancer mutation recurrence is positively associated with mammalian conservation across the protein. The important exception is R249: evolution preserved it completely, but it ranks only nineteenth by pan-cancer mutation count. That mismatch is the central biological insight—conservation identifies constraint; it does not fully determine cancer recurrence.

Highlights

🎯 Six out of six canonical hotspots are invariant across the committed 56-sequence mammalian dataset.

🧪 Domain-matched testing avoids the weak comparison of hotspots against the entire, unevenly conserved protein.

📊 Canonical hotspots have mean conservation 1.000 versus 0.934 for DNA-binding-domain controls; one-sided Mann–Whitney P = 0.0156.

🎲 The committed matched permutation test reports empirical one-sided P = 0.02359.

📈 Across 393 human-coordinate residues, mutation count and conservation show a reported Spearman association of ρ = 0.430; P = 4.49 × 10⁻¹⁹.

🌳 The hotspot–control contrast remains positive after lineage-removal and order-aware sensitivity analyses.

⚠️ R249 breaks the simplistic story: conservation is not a codon-level model of mutation exposure, tumour selection or cancer frequency.

Contents

Headline result

Research map

The six hotspots

The R249 exception

Visual evidence

Methods in one view

Inspect the analysis

Evidence boundaries

Analysis versions

Publication and citation

Research team

Contact

<a id="headline-result"></a>

Headline result

<table>
  <tr>
    <td align="center" width="25%"><h2>56</h2><sub>curated mammalian<br>TP53 sequences</sub></td>
    <td align="center" width="25%"><h2>6 / 6</h2><sub>canonical hotspots<br>fully conserved</sub></td>
    <td align="center" width="25%"><h2>0.02359</h2><sub>empirical one-sided<br>permutation P</sub></td>
    <td align="center" width="25%"><h2>0.430</h2><sub>reported Spearman ρ<br>across 393 residues</sub></td>
  </tr>
</table>

<a href="figures/main/Figure_1_Conservation_Profile.png">
  <img src="figures/main/Figure_1_Conservation_Profile.png" alt="Residue-level mammalian TP53 conservation profile" width="100%">
</a>

<p align="center"><sub><strong>Click the figure to open it at full resolution.</strong> The six canonical hotspots reach the maximum conservation value in the committed analysis.</sub></p>

Interpretation: the canonical hotspot residues show unusually strong evolutionary constraint. This supports functional sensitivity at those positions; it does not prove why a tumour acquires a particular TP53 mutation.

<a id="research-map"></a>

Research map

#

Question

What was tested

Open the evidence

1  🧬

Where is TP53 conserved?

Residue-level conservation, entropy and gaps across 56 mammalian sequences mapped to the 393-aa human reference.

Conservation profile · Residue table

2  🎯

Are cancer hotspots exceptional?

Six canonical hotspots versus non-hotspot residues from the same DNA-binding domain.

Hotspot comparison · Statistics

3  🌳

Could taxonomic sampling drive the result?

Full dataset, lineage-removal subsets and one-species-per-order sensitivity analysis.

Sensitivity figure · Phylogeny

4  📈

Does conservation track cancer recurrence?

Codon-level TCGA PanCancer/cBioPortal mutation counts integrated with mammalian conservation.

Correlation figure · Mutation data

5  🧩

Where do recurrent residues sit in the protein?

DNA-contact and structural-core hotspots mapped across TP53 domains.

Domain map · Structural summary

6  ⚠️

Where does the simple explanation fail?

R249 used as a counterexample to “high conservation automatically means highest recurrence.”

Interpretation · Limitations

<a id="the-six-hotspots"></a>

The six hotspots

Hotspot

Functional class

Conservation

PanCancer mutations

Recurrence rank

R175

Structural core

1.000

167

#3

G245

Structural core

1.000

91

#6

R248

DNA contact

1.000

225

#2

R249

Structural core

1.000

47

#19

R273

DNA contact

1.000

268

#1

R282

Structural core

1.000

91

#5

<sub>Sources: residue_conservation.csv and cbioportal_mutation_frequency_by_codon.csv.</sub>

<a id="the-r249-exception"></a>

The R249 exception

R249 is perfectly conserved across the mammalian alignment—but only nineteenth by mutation count in the committed pan-cancer table.

That is not an inconvenient outlier to hide. It is the result that prevents overclaiming.

Evolutionary conservation measures long-term protein-level constraint. Cancer recurrence is also shaped by nucleotide context, mutational exposure, tumour type, tissue environment, clone-specific fitness and ascertainment in available cohorts. The two signals overlap, but they are not interchangeable.

Conservation can support

Conservation cannot determine alone

Functional importance of a residue

How often its codon is exposed to a specific mutational process

Long-term intolerance to amino-acid change

Tumour-type-specific selection

Prioritisation for structural or functional testing

Clinical risk, prognosis or treatment response

<a id="visual-evidence"></a>

Visual evidence

<table>
  <tr>
    <td width="50%" align="center">
      <a href="figures/main/Figure_2_Hotspot_vs_Control_Boxplot.png">
        <img src="figures/main/Figure_2_Hotspot_vs_Control_Boxplot.png" alt="TP53 hotspot versus DNA-binding-domain control conservation" width="100%">
      </a><br>
      <sub><strong>Constraint.</strong> Hotspots versus domain-matched controls.</sub>
    </td>
    <td width="50%" align="center">
      <a href="figures/main/Figure_3_Phylogenetic_Sensitivity.png">
        <img src="figures/main/Figure_3_Phylogenetic_Sensitivity.png" alt="Phylogenetic sensitivity analysis of TP53 hotspot conservation" width="100%">
      </a><br>
      <sub><strong>Robustness.</strong> Sensitivity to taxonomic composition.</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <a href="figures/main/Figure_4_Mutation_Count_vs_Conservation.png">
        <img src="figures/main/Figure_4_Mutation_Count_vs_Conservation.png" alt="TP53 cancer mutation count versus mammalian conservation" width="100%">
      </a><br>
      <sub><strong>Recurrence.</strong> Cancer mutation count versus conservation.</sub>
    </td>
    <td width="50%" align="center">
      <a href="figures/main/Figure_5_TP53_Domain_Lollipop_Map.png">
        <img src="figures/main/Figure_5_TP53_Domain_Lollipop_Map.png" alt="TP53 domain and recurrent mutation map" width="100%">
      </a><br>
      <sub><strong>Structure.</strong> Recurrent mutations across TP53 domains.</sub>
    </td>
  </tr>
</table>

<details>
<summary><strong>🌳 Open the mammalian TP53 phylogeny</strong></summary>

<br>

<a href="figures/main/Figure_6_Mammalian_TP53_Phylogeny_CLEAN.png">
  <img src="figures/main/Figure_6_Mammalian_TP53_Phylogeny_CLEAN.png" alt="Maximum-likelihood phylogeny of mammalian TP53 protein sequences" width="100%">
</a>

The maximum-likelihood tree provides evolutionary context for the 56-sequence alignment. Related species are not statistically independent, which is why the study also reports lineage-removal and order-aware sensitivity analyses.

</details>

<p align="right"><a href="#top">↑ Back to top</a></p>

<a id="methods-in-one-view"></a>

Methods in one view

flowchart TB
    A["56 mammalian TP53 proteins"] --> B["Align + map to human coordinates"]
    B --> C["Conservation + entropy"]
    C --> D["DBD tests + phylogenetic sensitivity"]
    D --> E["Cancer recurrence integration"]
    E --> F["Evidence-bounded interpretation"]

<details>
<summary><strong>🔬 Expand the analytical design</strong></summary>

Curate mammalian TP53 protein sequences with accession-level traceability.

Align sequences with MAFFT and anchor positions to the human TP53 reference.

Calculate majority-residue conservation, human-residue conservation, Shannon entropy and gap statistics.

Verify the expected human residues at R175, G245, R248, R249, R273 and R282.

Compare the canonical hotspots with non-hotspot residues from the same DNA-binding domain.

Evaluate the hotspot mean with one-sided Mann–Whitney and matched permutation tests.

Repeat the hotspot–control comparison across taxonomic sensitivity subsets.

Integrate TCGA PanCancer/cBioPortal mutation counts at human TP53 codons.

Add domain, structural-class and maximum-likelihood phylogenetic context.

Separate observed evidence from causal or clinical claims.

Full documentation: methodology · statistics · provenance.

</details>

<a id="inspect-the-analysis"></a>

Inspect the analysis

Clone the repository

git clone https://github.com/Rita1791/TP53-Evolutionary-Conservation-Mammals.git
cd TP53-Evolutionary-Conservation-Mammals

Create an inspection environment

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirement.txt

Open the evidence directly

Need

Start here

Curated sequence set

TP53_curated.fasta

Accession and species audit

TP53_sequence_accession_audit.csv

Residue-level conservation

residue_conservation.csv

Cancer recurrence data

cbioportal_mutation_frequency_by_codon.csv

Permutation result

permutation_hotspot_statistics.csv

Phylogenetic tree

TP53_mammals.treefile

Analysis scripts

scripts/

Reviewer quick start

docs/reviewer_quickstart.md

[!NOTE]The repository currently supports evidence inspection and modular analysis, not a verified one-command clean rebuild. The committed tables and figures can be inspected directly; the end-to-end script, tests and output schemas still require reconciliation before the workflow should be advertised as fully reproducible.

<details>
<summary><strong>🧾 Open the reproducibility audit</strong></summary>

requirement.txt exists, but some documentation still refers to a missing environment.yml.

Alignment and conservation scripts do not yet agree on every path and output schema.

Current tests expect functions or columns that do not consistently match the committed implementation and tables.

The standalone permutation module does not reproduce every committed statistic under its current metric selection.

Exact software versions, checksums and a clean tagged release remain to be locked.

Read the full reproducibility record.

</details>

<a id="evidence-boundaries"></a>

Evidence boundaries

✅ Supported by the study

❌ Not established by the study

Strong mammalian conservation at the six canonical hotspots

That conservation causes a cancer mutation

Greater reported hotspot conservation than DBD controls

Personal cancer risk or diagnostic classification

Positive association between recurrence and conservation

Prognosis, treatment response or clinical utility

Robust effect direction across reported taxonomic subsets

Statistical independence of 56 related species

R249 as evidence that recurrence needs additional explanation

A complete codon-level evolutionary or mutational model

<details>
<summary><strong>⚠️ Read the limitations before reusing a result</strong></summary>

The study uses protein-sequence conservation rather than a codon-aware evolutionary model. Mammalian orders are unevenly represented. TCGA PanCancer/cBioPortal counts reflect the available cohorts rather than universal mutation probabilities. Structural interpretation is class-based and should be extended with experimental structure, stability and DNA-contact evidence. None of the outputs are validated for clinical decision-making.

Full discussion: docs/interpretation_and_limitations.md.

</details>

<a id="analysis-versions"></a>

Analysis versions

[!IMPORTANT]The linked Research Square preprint describes an earlier 10-species analysis. The current repository contains an expanded 56-sequence analysis. Their sample sizes and numerical results must not be mixed.

Evidence snapshot

Scope

Correct use

Research Square preprint v1

Earlier 10-species analysis

Cite as the frozen published record

Current repository analysis

Expanded 56-sequence MAFFT analysis

Use for committed repository tables, figures and sensitivity analyses

See docs/analysis_versions.md for the reconciliation rule.

<a id="publication"></a>

Publication

Rawat, R. R., Nadar, S., & Uppal, G. K. (2026).Evolutionary Conservation and Functional Constraint of TP53 Mutation Hotspots Across Mammalian Species.Research Square. https://doi.org/10.21203/rs.3.rs-9299199/v1



<details>
<summary><strong>📖 Read the study abstract</strong></summary>

TP53 is the most frequently mutated tumour-suppressor gene in human cancer, yet the evolutionary constraints underlying recurrent TP53 mutation hotspots remain incompletely characterised. This study integrates comparative genomics, phylogenetic analysis and cancer mutation data to test whether recurrent human TP53 hotspot residues preferentially occur at evolutionarily constrained mammalian positions. A curated alignment of 56 mammalian TP53 protein sequences was mapped to the 393-residue human reference. All six canonical hotspots were completely conserved and were more conserved than non-hotspot residues within the DNA-binding domain. The pattern remained positive across phylogenetic sensitivity analyses. Mutation recurrence showed a positive association with evolutionary conservation across TP53, while the lower recurrence rank of fully conserved R249 indicated that conservation alone cannot explain the cancer-frequency landscape.

</details>

<a id="cite-this-work"></a>

Cite this work

@article{rawat2026tp53,
  author  = {Rawat, Ritika Rajendra and Nadar, Sermarani and Uppal, Gursimran Kaur},
  title   = {Evolutionary Conservation and Functional Constraint of TP53 Mutation Hotspots Across Mammalian Species},
  year    = {2026},
  journal = {Research Square},
  doi     = {10.21203/rs.3.rs-9299199/v1},
  url     = {https://doi.org/10.21203/rs.3.rs-9299199/v1}
}

GitHub also exposes Cite this repository in the sidebar through CITATION.cff. The placeholder ORCID in that file should be replaced or removed before a tagged release.

<a id="research-team"></a>

Research team

Ritika Rajendra Rawat — conception, computational workflow, sequence curation, analysis, phylogenetics, cancer-data integration, visualisation, interpretation and manuscript drafting.

Sermarani Nadar — scientific discussion, interpretation, critical review and manuscript approval.

Gursimran Kaur Uppal — scientific discussion, interpretation, critical review and manuscript approval.

<a id="contact"></a>

Contact

For comparative genomics, evolutionary oncology, TP53 biology, reproducible bioinformatics or research collaboration:

<div align="center">



</div>

License

Code and repository material are released under the MIT License. Third-party biological data and external resources retain their original terms of use.

<div align="center">

Evolutionary conservation is the evidence trail.

R249 is the reminder not to oversimplify it.

↑ Back to top · Read the preprint · Open the figures · Contact the author

<sub>Comparative-genomics research · Not validated for clinical use</sub>

</div>
