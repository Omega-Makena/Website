---
title: "Scarcity: A Streaming Relationship-Discovery and Federated-Learning Framework for Multivariate Time Series Under Data Scarcity"
description: Preprint outlining the Scarcity framework, its methodology, and its measured behaviour.
section: Writing
subsection: My Papers
date: 2026-09-18
---

**Author:** Omega Makena M. *(corresponding: mwebiamakenaa@gmail.com)*
**Affiliation:** Innova Limited
**Preprint — draft, September 2026. Not peer reviewed.**

---

## Abstract

Many real multivariate time series arrive under scarcity: few samples per variable, high noise,
and a data-generating process that drifts. We present **Scarcity**, a framework that learns and
maintains a living knowledge graph of *typed* relationships from such streams, one row at a time.
Its discovery core reasons over **fifteen relationship types** — causal, correlational, temporal,
functional, equilibrium, compositional, competitive, synergistic, probabilistic, structural,
mediating, moderating, graph, similarity, and logical — of which causal dependence is one class
among many, not the headline. Each candidate relationship is a **hypothesis with a lifecycle**:
born tentative, promoted to active as evidence accumulates, decayed and pruned when evidence turns
against it or a regime break is detected. Two design commitments organize the framework. First,
**calibration before trust**: the engine's raw per-edge confidence is not a significance test, and
edges are gated against a type-appropriate permutation null with false-discovery-rate control and
stability selection before they are believed. This gate is the engine's **default**, runs online with
an autocorrelation-robust effective-sample-size correction, and returns each surviving edge with a
p-value and a partial-R² effect size; an explicit **epistemic ladder** then carries an edge only as
far as the evidence allows — from discovered, through calibrated and predictive, to identified,
estimated, and robust — refusing to silently upgrade a claim past what has been shown. On a controlled
synthetic benchmark with known ground truth this yields exact structure recovery (strict edge
F1 = 1.00; per-type recall = 1.00 across all fifteen types) at a measured null false-positive rate of
0.00, and against a panel of five classical detectors across six canonical failure modes it is the
only method that reaches the correct answer in every one. Second, a deliberate **refusal**: the
framework recovers and trusts *structure* cheaply but declines to estimate per-system *magnitudes*
freely, borrowing them instead from a **federation** of peers that never share raw data — pooling
three countries of macroeconomic data (effective sample ≈34→102) raised the maximum confidence of
otherwise-underpowered relationship types (equilibrium 0.12→0.58, moderating 0.00→0.44, logical
0.18→0.53) and unlocked all fifteen. Around this sit meta-learning (episodic memory and an online
Reptile optimizer that carry priors across domains), a dynamic resource governor (keeping every
component within a compute budget), and privacy machinery (local differential privacy and secure
aggregation). The framework has been run across three domains — macroeconomics, a mechanistic
biological twin (four disease models where it recovers the known coupling graph, form F1 up to 1.00
against a zero shuffle null), and live Bitcoin microstructure (where it recovers and correctly
*types* a 29-edge order-flow graph) — and it is the discovery layer of a national
economic-intelligence platform and a high-frequency trading system, not only a benchmark artefact.
We are candid about limits. On real macroeconomic data at genuine scarcity (N≈34),
graph-conditioned anomaly detection *loses* to a blind Z-score baseline, and the break-even where
discovered structure begins to help lies at roughly 200–300 effective observations; forecasting
shows no dominant method with bootstrap confidence intervals too wide (±1.0–1.5 MAE at 24 test
points) to certify most differences; and federation helps some targets and hurts others. The
framework's discovery is Granger-predictive, not interventional: structural causal identification is
explicitly out of scope for the online engine and delegated to a separate offline do-calculus
pipeline. Scarcity is domain-agnostic — no module carries domain logic — and is released as an
installable Python package. This paper introduces the framework, its methodology, and its measured
behaviour, honest results and honest failures alike.

---

## 1. Introduction

The word *scarcity* carries two senses here, and the framework is named for both.

*Scarcity, the regime* is a data condition: few samples per variable, high measurement noise, and a
data-generating process that will not sit still. It is the ordinary situation for a great deal of
real-world data — an annual macroeconomic series has a few dozen points, a new sensor deployment has
days of history, a cold-start domain has almost nothing — and it is exactly the regime in which
standard batch methods, which assume enough data to estimate everything at once, are least at home.

*Scarcity, the framework* is the system this paper introduces: a streaming engine that ingests such
data one row at a time and maintains a living knowledge graph of typed relationships between
variables. Its organizing question is not "what is the best model of this dataset?" but "as evidence
trickles in, which relationships can I actually justify believing, of what kind, and how confident
should I be — and which magnitudes should I decline to estimate and borrow from elsewhere instead?"

The framework rests on one conviction and one discipline. The conviction is that **relationships are
active constraints that must survive new evidence** — not results computed once, but hypotheses that
live or die as data arrives. The discipline is that **structure and magnitude are recovered on
different terms**: the form of a relationship (its existence, type, and direction) is treated as
cheap to recover and worth trusting once calibrated; its magnitude (the effect size, the rate
constant) is treated as expensive and often not identifiable from one scarce stream, and is borrowed
from a federation of peers rather than invented locally. Everything else in the framework —
calibration, federation, meta-learning, resource governance — follows from those two commitments.

This paper describes the framework's design (§2–§3), its discovery methodology and the fifteen
relationship types (§4), the calibration procedure that turns raw scores into trustworthy edges
(§5), the federation and meta-learning that supply borrowed magnitudes and cross-domain priors (§6),
and the measured behaviour on both controlled and real data — including where it fails (§7–§8). A
companion theoretical paper interprets these behaviours; here we stay with the engineering and the
evidence.

