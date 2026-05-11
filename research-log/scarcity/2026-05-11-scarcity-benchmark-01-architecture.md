---
title: "Scarcity Benchmark 01: Architecture and Protocol"
description: "Overview of the Scarcity federated causal discovery system, its four-layer architecture, and evaluation protocol."
date: 2026-05-11
---

# Scarcity — Benchmark Findings Report

**Date:** 2026-05-11 (§39 engine-routed calibration re-run; §38 full-mode calibration results; §37 weakness audit; §36 typed validation v3 fixes; §35 real-data typed discovery validation; §34 synthetic GT validation suite; prior: 2026-04-26 v11 KEN)
**Environment:** Python 3.11.9 | numpy 2.3.5 | scipy 1.15.3 | Windows 11
**Dataset:** World Bank annual indicators — Kenya (KEN), Tanzania (TZA), Uganda (UGA), 1990–2023
**Indicators:** 19 macroeconomic series
**Scripts:** `scripts/benchmark_proper.py`, `scripts/benchmark_comprehensive.py`,
             `scripts/benchmark_reviewer.py`, `scripts/benchmark_economic_simulation.py`,
             `scripts/experiment_east_africa_federation.py`, `scripts/benchmark_scientific_questions.py`,
             `scripts/benchmark_harness.py` (comprehensive 26-stage harness)
**Artefacts:** `artifacts/meta/`, `artifacts/harness/`

---

## Contribution

Scarcity is a **federated causal discovery system for streaming, data-scarce environments** where
supervised methods fail and centralised learning is infeasible. It discovers structural patterns
incrementally as observations arrive — without requiring a full dataset upfront and without
centralising data — and uses those patterns to drive policy simulation.

**The primary contribution is a binary capability unlock:** local evidence accumulation reaches
confidence 0.205 (below the 0.25 simulation gate); federated evidence-sharing lifts confidence
to 0.298 (above the gate), enabling shock propagation that is 91% directionally coherent with
documented economic relationships from IMF and World Bank publications.

This is not a marginal improvement over a weaker model. Without federation, the PolicySimulator
returns empty trajectories for all shocks. With federation, it produces economically meaningful
shock propagation validated against macroeconomic theory. No supervised baseline achieves this:
AR(1) and its variants are predictors, not discoverers; they have no simulation capability at any
level of confidence.

---

## System Architecture

Scarcity is a four-layer platform. The benchmark exercises the bottom two layers directly; the
upper two are the operational consumers of what the benchmark validates.

```
 ┌─────────────────────────────────────────────────────────────────────┐
 │  PRESENTATION LAYER                                                  │
 │  K-SHIELD · Institution Portal · SENTINEL dashboards (Streamlit)    │
 ├─────────────────────────────────────────────────────────────────────┤
 │  INTELLIGENCE LAYER                                                  │
 │  KShieldHub · EconomicGovernor · PulseSensor (15 SIGINT signals)    │
 │  KenyaCalibration · ScenarioTemplates · ScarcityBridge              │
 ├─────────────────────────────────────────────────────────────────────┤
 │  FOUNDATION LAYER  ◄── benchmark targets this layer                 │
 │  scarcity.engine      OnlineDiscoveryEngine (15 hypothesis types)   │
 │  scarcity.federation  FederationNode / FederationHub / baskets      │
 │  scarcity.simulation  MultiSectorSFCEngine + IO structure (KNBS)    │
 │  scarcity.meta        Reptile / MAML meta-learner + GlobalMetaMemory│
 │  scarcity.governor    DynamicResourceGovernor (DRG)                 │
 │  scarcity.causal      DoWhy causal identification                   │
 ├─────────────────────────────────────────────────────────────────────┤
 │  DATA LAYER                                                          │
 │  World Bank REST API · FRED · FederatedDatabases · StreamIngester   │
 └─────────────────────────────────────────────────────────────────────┘
```

### A. OnlineDiscoveryEngine — hypothesis survival paradigm

