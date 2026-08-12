<a id="readme-top"></a>

<div align="center">

<p>
  <img src="https://img.shields.io/badge/TP53-EVOLUTIONARY_CONSERVATION-7C3AED?style=for-the-badge&labelColor=111827" alt="TP53 evolutionary conservation">
</p>

🧬 The Residues Evolution Refused to Change

56 mammals · 393 amino acids · 6 cancer hotspots · 0 substitutions

<p>
  A comparative-genomics investigation into a biological contradiction:<br>
  <strong>cancer repeatedly changes the same TP53 residues that evolution preserved.</strong>
</p>

<p>
  <a href="https://github.com/Rita1791/TP53-Evolutionary-Conservation-Mammals"><img src="https://img.shields.io/badge/GITHUB-Repository-181717?style=for-the-badge&logo=github&logoColor=white" alt="Open GitHub repository"></a>
  <a href="https://in.linkedin.com/in/ritika-rawat-551107219"><img src="https://img.shields.io/badge/LINKEDIN-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Connect on LinkedIn"></a>
  <a href="mailto:ritikarvl2627@gmail.com?subject=TP53%20Evolutionary%20Conservation%20Research"><img src="https://img.shields.io/badge/EMAIL-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email the corresponding author"></a>
  <a href="https://www.researchgate.net/profile/Ritika-Rawat-10"><img src="https://img.shields.io/badge/RESEARCHGATE-Profile-00CCBB?style=for-the-badge&logo=researchgate&logoColor=white" alt="View ResearchGate profile"></a>
</p>

<p>
  <a href="https://doi.org/10.21203/rs.3.rs-9299199/v1"><img src="https://img.shields.io/badge/DOI-Read_Preprint-7C3AED?style=flat-square&logo=doi&logoColor=white" alt="Read the preprint"></a>
  <a href="data/processed/TP53_sequence_accession_audit.csv"><img src="https://img.shields.io/badge/DATA-56_Sequences-0F766E?style=flat-square&logo=databricks&logoColor=white" alt="Inspect the sequence audit"></a>
  <a href="CITATION.cff"><img src="https://img.shields.io/badge/CITE-CITATION.cff-1D4ED8?style=flat-square&logo=zotero&logoColor=white" alt="Cite this repository"></a>
  <a href="https://github.com/Rita1791/TP53-Evolutionary-Conservation-Mammals/issues/new"><img src="https://img.shields.io/badge/QUESTION-Open_an_Issue-2563EB?style=flat-square&logo=github&logoColor=white" alt="Open a GitHub issue"></a>
</p>

Evolution said “do not change.” Cancer changed them anyway.

</div>

<table>
  <tr>
    <td align="center" width="25%"><a href="#finding"><strong>⚡ See the answer</strong></a><br><sub>60-second result</sub></td>
    <td align="center" width="25%"><a href="#hotspots"><strong>🎯 Meet the six</strong></a><br><sub>Hotspot evidence</sub></td>
    <td align="center" width="25%"><a href="#evidence"><strong>📊 Explore figures</strong></a><br><sub>Four evidence lenses</sub></td>
    <td align="center" width="25%"><a href="#run"><strong>💻 Inspect the code</strong></a><br><sub>Run and repository map</sub></td>
  </tr>
  <tr>
    <td align="center"><a href="#versions"><strong>🧾 Check versions</strong></a><br><sub>10 vs 56 sequences</sub></td>
    <td align="center"><a href="#boundaries"><strong>🛡️ Audit claims</strong></a><br><sub>Limits and gaps</sub></td>
    <td align="center"><a href="#citation"><strong>📚 Cite the study</strong></a><br><sub>DOI and metadata</sub></td>
    <td align="center"><a href="#contact"><strong>🤝 Collaborate</strong></a><br><sub>Email and profiles</sub></td>
  </tr>
</table>