---

## 2. Design Principles

Five principles run through every module.

**Hypothesis survival.** A relationship is not a finding but a standing constraint. Every candidate
enters a lifecycle — *tentative* on proposal, *active* once confidence and stability cross
thresholds, *decaying* when evidence weakens or a structural break is detected, *dead* when
confidence collapses — so the knowledge graph is adaptive rather than a one-shot snapshot.

**Calibration before trust.** The engine's per-edge confidence is a ranking signal, not a p-value.
No edge is trusted until it has passed a type-appropriate permutation null with false-discovery-rate
control and stability selection (§5). This is the single most important methodological guardrail in
the framework: without it, raw confidence produces confident nonsense.

**The refusal — recover structure, borrow magnitude.** The framework recovers form cheaply and
trusts it once calibrated, but it does not freely estimate per-system magnitudes that a scarce
stream cannot support. Those are borrowed from the federation. This is a deliberate asymmetry, not a
missing feature.

**Domain agnosticism.** No module contains domain-specific logic. Variable names are strings,
relationship types are general statistical patterns, groupings are configurable. The same engine
runs on any multivariate time series; the framework was explicitly decoupled from its original
economics domain so that nothing domain-specific remains.

**Decoupling through an event bus, privacy by default, and adaptive resource control.** Modules
communicate through a shared asynchronous EventBus and do not call each other directly, so any
component can be replaced or disabled without breaking the others; the federation layer applies
differential privacy before any update leaves a node and uses secure aggregation so the server never
sees a raw update; and a single resource governor is the only component permitted to reach into
others and adjust their runtime parameters, keeping the whole system within a compute budget.

---

## 3. Architecture

Scarcity is layered. Reading from the foundation upward:

- **`runtime/` — foundation.** An asynchronous pub/sub EventBus plus telemetry: latency tracking,
  data- and concept-drift monitors. Every module depends on this; nothing else is depended on so
  universally.
- **`stream/` — ingestion.** Reads any source, segments it into sliding or tumbling windows, tracks
  schema evolution, shards by variable group, and supports deterministic replay for reproducibility.
  A PI-controller regulates ingestion rate under backpressure.
- **`engine/` — the discovery core (§4).** Maintains a pool of competing relationship hypotheses,
  promotes the strongest into the knowledge graph, and continuously revises it. The largest module.
- **`causal/` — offline inference.** A batch do-calculus pipeline (DoWhy identification + EconML
  heterogeneous effects) that quantifies effect *magnitudes* for a specific query. Complementary to
  the engine: the engine finds *what* to investigate, this estimates *how much*, with two validity
  layers — refutation tests (placebo, random common cause, subset) for robustness to perturbation,
  and a Cinelli–Hazlett omitted-variable-bias **sensitivity analysis** for robustness to a
  confounder that was never measured (the robustness value: how strong such a confounder would have
  to be to explain the effect away).
- **`federation/` — federated learning (§6).** Multiple nodes learn a shared graph without moving
  raw data; two-layer aggregation, gossip, secure aggregation, a differential-privacy guard, trust
  scoring, and conflict reconciliation.
- **`fmi/` — federation–meta interface.** Translates aggregated federation updates into priors and
  adaptation signals the meta-learner can consume, and back.
- **`meta/` — meta-learning (§6).** Episodic memory keyed by context embedding, plus an online
  Reptile optimizer that accumulates a good initialization across domains and warm-starts new ones.
- **`governor/` — dynamic resource governor.** A tight control loop (default 0.5 s) that senses CPU,
  memory, and latency, forecasts usage, and throttles or expands each subsystem against per-subsystem
  policies.
- **`synthetic/` and `dashboard/`.** Ground-truth data generation and benchmarking; a thin read-only
  FastAPI window onto the live engine.

The one-way dependency on the EventBus is the structural backbone: `stream → engine → exporter → bus`
is the only direct path; every other interaction is a published event that any module may subscribe
to or ignore.

---

## 4. The Discovery Core

### 4.1 The hypothesis lifecycle

Every potential relationship between two variables begins as a hypothesis and is carried through a
four-state lifecycle by three cooperating components. The **HypothesisPool** is the registry of all
living hypotheses; it enforces a capacity limit and includes a regime tracker that uses a cumulative-sum
(CUSUM) test to detect structural breaks — shifts in the data-generating process that should trigger
re-evaluation of every active hypothesis. The **MetaController** drives the state transitions
(tentative→active→decaying→dead) against evidence, stability, and confidence thresholds. The
**BanditRouter** decides which candidate relationships to explore next, maintaining a Beta posterior
per relationship-type arm (Thompson sampling by default) so exploration of rare types is balanced
against exploitation of productive ones, updated by the **Evaluator**, which scores candidates by
predictive gain, bootstrap confidence, and stability, with a latency penalty and a diversity bonus.

An **AdaptiveGrouper** maintains a dynamic clustering of variables — groups split when variables are
better explained apart and merge when they behave as a unit — to prioritize which pairs the pool
examines, and a **HypothesisArbiter** resolves contradictory claims about the same pair using a fixed
type hierarchy (logical > functional > causal > compositional > temporal > competitive/synergistic >
structural > correlational/probabilistic/equilibrium), breaking ties by confidence.

### 4.2 The fifteen relationship types

Relationships are not interchangeable; each type is tested on its own statistical footing.

