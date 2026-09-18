---
title: BioTwin
date: 2026-08-24
description: Continuous-time biological digital-twin platform for modeling patient state across multiple biological scales and disease domains.
category: Research
---

# BioTwin

### A Hierarchical, Continuous-Time Architecture for Biological State Modeling

BioTwin is an experimental biological digital-twin architecture for modeling evolving biological systems across multiple temporal and biological scales.

The system is designed around three disease domains:

* **CNS conditions**
* **Oncology**
* **Autoimmune disease**

Rather than treating biological observations as a sequence of independent predictions, BioTwin represents the patient as a continuously evolving latent state and assimilates new observations when they provide evidence that the current model is becoming inconsistent with the observed system.

BioTwin is currently a **research prototype**, not a clinical system or validated medical device.

---

## Architecture

BioTwin is divided into two processes with a deliberately narrow boundary.

```text
┌─────────────────────────────────────────────┐
│ embedding_service                           │
│ PyTorch · Offline                           │
│                                             │
│ Raw modality data                           │
│       ↓                                     │
│ Preprocessing                               │
│       ↓                                     │
│ Frozen pretrained encoders                  │
│       ↓                                     │
│ EmbeddingArtifact                           │
└──────────────────┬──────────────────────────┘
                   │
             Artifact Store
                   │
                   ▼
┌─────────────────────────────────────────────┐
│ dynamics_core                               │
│ JAX · Diffrax · Equinox                     │
│                                             │
│ EmbeddingArtifact                           │
│       ↓                                     │
│ Surprise / discrepancy detection            │
│       ↓                                     │
│ Assimilation + structured prior             │
│       ↓                                     │
│ Continuous-time state update                │
│       ↓                                     │
│ PatientStateStore                           │
│       ↓                                     │
│ Multi-scale latent patient state            │
└─────────────────────────────────────────────┘
```

The two processes do not share a runtime.

The **`EmbeddingArtifact` is the sole inter-process contract**. This keeps representation learning separate from the biological dynamics engine and allows the two components to evolve independently.

---

## From Observations to State

The first process converts heterogeneous biological observations into standardized embedding artifacts.

Each artifact carries not only an embedding but also contextual information such as:

* patient identity
* modality
* biological scale
* uncertainty
* missingness
* timestamp
* quality
* provenance
* model version

The second process does not retrain the encoders when new observations arrive.

Instead, it uses the resulting artifacts to update the patient's estimated latent state.

This distinction is fundamental to the architecture:

> **Online behaviour is data assimilation, not online training.**

Population-level parameters are learned offline. Individual patient states and patient-specific posteriors are updated as observations arrive.

---

## Six Biological Scales

BioTwin organizes the latent state across six nested scales:

| Scale       | Characteristic timescale | Example modalities                                  |
| ----------- | ------------------------ | --------------------------------------------------- |
| Subcellular | milliseconds             | Genomics, epigenomics, liquid biopsy                |
| Cellular    | minutes                  | scRNA-seq, proteomics, metabolomics                 |
| Tissue      | hours                    | Histopathology, bulk transcriptomics                |
| Organ       | days                     | MRI, CT, PET, ECG, EEG, microbiome                  |
| System      | weeks                    | Wearables, gait, neuroimmune measurements           |
| Organism    | months–years             | EHR, laboratory measurements, QoL, cognitive scores |

Adjacent scales are coupled through `ScaleCouplingOperator`, allowing information to propagate both upward and downward through the hierarchy.

The resulting dynamics are modeled as a **stiff continuous-time system**: processes operating on very different timescales can influence one another while remaining represented within a common dynamical model.

---

## Continuous-Time Dynamics

The dynamics core uses a latent ODE implemented with **JAX, Diffrax, and Equinox**.

This allows the model to operate on irregularly sampled observations rather than requiring every modality to be synchronized to a fixed timestep.

Missing observations are treated as a normal property of the system rather than an exceptional case.

The solver integrates the latent state between observations, while assimilation updates the state when new evidence becomes available.

---

## Surprise-Driven Assimilation

BioTwin does not update its state simply because a new observation has arrived.

Instead, assimilation can be triggered when the observation indicates a meaningful discrepancy between the model and the observed system.

Three mechanisms are currently defined:

### Innovation

The discrepancy between an observation and its predicted value relative to expected observation noise.

### Prediction Error

Forward prediction error exceeds a defined threshold over a held-out window.

### KL Divergence

The posterior distribution moves sufficiently far from the prior distribution.

These mechanisms produce a `SurpriseSignal`, which determines whether the current state should be assimilated.

The underlying idea is simple:

> **The model should pay attention when the system behaves differently from what it expected.**

---

## Hierarchical Cohort Modeling

Patient-specific modeling is structured as a hierarchical Bayesian problem.

The architecture supports three regimes:

| Regime        | Cohort size | Modeling approach           |
| ------------- | ----------: | --------------------------- |
| `cold_start`  |       N = 1 | Structured knowledge prior  |
| `small_n`     |    N = 2–50 | Partial pooling             |
| `full_cohort` |      N > 50 | Hierarchical Bayesian model |

These are different operating regimes of the same model rather than separate implementations.

In particular, **N = 1 is treated as a strict special case of the hierarchical model**.

As additional cohort information becomes available, the model can move from knowledge-driven priors toward increasingly informed population-level estimates.

---

## Disease Architecture

The disease-specific models share a common latent structure where appropriate.

```text
                SharedImmuneCore
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       CNSHead    OncologyHead   AutoimmuneHead
```

The shared immune representation provides a common structure for biological processes that cross disease boundaries, while disease-specific heads capture domain-specific dynamics.

The current architecture covers:

* neurodegenerative and neuropsychiatric processes
* clonal evolution and treatment resistance
* autoimmune flare/remission dynamics
* neuroimmune interactions

This is an architectural hypothesis rather than a claim that these relationships have been clinically established.

---

## Biological Knowledge as Structural Prior

External biological knowledge is used as a **structural prior**, not as an observation stream.

The knowledge layer can incorporate:

* KEGG
* Reactome
* SNOMED CT
* Gene Ontology
* Human Phenotype Ontology
* DrugBank
* Protein-protein interaction networks
* Gene regulatory networks

These structures are represented through a `BioHypergraphStore` built on the existing Scarcity hypergraph infrastructure.

Their role is to constrain and initialize the model, particularly during cold-start conditions.

---

## Relationship to Scarcity

BioTwin is built alongside the Scarcity codebase and directly reuses its infrastructure rather than maintaining a fork.

The reuse spans several layers:

| Scarcity component     | BioTwin use                                            |
| ---------------------- | ------------------------------------------------------ |
| Runtime                | Event bus, telemetry, drift monitoring                 |
| Resource Governor      | Solver and stiffness-resource management               |
| Federation             | Privacy-preserving distributed learning infrastructure |
| Meta-learning          | Adaptation and cohort-model initialization             |
| FMI                    | Private cross-site meta-prior transport                |
| Relationship Discovery | Typed structural relationship discovery                |
| Hypergraph Store       | Biological knowledge representation                    |
| Forecasting            | Downstream temporal modeling                           |
| Anomaly Detection      | Streaming anomaly detection                            |
| Simulation             | Graph-based shock propagation                          |
| Stream                 | Asynchronous ingestion and replay                      |
| Synthetic              | Cohort and cold-start generation                       |
| Causal                 | Clinical estimand integration                          |

This is substantive reuse of the existing research infrastructure rather than a separate implementation with similar interfaces.

---

## Why the Architecture Exists

Biological data is heterogeneous, asynchronous, incomplete, and distributed across very different scales.

A genomics measurement, an MRI scan, a laboratory result, and a longitudinal clinical observation do not naturally exist on the same temporal axis.

BioTwin therefore explores a different abstraction:

> **Represent the biological system as a continuously evolving state rather than as a collection of independent predictions.**

The architecture then provides mechanisms for:

1. encoding heterogeneous observations,
2. placing them into a multi-scale state representation,
3. evolving that state continuously through time,
4. detecting when observations disagree with the current model,
5. assimilating those observations,
6. and incorporating cohort information without requiring large patient datasets from the beginning.

---

## Current Status

BioTwin is an **experimental research architecture**.

The current work is primarily concerned with whether this decomposition—representation learning, continuous-time dynamics, hierarchical modeling, surprise-driven assimilation, and structured biological priors—provides a coherent foundation for biological digital-twin research.

It should not be interpreted as clinical validation, diagnostic software, treatment recommendation infrastructure, or a deployed patient-management system.

The architecture is intentionally explicit about these boundaries.

---

## Research Direction

BioTwin explores whether biological systems can be modeled through **continuous state estimation across nested scales under irregular and incomplete observation**.

The central research questions are therefore not simply:

> Can the model predict the next observation?

They are closer to:

> Can a useful latent biological state be maintained as new and incomplete evidence arrives?

> Can that state remain coherent across biological timescales?

> Can structured biological knowledge improve estimation when patient data is scarce?

> And can discrepancies between modelled and observed behaviour provide a principled trigger for state assimilation?

These are the questions the current architecture is designed to investigate.