[!IMPORTANT]Version rule: this repository contains the expanded 56-sequence MAFFT analysis. The linked Research Square preprint is an earlier 10-species snapshot. They belong to the same research programme, but their sample sizes and statistics are not interchangeable.

<a id="story"></a>

01 · 🧩 The biological mystery

TP53 is damaged in a vast range of human cancers, but the mutations are not spread evenly across the protein. A small group of codons is hit again and again.

Mammalian evolution offers a second, independent record: millions of years of sequence change. If the same hotspot residues remain unchanged across divergent mammals, that is evidence that evolution has strongly constrained them.

This project therefore asks one precise question:

Are recurrent human TP53 cancer hotspots unusually conserved across mammals—and does conservation explain how often each hotspot appears in cancer?

The answer has two layers:

What the data say clearly

Where the story becomes interesting

All six canonical hotspots are invariant in the committed 56-sequence table.

Their cancer recurrence is not equally high.

Hotspots are more conserved than the reported DNA-binding-domain control background.

Conservation alone cannot explain the ranking of every hotspot.

Mutation recurrence and conservation show a positive reported association.

R249 is completely conserved but ranks only 19th by mutation count.

<a id="finding"></a>

02 · ⚡ The finding in one screen

<table>
  <tr>
    <td align="center" width="25%">
      <h2>56</h2>
      <sub>curated mammalian<br>TP53 sequences</sub>
    </td>
    <td align="center" width="25%">
      <h2>6 / 6</h2>
      <sub>canonical hotspots<br>fully conserved</sub>
    </td>
    <td align="center" width="25%">
      <h2>P = 0.0236</h2>
      <sub>committed DBD-matched<br>permutation result</sub>
    </td>
    <td align="center" width="25%">
      <h2>ρ = 0.430</h2>
      <sub>reported genome-wide<br>recurrence association</sub>
    </td>
  </tr>
</table>

<div align="center">

Six perfect conservation scores. Six zero-entropy sites. One important exception to a simple story.

</div>



<details>
<summary><strong>How should I read this figure?</strong></summary>

The x-axis follows the 393-residue human TP53 reference. The profile shows how strongly each human-coordinate position is retained across the curated mammalian sequences. The canonical cancer hotspots sit inside the DNA-binding domain and reach the maximum observed conservation value in the committed analysis.

This demonstrates evolutionary constraint. It does not by itself establish why those codons mutate in tumours.

</details>

<a id="hotspots"></a>

03 · 🎯 Meet the six

<table>
  <tr>
    <th>Hotspot</th>
    <th>Functional class</th>
    <th>Mammalian conservation</th>
    <th>PanCancer mutations</th>
    <th>Recurrence rank</th>
  </tr>
  <tr>
    <td><strong>R175</strong></td>
    <td>Structural</td>
    <td><strong>1.000</strong> · invariant</td>
    <td>167</td>
    <td>#3</td>
  </tr>
  <tr>
    <td><strong>G245</strong></td>
    <td>Structural</td>
    <td><strong>1.000</strong> · invariant</td>
    <td>91</td>
    <td>#6</td>
  </tr>
  <tr>
    <td><strong>R248</strong></td>
    <td>DNA contact</td>
    <td><strong>1.000</strong> · invariant</td>
    <td>225</td>
    <td>#2</td>
  </tr>
  <tr>
    <td><strong>R249</strong></td>
    <td>Structural</td>
    <td><strong>1.000</strong> · invariant</td>
    <td>47</td>
    <td><strong>#19 ← the twist</strong></td>
  </tr>
  <tr>
    <td><strong>R273</strong></td>
    <td>DNA contact</td>
    <td><strong>1.000</strong> · invariant</td>
    <td>268</td>
    <td>#1</td>
  </tr>
  <tr>
    <td><strong>R282</strong></td>
    <td>Structural</td>
    <td><strong>1.000</strong> · invariant</td>
    <td>91</td>
    <td>#5</td>
  </tr>
</table>