| Type | What it captures | Statistical basis |
|------|------------------|-------------------|
| Causal | A drives B with a lag | Granger causality |
| Correlational | A and B move together | Pearson correlation |
| Temporal | Auto-regressive structure | AR/VAR via recursive least squares |
| Functional | A is a smooth function of B | Local polynomial / Nadaraya–Watson |
| Equilibrium | A and B revert to a long-run balance | Engle–Granger cointegration + Dickey–Fuller |
| Compositional | B is a linear combination of several variables | Multivariate regression |
| Competitive | A gains as B loses | Variance-difference F-test |
| Synergistic | A and B jointly exceed their parts | Partial F-test on interaction |
| Probabilistic | A and B share a distribution family | KS two-sample + Jensen–Shannon |
| Structural | A partitions B into distinct groups | Intraclass correlation (ANOVA-based) |
| Mediating | C carries the A→B path | Sobel test on the indirect effect |
| Moderating | C changes the strength of A→B | Partial F-test on the interaction |
| Graph | Non-linear coupling a linear test misses | Mutual information vs Pearson excess |
| Similarity | Variables fall into shared clusters | k-means++ with online silhouette |
| Logical | A and B satisfy a Boolean rule | Rule-based test |

Causal dependence is one row of fifteen — the hardest to establish and, in this framework, the least
privileged: the online engine measures Granger-style predictive structure, and any claim stronger
than that is delegated to the offline `causal/` pipeline (§3) and hedged accordingly (§8).

### 4.3 Estimators, hardening, and the two backends

Every model update is guarded against the pathologies of continuous noisy streams: a **Winsorizer**
clips values to the 1st–99th percentile so outlier spikes cannot corrupt the recursive-least-squares
covariance, an **online median-absolute-deviation** estimator supplies a robust spread, and a **Huber
gradient** degrades gracefully under outliers.

Each of the fifteen types carries a **standard, literature-grounded estimator** rather than an ad-hoc
score: Granger F-tests with transfer entropy for causality, Miller–Madow-corrected mutual information
for non-linear coupling, an augmented Dickey–Fuller test for equilibrium, a Sobel test on the
indirect path for mediation, one-way ANOVA for structural grouping, and interaction F-tests for
synergy and moderation, with a Wilson–Hilferty χ² approximation as a scipy-free fallback. A recurring
discipline underlies them: because a bare significance test is uniform under the null and therefore
false-fires, the specialized estimators gate on **effect size** — near zero under the null regardless
of sample size — not on raw significance.

The engine runs on **two interchangeable backends behind one interface.** The **batched (tensor)**
path (`vectorized=True`, `GPUDiscoveryEngine`) is the **default whenever `torch` is present**: it
processes all hypotheses per row as a single tensor operation — a batched recursive-least-squares
kernel over the whole pool, with hypotheses regrouped by their functional form so each estimator runs
once across its whole cohort rather than in a Python loop — and implements the same fifteen type
estimators in batched form (interaction-coefficient significance for synergy and moderation, a Sobel
test from the stored series for mediation, batched ANOVA for structure, an AR(1) unit-root test for
equilibrium, and effect-size-gated tests for the conditional and logical types). Regrouping the
hypotheses by functional form so each estimator runs once per cohort — rather than once per hypothesis
inside a Python loop — is what makes the tensor path fast: on GPU it collapses the per-row work to a
handful of batched operations over the whole pool, an order-of-magnitude speedup on a wide pool that
returns the same typed graph (the shipped `scaling.py` benchmark reports per-row throughput for both
backends across pool sizes). The **pure-Python** path (`vectorized=False`)
remains the authoritative reference for reproducibility — it streams the hypothesis objects one row at
a time, needs no GPU, and is the backend behind this paper's synthetic and real-data tables; the
batched path falls back to it cleanly when torch is absent (`vectorized=None` selects automatically).
Both backends emit the identical `get_knowledge_graph()` and the GPU path is validated both by
construction — each estimator fires on data that contains its relationship and stays quiet on data
that does not — and against the pure-Python path directly.

The recursive-least-squares core is hardened for long streams. Because the RLS covariance can wind up
and diverge to non-finite values after several thousand steps, each update symmetrizes the covariance
and caps its trace, so the batched kernel stays numerically stable at the hundred-thousand-row scale
of the microstructure study (§7.2) rather than emitting `NaN` confidences.

---

## 5. Calibration: Turning Scores Into Trustworthy Edges

This is the methodological heart of the framework, and the reason its recovery numbers are worth
anything. The engine emits, per candidate edge, a raw confidence and a fit statistic. Neither is a
significance test. An edge is trusted only after passing a three-stage gate:

1. **Type-appropriate permutation null.** The null is matched to the relationship's structure:
   *block permutation* for lagged directional relationships (preserving short-range autocorrelation),
   *random shuffle* for contemporaneous relationships, and *phase randomization* for self-referential
   types (temporal, equilibrium, structural) that must preserve a variable's own spectrum. A single
   generic shuffle would be wrong for most of the fifteen types.
2. **False-discovery-rate control.** A dual statistic — the minimum of the confidence and fit
   p-values — is passed through a Benjamini–Hochberg step-up procedure at q = 0.05, so the reported
   edge set controls the expected proportion of false edges rather than any single test.
3. **Stability selection.** Edges must recur across resampled windows to survive, suppressing
   edges that appear once by chance.

On a controlled synthetic benchmark whose ground-truth structure is known by construction (a formal
`VariableProcess` design that guarantees dependence without leakage), this gate produces **exact
recovery** — strict, family, and edge F1 all 1.00 (17 true positives, 0 false positives, 0 false
negatives), with per-type recall of 1.00 across all fifteen types — at a measured **null
false-positive rate of 0.00** on held-out null pairs. The calibration detail bears out the mechanism:
genuine edges (e.g. a structural edge at confidence 0.98, a causal edge at 0.81) clear their nulls,
while planted null pairs return p = 1.00 and are correctly rejected.

