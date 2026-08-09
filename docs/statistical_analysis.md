# 📊 Statistical Analysis

> **A transparent statistical framework for evaluating whether recurrent human TP53 cancer-associated hotspot residues exhibit distinct evolutionary conservation relative to an appropriate control set across mammals.**

---

## 🧭 1. Purpose

The statistical component of this project is designed to evaluate the central comparative question:

> **Are recurrent human TP53 cancer mutation hotspots more evolutionarily constrained across mammals than an appropriate set of non-hotspot control residues?**

The statistical analysis is performed after:

1. mammalian TP53 sequence curation;
2. multiple sequence alignment;
3. residue-level conservation measurement;
4. definition of human TP53 cancer-associated hotspots;
5. construction of the control residue set.

The statistical workflow therefore evaluates a **predefined biological hypothesis** rather than identifying hotspots solely from the conservation data.

---

# 🧬 2. Statistical Analysis Framework

The analytical framework can be represented as:

```text
Curated mammalian TP53 sequences
                │
                ▼
       Multiple sequence alignment
                │
                ▼
      Residue-level conservation
                │
                ▼
        ┌───────────────┐
        │ Human TP53    │
        │ hotspot sites │
        └───────┬───────┘
                │
                ▼
      Matched control residues
                │
        ┌───────┴────────┐
        ▼                ▼
   Hotspot group    Control group
        │                │
        └───────┬────────┘
                ▼
       Statistical comparison
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
   Distribution Effect   Null
    comparison   size   model
        │       │        │
        └───────┼────────┘
                ▼
       Biological interpretation

````

* * *

# 🎯 3. Primary Statistical Question

The primary analysis evaluates whether the conservation distribution associated with recurrent human TP53 cancer hotspots differs from that of the selected control residues.

### Null hypothesis

> **H₀:** The conservation values of hotspot residues are not systematically different from those of the control residues.

### Alternative hypothesis

> **H₁:** The conservation values of hotspot residues differ systematically from those of the control residues.

The direction and magnitude of the observed difference are considered together with statistical uncertainty.

* * *

# 🎯 4. Predefined Human TP53 Hotspots

The hotspot analysis focuses on recurrent human TP53 cancer-associated residues:

| Position | Residue |
| --- | --- |
| 175 | **R175** |
| 245 | **G245** |
| 248 | **R248** |
| 249 | **R249** |
| 273 | **R273** |
| 282 | **R282** |

These positions are defined using the human TP53 reference coordinate system.

The hotspot set is therefore specified independently of the mammalian conservation results.

This separation is important because it prevents the analysis from selecting residues as "hotspots" merely because they were found to be highly conserved.

* * *

# 🧠 5. Avoiding Circular Statistical Inference

The analysis follows:

```
Known recurrent human cancer-associated residues
                    ↓
            Map to alignment
                    ↓
        Quantify conservation
                    ↓
       Compare against controls

```

rather than:

```
Find highly conserved residues
                    ↓
Call them cancer hotspots

```

The former approach allows the evolutionary analysis to test an independently motivated biological hypothesis.

* * *

# 🧬 6. Control Residues

The hotspot group is evaluated against a set of **DNA-binding-domain-matched control residues**.

The rationale is that TP53 conservation is not uniform across the entire protein.

A comparison between hotspot residues and every other TP53 residue could therefore be influenced by differences in:

*   protein domain;
*   functional region;
*   structural constraint;
*   evolutionary conservation.

The control strategy therefore attempts to make the comparison biologically more appropriate by retaining the analysis within the relevant TP53 domain context.

* * *

# ⚖️ 7. Hotspot–Control Comparison

The core comparison is:

```
             EVOLUTIONARY CONSERVATION

             ┌─────────────────────┐
             │                     │
             ▼                     ▼
      TP53 HOTSPOTS          CONTROL RESIDUES
             │                     │
             │                     │
             └──────────┬──────────┘
                        ▼
                 Statistical
                  comparison

```

The interpretation focuses on whether hotspot residues show evidence of elevated evolutionary constraint relative to the control distribution.

* * *

# 📊 8. Conservation Measurements

Residue-level conservation values are derived from the curated mammalian TP53 alignment.

The processed conservation dataset is stored at:

```
data/processed/residue_conservation.csv

```

This dataset provides the quantitative measurements used for downstream statistical comparisons.

The statistical workflow therefore operates on derived residue-level measurements rather than directly on raw sequence strings.

* * *

# 📈 9. Primary Distribution Comparison

The primary comparison evaluates the distribution of conservation measurements between:

```
Hotspot residues
        VS
DNA-binding-domain-matched controls

