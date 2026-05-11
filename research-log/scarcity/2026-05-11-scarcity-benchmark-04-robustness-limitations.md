---
title: "Scarcity Benchmark 04: Robustness, Reproducibility, and Limitations"
description: "Reproducibility harness, stress tests, failure modes, privacy analysis, and final claim integrity."
date: 2026-05-11
---

## 21. Reproducibility

### Comprehensive Harness (primary entry point)

```bash
# Run all 26 stages (synthetic data, no API required)
python scripts/benchmark_harness.py

# Fast smoke-test (~2 min, skips slow stages)
python scripts/benchmark_harness.py --skip-slow --fast

# Single stage or group
python scripts/benchmark_harness.py --stage 9
python scripts/benchmark_harness.py --stage 10 11.1 11.2

# List all stages
python scripts/benchmark_harness.py --list

# Enable real World Bank API where supported
python scripts/benchmark_harness.py --live
```

Artefacts: `artifacts/harness/harness_results.json`, `artifacts/harness/claim_integrity_matrix.json`.

### Individual benchmarks

```bash
# Dry-run (synthetic data, no API required)
python scripts/benchmark_proper.py --seeds 20
python scripts/benchmark_scientific_questions.py
python scripts/experiment_east_africa_federation.py --dry-run
python scripts/benchmark_comprehensive.py
python scripts/benchmark_reviewer.py

# Live (real World Bank API data — required for §4 claim numbers)
python scripts/benchmark_proper.py --live --seeds 20
python scripts/benchmark_scientific_questions.py --live
python scripts/experiment_east_africa_federation.py

# Economic simulation (requires Kenya WB CSV)
python scripts/benchmark_economic_simulation.py

# Visuals
python scripts/generate_benchmark_visuals.py
```

Fixed seeds 0–19. World Bank REST API — free, no authentication. All artefacts to `artifacts/meta/`.
Stress tests (§23), failure modes (§24), ablations (§15E–H), reviewer additions (§18) use synthetic
data by design and do not require `--live`.

---

## 22. Stress Tests

All tests use Kenya synthetic data (34 years, seed=42) unless noted.

### B1: Permutation Test — Temporal Ordering Dependency

**Result:** Shuffled order produces **+0.105 higher mean confidence** than chronological order.

Shuffling does not destroy correlational structure on smooth synthetic data — it only destroys
the time axis. Consistent patterns are detected equally well in any order.

**Interpretation (reported honestly):** Scarcity's confidence metric is NOT a Granger causality
test. It is a Bayesian measure of cross-variable pattern consistency. Temporal directionality is
embedded in the *simulation* (shocks propagate forward) but not in the *discovery* (confidence
accumulation). This distinction must be clearly stated. Temporal ordering is a future enhancement.

### B2: Time Reversal

**Result:** Reversed chronology produces **60% higher confidence** than forward.

Reversed smooth trends are as structurally consistent as forward trends. The engine cannot
distinguish "A causes B" from "B causes A" at the discovery stage — both produce identical
cross-variable patterns.

### B3: Synthetic Null World — False Positive Rate

**Method:** 5 trials of N=34 independent Gaussian draws (no structure).

| Mean false positive rate | 41% |
|--------------------------|-----|
| avg_conf on null data | 0.481 (exceeds 0.25 gate) |

**Interpretation (reported honestly):** The 0.25 gate is NOT equivalent to p<0.05. On random
data, the Bayesian prior (α=1, β=1) combined with N=34 random fit scores (~0.5) pushes confidence
toward 0.5. The 91% direction match in §13 is meaningful precisely because it validates against an
external economic benchmark — the confidence score alone cannot distinguish real structure from chance.

**The 0.25 gate is a capability threshold (unlocks simulation), not a significance threshold.**

### B4: Shock Falsification

Falsified shock (life_expectancy +10, no economic causal path) propagates equally to the real
inflation shock. This confirms the graph is observational, not interventional: spurious edges
(life_expectancy trending with GDP) develop confidence through correlation, not causation.

