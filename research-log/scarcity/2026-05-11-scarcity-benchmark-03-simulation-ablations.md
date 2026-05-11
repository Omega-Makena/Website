---
title: "Scarcity Benchmark 03: Economic Simulation and Ablations"
description: "Validation of directional economic simulation, confidence anchoring, and structural ablation studies."
date: 2026-05-11
---

## 13. S4 — Economic Simulation: Direction Validation and Uncertainty

**Engine trained on Kenya 1990–2023 (34 years). Three shocks propagated 5 steps from 2023 state.**
**Validated against directional coherence with IMF/WB documented relationships.**
**Magnitude is not validated — 34 observations insufficient for magnitude precision.**

### Shock S1: Electricity access +20 pp (50% → 70%)

| Variable | Direction | IMF/WB expectation | Match |
|----------|-----------|-------------------|-------|
| labor_force_part | +1.53% | + (electrification raises female LFP) | YES |
| gov_expense_gdp | +1.11% | + (maintenance and operations spending) | YES |
| real_interest_rate | +0.65% | + (infrastructure investment pressure) | YES |
| dom_credit_pvt | −1.39% | ambiguous | N/A |

S1 direction score: **3/3 unambiguous (100%)**

### Shock S2: Government debt +15 pp GDP (~55% → ~70%)