The lesson the framework encodes is blunt: **raw confidence without this gate is not evidence.** The
same engine run without calibration would report a dense, confident, and largely spurious graph.

**Calibration is the default, and it runs online.** In earlier releases the gate lived only in the
offline benchmark harness; it is now built into the engine itself. `get_knowledge_graph(calibrated=True)`
is the default on both backends, so an uncalibrated graph is something a caller must now ask for
explicitly rather than the other way round; on the default tensor backend each surviving edge is
returned with a `p_value` and a partial-R² effect size, not just a confidence (the pure-Python
reference applies a softer internal deflation). Two refinements make the gate sound in the streaming
setting,
where the i.i.d. permutation assumption is weakest. First, the online significance test is
**autocorrelation-robust**: the per-predictor t-statistic from the recursive-least-squares fit is
shrunk by an effective sample size, `n_eff = n·(1 − r₁ᵃr₁ʸ)/(1 + r₁ᵃr₁ʸ)` (the Bayley–Hammersley
correction from the lag-1 autocorrelations of predictor and target), so a serially correlated stream
is not mistaken for a longer independent one. Second, a `min_partial_r2` floor lets a caller demand a
minimum effect size, not merely significance — the guard that keeps large-`n` streams from promoting
vanishing effects. For the genuinely sequential case, where hypotheses are tested in arrival order and
the horizon is open-ended, the package also ships a standalone LORD++ online-FDR controller
(`scarcity.engine.online_fdr.LordOnlineFDR`) that spends an error-budget "wealth" across an unbounded
test stream while controlling the false-discovery rate — the online counterpart to the batch
Benjamini–Hochberg step used over a fixed edge set.

### 5.1 From discovery to identification: the epistemic ladder

Calibration decides which edges to *believe*; it does not by itself decide how much to *claim* about
them. The framework separates those with an explicit **epistemic ladder** — a six-rung scale that an
edge climbs only as far as the evidence carries it: `DISCOVERED` (the engine proposed it) →
`HYPOTHESIZED` (it survives the calibration gate) → `PREDICTIVE` (it improves genuinely held-out
prediction) → `IDENTIFIED` (a valid adjustment set exists for it) → `ESTIMATED` (its magnitude is
estimated on the adjusted regression) → `ROBUST` (the estimate withstands a placebo test and an
omitted-variable-bias sensitivity analysis). The `EpistemicPipeline` (`scarcity.pipeline`) drives an
edge up this ladder using real analyses at each step — a held-out R² for `PREDICTIVE`, a
Frisch–Waugh–Lovell adjusted t-statistic and the Cinelli–Hazlett robustness value for `IDENTIFIED`
through `ROBUST` — and records where each edge stopped and why. Symmetric relationship types (a
correlation has no direction to identify) are capped at `HYPOTHESIZED` by design. The ladder is the
framework's honesty made procedural: an edge labelled `HYPOTHESIZED` is precisely one that is real but
not yet shown to be predictive or identifiable, and the API refuses to silently upgrade it. When an
edge *is* used to predict, `scarcity.causal.uncertainty.predict_with_uncertainty` propagates both the
parameter covariance and each parent's inclusion confidence into the prediction interval, so a
forecast built on a merely-hypothesized parent inherits a wider band than one built on a robust
one — the discovery confidence is carried through to the output rather than discarded at the boundary.

---

## 6. Borrowing Magnitude: Federation and Meta-Learning

The framework's refusal to estimate scarce magnitudes locally is made good by two layers.

**Federation.** Multiple Scarcity nodes — on different machines, institutions, or data silos — learn
a shared knowledge graph while each keeps its raw data private; only model updates cross the wire.
Aggregation is two-layer (device-level then server-level), with a differential-privacy guard adding
calibrated noise before any update leaves a node, secure aggregation so the coordinator sees only the
sum, a privacy-budget accountant that halts updates when the budget is spent, and trust scoring plus
conflict reconciliation for disagreeing peers. The point of federation here is statistical power:
pooling raises the effective sample per relationship. On East African macro data, pooling three
countries lifted the effective sample from ≈34 to ≈102 and **unlocked relationship types that lack
power at a single country** — equilibrium confidence rose 0.12→0.58, moderating 0.00→0.44, logical
0.18→0.53, causal 0.62→0.96 — surfacing plausible macro drivers that annual single-country data
cannot reliably identify.

Federation is not universally beneficial, and the framework does not pretend otherwise (§7).

**Meta-learning.** Rather than discard knowledge when moving to a new domain, the meta layer
accumulates it. An episodic memory stores, per past context, the embedding, the parameters applied,
and the observed performance deltas, retrieved by cosine similarity to the current context; an online
Reptile optimizer takes a step toward each task's solution so the meta-initialization drifts toward
one good for all tasks; and a warm-start profile lets a node joining mid-stream begin from borrowed
priors rather than from scratch. The Federation–Meta Interface (`fmi/`) is the translation layer that
turns aggregated federation updates into these priors and carries meta-beliefs back.

---

## 7. Evaluation

The framework has been run across a deliberate spread of settings, chosen to span the *ground-truth*
axis: a synthetic benchmark where the structure is known by construction; a mechanistic biological
twin where the structure is known because we wrote the generating equations; and two real-world
domains — macroeconomics and financial-market microstructure — where the structure is unknown and
the scarcity is genuine. We report each honestly, and the contrast between them is the framework's
actual message: structure is recoverable and useful *when the sample supports it*, and the correct
posture when it does not is calibrated abstention plus borrowed magnitude.