<sub>Committed sources: residue_conservation.csv and cbioportal_mutation_frequency_by_codon.csv.</sub>

🧨 The R249 plot twist

flowchart LR
    A["R249 across 56 mammals"] --> B["Conservation = 1.000"]
    B --> C["Strong functional constraint"]
    C --> D{"Does that guarantee top cancer recurrence?"}
    D -->|No| E["PanCancer rank = 19"]

R249 is the residue that stops this project from making a lazy conclusion. It is just as conserved as R273 or R248, yet far less recurrent in the committed pan-cancer table.

That gap points to biology beyond conservation: mutational exposure, nucleotide context, tumour type, structural consequences and clonal selection can all shape recurrence. Conservation identifies importance; it does not dictate epidemiology.

[!TIP]The strongest insight is not that conservation and cancer recurrence match. It is that they overlap strongly without being identical.

<a id="workflow"></a>

04 · 🔬 From sequence to biological argument

flowchart TB
    A["56 curated mammalian TP53 proteins"] --> B["MAFFT alignment"]
    B --> C["Human-coordinate mapping<br>NP_001394193 · 393 aa"]
    C --> D["Conservation · entropy · gaps"]
    D --> E{"Challenge the signal"}
    E --> F["Hotspots vs DBD controls"]
    E --> G["Taxonomic sensitivity"]
    E --> H["Cancer recurrence"]
    F --> I["Constraint ≠ complete recurrence model"]
    G --> I
    H --> I

<details>
<summary><strong>Open the full 10-step analytical path</strong></summary>

Curate mammalian TP53 protein sequences with accession-level traceability.

Align the sequences with MAFFT.

Anchor alignment coordinates to the 393-residue human TP53 reference.

Calculate majority-residue conservation, human-residue conservation, entropy and gap statistics.

Confirm the expected human amino acid at R175, G245, R248, R249, R273 and R282.

Compare the six hotspots with non-hotspot residues from the same DNA-binding domain.

Test the hotspot mean using one-sided Mann–Whitney and matched permutation approaches.

Integrate codon-level TCGA PanCancer recurrence exported through cBioPortal.

Challenge taxonomic composition using lineage-removal and order-aware sensitivity analyses.

Add phylogenetic and structural context, then interpret the result within explicit limits.

</details>

<a id="evidence"></a>

05 · 📊 Choose an evidence lens

<details open>
<summary><strong>01 — Constraint: are hotspots exceptional inside the DNA-binding domain?</strong></summary>

<br>



The manuscript reports mean conservation of 1.000 for the six canonical hotspots versus 0.934 for non-hotspot DNA-binding-domain controls, with one-sided Mann–Whitney P = 0.0156. The committed matched permutation table reports empirical one-sided P = 0.02359.

Why use domain-matched controls? Because comparing hotspots with the entire protein would be an easier test. The stricter question is whether hotspots remain unusual even inside TP53's already constrained functional core.

</details>

<details>
<summary><strong>02 — Recurrence: does evolutionary conservation track human cancer frequency?</strong></summary>

<br>



Across all 393 human-coordinate residues, the manuscript reports a positive Spearman association between mutation count and majority-residue conservation: ρ = 0.430; P = 4.49 × 10⁻¹⁹.

The relationship is real at the dataset level, but it is not deterministic. The spread of points—and especially R249—shows why a correlation should not be mistaken for a complete mechanism.

</details>

<details>
<summary><strong>03 — Robustness: is the result just a taxonomic sampling artefact?</strong></summary>

<br>



The analysis tests whether the hotspot-control contrast survives changes in species composition, including removal of overrepresented lineages and order-aware subsets. The reported direction of effect remains positive across the sensitivity analyses.

This reduces—but does not eliminate—the problem of phylogenetic dependence. Fifty-six related species are not equivalent to 56 independent experiments.

</details>

<details>
<summary><strong>04 — Structure: where do recurrent residues sit in TP53?</strong></summary>

<br>