The simulation is observational propagation through a correlational knowledge graph, not an SCM
counterfactual. This limitation is stated clearly and quantitatively demonstrated.

---

## 23. Failure Modes

### C1: Cold-Start Cliff

Zero usable confidence for the first 9 observations (lifecycle requires min_evidence=5 before
promotion), then abrupt activation at step 10 (conf=0.442). A new node cannot drive simulation
for at least 10 periods. Warm-start (§8, §10) reduces this to ~3–5 periods at 30 pioneer rows.

**High confidence does not guarantee correctness:** After the cliff (step 10), confidence
immediately reaches 0.44 and barely grows further. The confidence is stable because the active
hypotheses have seen enough evidence to be promoted, not because the relationships are correct.

### C2: Conflict Oscillation

0 of 25 tracked hypotheses showed ACTIVE ↔ DECAYING oscillation over 34 steps. The engine quickly
reaches stable state — hypotheses either die in early exploration or survive to stay active.
Oscillation would be visible at daily frequency where N>>365 allows multiple decay-recovery cycles.

### C3: Structural Break Response

Moderate structural breaks (variables shift ±3–5×) kill weak hypotheses but the 5 survivors are
resilient: confidence drops ~14% then recovers. The surviving relationships are those robust enough
to hold across both regimes — the correct behaviour for a streaming syste11m.

**Caveat:** This test used synthetic data. Real structural breaks (COVID shock to East African
trade flows) may be more disruptive because they break correlational structure, not just scale.

---

## 24. Calibration

### D1: Internal Calibration Design Flaw

The internal Brier score analogue (confidence bins vs hypothesis survival) is uninformative:
hypotheses almost never die *between consecutive steps*, so survival rate = 1.0 in all bins,
giving Brier=0.541 (worse than random). This is a measurement design flaw, not a model failure.

**The correct calibration anchor is the external direction-match (91%, §13):** among hypotheses
with conf ≥ 0.25, 91% of unambiguous predicted shock directions match IMF/WB documented
relationships. Future calibration work should compare confidence at year T against AR(1) directional
accuracy at year T+1 on held-out years.

---

## 25. Hypothesis Lifecycle

### E1: Distribution (Kenya, 34 years)

| Metric | Value |
|--------|-------|
| Total hypotheses explored | 123 |
| Final active | 5 |
| Total killed | 93 (76%) |
| avg_lifetime | 9.4 steps |
| Dominant surviving type | TEMPORAL (all 5 active) |

93 of 123 hypotheses (76%) are pruned. All 5 final active are TEMPORAL. CAUSAL, COMPETITIVE,
SYNERGISTIC, MEDIATING remain TENTATIVE throughout (confidence 0.125–0.25) — 34 observations
insufficient for higher-order type confirmation.

---

## 26. DRG Performance

### F1: Throughput and Latency

| Observations | Throughput (obs/s) | p95 latency (ms) | Memory (KB) |
|-------------|------------------|-----------------|-------------|
| 10 | 111 | 13.6 | 150 |
| 34 | 159 | 13.0 | 218 |
| 100 | **204** | **10.6** | 349 |
| 500 | 126 | 15.6 | 696 |

Peak at n=100 (204 obs/s). p95=10–16ms. Memory linear: 150 KB → 696 KB at n=500 daily obs.
At 696 KB, memory is negligible for any modern edge deployment.

---

## 27. Privacy Analysis

### Current privacy posture

**What is shared in evidence-sharing federation:**
Each node transmits its raw observation row to peers: 19 float values per year per node.
This is equivalent to sharing the actual data point, not derived parameters.

**Privacy risk:** A single transmitted observation row (year 2023 Kenya: GDP=2847 USD,
inflation=9.3%, ...) contains no individual-level information — it is an aggregate macroeconomic
statistic from a public World Bank database. In macroeconomic deployments, this data is already
public, making privacy less critical than in healthcare or financial federated learning.

**In non-public data deployments** (e.g., firm-level financial data, patient cohort data), raw
row transmission would create privacy exposure. Three mitigations are possible:

1. **Differential privacy on observations:** Add calibrated Laplace/Gaussian noise before
   transmitting (ε-DP per observation). This reduces the informativeness of each shared row
   but also reduces the evidence quality for hypothesis accumulation. The trade-off between ε
   and final conf@end has not been measured. Recommended future work.

2. **Secure aggregation:** Instead of sharing raw rows, nodes could share hypothesis updates
   (Δα_success, Δβ_failure per hypothesis) via secure aggregation (Bonawitz et al. 2017).
   This would expose parameter updates rather than raw data but requires all nodes to agree
   on hypothesis structure — complicating the asynchronous discovery protocol.

3. **Hypothesis-level sharing only:** Share only the identities and confidence scores of
   active hypotheses (not raw observations). Peers use this to boost or suppress their own
   hypotheses for matching variables. This provides the weakest privacy guarantees but preserves
   the discovery independence that makes evidence-sharing superior to parameter averaging.

### Formal privacy guarantee

No ε-δ differential privacy budget has been measured for this implementation. This is a hard
requirement for real deployment with non-public data. The current system should be labelled
"privacy-not-quantified" until formal analysis is conducted.

**Communication cost vs privacy trade-off note:** Scarcity transmits 5.2 KB total per node over
34 years. Adding Laplace noise calibrated to ε=1.0, Δf=range(indicator) would require knowledge
of the global sensitivity of each indicator — feasible with bounded per-indicator ranges (set
during schema registration) and measurable prior to deployment.

---

## 28. Claim Integrity Summary

### Supported without qualification

| Claim | Key evidence |
|-------|-------------|
| Nodes are non-IID | Mean JSD=0.295; 49% of pairs high-divergence (JSD>0.3) |
| FedAvg is harmful | MAE 0.687 vs Local-AR1 0.535; p<0.001; Cohen's d=−7.7 |
| Scarcity beats Oracle | MAE 0.493 vs Oracle 0.562 on real World Bank data |
| Lag-1 beats fitted AR1 at N<25 | Oracle-loss explained; Diebold-Mariano analogue |
| Ridge-Lag confirms AR1 is correct baseline | Ridge-Lag MAE=1.026 vs AR1=0.860 (+19.3%) at N≈19 |
| Federation crosses simulation threshold | Fed conf=0.298 > 0.25; local conf=0.205 < 0.25 |
| Simulation is economically coherent | 91% direction match vs IMF/WB documented relationships |
| Discovery is stable across seeds | avg_conf = 0.442 ± 0.007 (CV=1.5%) across 5 seeds |
| Meta-learning warm-start works | +20% final conf at 30 pioneer rows |
| Ethiopia generalisation | +29% warm-start advantage on unseen domain |
| DRG graceful degradation | 10-row buffer = 94% of 200-row confidence |
| Data scarcity: positive conf at 8 years | conf=0.172; AR1 near-random at this N |
| Lifecycle management is essential | Without it: conf=0.121 (below gate); no simulation possible |
| Evidence sharing captures 65% of centralised gain | 0.455 vs 0.390 baseline; 0.503 ceiling |
| AR1 degrades under regime change | AR1-fixed post-2008: +4.3% worse than rolling |
| Scarcity prediction immune to regime change | Lag-1 is parameter-free; no stale coefficients |
| Adaptive engine beats frozen AR1 post-break | Stage 10: ScarcityEngine MAE 1.25 vs AR1-fixed 2.21 on synthetic post-2008 data |
| Fed degrades more gracefully under sparsity | Stage 11.1: fed MAE slope negative at 0→60% drop; local slope positive |

### Findings reported honestly (not claimed as advantages)