### 7.1 Controlled recovery (synthetic ground truth)

On a synthetic benchmark whose dependency structure is known by construction (a `VariableProcess`
design that guarantees dependence without leakage), the discovery core plus the calibration gate
achieve **exact recovery** — precision, recall, and F1 all 1.00 (17 true positives, 0 false
positives, 0 false negatives), with per-type recall 1.00 across all fifteen relationship types — at
a **null false-positive rate of 0.00** on held-out null pairs. Given the recovered graph,
graph-conditioned anomaly detection — flagging large residuals against a variable's discovered
parents — reaches **F1 = 0.80 with zero false positives** at N = 3000, a +22.5% improvement over a
blind Z-score baseline, and specifically catches *structural* anomalies (a relationship quietly
breaking) that a univariate detector cannot see. These establish that when the ground truth exists
and the sample is adequate, the framework recovers it without inventing edges. They are necessary
checks, not claims about scarce real data.

### 7.2 Three domains

**Macroeconomics — real, scarce, no ground truth.** On World Bank annual indicators for seven East
African economies (≈34 observations each, 1990–2023), the framework behaves exactly as its name
predicts, and we report it plainly. *Calibration is decisive and mandatory:* raw engine confidence
admits false positives at 41% and ranks the first true relationship 123rd; the
permutation/FDR/stability gate drives the null FPR to 0.00 and the first true relationship to rank 4
— ahead of graphical lasso (11) and a correlation+AR scan (8). *The scarcity paradox is measured:*
feeding the recovered structure to a shallow consumer helps (type-aware features beat raw lags by
4–7%), while feeding the same structure to progressively deeper consumers degrades them
monotonically, a graph neural network ending 96% worse than persistence — and no per-system consumer
beats persistence at N≈34. *Graph-conditioned anomaly inverts under scarcity:* at N≈34 a blind
Z-score wins (F1 0.44 vs 0.19), the break-even where discovered structure begins to help lying
between ≈100 and ≈300 observations. *Federation is target-specific but real:* pooling three countries
lifts the effective sample ≈34→≈102 and unlocks types that lack power singly (equilibrium confidence
0.12→0.58, moderating 0.00→0.44, logical 0.18→0.53, causal 0.62→0.96); a coherence signal predicts
the direction of federation benefit for 8 of 10 targets (Spearman ρ ≈ 0.50).

**Biology — a mechanistic oracle, ground truth by construction.** Pointed at a digital twin built
from four validated, published disease models — diabetes, oncology, fibromyalgia, autoimmune, one
per organ system — where the generating ODEs, and therefore the true coupling graph, are known, the
same engine recovers the known structure of every head while the temporal-shuffle null collapses to
zero: form F1 = 1.00 for oncology and autoimmune, 0.80 for fibromyalgia, and 0.4–0.5 for diabetes
(lowered by indirect edges and a meal-dominated variable), against a shuffle null of 0.00 throughout;
identifiability splits into a stiff tier recoverable from a handful of samples and a slow tier that
is not, separated by 2.5× to 224× in sensitivity. This is a second, independent ground-truth check —
on *mechanistic* rather than synthetic structure, on data the engine was not tuned for — and it
holds across four organ systems. (Synthetic ground truth: mechanistic-generalization evidence, not
clinical validation.)

**Financial markets — real, fast, adversarial.** Pointed blind at six days of Bitcoin order-flow
microstructure (≈100,000 five-second bars derived from ~6 million signed trades), with no target or
adjustment set specified, the engine recovers a 29-edge typed graph and — the decisive observation —
*types it correctly*, separating a volatility relation (trade intensity → next-return magnitude,
typed functional) from a directional one (order-flow imbalance ↔ return, typed correlational), a
distinction a posed query cannot make. The offline arm recovers a robust order-flow → return effect
(placebo p < 0.001). The framework was then used to build a high-frequency trading strategy on this
structure; consistent with its calibrated-abstention design, the strategy declines to trade the
directional edge — real but transient and below transaction cost — while the engine's own typing
points to the recoverable magnitude, a realized-volatility forecast reaching out-of-sample R² 0.40.
Real adversarial data; single asset, short window (§8).

### 7.3 Where classical detectors break

A recovery method is only as interesting as the mistakes it avoids, so we ran the calibrated engine
against five standard relationship detectors — Pearson correlation, Spearman correlation, mutual
information, Granger causality, and the PC constraint-based structure learner — across six canonical
failure modes with known correct answers: *no relationship*, *confounding*, *collider*, *reverse
causality*, *feedback*, and *weak signal* (three seeds, majority verdict). No classical method clears
all six: correlation-family detectors are misled by reverse causality and feedback, mutual information
partially so; Granger and PC miss the *contemporaneous* confounded association because their lagged
tests have nothing to fire on. The calibrated Scarcity engine is the only method that reaches the
correct answer in every scenario — passing where each baseline individually fails — because it tests
several relationship types per pair rather than committing to one detector's blind spot. This is a
targeted claim, not a leaderboard: the scenarios are chosen precisely as the places a single-statistic
detector fails, and Scarcity's advantage is coverage of relationship *type*, not a better estimate of
any one of them.