```

The analysis should not rely exclusively on a single summary statistic.

The following characteristics are relevant:

*   central tendency;
*   spread;
*   distributional differences;
*   effect magnitude;
*   uncertainty;
*   robustness under resampling.

This provides a more informative assessment than reporting a p-value alone.

* * *

# 🧪 10. Mann–Whitney U Test

Where implemented in the computational workflow, the Mann–Whitney U test provides a non-parametric comparison between hotspot and control conservation values.

The test is appropriate when the analysis does not require assuming normally distributed conservation measurements.

### Interpretation

A statistically significant result indicates evidence that the two groups differ in their conservation distributions.

However:

> **Statistical significance alone does not establish biological importance.**

The magnitude and direction of the difference must also be considered.

* * *

# 📐 11. Effect Size

Effect size is considered alongside hypothesis-testing results.

This distinction is important because:

```
p-value
   ≠
effect size
   ≠
biological importance

```

A small p-value can occur without a biologically meaningful effect, while a biologically interesting effect may remain uncertain when the sample is small.

Where implemented, the repository therefore retains effect-size estimates alongside the primary statistical comparison.

* * *

# 🔄 12. Bootstrap Analysis

Bootstrap resampling can be used to evaluate the stability of the observed hotspot-versus-control difference.

Conceptually:

```
Observed dataset
       ↓
Repeated resampling
       ↓
Recalculate statistic
       ↓
Empirical distribution
       ↓
Confidence interval

```

The bootstrap framework provides an estimate of uncertainty around the observed statistic without relying exclusively on parametric assumptions.

Bootstrap results should therefore be interpreted as an uncertainty assessment rather than as independent biological observations.

* * *

# 🔁 13. Permutation Analysis

Permutation testing provides an empirical null-model framework for evaluating whether the observed hotspot conservation is stronger than expected under matched random assignment.

The processed permutation results are stored at:

```
data/processed/permutation_hotspot_statistics.csv

```

The corresponding outputs are retained under:

```
results/statistics/

```

Conceptually:

```
Observed hotspot configuration
             │
             ▼
      Calculate statistic
             │
             ▼
     Randomly reassign labels
             │
             ▼
      Repeat many times
             │
             ▼
   Empirical null distribution
             │
             ▼
Compare observed statistic
against null distribution

```

This provides a complementary perspective to the conventional distributional test.

* * *

# 🧬 14. Why Permutation Testing Is Useful

The hotspot set is small and biologically predefined.

Permutation testing therefore provides a useful robustness framework because it asks:

> **Would a comparable hotspot-sized set of residues show a similar conservation pattern under a null model?**

This is different from asking only whether two distributions have different ranks or locations.

* * *

# 🧬 15. Mutation–Conservation Integration

The evolutionary analysis is integrated with human cancer mutation recurrence.

The mutation dataset is stored at:

```
data/raw/cbioportal_mutation_frequency_by_codon.csv

```

The conceptual relationship is:

```
Cancer mutation recurrence
            +
Evolutionary conservation
            ↓
Residue-level integration
            ↓
Mutation–conservation interpretation

```

The mutation dataset is treated as an independent evidence layer from the mammalian sequence conservation analysis.

* * *

# 📊 16. Correlation Analysis

Where implemented, rank-based correlation can be used to evaluate whether mutation recurrence and evolutionary conservation show a monotonic relationship across residues.

A Spearman correlation evaluates the relationship between the ranked values of two variables.

Conceptually:

```
Mutation recurrence
        │
        ▼
      Rank
        │
        │
        ├──────────────┐
        │              │
        ▼              ▼
Conservation       Correlation
     rank              ρ
        │              │
        └──────────────┘

```

A correlation should not be interpreted as evidence of causation.

* * *

# 🌳 17. Phylogenetic Dependence

Mammalian sequences are evolutionarily related.

Consequently, sequence observations across species cannot necessarily be treated as fully independent observations.

This is an important consideration when interpreting evolutionary conservation.

The repository therefore includes phylogenetic analysis and sensitivity analyses to evaluate whether the principal conservation pattern remains stable under alternative taxonomic sampling.

* * *

# 🌿 18. Phylogenetic Sensitivity

The sensitivity framework includes alternative sequence-sampling scenarios such as:

```

1. Full mammalian dataset
2. Excluding primates
3. Excluding rodents
4. Excluding primates and rodents
5. One representative species per mammalian order

```

The purpose is not to claim that these analyses completely remove phylogenetic dependence.

Rather, they evaluate whether the principal observation is strongly dependent on particular taxonomic groups.

* * *

# 🧪 19. Statistical Evidence Hierarchy

The project therefore considers multiple forms of evidence:

```
                 STATISTICAL EVIDENCE
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
 Distribution        Effect size      Permutation
 comparison                            null model
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                 Bootstrap uncertainty
                         │
                         ▼
                Mutation association
                         │
                         ▼
                Phylogenetic sensitivity
                         │
                         ▼
                Integrated interpretation

```

The purpose is to avoid making the scientific conclusion dependent on a single statistical test.

* * *

# ⚠️ 20. Multiple Testing

If multiple independent statistical hypotheses are evaluated, the analysis should distinguish the primary hypothesis from secondary or exploratory analyses.

The principal hotspot-versus-control comparison should therefore be clearly separated from:

*   exploratory correlations;
*   subgroup analyses;
*   phylogenetic sensitivity analyses;
*   structural comparisons;
*   and other secondary analyses.

Any multiple-testing correction should be documented explicitly in the corresponding computational implementation and output.

* * *

# 📌 21. Statistical Interpretation

The statistical results should be interpreted in the context of evolutionary biology.

A statistical difference between hotspot and control residues can support the interpretation that recurrent cancer-associated residues occupy a distinct evolutionary conservation regime.

However:

```
Statistical association
        ≠