The hotspot set combines DNA-contact residues with structural-core residues. This matters because identical conservation scores can reflect different functional roles and different routes to loss of TP53 activity.

</details>

06 · 🧠 Evidence, not overclaiming

Evidence level

What this repository supports

Observed

All six canonical sites have human-residue conservation 1.000, entropy 0, and no gaps in the committed 56-sequence table.

Compared

Hotspots show greater reported conservation than DNA-binding-domain non-hotspot controls.

Associated

Mutation recurrence and conservation have a positive reported residue-level correlation.

Stress-tested

The effect direction is retained across reported taxonomic sensitivity subsets.

Not established

Causal mechanism, clinical risk, prognosis, treatment response or mutation-specific pathogenicity.

<a id="run"></a>

07 · 💻 Run & inspect

Clone

git clone https://github.com/Rita1791/TP53-Evolutionary-Conservation-Mammals.git
cd TP53-Evolutionary-Conservation-Mammals

Create a lightweight inspection environment

python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirement.txt

<details>
<summary><strong>Show the six committed hotspot records</strong></summary>

python - <<'PY'
import pandas as pd

df = pd.read_csv("data/processed/residue_conservation.csv")
hotspots = df[df["is_canonical_hotspot"] == True]

columns = [
    "human_position",
    "human_residue",
    "human_residue_conservation",
    "shannon_entropy",
    "gap_count",
]

print(hotspots[columns].to_string(index=False))
PY

</details>

<details>
<summary><strong>Re-run the standalone permutation module</strong></summary>

python scripts/permutation_analysis.py \
  --iterations 100000 \
  --seed 42 \
  --output permutation_check.csv

The module runs independently, but its current metric selection does not reproduce every value in the committed permutation CSV. That discrepancy is documented under Scientific boundaries.

</details>

[!NOTE]This is currently an evidence-inspection workflow, not a clean one-command rebuild. The committed tables and figures are usable; the end-to-end script and tests still require schema reconciliation.

08 · 🗺️ Repository map

Area

What lives there

data/raw/

Source mutation exports and supporting inputs

data/processed/

Curated FASTA, accession audit and residue-level conservation

scripts/

Alignment, conservation, permutation and downstream analysis modules

results/

Hotspot, statistical, mutation and phylogenetic outputs

figures/main/

Six publication figures in PNG and PDF

figures/supplementary/

Supplementary visual evidence

docs/

Methods, provenance, interpretation and version rules

publication/

Manuscript source and submitted research material

🚪 Pick your entry point

I want to…

Open

Understand the biology without heavy statistics

result_interpretation_for_non_specialists.md

Review the methods

methodology.md

Audit accessions and data origin

provenance.md

Inspect the statistical logic

statistical_analysis.md

Check limitations before citing

interpretation_and_limitations.md

Separate the 10-species and 56-sequence analyses

analysis_versions.md

<a id="boundaries"></a>

09 · 🛡️ Scientific boundaries

<details>
<summary><strong>What is solid, what is incomplete, and what must not be claimed</strong></summary>

Supported

The six canonical hotspots are invariant in the committed 56-sequence conservation table.

The reported hotspot-control comparison supports unusually strong constraint within the DNA-binding domain.

The reported recurrence correlation supports an association between evolutionary conservation and cancer mutation frequency.

R249 demonstrates that conservation is not a complete predictor of recurrence.

Current reproducibility gaps

The repository has requirement.txt, while some documentation refers to a missing environment.yml.

Alignment and conservation scripts do not yet agree on all paths and output schemas.

Current tests import functions or require columns that do not match the committed implementation and permutation table.

The standalone permutation module does not exactly reproduce the committed null mean under its current metric selection.

Exact software versions, checksums and a clean end-to-end release remain to be locked.

Not supported

Conservation does not prove that a mutation causes cancer.

The study does not estimate personal cancer risk.

The analysis is not a diagnostic, prognostic or treatment-selection tool.