**Reproducibility.** A seeded run is bit-reproducible: `set_seeds()` fixes the NumPy and Torch
generators and enables deterministic kernels (`torch.use_deterministic_algorithms`, deterministic
cuBLAS), so the calibrated graph is identical run to run on the same seed, on CPU or GPU. The whole
hardening suite — scaling, drift, dirty-data robustness, the online-FDR characterization, ablations,
threshold sensitivity, the discovery baselines, and the failure-mode matrix above — regenerates from a
single command, `python benchmark/scripts/run_all.py`, which writes a provenance-stamped
`benchmark/RESULTS.md` recording the git commit, timestamp, and Python/Torch versions that produced
each table.

### 7.4 The framework in use

Scarcity is not a benchmark artefact; it is the discovery layer of working systems. The same engine
underlies a national economic- and threat-intelligence platform (K-Shield / K-Scarcity), where it
learns relationships from institutional data feeds and hands the typed graph to a stock-flow-
consistent macro simulator; it powers the high-frequency trading system of §7.2; and it is the
recovery substrate of the biological digital-twin programme from which the four-head results come.
The evaluation suite of this paper is itself built on the framework's calibration and reporting
machinery. The design goal is the same across all of them: recover form cheaply, refuse to invent
magnitude, and re-discover under drift.

## 8. Limitations and Scientific Honesty

- **Granger, not structural, causality.** The online engine's `causal` type measures Granger-style
  predictive structure from observational data. It does **not** perform structural causal
  identification; intervention validity and identifiability are explicitly unsupported by the engine
  and are delegated to the offline `causal/` do-calculus pipeline, which is itself bounded by the
  usual observational assumptions.
- **Adaptive inference weakens permutation guarantees.** Because the engine is online and stateful,
  classical permutation-null assumptions hold only approximately. The online gate mitigates the most
  common violation — serial dependence — by shrinking its test statistic to an effective sample size
  (§5), and offers a LORD++ online-FDR controller for the sequential setting; but Benjamini–Hochberg
  over the edge set still assumes weak dependence, and strong dependence may call for a more
  conservative (Benjamini–Yekutieli) correction. The effective-sample correction reduces this error,
  it does not eliminate it.
- **Observational equivalence.** Under high noise or short samples, some structures are statistically
  indistinguishable, and the framework cannot resolve them.
- **Benchmark scope.** The exact-recovery result uses generator-native assumptions; adversarial and
  fully out-of-distribution benchmarks remain future work. The real-data results are the honest
  counterweight.
- **Federation is not free.** It raises statistical power but can inject cross-node bias; its benefit
  is target-specific and must be routed, not assumed.
- **Biological ground truth is synthetic.** The digital-twin results (§7.2) are
  mechanistic-generalization evidence, not clinical validation: the generating models are validated
  from the literature but the trajectories are our own, so the results bound identifiability *in
  principle*; real cohort data would add model mismatch.
- **Financial-markets scope.** The microstructure result (§7.2) is a single asset (BTC/USD) over six
  days; breadth across assets, venues, and regimes is future work, and the strategy's abstention
  conflates genuine market efficiency with retail-scale transaction costs and a feature set lacking
  limit-order-book depth — it shows *this* edge is unexploitable under *these* costs, not that none
  exists.

We state these because the framework's value is precisely in being calibrated about its own
confidence; a version that overclaimed would defeat its purpose.

## 9. Availability

Scarcity is an installable, domain-agnostic Python package.

```bash
pip install scarcity            # core: numpy, pandas, scipy
pip install "scarcity[causal]"  # + DoWhy / EconML for the offline arm (§9.1, step 4)
pip install "scarcity[all]"     # + gpu, stream, dashboard extras
```

The core install covers the discovery engine, the simple federation hub/node, meta-learning, the
resource governor, streaming, and synthetic data. Heavier subsystems are optional extras (`[gpu]`
for the torch/vectorized backend, `[stream]` for WebSocket transports and sharding, `[dashboard]`
for the FastAPI server); importing a subpackage without its extra raises `ImportError`. Each
subpackage of `scarcity` maps to a layer of §3: `engine`, `causal`, `federation`, `fmi`, `meta`,
`governor`, `stream`, `runtime`, `synthetic`, `dashboard`.

### 9.1 A guided tour of the library

This section walks through the installed package end to end, using only its public API — no
repository checkout and no proprietary data. Everything in steps 1–4 runs from a bare
`pip install "scarcity[causal]"`.

**Step 1 — a stream with a relationship planted in it.** We build a three-variable stream in which
`x` drives `y` with a true coefficient of 0.8, while `z` is independent noise, so we know the ground
truth and can check what the engine recovers.

```python
import numpy as np

rng = np.random.default_rng(0)
n = 6000
x = rng.standard_normal(n)
z = rng.standard_normal(n)                     # independent noise
y = 0.8 * x + 0.2 * rng.standard_normal(n)     # x drives y; true coefficient 0.8

stream = [{"x": float(x[t]), "y": float(y[t]), "z": float(z[t])} for t in range(n)]
```

**Step 2 — discover typed relationships online.** The engine ingests one row at a time and maintains
the hypothesis pool of §4. Left to itself the engine picks the **tensor backend** whenever `torch` is
present (§4.3), which is what a production caller wants; this tour pins `vectorized=False` so the
snippet runs identically without a GPU and stays the reproducible reference. We also pass
`calibrated=False` to look at the *raw* ranking first, then turn the gate on in Step 3b.

```python
from scarcity.engine import OnlineDiscoveryEngine, RelationshipType

def discover(rows, calibrated=False):
    eng = OnlineDiscoveryEngine(vectorized=False)   # omit vectorized=... to auto-select the GPU path
    eng.initialize({"fields": [{"name": "x"}, {"name": "y"}, {"name": "z"}]})
    for r in rows:
        eng.process_row(r)                     # per-row update; state lives in the engine
    return eng.get_knowledge_graph(calibrated=calibrated)

graph = discover(stream)                         # raw view; calibrated=True is the engine default
```