The engine treats relationship discovery as a **survival-of-the-fittest competition** among
hypotheses. Each hypothesis is a probabilistic model of one relationship between two variables.

```
 Streaming rows
       │
       ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │  HypothesisPool  (up to 15 types per variable pair)             │
 │                                                                  │
 │  CausalHypothesis       — Granger F-test; forward + backward    │
 │                           Bayesian accumulators (α_fwd/β_fwd,   │
 │                           α_bwd/β_bwd); direction set via       │
 │                           F-ratio asymmetry guard (F_fwd/F_bwd  │
 │                           ≥ 1.3); confidence = conf_fwd         │
 │                                                                  │
 │  TemporalHypothesis     — AR(1) autoregressive persistence       │
 │  CorrelationalHypothesis— Online Pearson; bidirectional signal   │
 │  MediationHypothesis    — Two-stage Sobel test (X → M → Y)      │
 │  FunctionalHypothesis   — Polynomial regression                  │
 │  + 10 additional types (Equilibrium, Structural, Compositional, │
 │    Competitive, Synergistic, Moderating, Probabilistic,         │
 │    Graph, Similarity, Logical)                                   │
 └─────────────────────────────────────────────────────────────────┘
       │  each row: fit_step → evaluate → update Bayesian accumulators
       ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │  MetaController — hypothesis lifecycle state machine             │
 │                                                                  │
 │  TENTATIVE ──► ACTIVE ──► DECAYING ──► DEAD                     │
 │                                                                  │
 │  Promotions: conf ≥ 0.25 AND evidence ≥ min_ev                  │
 │  Kill condition: conf < 0.10 AND evidence > 20                   │
 │  BH-FDR at q=0.05: soft penalty (×0.92) on low-evidence hyps    │
 └─────────────────────────────────────────────────────────────────┘
       │
       ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │  HypothesisArbiter — one winner per (source, target) pair        │
 │  Sorted by (confidence, get_strength) descending                 │
 │  Causal > Temporal > Correlational (type priority)               │
 └─────────────────────────────────────────────────────────────────┘
       │
       ▼
 ┌─────────────────────────────────────────────────────────────────┐
 │  HypergraphStore — knowledge graph with temporal decay           │
 │  Edges: (source, target, effect_size, confidence, stability)     │
 │  Simulation gate: confidence ≥ 0.25 → emitted to PolicySimulator│
 └─────────────────────────────────────────────────────────────────┘
```

**Key internal algorithms:**