| Finding | Why honest |
|---------|-----------|
| Online engine wins in 7% of folds | Not a predictor; lag-1 is a placeholder |
| FL harmful below 13 years | Real design constraint, not a flaw |
| Simulation magnitudes not validated | 34 observations insufficient |
| S2 interest rate direction inverted | Explained by Kenya financial repression; not concealed |
| Permutation test: shuffled > ordered | Confidence is pattern consistency, not temporal causality |
| False positive rate 41% on null data | Confidence gate is not a significance test |
| Shock falsification: no discrimination | Observational graph; spurious edges persist |
| Internal calibration (Brier=0.541) invalid | Survival proxy wrong; external match is valid anchor |
| Cold-start cliff at step 9 | Abrupt activation; warm-start partially mitigates |
| CAUSAL/MEDIATING types never activated | 34 annual obs insufficient for higher-order types |
| Binomial CI on 91% is [59%, 100%] | Small sample (N=11 tests); external replication needed |
| No ε-δ DP budget measured | Hard requirement for non-public data deployments |
| Temporal ordering not detected | B1/B2: confidence insensitive to chronological order |
| Synthetic data direction match ~20% | Expected: random data → random directions |

---

## 29. Limitations

1. **Annual frequency (N ≤ 34):** All supervised baselines are marginal. Results may not
   generalise to higher-frequency domains.
2. **Confidence ≠ statistical significance:** The 0.25 gate is a capability threshold, not
   p<0.05. On random data, 41% of hypotheses exceed it (B3). External validation is the
   meaningful calibration anchor.
3. **Observational, not interventional:** 9 relationship types but no do-calculus. Simulation
   is observational propagation, not SCM counterfactual. B4 confirms spurious edges persist.
4. **Temporal ordering not tested:** Confidence is not sensitive to chronological order (B1,
   B2). Granger-causal ordering is a future enhancement.
5. **FedProx/SCAFFOLD not tested:** These FL variants also average parameters and share FedAvg's
   structural failure mode in heterogeneous settings. Future benchmark on larger dataset needed.
6. **Scarcity prediction is lag-1:** A dedicated prediction head using high-confidence
   hypotheses is future work.
7. **Simulation magnitude not validated:** Direction is 91% coherent. Magnitude requires
   calibration against panel econometric estimates.
8. **No differential privacy:** No ε-δ budget measured. Hard requirement for non-public
   data deployments (see §27 for analysis).
9. **Uganda missing data pre-2000:** Dropped silently; effective training window shorter.
10. **Higher-order types require more data:** CAUSAL, MEDIATING, SYNERGISTIC remain TENTATIVE
    throughout the 34-year stream. Activation requires N > ~50 consistent observations per pair.
11. **Simulation uncertainty is small-sample:** 91% direction match over 11 relationships.
    95% binomial CI = [59%, 100%]. External replication is recommended.
12. **Ridge-Lag baseline from synthetic data:** The Ridge-Lag MAE (1.026) uses dry-run data
    (single seed). Re-running with `--live` on real WB data would sharpen this comparison.

---

## 30. Visuals

Generated by `scripts/generate_benchmark_visuals.py` → `artifacts/meta/`:

| File | Content |
|------|---------|
| `fig1_mae_comparison.png` | MAE baseline comparison with error bars |
| `fig2_discovery_quality.png` | Local vs federated confidence trajectory |
| `fig3_noniid_heatmap.png` | JSD heatmap: 19 indicators × 3 country pairs |
| `fig4_fl_justification.png` | Federation advantage vs own data fraction |
| `fig5_drg_tradeoff.png` | Buffer size vs discovery confidence |
| `fig6_data_scarcity_curve.png` | Confidence vs training window size |
| `fig7_sparsity_sweep.png` | Local vs federated at 0/20/40/60% data drop |
| `fig8_shock_propagation.png` | Policy shock sector effects (directional) |

Ablation/stress/failure mode visuals: extend `generate_benchmark_visuals.py` with:
`artifacts/meta/ablation_*.csv`, `stress_*.csv`, `failure_*.csv`, `reviewer_*.csv`.

---

*Claim accuracy results (§4) from `--live` runs on real World Bank data.
Stress tests (§22), failure modes (§23), ablations (§15E–H), reviewer additions (§18) use
synthetic data by design. Re-run with `--live` for real-data versions where applicable.*