**Step 3 — read and interpret the typed knowledge graph.** `get_knowledge_graph()` serializes the
strongest surviving hypotheses. Each edge carries its `type` (one of the fifteen
`RelationshipType`s), its `variables`, and a `metrics` block with the raw confidence, fit, and
accumulated evidence.

```python
for edge in sorted(graph, key=lambda e: -e["metrics"]["confidence"]):
    m = edge["metrics"]
    print(edge["type"], edge["variables"], round(m["confidence"], 3), "ev=", m.get("evidence"))
# top edge: correlational ['x', 'y'] conf 1.0 ev 6000   (the planted relation)
# z stays negligible; untested triples sit at the neutral 0.5 prior with evidence 0
```

The `evidence` field matters as much as `confidence`: the neutral-prior triples print `conf 0.5,
ev 0` — hypotheses the engine seeded but never tested — and must not be mistaken for findings.

**Step 3b — calibrate before trusting (the §5 gate).** These raw confidences are a **ranking signal,
not a significance test**, so no edge should be trusted until it passes the §5 gate — and that gate is
now the **engine default**. `get_knowledge_graph(calibrated=True)` (the default on both backends) runs
it inline: on the tensor backend it applies the type-appropriate permutation nulls with BH-FDR at
`q = 0.05` and returns each surviving edge with a permutation `p_value` and a partial-R² effect size,
dropping the rest. On this stream it keeps the `x–y` relation — typed correlational, functional,
probabilistic, and structural, all at `p ≈ 0` — and cuts the noise variable `z` entirely; passing
`min_partial_r2=…` adds an effect-size floor on top of significance. You can also reproduce the
*principle* over the public API on either backend — re-discover on column-shuffled copies that destroy
real structure, and keep only edges that beat every null run and clear a floor:

```python
def confmap(g):
    return {(e["type"], tuple(e["variables"])): e["metrics"]["confidence"] for e in g}

real, null = confmap(graph), {}
for seed in range(5):
    r = np.random.default_rng(100 + seed)
    shuffled = [{"x": float(a), "y": float(b), "z": float(c)}
                for a, b, c in zip(r.permutation(x), r.permutation(y), r.permutation(z))]
    for k, c in confmap(discover(shuffled)).items():
        null.setdefault(k, []).append(c)

trusted = [k for k, c in real.items() if c > max(null.get(k, [0.0])) and c >= 0.10]
# -> [('correlational', ('x', 'y'))]   real conf 1.00 vs null max 0.00; every other edge is cut
```

**Step 4 — quantify a magnitude with the offline causal arm.** The engine finds *what* to
investigate; `scarcity.causal` estimates *how much*, via DoWhy identification plus EconML
heterogeneous effects. It takes a pandas `DataFrame` and an `EstimandSpec`.

```python
import pandas as pd
from scarcity.causal import run_causal, EstimandSpec, EstimandType, RuntimeSpec

df = pd.DataFrame(stream)
spec = EstimandSpec(treatment="x", outcome="y", confounders=["z"], type=EstimandType.ATE)
result = run_causal(df, spec, RuntimeSpec())
for art in result.results:               # one EffectArtifact per spec
    print(art.spec.treatment, "->", art.spec.outcome, round(art.estimate, 3))
    print("  95% CI:", art.confidence_intervals)
    print("  refuters:", {k: v["passed"] for k, v in art.refuter_results.items()})
    # -> x -> y 0.796
    #    95% CI: (0.791, 0.801)
    #    refuters: {'random_common_cause': True, 'placebo_treatment': True, 'data_subset': True}
```

Each `EffectArtifact` carries the point `estimate`, its `confidence_intervals`, and
`refuter_results` — the placebo, random-common-cause, and data-subset refutations, each
re-estimating the effect under a perturbation: the two stability refuters leave it near 0.80, while
the placebo (a fake treatment) collapses it to 0. `refuter_results` also carries a `sensitivity`
entry: the refuters test robustness to *perturbation*, but not to a confounder that was never
measured, so the arm adds a Cinelli–Hazlett omitted-variable-bias analysis — the **robustness
value** (the minimum strength, as a partial R² with both treatment and outcome, an unmeasured
confounder would need to nullify the effect) and the treatment's own partial R² as a benchmark,
computed from the adjusted-regression t-statistic and verified against the canonical sensemakr
Darfur values.

**Step 5 — borrow structure across nodes (federation).** The same engine wires into a federation so
several nodes learn a shared graph without moving raw data (§6). Nodes are organized around
*baskets* (named variable groups with a schema); a `FederationHub` registers `FederationNode`s,
streams observations to each, and reconciles their directed findings.

```python
from scarcity.engine import FederationNode, FederationHub

hub = FederationHub()
hub.register(FederationNode("node_a"))
hub.register(FederationNode("node_b"))
hub.observe_all(basket_rows)             # each node updates locally on its own rows
hub.sync_directions()                    # reconcile edge directions across peers
print(hub.summary())                     # per-basket findings, trust, pooled structure
```

Federation raises statistical power — recall (§6) that pooling three countries unlocked
relationship types that lack power singly — but it is target-specific and must be routed, not assumed
(§7.2).