Species cannot be treated as statistically independent observations.

The 56-sequence values cannot be silently substituted into the older 10-species preprint.

For the full audit, read docs/reproducibility.md and docs/interpretation_and_limitations.md.

</details>

<a id="versions"></a>

10 · 🧾 Analysis versions

Evidence snapshot

Scope

Use it for

Research Square preprint v1

Earlier 10-species analysis

The frozen published record

Current repository analysis

Expanded 56-sequence MAFFT analysis

Committed tables, figures and sensitivity results

Mixing these versions would be scientifically wrong. See docs/analysis_versions.md before reporting numerical results.

11 · 🚀 What comes next

Lock a versioned environment and all external tool versions.

Reconcile alignment, conservation and downstream table schemas.

Store permutation metric, seed and iteration count in every result.

Repair tests and add continuous integration.

Add input and output checksums.

Tag the reconciled 56-sequence workflow as a release.

Extend phylogeny-aware modelling beyond subset removal.

Test the evolutionary hypotheses with structural or experimental evidence.

<a id="citation"></a>

12 · 📚 Cite this work

Rawat, R. R., Nadar, S., & Uppal, G. K. (2026).Evolutionary Conservation and Functional Constraint of TP53 Mutation Hotspots Across Mammalian Species.Research Square. https://doi.org/10.21203/rs.3.rs-9299199/v1

Repository citation metadata is provided in CITATION.cff. Before release, replace or remove the placeholder ORCID currently present in that file.

13 · 👥 Research team

Researcher

Contribution

Ritika Rajendra Rawat

Study design, sequence curation, computational workflow, analysis, phylogenetics, cancer-data integration, visualisation, interpretation and manuscript drafting

Sermarani Nadar

Co-author of the associated research

Gursimran Kaur Uppal

Co-author of the associated research

<a id="contact"></a>

14 · 🤝 Contact & collaboration

Interested in comparative genomics, evolutionary oncology, TP53 biology, reproducible bioinformatics or research collaboration? Use the route that matches your purpose:

<table>
  <tr>
    <td align="center" width="25%">
      <a href="mailto:ritikarvl2627@gmail.com?subject=TP53%20Research%20Collaboration"><strong>✉️ Email</strong></a><br>
      <sub>Research and collaboration</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://in.linkedin.com/in/ritika-rawat-551107219"><strong>💼 LinkedIn</strong></a><br>
      <sub>Professional connection</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://www.researchgate.net/profile/Ritika-Rawat-10"><strong>🔬 ResearchGate</strong></a><br>
      <sub>Research profile</sub>
    </td>
    <td align="center" width="25%">
      <a href="https://github.com/Rita1791/TP53-Evolutionary-Conservation-Mammals/issues/new"><strong>💬 GitHub issue</strong></a><br>
      <sub>Technical questions</sub>
    </td>
  </tr>
</table>

<div align="center">

<a href="mailto:ritikarvl2627@gmail.com?subject=TP53%20Evolutionary%20Conservation%20Research"><img src="https://img.shields.io/badge/EMAIL-Ritika_Rawat-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email Ritika Rawat"></a><a href="https://in.linkedin.com/in/ritika-rawat-551107219"><img src="https://img.shields.io/badge/LINKEDIN-Ritika_Rawat-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="Ritika Rawat on LinkedIn"></a><a href="https://www.researchgate.net/profile/Ritika-Rawat-10"><img src="https://img.shields.io/badge/RESEARCHGATE-Follow_Research-00CCBB?style=for-the-badge&logo=researchgate&logoColor=white" alt="Follow research on ResearchGate"></a>

</div>

<div align="center">

The six hotspots were not the end of the analysis.

They were the start of a better question.

Why do equally conserved residues recur so differently in cancer?

⬆ Back to top · 📖 Read the preprint · ⭐ View the repository

<sub>MIT licensed · Computational research only · Not validated for clinical use</sub>

</div>
