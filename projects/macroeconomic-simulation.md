---
title: Macroeconomic Systems
date: 2026-08-15
description: Testing structural relationship discovery under genuine data scarcity.
category: Independent Research
---

# Macroeconomic Systems

### Testing Structural Relationship Discovery Under Genuine Data Scarcity

Macroeconomics is where Scarcity began.

In **April 2025**, I was working on macroeconomic simulation and encountered a practical constraint: annual macroeconomic datasets can contain only a few dozen observations per variable. That creates a difficult regime for methods that need enough observations to estimate a large number of relationships, especially when the underlying data-generating process can change over time.

This became the original research problem behind **Scarcity**:

> **What structure can be recovered from a multivariate system when there are simply not enough observations to estimate everything reliably?**

The macroeconomic work became both the motivating application and one of the framework's main real-data evaluations.

---

## The Dataset

The real-data evaluation uses **World Bank annual indicators for seven East African economies**, covering approximately **1990–2023**.

At the individual-country level, this provides roughly:

**N ≈ 34 observations per variable.**

That is genuine scarcity rather than an artificially downsampled large dataset.

The variables describe interacting aspects of national economic systems, and the objective was not to construct a single forecasting model. Instead, the experiment asks whether Scarcity can recover useful relationships between variables and whether those relationships remain useful when passed into downstream models.

This distinction matters because relationship discovery and prediction are not the same problem.

---

# 1. Discovering Structure

Scarcity processes observations sequentially and maintains a living graph of typed relationships.

For the macroeconomic experiment, the engine was not restricted to correlation or a single notion of causality. It considers **fifteen relationship types**:

* causal
* correlational
* temporal
* functional
* equilibrium
* compositional
* competitive
* synergistic
* probabilistic
* structural
* mediating
* moderating
* graph
* similarity
* logical

The purpose is to distinguish different forms of dependence rather than collapse every observed association into one statistic.

For example, a long-run equilibrium relationship and a contemporaneous correlation are treated as different hypotheses and evaluated using different statistical machinery.

The engine is also streaming: observations are incorporated one row at a time rather than requiring the complete dataset to be available before relationship discovery begins.

---

# 2. Calibration Changes the Result

One of the clearest macroeconomic findings is that **raw relationship confidence cannot be trusted as evidence**.

On the real macroeconomic data, the uncalibrated engine produced a **41% false-positive rate** and ranked the first true relationship at **123rd**.

Applying the calibration gate changes the result substantially.

The calibrated system uses:

1. type-appropriate permutation nulls,
2. false-discovery-rate control,
3. stability selection.

After calibration:

* null false-positive rate: **0.00**
* rank of the first true relationship: **4**

For comparison, the first true relationship ranked:

| Method                   |  Rank |
| ------------------------ | ----: |
| **Scarcity, calibrated** | **4** |
| Correlation + AR scan    |     8 |
| Graphical lasso          |    11 |
| Scarcity, raw confidence |   123 |

The important result is not simply that Scarcity produces a graph.

It is that **calibration materially changes which relationships are considered credible**.

Raw confidence is a ranking mechanism. It is not a significance test.

---

# 3. What Happens When the Graph Is Used?

Recovering structure is only useful if the recovered structure helps with something downstream.

The next experiment therefore fed the discovered macroeconomic graph into downstream learning systems.

This produced an important negative result.

At approximately **N ≈ 34**, a shallow consumer using type-aware structural features improved over raw lag features by roughly **4–7%**.

But increasing model depth did not continue that improvement.

Performance degraded as the downstream consumers became more complex, with a graph neural network ending approximately **96% worse than persistence**.

More importantly:

> **No per-system downstream consumer beat the persistence baseline at N ≈ 34.**

This is a useful boundary for the framework.

The existence of a recoverable relationship does not imply that a complex predictive model can exploit it under severe sample scarcity.

---

# 4. Graph-Conditioned Anomaly Detection

The same question was tested using anomaly detection.

Instead of detecting unusual observations independently for each variable, the graph-conditioned approach asks whether a variable is unusual **relative to its discovered parents**.

This works well in controlled synthetic data, where the generating structure is known and enough observations are available.

The real macroeconomic data produced the opposite result at genuine scarcity.

At **N ≈ 34**:

| Detector                    |       F1 |
| --------------------------- | -------: |
| Blind Z-score               | **0.44** |
| Graph-conditioned detection | **0.19** |

The graph therefore made the real-data anomaly detector worse at this sample size.

A subsequent sample-size sweep showed that the situation changes with more observations. The approximate break-even region where graph conditioning begins to become useful lies between **N ≈ 100 and N ≈ 300** effective observations.

This became one of the more important conclusions of the research:

> **Recovering structure and having enough data to exploit that structure are separate problems.**

Scarcity can recover useful organizational information before the downstream model has enough statistical power to benefit from it.

---

# 5. Federation Across Countries

The macroeconomic setting also provided a natural test of the framework's federation mechanism.