*Verified.* Steps 1–4 were run against `scarcity` 0.1.0 on CPython 3.11: the engine recovers
`correlational (x, y)` at confidence 1.00 on 6000 observations of evidence, the shuffle-null gate of
step 3b leaves exactly that one edge (real 1.00 vs null 0.00) and cuts every other, and the offline
arm returns an average treatment effect of 0.80 with a 95% interval of (0.791, 0.801) — the planted
coefficient — its placebo refutation collapsing the effect to 0 and both stability refutations
holding near 0.80.

### 9.2 Reproducing the paper's numbers

Steps 1–5 exercise the library; the *benchmark tables* in §5–§7 are reproduced from the public
repository (the benchmark harness — labelled `VariableProcess` generators, the World Bank loaders,
and the baseline models — ships in the repo tree, not inside the pip package). Environment:
`pip install "scarcity[all]"` plus the baselines the benchmarks compare against
(`pip install prophet statsmodels torch scikit-learn`), Python ≥ 3.9. The real-data results use
public World Bank national-accounts indicators for the East African economies; no private data is
involved. One command runs the suite —

```bash
python benchmark/scripts/benchmark_full_system.py --phase all
```

— writing reports to `benchmark/reports/outputs/`, including the claim-integrity matrix that grades
each result as supported, partially supported, or unsupported. Single results:

| Result in this paper | Command |
|---|---|
| §5 / §7.1 exact recovery — per-type recall 1.00, null FPR 0.00 | `benchmark_full_system.py --phase synthetic` |
| §7.1 graph-conditioned anomaly (F1 0.80, N=3000) | `benchmark/scripts/benchmark_anomaly.py` |
| §7.2 real anomaly at N≈34 (Z-score 0.44 vs graph 0.19) | `benchmark/scripts/benchmark_anomaly_real.py` |
| §7.2 forecasting (10 targets × 4 horizons, bootstrap CIs) | `benchmark/scripts/benchmark_forecasting_horizons.py` |
| §7.2 / §6 federation routing (8/10, Spearman ρ ≈ 0.50) | `benchmark/scripts/benchmark_federation_diagnostic.py` |
| break-even N-sweep (when graph-conditioning helps) | `benchmark/scripts/benchmark_n_sweep.py` |
| §7.3 baselines × failure modes (Scarcity clears all six) | `benchmark/scripts/baselines_failure_modes.py` |

The hardening benchmarks introduced in §7.3 — scaling, drift, dirty-data robustness, online-FDR
characterization, ablations, threshold sensitivity, the discovery baselines, and the failure-mode
matrix — are additionally wrapped by a single orchestrator that runs the suite and writes one
provenance-stamped report:

```bash
python benchmark/scripts/run_all.py            # full configs -> benchmark/RESULTS.md
python benchmark/scripts/run_all.py --quick     # fast smoke (small n / few seeds)
```

`RESULTS.md` records the git commit, timestamp, and Python/Torch versions alongside each table, so a
reviewer can see exactly which revision produced the numbers.

The exact-recovery claim is the one most worth re-running yourself: it is the check that the discovery
core plus the calibration gate return zero false positives when the ground truth exists, on a
generator whose structure is known by construction.

## 10. Conclusion

Scarcity treats structure and magnitude as different kinds of thing. It recovers the form of
relationships — across fifteen types, with a calibration gate strict enough to return zero false
positives on controlled ground truth — and it refuses to invent the magnitudes a scarce stream cannot
support, borrowing them from a federation of peers instead. The controlled results show the discovery
core works when the sample supports it; the real-data results show, just as clearly, where it does
not, and the framework's response to that boundary — calibrated abstention, borrowed magnitude,
adaptive re-discovery under drift — is its actual contribution. It is released as a domain-agnostic
package, and this paper is its introduction: the design, the methodology, and the measured behaviour,
successes and failures reported on the same page.

---

## References

1. Granger, C. W. J. (1969). Investigating Causal Relations by Econometric Models and Cross-Spectral Methods. *Econometrica*, 37(3), 424–438.
2. Engle, R. F., & Granger, C. W. J. (1987). Co-integration and Error Correction. *Econometrica*, 55(2), 251–276.
3. Benjamini, Y., & Hochberg, Y. (1995). Controlling the False Discovery Rate. *JRSS B*, 57(1), 289–300.
4. Benjamini, Y., & Yekutieli, D. (2001). The Control of the False Discovery Rate Under Dependency. *Annals of Statistics*, 29(4), 1165–1188.
5. Meinshausen, N., & Bühlmann, P. (2010). Stability Selection. *JRSS B*, 72(4), 417–473.
6. Page, E. S. (1954). Continuous Inspection Schemes. *Biometrika*, 41(1/2), 100–115.
7. Thompson, W. R. (1933). On the Likelihood That One Unknown Probability Exceeds Another. *Biometrika*, 25(3/4), 285–294.
8. Nichol, A., Achiam, J., & Schulman, J. (2018). On First-Order Meta-Learning Algorithms. *arXiv:1803.02999*.
9. McMahan, B., et al. (2017). Communication-Efficient Learning of Deep Networks from Decentralized Data (FedAvg). *AISTATS*.
10. Bonawitz, K., et al. (2017). Practical Secure Aggregation for Privacy-Preserving Machine Learning. *ACM CCS*.
11. Dwork, C., & Roth, A. (2014). The Algorithmic Foundations of Differential Privacy. *Found. Trends Theor. Comput. Sci.*, 9(3–4).
12. Sharma, A., & Kiciman, E. (2020). DoWhy: An End-to-End Library for Causal Inference. *arXiv:2011.04216*.
13. Chernozhukov, V., et al. (2018). Double/Debiased Machine Learning (EconML). *Econometrics Journal*, 21(1).