| Algorithm | Where | Role in benchmark |
|-----------|-------|-------------------|
| Incremental Granger F-test (RLS) | `CausalHypothesis.update()` | Sets direction (+1/−1/0); primary signal |
| Bayesian accumulator (α/β) | `CausalHypothesis` | confidence = α_fwd / (α_fwd + β_fwd) |
| F-ratio asymmetry guard | `relationships.py` | F_fwd/F_bwd ≥ 1.3 before direction commit |
| BH-FDR correction (q=0.05) | `discovery.py` | Penalises low-evidence hypotheses (fix #1) |
| Live-direction override | `relationships.py` | Mini-buffer ≥15 live rows overrides pretrain direction (fix #2) |
| Page-Hinkley drift detection | `vectorized_core.py` | Resets coefficients on structural breaks |
| Thompson sampling (BanditRouter) | `bandit_router.py` | Exploration-exploitation over hypothesis types |
| Sobel mediation test | `relationships_extended.py` | X → M → Y indirect effects |

### B. Federation layer — basket-routed evidence sharing

The benchmark runs federation through `FederationHub` → `FederationNode` → per-basket engines.
This is distinct from FedAvg: nodes share **observation rows**, not model parameters.

```
 ┌───────────────────────────────────────────────────────────────┐
 │  FederationHub                                                 │
 │  ├─ register(node)                                             │
 │  ├─ broadcast(row, source_node_id)                             │
 │  └─ sync_directions() — majority-vote CausalHypothesis dirs   │
 └──────────────────────┬────────────────────────────────────────┘
                        │ peer rows (trust-weighted, renormalised)
          ┌─────────────┼─────────────────┐
          ▼             ▼                 ▼
   FederationNode    FederationNode   FederationNode
       KEN               TZA               UGA
          │
          │  per-basket isolated engines
          ├── basket: macro        → OnlineDiscoveryEngine
          ├── basket: financial    → OnlineDiscoveryEngine
          ├── basket: infrastructure → OnlineDiscoveryEngine
          └── basket: human_capital → OnlineDiscoveryEngine
```

**Basket routing** (`BasketRegistry`) ensures cross-basket contamination is impossible: each
engine sees only the variables in its own sector schema, enforced at both `pretrain()` and
`receive_peer()` boundaries.

**Peer renormalisation** (fix #3): before feeding a peer row to own-country engines, the row is
z-scored to peer-country scale then re-expressed in own-country scale using rolling-window
mean/std (last 15 own observations), removing cross-country level differences while preserving
relative moves.

**begin_live_stream()**: after pretraining, all hypothesis confidences are discounted by 50% and
evidence counts are capped at 10, so live observations can revise pretrained directions without
the MetaController kill condition firing prematurely.

### C. Simulation engine — Stock-Flow Consistent economy

The `PolicySimulator` (and underlying `MultiSectorSFCEngine`) consumes the knowledge graph
produced by the engine. It propagates shocks forward through discovered relationships.

```
  Discovered relationships (conf ≥ 0.25)
          │
          ▼
  ScarcityBridge.create_learned_economy()
          │
          ▼
  MultiSectorSFCEngine  (4 SFC sectors: AGR / MFG / SRV / INFORMAL)
  ├─ production.py    CES output function
  ├─ labor_market.py  Wages + unemployment (Okun's Law)
  ├─ price_system.py  CPI + import prices (Phillips Curve)
  ├─ government.py    Fiscal block (taxes, debt, expenditure)
  ├─ monetary.py      Taylor Rule + interest pass-through
  ├─ foreign.py       Current account + FX
  └─ banking.py       Credit, CAR, NPL
          │
          ▼
  Shock propagation (5 steps from base state)
  → directional response per variable validated vs IMF/WB theory
```

The IO structure (`io_structure.py`) bridges KNBS 9-sector to SFC 4-sector using the standard
IO aggregation formula. Column sums satisfy the Hawkins-Simon condition (AGR=0.42, MFG=0.46,
SRV=0.49), ensuring the Leontief inverse is economically meaningful.

### D. How the benchmark exercises the architecture

The discovery benchmark (`scripts/benchmark_discovery.py`) runs four conditions (A–D) that
directly stress-test specific architectural paths:

| Condition | Engine init | Peer data | Architecture path exercised |
|-----------|-------------|-----------|----------------------------|
| A. Cold-start, no fed | Fresh | None | Engine alone; all signal from 44 KEN rows |
| B. Cold-start + fed | Fresh | TZA+UGA | Hub broadcast + basket routing + peer renorm |
| C. Pretrained, no fed | SSA prior | None | begin_live_stream + live-direction override |
| D. Pretrained + fed | SSA prior | TZA+UGA | All paths; direction sync from hub |

The 70% conf-weighted sign accuracy target in conditions A/B directly measures whether the
**Bayesian accumulator + F-ratio asymmetry guard + BH-FDR** pipeline produces directionally
reliable hypotheses from 44 annual observations. The pretrained conditions (C/D) additionally
test whether **begin_live_stream + live-direction override** can correct SSA-corpus direction
inversion with only 44 live override observations.

---

## 1. What This Benchmark Tests

### Primary claims (paper stands or falls on these)

| Claim | Section |
|-------|---------|
| **C1.** The nodes have genuinely non-IID data — FL prerequisite satisfied | §6 |
| **C2.** Federation is harmful with FedAvg but beneficial with Scarcity's evidence-sharing | §4, §9 |
| **C3.** Scarcity accumulates useful relationship evidence where all supervised baselines fail | §4, §12 |

### Supporting claims

| Claim | Section |
|-------|---------|
| **S1.** Meta-learning warm-start accelerates new node onboarding | §8 |
| **S2.** Scarcity generalises to an unseen domain (Ethiopia) | §10 |
| **S3.** The DRG provides a quantifiable compute/accuracy trade-off | §11 |
| **S4.** Discovered relationships produce economically coherent shock propagation | §13 |

### Characterisation findings (honest accounting, not claims)

| Finding | Section |
|---------|---------|
| Online engine does not outperform batch AR1 on point prediction | §7 |
| FL is harmful below 13 years of local data (cold-start threshold) | §9 |
| Buffer size does not affect annual-frequency results | §15C |
| Confidence ≠ statistical significance; 41% false positive rate on null data | §22 |
| Temporal ordering not detected; confidence measures pattern consistency | §22 |
| Only TEMPORAL hypothesis type confirmed at annual frequency (N≤34) | §17 |

---

## 2. Evaluation Protocol

**Prediction accuracy** — rolling leave-one-year-out:

```
For each year T from (start + 5) to 2023:
    train on all years < T
    predict year T, compute normalised MAE and R²
```

Normalisation: z-score per indicator on training data. MAE < 1.0 beats naive z-score predictor.

**No fold leakage:** Year T is never in the training set. Normalisation statistics are computed
on the held-out actuals after all folds complete — not on training data. Oracle-AR1 uses the same
temporal boundary as Local-AR1 (pools all countries but trains only on rows with year < T).

**Discovery quality** (Scarcity only):
- `conf@end` — mean confidence of active hypotheses at stream end
- `steps→0.25` — first step at which mean confidence crosses the simulation gate

**Statistical rigour:** 20 random seeds, mean ± std, 95% CI, Welch t-test (two-tailed), Cohen's d.

**What seeds affect:**
- RandomBaseline: seeded directly; predictions vary across seeds
- Synthetic data (dry-run): numpy.random seeded; data varies per seed
- AR1, FedAvg, Oracle, Scarcity: deterministic given fixed data; seed-invariant on real WB data

---

## 3. Baselines

| Level | Method | Description |
|-------|--------|-------------|
| Trivial | **Random** | Predict U[min, max] |
| Trivial | **Mean** | Predict training mean |
| Standard | **Local-AR1** | AR(1) per indicator, local data only (Hamilton 1994) |
| Stronger-still-fails | **Ridge-Lag** | Ridge regression on all 18 cross-variable lag-1 features |
| FL standard | **FedAvg-AR1** | AR(1) + federated parameter averaging (McMahan et al. 2017) |
| Upper bound | **Oracle-AR1** | AR(1) on pooled all-node data — not deployable |
| Proposed | **Scarcity** | Scarcity engine, cross-node evidence sharing |

### Why AR(1) is the right supervised baseline

VAR requires N > k·p = 19 rows minimum; LSTM requires ~100+ sequences; ARIMA and Prophet
degenerate on annual data. At N=5–24, AR(1) is the strongest numerically stable supervised
baseline (Hamilton 1994).

**Ridge-Lag validation (§4b):** To confirm this is not a weak baseline choice, we add Ridge
regression with all 18 cross-variable lag-1 features (α=10 regularisation). Despite being
strictly more powerful than AR(1) in capability, Ridge-Lag produces **MAE=1.026 vs AR(1)=0.860**
at mean N=19 training rows with 18 features per indicator — 19.3% worse. This confirms the p/n
ratio (19 features, 5–24 rows) is genuinely the binding constraint, not the choice of AR(1) as
baseline. More complex models fail harder at this sample size.

**Modern FL variants:** FedProx (Li et al. 2020) and SCAFFOLD (Karimireddy et al. 2020) are
stronger FL variants but still average model parameters — they share FedAvg's structural failure
mode in heterogeneous settings. They require larger datasets for a fair comparison.