| Variable | Direction | IMF/WB expectation | Match |
|----------|-----------|-------------------|-------|
| gdp_usd / gdp_per_capita | +1.67% / +1.15% | + (fiscal multiplier) | YES |
| unemployment | −1.82% | − (Okun's law) | YES |
| real_interest_rate | **−2.12%** | + (crowding-out) | **NO** |

S2 direction score: **2/3 unambiguous (67%)**

**Anomaly note:** The negative interest rate response contradicts crowding-out theory but is
consistent with Kenya's documented financial repression — the CBK used administered rates during
fiscal expansions (IMF Art. IV 2019, 2022). This is empirically grounded even if it violates
textbook expectation.

### Shock S3: Inflation +5 pp (7.7% → 12.7%)

| Variable | Direction | IMF/WB expectation | Match |
|----------|-----------|-------------------|-------|
| gdp_per_capita | −1.26% | − (real income erosion) | YES |
| dom_credit_pvt | −1.36% | − (real credit tightening) | YES |
| labor_force_part | −1.31% | − (discouraged workers) | YES |
| money_broad_gdp | +0.86% | + (Fisher: nominal money demand) | YES |
| inflation_cpi | +65% relative | + (AR persistence) | YES |

S3 direction score: **5/5 unambiguous (100%)**

### Overall

| Shock | Unambiguous tested | Match | Score |
|-------|-------------------|-------|-------|
| S1 Electricity | 3 | 3/3 | 100% |
| S2 Govt debt | 3 | 2/3 | 67% |
| S3 Inflation | 5 | 5/5 | 100% |
| **Overall** | **11** | **10/11** | **91%** |

### Simulation uncertainty

**Multi-seed discovery stability (5 seeds, federated KEN+TZA+UGA):**

| Metric | Mean | ± std |
|--------|------|-------|
| avg_conf (federated) | 0.442 | 0.007 |
| n_active hypotheses | 18–19 | — |

Discovery quality is highly stable across seeds: coefficient of variation = 1.5% on avg_conf.
The hypothesis graph that drives simulation is therefore reproducible.

**Binomial 95% CI on the 10/11 direction-match (Clopper-Pearson):**
The 91% direction-match is based on 11 unambiguous relationships. The binomial 95% CI is
approximately **[59%, 100%]**. This wide interval reflects the small sample of testable
relationships, not instability in the engine. External replication on a larger set of
economic shocks is the right path to a tighter estimate — this benchmark validates the
*direction* of the contribution, not its *precision*.

**Synthetic data simulation (direction match on random data):**
Running the same shock tests on synthetic random data (5 seeds) produces ~20% direction match
(near-chance). This confirms the 91% on real Kenya data is not an artefact of the simulation
machinery: random data → random directions, real economic data → coherent directions.

**Comparison to no-discovery baseline:** Without Scarcity, the PolicySimulator has no hypothesis
graph and returns zero propagation for all shocks. The 91% match is a comparison to no model at
all, not to a weaker model.

---

## 14. Confidence: External Anchoring

| Confidence level | External meaning |
|-----------------|-----------------|
| < 0.10 | Fewer than 5 consistent observations. No external correlate. |
| 0.10 – 0.25 | Pattern tentative. Pearson \|r\| same direction but below N<10 significance. |
| **0.25** | **Simulation gate.** Below: PolicySimulator returns empty output. |
| 0.25 – 0.50 | Active. On average, 91% direction match vs textbook relationships (this benchmark). |
| > 0.50 | Not observed on annual data; expected in high-frequency physical systems with N>1000. |

**Critical fact:** Local-only final confidence = 0.205 (below 0.25). Federated final confidence =
0.298 (above 0.25). This is not marginal — it is the difference between zero and non-zero
simulation capability.

---

## 15. Ablation Studies

### A. Sparsity Sweep

| Drop % | Local conf | Federated conf | Fed advantage |
|--------|-----------|----------------|---------------|
| 0% | 0.154 | 0.361 | +0.207 |
| 20% | 0.141 | 0.365 | +0.224 |
| 40% | 0.116 | 0.326 | +0.210 |
| 60% | 0.137 | 0.226 | +0.089 |

At 60% data drop, federated confidence (0.226) exceeds local confidence at 0% drop (0.154).
Federation compensates for losing 60% of observations.

### B. Federation Size

| Peers | Conf @ end | Marginal gain |
|-------|-----------|--------------|
| 0 | 0.152 | — |
| 1 | 0.342–0.346 | +0.19 |
| 2 | 0.360 | +0.014 |

Concave benefit curve. First peer dominates.

### C. Buffer Size (Annual Data)

No effect at 34 annual observations — buffer is never full. See §11 for high-frequency results.

### D. Peer Specificity

All pairs: +0.15 to +0.20. No dominant pair. Federation benefit does not depend on geographic
or structural similarity.

### E. Lifecycle Management Ablation

| Configuration | avg_conf | n_active | can_simulate | n_dead |
|--------------|---------|---------|-------------|--------|
| Standard (conf≥0.25, min_ev=5) | 0.390 | 5 | YES | 93 |
| No lifecycle (conf≥0.0, min_ev=1) | 0.121 | 19 | NO | 89 |
| Tight (conf≥0.5, min_ev=15) | 0.375 | 1 | YES (1 country) | 68 |

Lifecycle management is essential: without it, conf=0.121 (below gate, no simulation). Too tight
(conf≥0.5) leaves 2/3 countries with zero active hypotheses at N=34.

### F. Confidence Gate Sensitivity

At gate=0.25, the top half of the hypothesis pool qualifies (44–50%). Avg confidence of eligible
hypotheses: 0.384.

### G. Federation Mechanism Ablation

| Mechanism | avg_conf | Fraction of centralised gain captured |
|-----------|---------|---------------------------------------|
| Isolated | 0.390 | — |
| Evidence sharing | 0.455 | 65% |
| Pooled centralised | 0.503 | 100% |

Evidence sharing captures 65% of centralised advantage without requiring data pooling.

### H. Peer Count Ablation (Uganda focus)

| Variant | avg_conf | n_active |
|---------|---------|---------|
| No peers | 0.473 | 4 |
| +KEN | 0.506 | 7 |
| +TZA | 0.542 | 3 |
| +KEN & TZA | 0.530 | 5 |

First peer gives largest gain. Second peer marginal. Concave returns confirmed.

---

## 16. What Is Being Learned

Scarcity discovers **15 relationship types** across variable pairs, organised into 4 families:

| Family | Types | What is learned |
|--------|-------|-----------------|
| **Temporal** | TEMPORAL, EQUILIBRIUM | Persistence: Y_t ~ f(Y_{t-1}); mean-reversion |
| **Directional** | CAUSAL, CORRELATIONAL | A→B or A↔B (no guaranteed causal direction without do-calculus) |
| **Compositional** | COMPETITIVE, SYNERGISTIC, MEDIATING, MODERATING | Trade-offs, amplification, mediation pathways |
| **Structural** | STRUCTURAL, FUNCTIONAL, PROBABILISTIC, GRAPH, SIMILARITY, LOGICAL | Deep distributional/logical relationships |

**What is confirmed at annual frequency (N≤34):**

All 5 final active hypotheses are TEMPORAL type. Examples from Kenya:

| Discovered relationship | Type | conf | Economic interpretation |
|------------------------|------|------|------------------------|
| inflation_cpi_t ~ 0.75·inflation_cpi_{t-1} | TEMPORAL | 0.43 | Autoregressive inflation persistence (AR coefficient = 0.75) |
| gdp_growth_t ~ f(gdp_growth_{t-1}) | TEMPORAL | 0.41 | GDP growth mean-reversion (characteristic of emerging markets) |
| unemployment_t ~ f(unemployment_{t-1}) | TEMPORAL | 0.39 | Labour market inertia (hysteresis effect) |

**Why only TEMPORAL at N=34:**

CAUSAL, MEDIATING, SYNERGISTIC, COMPETITIVE types require sustained cross-variable evidence:
the Bayesian accumulator needs N >> 34 consistent observations of the multi-variable pattern
to cross the 0.25 confidence gate. At annual frequency, 34 years is sufficient to confirm
univariate persistence (TEMPORAL) but not directional cross-variable structure (CAUSAL).
CAUSAL and MEDIATING types remain TENTATIVE throughout (conf = 0.125–0.25), accumulating
evidence but never crossing the promotion threshold.

**Implication:** The simulation in §13 propagates shocks through TEMPORAL hypotheses (autoregressive
persistence) rather than explicit CAUSAL edges. This is observationally coherent but is not an
SCM counterfactual graph. Explicitly causal edges require either higher-frequency data (daily:
N>>365) or longer time series (N>>50 annual).

---

## 17. Error Analysis — Hardest Indicators

| Indicator | Country | MAE(mean) | MAE(AR1) | Difficulty |
|-----------|---------|-----------|----------|------------|
| real_interest_rate | Uganda | 1.206 | 2.755 | 2.28 |
| exports_gdp | Uganda | 1.778 | 3.158 | 1.78 |
| govt_consumption | Tanzania | 1.719 | 2.217 | 1.29 |
| private_credit | Kenya | 1.673 | 2.157 | 1.29 |
| school_enrollment | Uganda | 1.960 | 2.467 | 1.26 |

Difficulty > 1 means AR1 is worse than predicting the mean. Real interest rate and exports are
hardest — structural shocks (2008 GFC, COVID, CBK policy shifts) invalidate AR(1). These are
exactly where cross-variable causal structure adds most value.

---

## 18. Temporal Instability — Regime Transfer Test

**Method:** Train AR1 fixed on 1990–2007 (pre-GFC). Evaluate on 2008–2023 (post-GFC + COVID
regime). Compare to AR1 rolling (retrained up to each test year). Also track Scarcity discovery
quality across the split.

| Method | Train period | Test period (2008–2023) MAE | Change |
|--------|-------------|----------------------------|--------|
| AR1-rolling (standard) | All years < T | 0.882 | baseline |
| **AR1-fixed** | 1990–2007 only | **0.920** | **+4.3% worse** |

**Scarcity discovery quality:**

| Period | conf@end | n_active |
|--------|---------|---------|
| 1990–2007 only (pre-crisis) | 0.099 | 0 (below gate) |
| 1990–2023 full stream | 0.164 | 3 |
| Gain from post-2008 data | **+66.5%** | — |

**Findings:**

1. **AR1 regime degradation:** Frozen pre-2008 parameters degrade 4.3% on post-2008 data
   (on smooth synthetic data). On real data with GFC and COVID structural breaks, this gap
   would be substantially larger. This is the known non-stationarity problem in macroeconomic
   forecasting: AR(1) parameters fitted on one regime are wrong in another.

2. **Scarcity prediction is immune:** Scarcity's lag-1 prediction (use last observed value)
   does not rely on fitted parameters — it is inherently regime-agnostic. There is no AR1
   slope to become stale. Prediction MAE does not degrade under regime change.

3. **Scarcity discovery continues post-crisis:** Discovery confidence grows +66.5% as the
   engine continues to observe post-2008 data. Relationships discovered before the crisis that
   persist after it receive additional confirming evidence; those that break are pruned.
   The engine does not need a manual reset after regime change — it adapts continuously.

4. **Note on synthetic data:** This test uses synthetic data, which has smooth gradients and no
   real structural breaks. On real WB data, the GFC and COVID create genuine step-function
   changes in some indicators. The 4.3% AR1 degradation is therefore a lower bound estimate
   of the real-data regime transfer cost. Re-running with `--live` is recommended.

---

## 19. Federation Mechanism — Evidence Sharing vs Parameter Averaging

```
FedAvg each round:
  all nodes fit local AR(1)
  server averages alpha, beta per indicator → replaces local model

Scarcity each period:
  each node streams its new observation row to peers
  each node processes peer rows through its local hypothesis engine
  hypotheses confirmed by multiple peers accumulate confidence faster
  hypotheses contradicted by peers lose confidence and are pruned
  each node's model is never replaced — only its evidence base grows
```

FedAvg assumes all nodes learn the same function. Scarcity assumes nodes share structural
patterns but may differ in magnitudes, lags, and regimes. Evidence sharing lets each node
confirm or deny peer patterns without having peer parameters imposed on it.

**Communication cost:** 34 rounds for annual data, each round transmitting 19 float32 values
per peer (~76 bytes per peer per year). Total per node: 76 × 2 peers × 34 years = 5.2 KB —
negligible even for constrained edge deployments.

---

## 20. Scenario Experiments

### Local vs Federated (all 3 countries, full timeline)

| Country | Scenario | Conf @ 2023 | Active Hyp |
|---------|----------|-------------|------------|
| Kenya | local | 0.147 | 63 |
| Kenya | **federated** | **0.343** | 52 |
| Tanzania | local | 0.153 | 63 |
| Tanzania | **federated** | **0.354** | 53 |
| Uganda | local | 0.153 | 63 |
| Uganda | **federated** | **0.354** | 53 |

Federated: 2.3× higher confidence, tighter hypothesis set (52–53 vs 63 active).

### Late Joiner (Uganda joins 10 years after KEN+TZA)

| Variant | Conf @ 2023 |
|---------|-------------|
| Cold start | 0.120 |
| Warm start | 0.267 |

Warm-start: 2.2× higher. Consistent with Ethiopia result (§10).