A single country's annual series contains only about 34 observations. Rather than pretending that those observations are sufficient for every relationship type, Scarcity can allow multiple nodes to contribute statistical information without sharing their raw data.

The experiment pooled information from **three countries**, increasing the effective sample from approximately:

**N ≈ 34 → N ≈ 102**

The additional statistical power unlocked relationship types that were weak or effectively inaccessible at the single-country level.

Examples include:

| Relationship type | Single node | Federated |
| ----------------- | ----------: | --------: |
| Equilibrium       |        0.12 |  **0.58** |
| Moderating        |        0.00 |  **0.44** |
| Logical           |        0.18 |  **0.53** |
| Causal            |        0.62 |  **0.96** |

This is one of the places where the framework's central distinction becomes operational:

> **Scarcity does not assume that every node should estimate everything locally.**

The local system can recover structural information while federation supplies additional statistical power.

But the result is not universally positive.

Federation was **target-specific**: some targets benefited while others did not. A coherence signal predicted the direction of federation benefit for **8 of 10 targets**, with **Spearman ρ ≈ 0.50**.

The appropriate conclusion is therefore not that federation always improves learning.

It is that **cross-node information can compensate for some forms of local sample scarcity, but the benefit has to be determined rather than assumed.**

---

# 6. From Economic Structure to Shock Propagation

The macroeconomic work also motivated a second direction: using discovered relationships as the structural substrate for economic simulation.

This became the basis for the later **K-Shield / K-Scarcity** work.

The general pipeline is:

**economic observations**

→ **relationship discovery**

→ **typed structural graph**

→ **economic simulation**

→ **shock propagation**

→ **scenario analysis**

The important distinction is between discovering the organization of an economic system and estimating the magnitude of every possible intervention.

Scarcity's architecture deliberately separates those tasks.

The discovery engine asks:

> **What relationships appear to exist, and of what type?**

The offline causal arm asks a narrower question:

> **For a specified treatment, outcome, and adjustment set, what magnitude can be estimated under the stated assumptions?**

The online engine's causal relationship type is **Granger-predictive**, not structural or interventional. Structural causal identification is delegated to the offline do-calculus pipeline.

---

# 7. What the Macroeconomic Experiment Actually Shows

The macroeconomic results are deliberately mixed.

They show that Scarcity can recover and calibrate structural relationships from extremely short real-world time series.

They also show that this does **not** automatically translate into better prediction or anomaly detection.

The measured results can be summarized as:

### Structure

Calibrated discovery substantially suppresses false positives and improves the ranking of plausible relationships.

### Prediction

Structural information can help shallow consumers, but deeper consumers can overfit the recovered structure under severe scarcity.

### Anomaly Detection

Graph conditioning is harmful at approximately 34 observations and only begins to become useful at substantially larger effective sample sizes.

### Federation

Additional nodes can increase statistical power and unlock relationship types that are underpowered locally, but the benefit varies by target.

### Causal Interpretation

The online discovery layer identifies predictive temporal structure; it does not establish intervention-level causality.

---

# 8. Why This Became Scarcity

The macroeconomic experiment produced the central asymmetry behind the framework.

There are two different things a system might want to recover:

**form** — which variables are related, how they relate, and what kind of relationship is present;

**magnitude** — how large the relationship is for a particular system.

With roughly 34 annual observations, trying to estimate every magnitude independently is often poorly supported.

The research therefore developed a different strategy:

> **Recover structure locally. Borrow magnitude where local data cannot support it.**

That principle eventually became part of the general Scarcity architecture and was subsequently tested outside economics.

---

# Limitations

The macroeconomic results have several important limitations.

**No ground truth.**
Unlike the synthetic and mechanistic experiments, the true causal structure of the real economies is not known. A discovered edge cannot therefore be treated as ground-truth recovery.

**Small samples.**
Approximately 34 observations per country is a fundamental limitation. Some relationship types simply do not have enough information to be reliably distinguished.

**Downstream degradation.**
The real-data experiments demonstrate that successful structure discovery does not guarantee useful downstream prediction.

**Federation is not universally beneficial.**
Pooling can increase statistical power while also introducing cross-node differences and bias. Its usefulness is target-dependent.

**Granger is not intervention.**
The online causal relationship type measures predictive temporal dependence. It does not establish that changing one economic variable would cause another to change.

**Limited geographic scope.**
The evaluation uses seven East African economies and therefore should not be interpreted as a universal test of macroeconomic systems.

---

# Status

This is an **independent research programme and real-data validation of Scarcity**, not a production macroeconomic forecasting system.

The value of the experiment is less in claiming that Scarcity can predict an economy from a few dozen observations and more in establishing the boundary conditions under which structural discovery is useful.

The central result is therefore not:

> *more structure always produces better models.*

It is closer to:

> **Structure can be recovered under scarcity, but exploiting that structure still requires sufficient information.**

That distinction is what led from the original macroeconomic simulation work to the broader Scarcity framework.