Causal mechanism
        ≠
Experimental validation
        ≠
Clinical prediction

```

The analysis therefore supports an **evolutionary hypothesis**, rather than independently establishing a molecular mechanism of TP53 oncogenesis.

* * *

# 🧬 22. Biological Interpretation Boundary

The central biological interpretation should remain appropriately conservative.

Evidence of elevated conservation at recurrent cancer-associated residues would be consistent with the hypothesis that these positions experience strong evolutionary constraint.

However, conservation alone cannot establish:

*   why a particular mutation causes cancer;
*   whether a mutation directly alters TP53 function;
*   whether the evolutionary constraint is responsible for mutation recurrence;
*   or whether a residue is clinically actionable.

Those questions require additional structural, biochemical, cellular, or clinical investigation.

* * *

# 📁 23. Statistical Output Map

| Analysis | Input | Purpose | Repository Location |
| --- | --- | --- | --- |
| Conservation comparison | Residue conservation | Hotspot/control comparison | `results/statistics/` |
| Effect-size analysis | Hotspot/control values | Quantify difference | `results/statistics/` |
| Bootstrap analysis | Conservation values | Estimate uncertainty | `results/statistics/` |
| Permutation analysis | Matched residue set | Empirical null model | `data/processed/` / `results/statistics/` |
| Mutation analysis | cBioPortal-derived data | Mutation–conservation relationship | `results/mutation_analysis/` |
| Phylogenetic sensitivity | Mammalian sequence subsets | Robustness to taxonomic sampling | `results/phylogeny/` |

> **Note:** The table should be updated if the computational implementation uses different filenames or statistical procedures.

* * *

# 🔍 24. Recommended Statistical Audit Path

A researcher reviewing the statistical component can follow:

```
START
  │
  ▼
Human TP53 hotspot definition
  │
  ▼
Control residue definition
  │
  ▼
Residue-level conservation
  │
  ▼
Hotspot vs control comparison
  │
  ├───────────────┬────────────────┐
  ▼               ▼                ▼
Effect size    Bootstrap       Permutation
  │               │                │
  └───────────────┼────────────────┘
                  ▼
       Mutation–conservation analysis
                  │
                  ▼
       Phylogenetic sensitivity
                  │
                  ▼
          Biological interpretation

```

* * *

# ⚠️ 25. Statistical Limitations

Several limitations should be considered.

### Small hotspot set

The predefined hotspot group contains only a limited number of residues.

### Non-independence

Mammalian sequences share evolutionary history.

### Control selection

The statistical conclusion depends partly on the biological appropriateness of the selected control residues.

### Database-derived mutation frequencies

Mutation frequencies depend on the underlying cancer datasets and their sampling characteristics.

### Conservation metric

Different definitions of conservation can emphasize different properties of the alignment.

### Statistical significance

A statistically significant result does not automatically establish biological or mechanistic significance.

* * *

# 🧠 26. Reproducibility Principle

The statistical workflow should remain traceable from:

```
Input dataset
      ↓
Statistical transformation
      ↓
Statistical test
      ↓
Effect estimate
      ↓
Uncertainty estimate
      ↓
Output file
      ↓
Figure / interpretation

```

Each statistical result should therefore be connected to a documented input and computational implementation.

* * *

# 🔗 27. Related Documentation

### Data provenance

👉 [`provenance.md`](provenance.md)

### Methodology

👉 [`methodology.md`](methodology.md)

### Reproducibility

👉 [`reproducibility.md`](reproducibility.md)

### Interpretation and limitations

👉 [`interpretation_and_limitations.md`](interpretation_and_limitations.md)

### Results

👉 `../results/README.md`

### Computational scripts

👉 `../scripts/`

* * *

# 🏁 28. Statistical Analysis Summary

The statistical framework is designed to move beyond a single significance test by combining:

```
Biologically defined hotspots
             +
Domain-matched controls
             +
Residue-level conservation
             +
Distributional comparison
             +
Effect-size estimation
             +
Uncertainty assessment
             +
Permutation-based null testing
             +
Mutation recurrence
             +
Phylogenetic sensitivity
             ↓
     Integrated evidence

```

The objective is not simply to determine whether a p-value crosses a threshold.

The objective is to determine whether the observed relationship between **human TP53 cancer-associated hotspots and mammalian evolutionary conservation** is:

*   statistically supported;
*   quantitatively meaningful;
*   robust to reasonable null models;
*   reasonably stable under alternative taxonomic sampling;
*   and biologically interpretable within the limitations of a computational comparative study.

* * *

> **Scientific principle:**  
> **Statistical evidence should strengthen a biological hypothesis—not replace biological reasoning.**
