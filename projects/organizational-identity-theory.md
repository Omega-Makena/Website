---
title: Organizational Identity Theory
section: Theory
date: 2026-08-04
description: The foundational paper (Paper 0) — form recovers under scarcity, magnitudes do not. Evidence from macroeconomics, mechanistic biology, and financial markets.
---

Organizational Identity Theory asks one question about systems that drift under
scarcity — few samples, high noise, constant change: **which of their properties can actually be
recovered from data, and which cannot?** The answer it proposes is that every such system carries a
*partially persistent organizational identity* — the *form* of how its parts relate — that survives
when the exact magnitudes through which it is expressed do not.

This is the foundational paper of the theory. It grew out of [**Scarcity**](/scarcity/), the online
relationship-discovery engine I built to learn structure from thin, drifting data, and it is tested
across three complementary domains: real macroeconomic time series, a controlled biological oracle,
and live financial-market microstructure. For who's behind it, see [**About**](/about/).

*This is a **living preprint** — a working draft, not peer reviewed, revised as the programme
develops. The full paper follows.*

---

**Organizational Identity Theory for Dynamic Data: The Foundational Paper (Paper 0) — Form Recovers Under Scarcity, Magnitudes Do Not (Evidence from Macroeconomics, Mechanistic Biology, and Financial Markets)**

**Author:** Omega Makena M. *(corresponding: mwebiamakenaa@gmail.com)*
**Affiliation:** Innova Limited
**Preprint — draft, June 2026. Not peer reviewed.**

---

## Abstract

Dynamic systems observed under scarcity — few samples, high noise, constant drift — pose
a recurring problem: which of their properties can actually be recovered from data, and
which cannot? **This is the foundational paper of Organizational Identity Theory for Dynamic
Data** — a framework we introduce here and intend to extend, domain by domain, in subsequent
work. Its claim:
every such system possesses a *partially persistent organizational identity* — a latent
organizational continuity we do not observe directly, but infer from **markers**, chief among
them the topological-conjugacy class of its flow and its statistically recoverable projection,
the typed dependency graph (the *form* of relationships). The hypothesis is that this identity
is more stable than the magnitudes through which it is expressed: its markers are recoverable
under scarcity, while the system's *magnitudes* (rate constants, hazards, effect sizes — the
coordinates within the identity class) are not uniformly recoverable. A **scarcity paradox** follows: because structure
recovery is cheap in data while magnitude exploitation is expensive — discovery works at low
sample size, exploitation needs high — and both draw on one budget, the regime in which recovered
structure is most valuable is exactly the regime in which a magnitude-hungry consumer of it fails
worst (not overfitting: a graph neural network ends 96% worse than a naive baseline, and no
structure-exploiting forecaster beats it). We support the theory
in **three domains** — two real-world (macroeconomics, financial markets) and one controlled
oracle (mechanistic biology). In **macroeconomics** (federated World Bank time series across seven
economies, plus a labelled synthetic benchmark), a streaming relationship-discovery engine
recovers typed structure with calibrated control of false positives (null false-positive
rate driven from 41% to 0%; first-ground-truth rank from 123 to 4), shallow consumers of
that structure improve forecasts by 4–7%, and progressively deeper magnitude-hungry
consumers fail monotonically — a graph neural network worsens by 96% over a naive baseline,
the scarcity paradox measured directly. In **biology** we build a mechanistic digital twin
whose generative equations are *known*, making it a ground-truth oracle, and test the theory
across four validated disease models from four organ systems (metabolic, oncologic,
chronic-pain, autoimmune). The same engine, pointed blind at simulated trajectories, recovers
the known coupling graph (edge-recovery F1 0.4–1.00 across the four heads, in every case far
above a per-variable time-shuffle null that collapses to ≈0); parameter identifiability separates into a **stiff** tier recoverable from a
single day of data and a **slow/sloppy** tier that is not recoverable at clinically plausible
horizons (stiff/slow sensitivity gaps 2.5×–224×); and an offline do-calculus engine recovers
a known causal effect (−34.8 mg/dl) that naive estimation biases four-fold. In **financial
markets** (six days of Bitcoin five-second bars built from ≈6 million signed high-frequency
trades) the same engine, pointed blind at the order-flow panel with no query posed, autonomously
recovers and *types* the microstructure relationship graph — correctly labelling
trade-intensity → next-return a functional/volatility relation (correlation with the absolute
next return 0.18, with the signed return −0.008) and order-flow-imbalance ↔ return correlational —
and the form/magnitude split reappears against an efficient market: the online engine cannot
certify the directional edge (no confidence threshold clears a multi-seed shuffle null — a 0%
false-positive rate only where it abstains, 40–80% where it would confirm), while the offline
do-calculus engine recovers a robust effect of order flow on the next return (placebo p < 0.001,
agreeing across ATE/ATT/ATC/CATE/ITE). Here the scarcity paradox becomes literal unexploitability:
the effect is real but transient (significant only to ≈1 minute) and below transaction cost at
every horizon and regime, so a magnitude-hungry trading strategy loses while the disciplined
engine, declining to certify what fails its null, abstains and thereby wins — and following the
engine's own typed discovery to the recoverable magnitude yields a genuine realized-volatility
forecast (out-of-sample R² to 0.40) where directional exploitation failed. The picture that
survives is not the slogan "form recovers, magnitudes do not" — a single insulin-sensitivity
parameter is recoverable from eight noisy samples — but a **recoverability hierarchy**: form
and stiff magnitudes recover from modest data; slow and sloppy magnitudes do not, and must be
borrowed from a cohort. The biological results are on synthetic ground truth and constitute
mechanistic-generalisation evidence, not clinical validation; the macroeconomic results are
on real data with the honest caveat that recovery is Granger-predictive, not interventional.
We present this as the **foundational paper** of the theory — fixing its definitions,
hypotheses, and falsification criteria, and treating the recovered graphs, motifs, and
attractor fingerprints as *markers* of identity rather than identity itself. Whether those
markers share one latent — the *concordance* test that would establish the construct — is
specified here and run as the programme's first dedicated empirical paper; this foundational
work supplies its prerequisite, that the markers are individually recoverable at all. These
three complementary domains — two real-world, one a controlled oracle — are the first of a
programme we intend to extend, domain by domain, to further systems that drift under scarcity.

---

## Letter to the Reader

*Paper 0*

This paper introduces a theory, but it did not begin as one. It began as a macroeconomic
simulator.

I wanted to simulate an economy, and I wanted the simulation driven by data. The problem was
immediate and stubborn: I had almost no usable economic data, and what I could find was messy
enough that I spent more time cleaning it than learning from it. So I stopped fighting the data
and changed the question. Instead of waiting for a complete dataset, could I build a system that
learns from whatever arrives, whenever it arrives, and simply keeps going? That, I later learned,
has a name: *online learning*.

That solved one problem and exposed the next. Learning continuously is costly, and re-learning
everything from scratch is wasteful. So I tried to put a layer on top — an accumulating knowledge
that would teach the system to learn faster and feed itself back in. I thought of it as the brain
of the thing. (The project had a different name then; "scarcity" came later.) That layer also had
a name: *meta-learning*.

By then I had spent the better part of a year on this, and a question I'd been avoiding became
impossible to ignore: was I building this for economics alone? That seemed too small, so I made
the system domain-agnostic — it should find structure in any field. Which revived the original
wound: I still had no data. My answer was to let the data come from users — but how do you learn
from people's data without taking it from them? That question has a name too: *federated learning*.

So the architecture assembled itself one forced discovery at a time, each a named field I backed
into rather than chose. And underneath all of it sat one conviction: *the relationship between two
variables — its direction, its sign — is the thing that does not change.* If I could recover that,
I could hand it to any downstream model and beat the scarcity that had defeated me at the start.
The whole system was a bet on that.

The bet broke. Fed the recovered structure, progressively deeper models did not improve — they got
monotonically worse, a graph neural network ending 96% worse than the most naive baseline
imaginable. Not overfitting; something more basic. The same scarcity that made structure
*discoverable* made it *unexploitable* — the two pull on one budget from opposite ends. I called
it the scarcity paradox, and it was the first sign my premise was wrong in an interesting way.

The deeper crack came later. I had been treating the recovered graph as the system's identity. But
the graph cannot be the identity, for a simple reason: I can always build a better engine. A finer
instrument finds more relationships, more types, subtler dependencies. If the graph *were* the
identity, a better instrument would hand me a different identity for the same unchanged system.
That is not allowed. The map cannot be the territory. So the graph is a *marker* of identity, not
identity — and so is everything else I can compute: the attractor fingerprint, the stiffness
profile, the motifs. All markers. None the thing itself.

Which is why, for now, I can only tell you what organizational identity is *not*. Not the
relationships. Not the graph. Not any single marker. The theory is, at this moment, defined by
exclusion — and I am at peace with the possibility that it stays that way, or that the decisive
test (do the markers point at one shared invariant, or just a pile of unrelated persistence
facts?) comes back negative and the thing I'm chasing turns out not to exist. People who have
looked at this tell me it's "just philosophy." I don't mind. I don't mind proving the theory true,
and I don't mind proving it false. I hold partial evidence and real faith that it's true — but I'm
certain the search will surface something worth more than the answer I expected when I started.

This is paper 0. It does not answer the question. It states what an answer must satisfy, rules out
the easy wrong answers, specifies the test that adjudicates the next one, and shows the markers are
individually recoverable — the prerequisite for asking whether they converge. The real tests come
after.

Every paper in this programme will open with a letter like this one. Read in sequence, they are
meant to be an honest log of the search — including, especially, the turns where it went wrong.

If you want a finished result, this will disappoint you. If you're willing to watch a question get
sharpened until it can be answered — true or false — read on.

And if you already know what stays the same when everything measurable about a system changes —
what makes a river a river — I would genuinely like to hear from you.

— Omega Makena M.
*Innova Limited · June 2026*

---

## 1. Definitions and Terminology

This paper introduces a new theory and, with it, a number of new terms. We define all of them
here, once, before they are used anywhere in the paper. Each entry gives a plain statement
first and the precise one second. A reader should be able to understand the whole paper from
this section alone; nothing below is defined only in passing.

**The lineage, in one sentence.** *Scarcity* is the research framework we developed for learning
from thin, drifting data; *Organizational Identity Theory* is the theory that framework produced
— an account of *what* in such data can be recovered, and what cannot.

### The scarcity setting

- **Scarcity (the regime).** *Plainly:* having too little informative data to pin a system down.
  *Precisely:* an operating regime defined by few informative observations, high noise, and
  ongoing drift (non-stationarity), in which a system must be learned from data that does not
  support estimating most of its quantities. When this paper says "scarcity" unqualified, it
  means this regime.
- **Scarcity (the framework).** *Plainly:* the system we built to learn from scarce, drifting,
  distributed data without trusting any one source too much — and the work *from which
  Organizational Identity Theory emerged.* *Precisely:* a federated, streaming
  relationship-discovery program whose major components are:
  - **Streaming typed discovery** — a population of typed relationship hypotheses (fifteen types:
    causal/Granger, correlational, functional, temporal, competitive, mediating, and others)
    tested incrementally against the data stream as active constraints, rather than one model fit
    in batch.
  - **Mandatory calibration** — every candidate relationship is gated against a type-appropriate
    permutation null with false-discovery-rate control and bootstrap stability selection; *no edge
    is trusted on the engine's raw confidence* (this is what drives the null false-positive rate
    from 41% to 0%).
  - **Federation without raw-data sharing** — structure and priors are learned across many scarce
    systems and transported between sites privately, so a system too data-poor to learn alone
    borrows strength from its peers without their raw observations ever moving.
  - **Meta-learned magnitude supply** — the quantities a single system cannot estimate are sourced
    from a cross-system prior (warm-started, adapted few-shot), never estimated freely from one
    system's scarce data.
  - **Uncertainty that widens under scarcity** — forecasts and effects carry intervals that grow
    automatically as data thins or drifts, instead of reporting false precision.

  *What makes it unique to this theory:* the framework is built on a refusal. It recovers and
  trusts *structure* cheaply, but it *refuses to estimate per-system magnitudes freely*, borrowing
  them from the federation instead. That architecture already embodied the form/magnitude split
  before the split had a name. Organizational Identity Theory is that operating principle made
  explicit: the framework works *because* form is recoverable under scarcity and magnitude is not
  — and the theory is the account of why.
- **Magnitude.** *Plainly:* a number that says *how much* — a rate, a strength, an effect size.
  *Precisely:* a continuous quantitative coordinate of a system (a rate constant, a hazard, a
  regression or effect coefficient), as opposed to the qualitative structure relating its
  variables. Magnitudes are the quantities scarcity makes hard to estimate.
- **Form (or direction).** *Plainly:* the *shape* of the relationships — what affects what, and
  with what sign — without the numbers. *Precisely:* the qualitative, typed structure of a
  system's dependencies: which variables couple, in which direction, through which relationship
  type. Form is what scarcity leaves recoverable.
- **The scarcity paradox.** *Plainly:* the very data shortage that makes structure *discovery*
  necessary and possible is what makes *exploiting* that structure impossible — discovery works at
  low sample size, but using the discovered structure quantitatively needs high sample size, and
  you have only one (small) data budget. *Precisely:* structure recovery is a *low-sample*
  operation (detecting an edge is a hypothesis test, cheap in data) while magnitude exploitation
  is a *high-sample* operation (each coefficient is an estimate whose variance scales as 1/N);
  because both draw on one per-system budget, the regime in which recovered structure is most
  valuable — scarcity — is exactly the regime in which a magnitude-hungry consumer of it fails
  worst. The engine that earns its keep by discovering structure *from scarce data* cannot have
  that structure exploited quantitatively, because quantitative exploitation needs the abundance
  scarcity denies. This is **not generic overfitting**: even a perfectly regularised model cannot
  estimate magnitudes the data does not contain. Measured directly in §5.1, where feeding the
  recovered structure to progressively deeper consumers degrades them monotonically — a graph
  neural network ends 96% worse than a naive persistence baseline, and *no* structure-exploiting
  forecaster beats persistence at all.

### The theory and its objects

- **Organizational Identity Theory (for Dynamic Data).** *Plainly:* the claim that every drifting
  system has a persistent organizational identity that survives data scarcity, even though its
  numbers do not. *Precisely:* the theory that a dynamic system observed under scarcity possesses
  a partially persistent *organizational identity* whose *markers* are recoverable from data while
  its *magnitudes* are not — and recoverable in a fixed order (the recoverability hierarchy). Its
  hypotheses H1–H3 are stated in §3.2; its falsification criteria in §3.7.
- **Organizational identity.** *Plainly:* the persistent "what the system *is*" that stays the
  same while all its numbers drift — never seen directly, only inferred. *Precisely:* a *latent
  construct* — the persistent organizational invariant of a system under the group of
  transformations that change its magnitudes and local functional forms while preserving it. Never
  observed directly; inferred from multiple markers; held to the seven rules of §3.1. Even its
  richest marker — the topological-conjugacy class of the system's flow — is a *marker*, not the
  identity: it is model-relative and lossy. *No single marker is the identity.*
- **Organizational marker.** *Plainly:* a measurable fingerprint of the identity — not the
  identity itself. *Precisely:* any separately computable descriptor that tracks the identity
  without being it: the typed dependency graph, a causal motif, the attractor fingerprint, the
  recoverability profile (and, deferred to later work, conservation and symmetry constraints).
  Markers are observable; identity is not.
- **Topological-conjugacy class (the primary marker).** *Plainly:* the *shape* of a system's
  behaviour — how many stable states it has and how they are arranged — ignoring the exact
  numbers. *Precisely:* the qualitative phase portrait of the flow (number and type of attractors,
  the saddles between them, the basins, the bifurcation skeleton), invariant under smooth
  coordinate changes and rate rescalings.
- **Bifurcation (= change of identity).** *Plainly:* the point where the system's behaviour
  changes *kind*, not merely degree — e.g. a healthy stable state disappears. *Precisely:* a
  qualitative change in the phase portrait (a change of conjugacy class). Under this theory a
  bifurcation *is* a change of organizational identity, whereas magnitude drift only moves a
  system *within* its identity.
- **Marker concordance.** *Plainly:* the different markers *agree* about what survives — evidence
  they are all measuring one underlying thing. *Precisely:* the agreement of distinct markers
  about what is preserved under a transformation; operationally, the low-rankness of the
  marker-by-transformation stability matrix (§3.8). Concordance is the empirical signature that a
  single latent identity exists (hypothesis H3); its absence would refute the construct. It is
  tested in the programme's first empirical paper, not this one.

### Recovery, stability, and the hierarchy

- **Organizational recovery.** *Plainly:* reading a system's structure off its data. *Precisely:*
  the estimation, from one system's data, of a recoverable marker of its identity — chiefly the
  typed dependency graph. Recovery is per-system and cheap; it is what survives scarcity.
- **Magnitude stability.** *Plainly:* whether a particular number can actually be measured from
  the data at hand. *Precisely:* the degree to which a magnitude is identifiable and persistent.
  *Stiff* magnitudes carry high information and are recoverable even at low sample size; *sloppy*
  or *slow* magnitudes carry near-zero information and are not recoverable at the horizons data
  spans. This property decides whether a magnitude can be estimated per-system or must be borrowed
  from a cohort.
- **Stiff vs. sloppy/slow magnitude.** *Plainly:* stiff = the data pins it down; sloppy/slow = the
  data barely constrains it. *Precisely:* measured by the normalised sensitivity
  S(θ) = ‖∂y/∂log θ‖ / ‖y‖ — large S is stiff, near-zero S is sloppy; "slow" denotes a sloppy
  parameter that governs a slowly accumulating state.
- **Recoverability hierarchy.** *Plainly:* things become recoverable in a fixed order — structure
  and stiff numbers first, slow numbers last or never. *Precisely:* the ordering that form and
  stiff magnitudes recover from modest data while slow and sloppy magnitudes do not. It is the
  theory's sharpest, most testable claim, and it corrects the cruder slogan "form recovers,
  magnitudes do not."
- **Organizational drift.** *Plainly:* the system's numbers slowly changing over time while it
  stays the same system. *Precisely:* the ongoing change of a system's magnitudes while its
  organizational identity persists — movement *within* a conjugacy class. A change that crosses a
  bifurcation is not drift but a change of identity.

### Methodological terms

- **Ground-truth oracle.** A system whose generating equations we wrote ourselves, so that
  recovered structure can be scored against the true structure and identifiability computed
  exactly. The biological digital twin is our oracle.
- **Stability matrix / concordance test.** The matrix **M** with markers as rows and
  transformations as columns, whose entries measure how stable each marker is under each
  transformation; the *concordance test* asks whether **M** is low-rank (one shared identity
  factor — the construct holds) or full-rank (no shared latent — the construct fails). Specified
  in §3.8; executed as the first empirical paper.
- **Online (form) vs. offline (magnitude) engine.** The two causal engines this paper uses: the
  *online* streaming Granger-style engine recovers directed structure cheaply (form, §4.1); the
  *offline* do-calculus engine (DoWhy / EconML) estimates effect magnitudes from the full dataset
  given that structure (magnitude, §4.6).

---

## 2. Introduction

A digital twin of a chronic-disease patient, a federated macroeconomic forecaster, and a
streaming sensor model share a structural predicament: they must learn from data that is
scarce, noisy, and non-stationary, yet the most valuable decisions ride on quantities the
data may not support. The naive response — fit the richest model the compute budget allows
— is actively harmful here. Deeper, more parametric consumers extract spurious magnitudes
from thin data and fail in proportion to their depth.

This paper **introduces** a theory of *what is recoverable* from such systems —
Organizational Identity Theory for Dynamic Data. Its thesis is that dynamic systems preserve
a **partially persistent organizational identity**: the typed arrangement of dependencies,
constraints, and interaction pathways is recoverable under drift and scarcity even when local
predictive magnitudes are unstable. A cell persists through near-total turnover of its
molecules; a patient persists through drift in every measurable magnitude; what persists, and
is recoverable, is the organization. We state the theory formally (Section 3) and support it
in three domains of evidence — macroeconomics, financial markets, and mechanistic biology
(Section 5).

We are careful about what we claim to observe. Organizational Identity Theory begins from the
observation that dynamic systems exhibit persistent organizational characteristics that remain
recoverable even when their quantitative details cannot be estimated. We do **not** claim to
observe organizational identity directly. We hypothesize, rather, that the differential
recoverability of organizational *markers* — dependency graphs, causal motifs, attractor
fingerprints, the recoverability hierarchy itself — reflects an underlying organizational
continuity that is more stable than the magnitudes through which it is expressed. Under this
view a recovered graph is not the identity; it is one observable marker of it, and no single
marker is the identity (Section 3.1). This is the same epistemic posture under which
temperature was a measured construct before statistical mechanics defined it, and the gene a
construct before its molecular basis was known: a latent inferred from convergent indicators,
not a thing observed (the logic of construct validity; Cronbach & Meehl, 1955). The present paper introduces that hypothesis and supplies its first
empirical evidence — the recoverability hierarchy of Section 5 — while deferring the decisive
test of whether the markers share one latent (their *concordance*, Section 3.8) to the
programme's first dedicated empirical paper.

**This is the foundational paper of the theory.** Its purpose is to establish the framework:
the definitions and lexicon (Section 3.2), the core and further hypotheses, the falsification
criteria, and a first three domains of evidence chosen to be maximally complementary — two real
(macroeconomics, broad and slow; financial markets, fast and adversarial, with money as the
referee), one controlled with known ground truth (mechanistic biology). It
is deliberately the *opening* of a research programme, not its closure. The same recovery /
identifiability / shuffle-control battery is intended to be carried, in subsequent work, to
further domains in which systems drift under scarcity — engineered and physical sensor
systems, ecological and climate dynamics, and neural recordings among them — each a fresh test
of the same identity claim and a step toward establishing (or falsifying) its generality.

Two things are empirically separable. The **form** (or direction) of a relationship — which
factors couple, with what sign, through which pathway — is low-dimensional and recoverable
at low sample size. The **magnitude** — the conditional-expectation coefficient, the rate
constant, the hazard — is higher-variance and, for many parameters, not recoverable at the
sample sizes where recovery is most needed. The regime in which recovery is most valuable
(few samples) is exactly the regime in which a magnitude-hungry consumer fails most
catastrophically. We call this the **scarcity paradox**, and treat it not as a curiosity
but as a governance constraint: a deep consumer that estimates magnitudes *freely* from one
system's scarce data is forbidden; a deep consumer that *borrows* its magnitudes from a
cohort or federation, and carries honest uncertainty, is permitted.

The three domains of evidence play complementary roles. **Macroeconomics** (Section 5.1)
supplies *real-world* evidence — federated national-accounts time series across seven
economies — and the cleanest empirical instance of the scarcity paradox: as a consumer of
the recovered structure is made deeper, its accuracy collapses monotonically. Its limitation
is that real systems have no ground-truth generative graph, and causal identification from
observational data is fundamentally constrained. **Biology** (Section 5.2) supplies what
macroeconomics cannot: a **mechanistic digital twin** whose generative differential equations
we wrote ourselves, making it a *ground-truth oracle*. There the recovered structure is scored
against the true coupling graph, parameter identifiability is computed exactly by sensitivity
analysis, and a known causal effect is recovered through do-calculus adjustment. **Financial
markets** (Section 5.7) supply the third role neither of the others can: a *real, fast,
adversarial* domain with a hard economic cost function, where the scarcity paradox stops being a
statistical curiosity and becomes literal — recovered structure that cannot be turned into profit
because the market has already priced it, so a magnitude-hungry consumer loses money while the
disciplined engine abstains. Together, real-world breadth (macro), controlled ground truth
(biology), and a priced adversarial test (markets) support the same theory from three sides.

We are explicit about scope. Every biological result is on synthetic ground truth — evidence
that the theory holds in mechanistic systems whose answer we know, not that any specific number
is clinically valid. The macroeconomic results are on real data, with the honest caveat that
the engine measures Granger-predictive recovery, not interventional identification. The
distinction is load-bearing and we maintain it throughout.

---

## 3. Theory: Organizational Identity for Dynamic Data

### 3.1 The organizational identity as a latent construct

Organizational identity is not something we observe. We treat it as a **latent construct** — a
persistent organizational continuity that is never measured directly, only inferred from
multiple *markers*. What we record from data — a dependency graph, a causal motif, an attractor
fingerprint — is a marker of the identity, not the identity itself. This is a deliberate
ontological commitment, and it is what keeps the theory honest: the recovered graph that
Section 5 scores so highly is evidence *about* a system's identity, never identity itself.

We hold a candidate organizational identity to five rules. An organizational identity:

1. **exists independently of the observer** — its markers are invariant to how, and how finely,
   the system is measured;
2. **survives a class of transformations** — there is a group of changes (magnitude rescaling,
   slow drift, smooth reparametrisation) under which it is invariant; that invariance group *is*
   the identity, in the same sense that a geometry is defined by the transformations that leave
   it unchanged (Klein's Erlangen program);
3. **is expressible through multiple markers** — at least two distinct, separately computable
   descriptors track it;
4. **is identical to no single marker** — every marker is a lossy projection; none may be
   substituted for the identity;
5. **explains differential persistence** — it accounts for *why some information survives
   scarcity while other information does not*.

Two further rules give the construct empirical teeth, and we state them explicitly because they
are what make it falsifiable rather than decorative. An organizational identity must also be:

6. **discriminant** — distinct identities must be *distinguishable* by the markers; a marker set
   that assigns everything one identity measures nothing;
7. **concordant** — the markers must *agree*: across transformations, what one marker reports as
   preserved, the others must too. If every marker responds idiosyncratically there is no shared
   latent behind them, only a pile of unrelated robustness facts, and the construct is empty.
   Concordance is therefore the theory's central testable consequence; we introduce it here and
   test it (Section 3.8) in the programme's first empirical paper, not this one.

With identity fixed as the latent, the remainder of this section's apparatus consists of its
**markers**.

Why even the richest descriptor is only a marker is worth stating plainly, because it is the move
on which the whole construct turns: *the engine can always be improved.* A finer instrument
discovers more relationship types, resolves more attractors, finds subtler dependencies. If any
one of these descriptors *were* the identity, a better instrument would assign a *different*
identity to the same unchanged system — which violates rule 1. An identity cannot depend on how,
or how well, it is measured. The map cannot be the territory. So each object below is a marker — a
lossy, instrument-relative projection of the identity — never the identity itself.

**The primary marker — the topological-conjugacy class.** The richest marker of a flow's
identity is the **topological-conjugacy class** of its vector field: the qualitative phase
portrait — the number and type of attractors, the saddles between them, the basins, the
bifurcation skeleton. It is invariant under exactly the transformations of rule 2 (smooth
coordinate changes, rate rescalings): magnitudes move a system *within* its class, and a
**bifurcation moves it between classes**. A bifurcation is therefore, precisely, a change of
organizational identity.

**Its recoverable projection — the typed dependency graph.** The conjugacy class is not
directly estimable from data; what an estimator recovers is the *typed dependency graph* —
which factors couple, with what sign and type — a lossy projection that keeps the labelled
skeleton and drops the metric detail. This is a second marker, and the one the recovery engine
of Section 4.1 produces; "form recovery" is recovery of this marker.

**A third marker — the attractor fingerprint.** The attractor count and stability arrangement,
computed by multi-start integration (Section 5.6), is a third, independently computed marker:
discrete, observer-independent, and the one on which we demonstrate rules 1–6 concretely on the
diabetes oracle.

These markers also explain the form/magnitude split structurally. The conjugacy class and its
projections are discrete/combinatorial objects (stable under drift, changing only at
bifurcations), whereas magnitudes are continuous coordinates *within* a class (drifting
constantly). Discrete structure is cheap to recover (a hypothesis test); continuous coordinates
are expensive (estimation with variance scaling). The construct's payoff is rule 5: it predicts
that the discrete markers persist under scarcity while the continuous magnitudes do not — which
is the recoverability hierarchy this paper measures.

### 3.2 Hypotheses

**Core hypothesis (H1).** Every dynamic system observed under drift and scarcity possesses a
*partially persistent organizational identity* (Section 3.1), whose **markers** are recoverable
from data even when the system's magnitudes are not. Precisely: the *form* (the support, sign,
and relationship-type of the dependency graph that is identity's recoverable marker) is
recoverable at low sample size; the *magnitudes* (the coordinates within the identity class) are
not recoverable at the same sample size.

**Further hypothesis (H2) — the scarcity paradox and the recoverability hierarchy.** Recovery and
magnitude-exploitation draw on one data budget *with opposite requirements* — discovery is a
low-sample operation, exploitation a high-sample one — so a downstream consumer fails in
proportion to the magnitude-depth it demands of per-system data, worst exactly where data is
thinnest (the *scarcity paradox*; this is a structural data-requirement mismatch, not model
overfitting). And recovery is *ordered*: univariate structure recovers first,
pairwise-directional second, three-way interactions last — recoverable, but only at several
times the sample size pairwise structure needs (Section 5.4); among magnitudes, stiff
(high-information) parameters recover before sloppy (low-information) ones (the *recoverability
hierarchy*).

**Concordance hypothesis (H3) — the markers share one latent.** The markers of Section 3.1 are
not independent robustness facts but expressions of a single identity: their stability under
transformation is governed by one dominant shared factor (the stability matrix of Section 3.8 is
low-rank), and that factor reproduces the recoverability hierarchy of H2. H3 is the decisive test
of the construct — its failure (a full-rank stability matrix, idiosyncratic markers) refutes the
latent. This paper states H3 and establishes its prerequisite, that the markers are individually
recoverable (Section 5); the programme's first empirical paper tests H3 directly.

**Lexicon.** Every term used here — organizational identity, organizational marker, marker
concordance, organizational recovery, magnitude stability, organizational drift, and the
scarcity regime and paradox — is defined once in the **Definitions and Terminology** section at
the front of the paper, and is not redefined here.

### 3.3 Form and magnitude

Consider a system whose state evolves under a vector field with couplings (drift),
stochastic forcing (diffusion), and regime-changing events (jumps). Each modelling object
decomposes into a recoverable part and a not-recoverable-at-low-N part:

| Object | Form / direction (recover per-system) | Magnitude (borrow from cohort/prior) |
|---|---|---|
| Couplings (drift) | which factors couple; sign of coupling; active pathways | rate constants, coupling strengths |
| Event intensity (jumps) | whether a regime is on the table; what raises vs lowers it | the hazard value itself |
| Diffusion | which channels are noisy | the noise scale |
| Competing risks | which risks exist | baseline rates |

The per-system learning target is the **typed dependency graph** — identity's recoverable
marker — not the coefficient vector.

### 3.4 The scarcity paradox

The paradox is sharper than a statement about model size. Structure *discovery* and magnitude
*exploitation* have **opposite data requirements**. Discovery is a low-sample operation:
detecting that an edge exists is a hypothesis test, and a typed dependency graph is recoverable
from tens of observations (Section 5). Exploitation — training a model that consumes that
structure to forecast, or to estimate an effect — is a high-sample operation: each coefficient is
an estimate whose variance scales as 1/N. Both draw on a single per-system data budget. Therefore
**the regime in which recovered structure is most valuable — scarcity — is exactly the regime in
which a magnitude-hungry consumer of it fails worst.** The engine earns its keep by discovering
structure *from scarce data*; the moment one tries to exploit that structure quantitatively, one
needs the abundance that scarcity, by definition, denies. Discovery needs low N; exploitation
needs high N; one small budget cannot be both.

This is **not generic overfitting.** The failure is not a property of model capacity alone but of
a structural mismatch in data requirements, and the regimes are distinct: below a dozen or so
observations a consumer correctly falls back to a structure-free baseline; through the low tens it
overfits the sparse structure it does find; and even at the few dozen a real macroeconomic series
affords (N≈34, Section 5.1) the sample is still too small to fit a deep model on the rich structure
it now sees. Even a perfectly regularised consumer cannot estimate magnitudes the data does not
contain — capacity control does not manufacture missing information.

We observe the full curve directly in the macroeconomic domain (Section 5.1). Feeding the engine's
recovered typed structure to a *shallow* consumer helps — type-aware edge features improve a
gradient-boosted forecaster by 4–7% over raw lags. Feeding the *same* structure to progressively
deeper, more magnitude-hungry consumers degrades them monotonically: a stacked foundation-model
meta-learner worsens by ~9–13%, and a graph neural network trained on the discovered topology ends
**96% worse** than a naive persistence baseline at the same ≈34-observation budget — and *no*
structure-exploiting forecaster beats persistence at all. Depth is punished in exact proportion to
the per-system magnitude it demands.

The resolution is not to ban depth but to **respect the split.** The discovered structure is
valuable precisely for the uses that consume *form* rather than per-system magnitude —
causal-adjustment-set selection (Section 5.5), anomaly detection against the recovered graph,
directional intervention rehearsal — all of which work at the low N where discovery itself works.
Any consumer that needs magnitudes must source them from a meta-learned cross-system prior,
adapted few-shot and transported across a federation, carrying uncertainty that widens
automatically under scarcity — never estimated freely from one system's scarce data.

### 3.5 The recoverability hierarchy

The theory's sharpest and most testable claim is an *ordering*. Structure does not all
recover at once. Univariate (autoregressive) structure recovers first; pairwise directional
structure second; three-way interactions (mediation, moderation, synergy) last — recoverable,
but only once the sample size reaches several times what pairwise structure needs, and
undetectable below that (measured in Section 5.4). The biological consequence is immediate:
drug–drug–patient interactions and immune-cross-talk terms are three-way terms, and are
therefore cohort/federation quantities rather than per-patient ones — a consequence of the
recoverability ordering we report, not a counsel of caution.

A refinement, forced on us by the data in Section 5, concerns magnitudes. Magnitudes are
not a single tier. **Stiff** parameters — those to which the observable is strongly
sensitive — are recoverable from very little data; **sloppy** or **slow** parameters — to
which the observable is weakly sensitive, often because they govern a slowly accumulating
state — are not recoverable at clinically plausible horizons. Sloppiness in this sense is a
well-studied property of multiparameter models (Sethna, Transtrum and colleagues); our
contribution is to place it inside the scarcity narrative and to show that it, not a flat
form-versus-magnitude split, is what the data supports.

### 3.6 Information-theoretic footing

The scarcity paradox (§3.4) and the magnitude tier of the hierarchy (§3.5) are stated above as
mechanisms and confirmed empirically in Section 5. In the idealised case they also *follow* from a
standard information inequality, which we record because it shows the split is a property of the
estimand under a data budget, not an artefact of any particular estimator.

**Lemma (detection is cheaper than estimation).** *Let θ be a scalar coupling parameter in a
regular parametric model with per-observation Fisher information i(θ); with N observations the
total information is I_N(θ) = N·i(θ). Then, to leading order:*

1. *(Detection — does the edge exist?) Testing H₀: θ = 0 against θ = θ\* by the score/Wald test,
   the statistic is non-central χ²₁ with non-centrality λ = N·θ\*²·i(θ\*). Achieving level α and
   power 1−β requires λ ≥ λ_c(α, β), so* **N_detect ≥ λ_c / (θ\*²·i(θ\*))**.
2. *(Estimation — what is θ?) Estimating θ to relative precision ε (Var θ̂ ≤ (εθ\*)²) requires,
   by Cramér–Rao, Var θ̂ ≥ 1/I_N(θ\*), so* **N_est ≥ 1 / (ε²·θ\*²·i(θ\*))**.
3. *(Cost ratio)* **N_est / N_detect ≥ 1 / (ε²·λ_c)** *— independent of θ: pinning a magnitude to
   fixed relative precision always costs a fixed multiple more data than detecting the edge, and
   the multiple grows without bound as ε → 0.*

*Moreover, writing the normalised sensitivity of §3.5 as S(θ) = ‖∂y/∂log θ‖ / ‖y‖, a Gaussian
observation model has information for log θ proportional to S(θ)², so* **N_est ∝ 1 / (ε²·S(θ)²)**.

**Proof sketch.** The score statistic for H₀: θ = 0 has, under the local alternative θ = θ\*, a
non-central χ²₁ law whose non-centrality is the squared standardised score, θ\*²·I_N(θ\*) to
leading order; requiring fixed power fixes a lower bound on that quantity, giving (1). The
Cramér–Rao bound Var θ̂ ≥ I_N(θ)⁻¹ for a regular unbiased estimator, set equal to the relative-
precision target (εθ\*)², gives (2); dividing gives (3). For the sensitivity form, in y = f(θ) +
η with η ∼ N(0, σ²I) the information for φ = log θ is σ⁻²‖∂f/∂φ‖² = σ⁻²S(θ)²‖y‖², and relative
precision on θ is absolute precision on log θ. ∎

Two readings follow. First, this *is* the scarcity paradox (§3.4) in one line: detection is a
low-N operation and exploitation a high-N one, on a shared budget, by a factor that widens as the
precision demanded on the magnitude tightens. Second, the inequality *grades the magnitudes*
(§3.5): a **stiff** parameter (S = O(1)) is estimable from moderate N, while a **sloppy/slow** one
(S → 0) requires N → ∞ — below the Cramér–Rao floor at any horizon over which S stays near zero.
Yet the edge it governs stays detectable whenever N·θ\*²·i(θ\*) clears λ_c: a relationship can be
present, and recoverable as *form*, exactly where its *magnitude* is information-theoretically out
of reach. The form/magnitude dissociation is derived, not assumed.

Two caveats fix the scope. The bound is asymptotic — a regular model, an unbiased estimator, and θ
off the boundary for the estimation half (the detection half is precisely the boundary case θ = 0,
which the score test is built for); online forgetting and finite samples move the constants, not
the scaling. And stream observations are dependent, so N enters as an effective sample size
N_eff < N, which shrinks both budgets but not their ratio. The full multi-parameter treatment —
the Fisher matrix whose eigenspectrum *is* the sloppiness structure of Sethna and Transtrum, under
dependent data and biased online estimators — is deferred; the scalar inequality already supplies
the footing the empirical ordering (Section 5.4) rests on.

### 3.7 Falsification

The theory is falsified if, on a system with known ground truth: tasks consuming only
form/direction fail under scarcity while magnitude-hungry tasks succeed (the asymmetry
reverses); or all tasks fail equally regardless of consumption type (recovery does no
work); or the recovered organization is a procedure artefact — i.e. data with the system's
temporal structure destroyed yields equivalent recovery. The third is directly testable and
is our principal control (Section 4.4).

A fourth criterion falsifies the latent construct itself, and is decisive. If the markers of
Section 3.1 do **not** concord — if the marker-by-transformation stability matrix (Section 3.8)
is full-rank, so that no shared factor governs which markers survive which transformations —
then there is no common latent and the construct is empty (the negation of rules 6–7). This
test is only interpretable with two controls: a **positive control**, a system whose shared
invariant is known to exist (the Topp diabetes oracle, whose attractor count *is* its conjugacy
invariant) and which the procedure must detect as concordant; and a **negative control**,
independent noise markers, which the procedure must *not* report as concordant. Without the
positive control a null cannot be distinguished from an underpowered instrument; without the
negative control a positive cannot be distinguished from a procedure that finds structure in
anything. We specify this test here and execute it — controls included — as the programme's
first empirical paper. The present paper is its prerequisite: it establishes that the markers
are individually recoverable (Section 5), without which concordance cannot be posed.

### 3.8 Markers, transformations, and the concordance test

The latent construct of Section 3.1 turns the theory's central empirical question into one
concrete object. We enumerate **candidate markers** of organizational identity and the
**transformations** under which their stability can be probed, and ask: *which markers remain
stable under which transformations?*

| Candidate marker | Status in this paper |
|---|---|
| typed dependency graph (form) | computed — Section 5.2 |
| causal motifs (directed structure) | computed — Sections 5.2, 5.5 |
| attractor fingerprint | computed — Section 5.6 |
| recoverability profile / hierarchy | computed — Sections 5.2–5.4 |
| conservation constraints | introduced, deferred |
| symmetry properties | introduced, deferred |

The candidate transformations are parameter variation, perturbation, sampling change, and
measurement change (all exercised in this paper), together with node addition/removal and
temporal/multi-scale evolution (introduced, deferred). Arrange them as a matrix **M** with
markers as rows and transformations as columns; the entry M[i,j] is the stability of marker
*i* under transformation *j* (1 = unchanged across the transformation's orbit, 0 = destroyed).

The latent-construct hypothesis (H3) makes a sharp, falsifiable prediction about **M**: if a
single organizational identity underlies the markers, **M** is **low-rank** — a dominant shared
factor (an *identity-fidelity*) explains which markers survive which transformations, and that
factor reproduces the recoverability hierarchy (rule 5). If instead **M** is full-rank — every
marker idiosyncratic, no shared ordering — there is no common latent and the construct is
refuted. This **concordance test**, run with the positive and negative controls of Section 3.7,
is the decisive experiment of the programme. We specify it here as part of the foundation and
run it as the **first empirical paper**; the present paper supplies the prerequisite — that the
individual markers are recoverable at all (Section 5) — without which the concordance question
cannot be posed.

### 3.9 Status of the claims

A foundational paper introduces more than any one work can prove. We therefore state explicitly,
for each concept, what this paper *establishes* and what it *defers*, so that demonstrated
results are never confused with the programme's promises. Everything marked *deferred* is a
stated direction, not a claim of this paper.

| Concept | Status in this paper |
|---|---|
| Scarcity regime | **defined and measured** (the scarcity paradox, §5.1) |
| Detection-vs-estimation footing | **proved** (idealised; the Cramér–Rao lemma, §3.6) |
| Recoverability hierarchy (H2) | **demonstrated** — four heads + macro (§5.2–5.4) |
| Form / magnitude dissociation | **argued** (§3.6) and **demonstrated** on the oracle (§5.2, §5.5) |
| Organizational identity (latent construct) | **introduced; initial evidence** via one marker (§5.6) |
| Organizational markers | **defined; 4 of 6 instantiated** (§3.8) |
| Marker concordance (H3 — the latent is real) | **introduced; deferred** to the first empirical paper |
| Conservation / symmetry markers | **introduced; deferred** |
| Multi-scale (vertical) persistence | **named; deferred** |
| Magnitude borrowing (cohort priors) | **motivated; deferred** to a methods paper |

---

## 4. Methods

### 4.1 The recovery engine

Structure is recovered by a streaming relationship-discovery engine that maintains a
population of typed relationship hypotheses (15 types spanning causal, correlational,
functional, temporal, competitive, mediating, and others) and tests each against the data
stream as an active constraint. Each candidate is calibrated against a type-appropriate
permutation null (block permutation for lagged relationships, random shuffle for
contemporaneous, phase randomisation for self-referential), with Benjamini–Hochberg control
of the false-discovery rate. An edge is reported only after it clears this significance
gate; calibration reduces the null false-positive rate to ≈0 on the synthetic benchmark
(Section 5.1). For the directional (Granger-style) hypotheses the engine also reports an
orientation and forward/backward test statistics, which we use to score directed edges. We
run the engine in its exact (non-vectorised) mode, which carries the calibrated per-edge
evidence used throughout.

### 4.2 The biological digital twin

The twin is a multi-scale mechanistic substrate (cells → tissues → organs → organ systems →
organism) on which **disease heads** act as parameter perturbations. Each head is founded on
a *published, validated* model so that its form and its literature parameters are not
invented:

- **Diabetes** — the Topp βIG model of glucose / insulin / β-cell-mass dynamics (Topp et
  al., 2000), parameters from a curated BioModels entry. Disease is a regime of reduced
  insulin sensitivity; the model is bistable (compensation vs glucotoxic collapse).
- **Oncology** — the Lotka–Volterra sensitive/resistant clone competition model used in the
  metastatic-prostate-cancer adaptive-therapy programme (Zhang et al., 2017; West et al.,
  2022). Asymmetric competition plus a cost of resistance reproduce competitive release.
- **Fibromyalgia** — the gate-control pain loop (Britton & Skevington, 1989; a recent
  Lotka–Volterra formalisation of ascending/descending pathways) extended with a slow
  central-sensitization gain. Fibromyalgia is the regime of heightened central gain and
  impaired descending inhibition, producing a bistable chronic-pain attractor with enhanced
  temporal summation (wind-up), the documented clinical hallmark (Staud et al.). This head
  replaces a generic protein-spreading CNS model, which is the wrong mechanism for a
  central-sensitization disorder.
- **Autoimmune** — the Vélez de Mendizábal et al. (2011) effector–regulatory T-cell
  cross-regulation model; relapses are driven by stochastic infection triggers.

Each head is implemented as a differentiable system, so the same trajectory used for
structure recovery can be inverted for parameter sensitivity.

### 4.3 The dissociation harness

For each head we generate a patient trajectory under an excitation appropriate to the
system (repeated meals for diabetes; adaptive therapy for oncology; a temporal-summation
pulse train for fibromyalgia; stochastic flare triggers for autoimmune) so that the state
variables genuinely co-vary — a system resting at a fixed point carries no recoverable
structure. We then measure, on the **same trajectory**:

- **Form recovery** — the engine's recovered typed edges, scored against the head's known
  coupling graph as directed-edge F1 (precision/recall over orientations), or undirected F1
  where the coupling is symmetric and the engine cannot resolve orientation. Indirect edges
  (a correlation between two children of a common driver) count as false positives, honestly
  lowering precision.
- **Magnitude identifiability** — the normalised sensitivity of an observable to a
  fractional change in a parameter, S(θ) = ‖∂y/∂log θ‖ / ‖y‖, computed by automatic
  differentiation. Large S means stiff/identifiable; near-zero S means sloppy. For each head
  we report a stiff parameter and a slow parameter, chosen **empirically** by a
  sensitivity-versus-horizon scan (intuition mis-identified the stiff parameter for several
  heads — see Section 5.4).

### 4.4 The shuffle control

The principal falsification check (Section 3.7) permutes each variable's time index
*independently*, destroying all cross-variable lead/lag structure while preserving each
marginal distribution. This is a stronger null than a joint row-permutation (which shuffles
all variables with one shared permutation and so preserves contemporaneous cross-variable
correlation while breaking only the time axis): the independent shuffle removes the
cross-variable dependence the recovered edges encode. Form recovery on this null must
collapse to ≈0; if it does not, the recovered structure is an artefact of the procedure
rather than the system's organization.

### 4.5 The breakpoint analysis

To locate where form recovery itself breaks, we shrink the observation budget N on one head
(oncology, the cleanest) and find the N at which directed-edge F1 collapses toward the
shuffle null. We use a contiguous shorter observation window rather than subsampling a fixed
trajectory, because subsampling a quasi-periodic signal aliases the oscillation and produces
spurious non-monotonicity.

### 4.6 Two causal engines: online form, offline magnitude

The form/magnitude split is realised by two distinct causal engines, and the division of
labour mirrors the theory exactly. The **online** engine is the streaming Granger
discovery described in Section 4.1: it recovers the *directed dependency structure* — which
factors couple, in which direction — cheaply and incrementally, and is what survives at low
N. This is *predictive* (Granger-style) recovery, not interventional identification.

The **offline** engine supplies the magnitude. Given the full dataset and the structure the
online engine discovered, it performs proper **do-calculus identification** (DoWhy: backdoor
adjustment for ATE/ATT/ATC, with placebo / random-common-cause / subset refutations) and
**heterogeneous-effect estimation** (EconML double-machine-learning for conditional effects).
The online structure supplies the adjustment set; the offline engine identifies and estimates
the effect through it. Online form → offline magnitude, automatically.

We validate this against the oracle with a **confounded treatment cohort** drawn from the
validated Topp diabetes model. Each simulated patient is run both treated (an
insulin-sensitiser) and untreated, so the true counterfactual average treatment effect is
known. Disease severity confounds both treatment assignment (sicker patients are more likely
treated) and the outcome (sicker patients have higher glucose), so the naive treated-minus-
untreated association is biased; recovering the true effect requires adjusting for the
confounder that the online engine discovers.

---

## 5. Results

### 5.1 Domain I — macroeconomics (real-world federated time series)

**Setup.** World Bank annual national-accounts indicators (19 series) for seven East African
economies — Kenya, Tanzania, Uganda, Rwanda, Ethiopia, Mozambique, Zambia — each ≈34 annual
observations (1990–2023), plus a labelled synthetic multivariate benchmark (N=3000, fifteen
relationship types with a known generative graph) for ground-truth scoring. The nodes are
genuinely heterogeneous: mean Jensen–Shannon divergence across country pairs is 0.295, with
49% of indicator pairs maximally divergent — a non-IID setting where the per-system
organizational identity, not a shared global model, is the right learning target. A streaming
discovery engine maintains a population of typed relationship hypotheses (causal/Granger,
correlational, functional, temporal, competitive, mediating, and others), each tested against
the data stream and calibrated against a type-appropriate permutation null.

**Form is recovered — but recovery is calibration-dependent, and we are explicit about it.**
On the synthetic benchmark with a known graph, the engine recovers typed structure at
precision and recall 1.00 with a null false-positive rate of 0.00. On real data, however, the
engine's *raw* internal confidence is not a significance test: on pure-noise data it admits
false positives at a **41% rate**, and the true relationships are not ranked highly (first
ground-truth match at rank **123** of ≈250). A post-hoc calibration — type-appropriate
permutation p-values, Benjamini–Hochberg FDR control, and block-bootstrap stability selection
— is mandatory and decisive, and it is what makes the engine competitive with, and then
better than, strong sparse baselines on ranking the true structure first (Kenya, full-mode
calibration):

| method (calibrated) | first-ground-truth rank | null FPR |
|---|---:|---:|
| streaming typed engine | **4** | 0.00 |
| correlation + AR "economist" scan | 8 | 0.00 |
| Pearson + Bonferroni | 9 | 0.00 |
| graphical lasso | 11 | 0.00 |
| *raw engine confidence (uncalibrated)* | *123* | *0.41* |

Calibration drives the null FPR from 0.41 to 0.00 and the first-ground-truth rank from 123 to
4. We report calibrated numbers throughout, and we report the honest comparator: at this
sample size simple sparse methods are close, and the engine's edge is ranking the true
relationship earliest (rank 4 vs 8–11), plus the breadth of its typed, streaming, federated
discovery — not a blanket accuracy supremacy.

**Shallow consumers of the recovered form benefit.** Using the recovered typed structure as
features for a shallow forecaster improves a gradient-boosted model by **4–7%** over raw-lag
features; and graph-conditioned anomaly residuals reach F1 = **0.80** at large sample size
(N≈3000) versus 0.65 for a blind univariate detector, catching structural decouplings the
blind detector cannot see.

**The scarcity paradox, measured.** This is the domain's sharpest result. As a consumer of
the recovered structure is made *deeper* — demanding more per-system magnitude from the same
≈34-observation budget — its accuracy collapses monotonically (five-country mean MAE,
one-step-ahead; naive persistence = 2.454):

| consumer of the recovered structure | depth | mean MAE | vs persistence |
|---|---|---:|---:|
| type-aware edge features → shallow tree | shallow | 2.541 | (−4.4% vs raw-lag features) |
| persistence + structure-informed delta | + | 2.489 | +1.4% |
| foundation-model stacked meta-learner | ++ | 2.791 | +8.9% |
| graph neural network on discovered topology | +++ | **4.812** | **+96%** |

No deep hybrid beats persistence; the graph neural network, the deepest consumer, is the
worst by far (+96%). The recovered structure *helps* a shallow consumer (type-aware features
beat raw lags by 4–7%) and *destroys* a deep one — the theory's predicted failure curve,
measured on real data.

**Caveats we report rather than hide.** Graph-conditioned forecasting and anomaly residuals
help only above roughly 200 effective observations and *hurt* below (the break-even sits
between ~100 and ~300 samples, where non-stationary trends inflate residuals). And the engine
measures **Granger-predictive recovery, not structural causal identification**: observational
equivalence is not resolved, and a deliberately non-causal shock propagates through the
discovered graph as readily as a real one. These limitations stem from the absence of
ground truth in real data — exactly what the biological domain supplies next.

### 5.2 Domain II — biology (mechanistic digital twin, controlled ground truth)

Where the macroeconomic domain has real data but no ground-truth graph, the biological domain
has a *known* generative model. We build a mechanistic digital twin from four validated,
published disease models — one per organ system — so the recovered structure can be scored
against truth and identifiability computed exactly. The same streaming engine, pointed blind
at simulated patient trajectories, recovers the known coupling graph of every head while the
shuffle null collapses (mean over three patients):

| Head | System | form F1 | shuffle null | stiff mag. | S(stiff) | slow mag. | S(slow) | stiff/slow |
|---|---|---:|---:|---|---:|---|---:|---:|
| Diabetes | metabolic | 0.4–0.5 | 0.00 | insulin sensitivity | ~0.43 | β-turnover rate | 0.03–0.24 | 15→2 |
| Oncology | oncologic | **1.00** | 0.00 | sensitive growth rS | 0.05–0.20 | resistant growth rR | ~0.000 | **~224** |
| Fibromyalgia | chronic pain | **0.80** | 0.00¹ | descending inhibition γ | 1.1–1.4 | sensitization rate εG | 0.13–0.35 | 3.3–10.6 |
| Autoimmune | autoimmune | **1.00** | 0.00 | regulatory prolif. αR | 0.7–2.4 | effector prolif. αE | 0.2–0.29 | 2.5–10 |

¹ one large-N shuffle leak (one horizon/seed); 0.00 at the other three horizons.

Three predictions hold on all four heads. **Form is recovered** — perfectly for oncology and
autoimmune (F1 = 1.00); for fibromyalgia at F1 = 0.80 (recall 1.00, precision lowered by an
indirect edge between two children of pain); for diabetes at 0.4–0.5 (precision lowered by
indirect edges and the always-missed insulin→glucose clearance arm, which is swamped because
glucose is meal-dominated — a theory-consistent identifiability limit). **The shuffle null
collapses** to ≈0 everywhere: destroying temporal structure annihilates recovery, so the
recovered form is the system's organization, not an artefact. **Magnitudes split into two
tiers**: each head has a stiff parameter, recoverable throughout, and a slow/sloppy parameter
that is not, separated by 2.5× to 224× in normalised sensitivity. Each slow parameter is
physiologically interpretable: one cannot estimate the resistant clone's growth rate while
it is competitively contained (oncology); the β-cell damage rate needs months of observation
(diabetes); the central-sensitization rate is weakly identified until wind-up has built
(fibromyalgia).

**Uncertainty (three seeds).** All biological values are means over three independently seeded
patients. The form-recovery result carries no seed noise: edge-recovery F1 is identical across
seeds for every head (the recovered edge set, and hence recall and precision, is structurally
determined), so the dissociation form F1 ≫ shuffle is exact, not averaged. For the magnitude
tiers we report the across-seed 95% interval (Student-t, two degrees of freedom). The
stiff-versus-slow sensitivity separation is significant — the two intervals are disjoint — at
every horizon for oncology (at N=60, S(stiff) = 0.201 vs S(slow) = 0.001) and fibromyalgia (at
N=500, 1.15 ± 0.10 vs 0.34 ± 0.05), and for autoimmune at N ≥ 400 (2.21 ± 0.70 vs 0.25 ± 0.23).
The one exception is autoimmune at its smallest horizon (N=200), where the stiff interval
(0.71 ± 0.68) overlaps the slow one (0.29 ± 0.29) and the separation is not yet significant at
three seeds — reported here rather than hidden. The claim-bearing quantity throughout is the
separation, and at three seeds it exceeds the across-seed interval everywhere except that single
low-N autoimmune cell.

### 5.3 Where form breaks

Form recovery is not free. Shrinking the oncology observation window locates a sharp
threshold: directed-edge F1 holds at 1.00 down to ≈36 observations, then collapses to ≈0 by
32 — a cliff, consistent with the engine's permutation-significance gate (below ≈36 samples
the edge cannot clear the null). The autoimmune head is more robust (≈30). Form recovery has
a real, modest, and sharply-defined data requirement.

### 5.4 The hierarchy, corrected by the data

Two findings reshaped the framing and we report them as results, not footnotes. First, the
stiff parameter was mis-identified by intuition for three of four heads — the parameter we
expected to be hard was in fact the more identifiable one — and had to be chosen by the
sensitivity scan. Second, and more importantly, **a single stiff magnitude is recoverable
from fewer observations than form**: insulin sensitivity is recovered to ≈2% error from
eight sparse, noisy samples, where form recovery needs ≈36. Declaring an edge must clear a
permutation-significance bar, a higher evidence threshold than fitting a well-posed scalar.

The clean slogan "form recovers, magnitudes do not" is therefore false. What the data
supports is the **recoverability hierarchy**:

> Form and stiff magnitudes recover from modest data (tens of observations); slow and sloppy
> magnitudes do not recover at the horizons clinical data spans.

The load-bearing, falsification-surviving claim is the bottom tier: the quantity one
genuinely cannot get per-system is the slow/sloppy magnitude — which is exactly the quantity
that must be borrowed from a cohort.

Third, the *structural* ordering itself — univariate, then pairwise, then three-way — is now
measured rather than asserted. Streaming diabetes-oracle trajectories of increasing length
through the discovery engine, and scoring the three-way (mediation) hypotheses by the Sobel
indirect-effect test, gives:

| N (observations) | univariate | pairwise | three-way (mediation) |
|---|:---:|:---:|:---:|
| 50  | — | — | — |
| 100 | ✓ | ✓ | — |
| 400 | ✓ | ✓ | — |
| 600 | ✓ | ✓ | ✓ |
| 800 | ✓ | ✓ | ✓ |

Univariate and pairwise structure recover together at ≈100 observations; three-way mediation
first clears significance at ≈600 — roughly six times the data — and remains recoverable out
to the full 3840-sample trajectory (Sobel p = 1.3×10⁻⁸). The predicted ordering holds. It is
worth stating plainly how we know the instrument is trustworthy, because it bears on the
theory's own falsification standard (Section 3.7): an earlier version of this measurement
returned *mediation never recovers* — which would have read as strong support for the
"or never" reading of the hierarchy. It was an artifact. Two defects in the online estimator
(an unscaled Sobel standard error, and covariance windup over long streams) suppressed the
signal entirely, and a redundant causal-steps total-effect gate rejected indirect-only
mediation by construction. Repaired — the standard error scaled by residual variance, the
covariance update put in Joseph form, and the total-effect gate dropped in favour of the
indirect-effect criterion (Zhao, Lynch and Chen 2010) — three-way structure recovers as
above, with a null false-positive rate of 0 on independent-noise and direct-effect-only
controls. A spurious "never" became a measured "last," which is the stronger and the more
honest result. (In a tightly coupled feedback system several variable triples exhibit genuine
statistical mediation; the claim is that three-way structure becomes detectable at this
scale, not that one canonical chain does.)

### 5.5 The magnitude arm: do-calculus effect recovery

The recoverable magnitudes of Section 5.2 are sensitivity-identifiable parameters; the
clinically central magnitude is an *interventional effect*, which requires more than
identifiability — it requires correct adjustment for confounding. Here the oracle pays off a
second way. Because we simulate each cohort patient **both treated and untreated** (Section 4.6),
the true counterfactual effect of the sensitiser is *known* — ATE = **−34.8 mg/dl** — so an
estimator can be scored against ground truth directly, rather than against the indirect
refutations (placebo, random-common-cause) that stand in for truth only when truth is
unavailable. On this confounded cohort:

| estimator | ATE (mg/dl) | error vs truth (−34.8) |
|---|---:|---:|
| naive treated − untreated (no structure) | **−7.9** | 26.9 (4.4× attenuated) |
| DoWhy backdoor, adjusting for severity (ATE / ATT / ATC) | **−34.2** | 0.6 |
| coupled: online-Granger adjustment set → DoWhy | **−34.2** | 0.6 |
| EconML double-ML (CATE, mean) | **−34.9** | 0.1 |

Two things hold. First, **the naive estimate is biased nearly five-fold** by confounding, and the
offline engine recovers the true effect to within 1 mg/dl — but only because it adjusts for the
confounder, *and the confounder is supplied by the form*. Run blind, the online engine
independently discovers the adjustment set ({severity}); handed that set, the offline engine
identifies the effect automatically. This is the form/magnitude pipeline made operational:
structure recovered cheaply online is exactly what licenses correct (do-calculus) magnitude
estimation offline.

Second — and this is the robustness argument — **the validation here is concordance against a
known answer, not an internal refutation suite.** Two methodologically independent estimators,
backdoor adjustment (a linear potential-outcomes fit) and double-machine-learning CATE (a
forest-based estimator), together with the structure-coupled pipeline, all land within 1 mg/dl of
the oracle's −34.8. (ATT and ATC are reported but are *not* independent votes: under a linear
backdoor they coincide with the ATE; and the LATE and mediation estimands abstain on this
single-confounder cohort, which contains no instrument or mediator chain — so of the offline
engine's estimand suite, the genuinely independent estimators on this design are the backdoor
family and the causal forest.) Agreement of independent estimators on the *true* value is a
stronger check than placebo or random-common-cause refutation, which only probe an estimator's
internal consistency. The refutation suite is in any case currently blocked by a version drift in
the offline causal library; with oracle ground truth in hand it is not the load-bearing check.

The honesty boundary is unchanged: the online arm is Granger-predictive, not interventional; the
*interventional* claim rests on the offline identification and the adjustment set the form
provides.

### 5.6 A marker of identity, measured: the attractor fingerprint

The latent construct of Section 3.1 predicts that a *marker* of identity — here the attractor
fingerprint — should obey its rules. Each of three such predictions is measurable on the diabetes
oracle (whose flow we know). We compute a system's identity fingerprint by multi-start
integration — running the slow β-cell dynamics to their attractor from a grid of initial
β-cell masses and counting the distinct steady states. The validated Topp system is
saddle-node bistable: a *compensated* patient has two attractors (a normoglycaemic one and
a hyperglycaemic one, separated by a saddle); a *decompensated* patient has one.

- **Same identity, different magnitudes.** A cohort of twelve compensated patients with
  insulin sensitivity and hepatic output varied widely shares a *single* identity (attractor
  count = 2 for all), while the β-cell mass at the healthy attractor — a within-class
  magnitude — spans 282 to 1165 mg (a ~4× range of compensatory hyperplasia). Identity is
  invariant to the magnitudes.
- **A bifurcation is an identity change.** Sweeping β-cell destruction (the type-1
  mechanism), the fingerprint flips from two attractors to one at a death rate of
  ≈0.014/day — exactly the analytic saddle-node, where the destruction rate first exceeds
  the maximum net β-cell growth rate (0.0135/day) so that no β-mass can sustain the healthy
  attractor. Disease progression *is* traversal of the bifurcation set; the patient's
  organizational identity changes there.
- **The invariant is discrete, the magnitudes continuous.** Across the compensated class the
  attractor count is fixed at 2 while the healthy-attractor β-mass drifts continuously from
  300 to 1000 mg as sensitivity falls. The identity is a discrete (combinatorial) object;
  the magnitudes are continuous coordinates within it.

This turns the construct from a stipulation into something with at least one concrete,
well-behaved marker: the attractor fingerprint is observer-independent (rule 1), invariant
under wide magnitude variation (rule 2), discrete and identity-distinguishing (rule 6), and it
changes precisely at a bifurcation. It is one marker, not the identity itself (rule 4). Whether
it *agrees* with the other markers — concordance, rule 7 / H3 — is exactly the question the
programme's first empirical paper takes up; this paper establishes only that the marker is
recoverable and well-behaved on its own.

### 5.7 Domain III — financial markets (real high-frequency microstructure)

The third domain is real data with a hard economic cost function, and it is the sharpest
external test of the theory precisely because it *can* fail commercially. Where the biological
twin is a controlled oracle and the macroeconomic series are real but slow, financial market
microstructure is real, fast, adversarial, and priced: if recovered structure carried
exploitable magnitude, the market would already have removed it. The domain therefore lets us
ask the theory's question with money as the referee.

**Setup.** Six days of Bitcoin (BTC/USD) order-flow data at five-second resolution — 103,628
bars derived from roughly six million signed trades (Binance aggregate-trade dumps, the
buyer-maker flag signing the aggressor). From the signed trades we form a microstructure panel:
returns, order-flow imbalance and signed flow, trade intensity (trade count per bar), realized
volatility, and volume-weighted-price deviation. As in macroeconomics this is an *observational*
domain — recovery is Granger-predictive and the offline effects are do-calculus on observational
data, not interventions. Here "scarcity" is not few samples (we have many) but scarcity of the
scarce thing that actually matters in a market: *exploitable* signal, with retail transaction
cost as the exploitation budget.

**Form is recovered — and typed — with no question posed.** Pointed blind at the seven-variable
panel, with no treatment, outcome, or adjustment set specified, the engine recovers a 29-edge
typed graph spanning **six** of its relation types (correlational ×19, functional ×4,
competitive ×2, logical ×2, probabilistic ×1, synergistic ×1). The decisive observation is not
that it finds edges but that it *types* them correctly. The only relation it draws to the
next-bar return is **trade-intensity → next-return, typed functional** — and that typing is
right: trade intensity predicts the *magnitude* of the next return (correlation with the
absolute next return +0.18) and not its *sign* (correlation with the signed next return −0.008).
The directional order-flow-imbalance ↔ return coupling it types separately as correlational. The
engine separated a volatility relation from a directional one on its own — a distinction a posed
"does imbalance predict return?" query cannot see, and which later explains the regime structure
of the directional effect. This is marker recovery in the wild: recovered structure that is not
merely present but semantically resolved.

**The online-form / offline-magnitude split reproduces (§4.6), now against an efficient market.**
The online Granger engine recovers the directed form, but its calibrated confidence never
cleanly clears the shuffle null at any operating point — and more data does not rescue it. A
multi-seed null-confirmation sweep on 20,000 bars makes the failure exact: at the only confidence
threshold with a 0% null false-positive rate the engine **abstains** (reports no directional
edge); the threshold low enough to *confirm* the real order-flow → return edge admits
shuffled-null confirmations **40–80%** of the time. There is no threshold that certifies the true
edge with a clean null. The offline do-calculus engine, given the full sample, nonetheless
recovers the magnitude the online arm cannot certify: a significant backdoor-adjusted effect of
order-flow imbalance on the next return (average treatment effect ≈ +8×10⁻⁶ per unit imbalance;
placebo-permutation p < 0.001 (0 of 1,000 permutations); the estimate agrees across every requested
estimand — ATE = ATT = ATC, with EconML double-machine-learning CATE and ITE concurring, all run
in one call). Online form, offline magnitude — the same division of labour validated on the
diabetes oracle in §5.5, here holding on real adversarial data.

**The scarcity paradox returns as literal unexploitability.** The recovered magnitude is real and
robust — and worthless to a magnitude-hungry consumer, exactly as the theory predicts. It fails
on two independent axes. It is *transient*: a horizon sweep (non-overlapping, so the significance
is honest and the scenario is a real hold-*H* trade) shows the effect significant only out to
about one minute, then insignificant and sign-flipping — price-impact decay, not a persistent
drift that could accumulate past costs. And it is *sub-cost everywhere*: against a round-trip cost
of 0.06%, the per-decision effect reaches at most ~8% of the cost hurdle, even in the regime where
it is strongest (the effect scales 14× with trade intensity and peaks in US trading hours, yet
never crosses the line). The consequence is measured, not asserted: a directional strategy built
on the signal loses to costs; a naive strategy that greedily trades the strongest lagged
correlation loses *more than not trading at all*; and the disciplined engine — which reports only
calibrated structure and declines to certify an edge that fails its null — "abstains," and by
abstaining beats both. Structure recovery is cheap and succeeds; magnitude exploitation is
expensive and fails; and here the failure is denominated in currency. This is the macroeconomic
scarcity paradox (§5.1) reproduced in a second real-data domain, with the graph-neural-network's
96%-worse collapse replaced by a trading strategy that bleeds to the cost of turning recovered
form into acted-upon magnitude.

**Following the form to the recoverable magnitude.** The theory does not say magnitudes are never
recoverable; it says *which* are, and the recovered form is the map. Here the engine's own typed
discovery — trade-intensity → next-return as **functional/volatility**, not directional — pointed
away from the unexploitable directional edge and toward a recoverable one. Modelling that relation
yields a genuine next-horizon realized-volatility forecast: out-of-sample R² rises from 0.10 at
five seconds to **0.40 at ten minutes**. Trade intensity is largely *redundant* with realized
volatility for the level of the forecast (incremental R² ≈ 0) — but it survives adjustment for
realized volatility (p < 0.001) and sharpens the variance tails (QLIKE improved ~17% at the
shortest horizon), the regime where volatility bursts live. The form told us which magnitude was
recoverable; the directional magnitude was not, the volatility magnitude was, and the engine
flagged the difference by *type* before any of it was tested.

**What this domain does and does not show.** It is real-data evidence that the recovery engine
extracts and correctly types genuine structure from adversarial high-frequency data, that the
form/magnitude split holds where the market itself is the adversary, and that the scarcity paradox
survives translation into a hard cost function. It is *not* a claim that no exploitable
microstructure edge exists for anyone: the exploitability failure confounds three things we cannot
separate here — genuine market efficiency, retail-scale transaction costs, and a trade-derived
feature set with no limit-order-book depth (no true microprice or queue imbalance) — and it rests
on a single asset over a six-day window. As in macroeconomics the recovery is observational, not
interventional. What travels is the pattern, now seen a third time and under the most hostile
conditions available: form recovers and types itself; magnitude is real but not uniformly
exploitable; and the recovered form is what tells you which magnitude to reach for.

---

## 6. Related work

This work sits beside three literatures and departs from each on two axes; stating the departures
precisely is the cleanest way to say what the contribution is.

**The discovery component is not a causal-discovery method.** Causal-structure discovery — PC
(Spirtes et al.), GES, FCI, NOTEARS (Zheng et al.), LiNGAM (Shimizu et al.) — searches for a
*single* object, a causal graph, under a *single* semantics (conditional independence or
structural equations). The engine here instead maintains a *population* of fifteen typed
relationship hypotheses (causal/Granger, correlational, functional, temporal, competitive,
mediating, and others) competing in a streaming survival contest, of which causal is *one* type.
The depth of the causal-discovery literature reflects the difficulty of identifying direction and
confounding from observational data — causal is the hardest cell of the typed space — not a
privileged status that would make this engine "a causal-discovery method." We do not claim to
out-recover the causal specialists at causal structure (at low N they are stronger, by design);
the contribution is the typed breadth, the streaming calibrated discovery, and the use to which
the recovered structure is put.

**Sloppy-model identifiability** (Transtrum, Sethna and colleagues) characterises the magnitude
side — which parameters are stiff and which are sloppy. We adopt that machinery and place it
inside the scarcity narrative; the novelty is its unification with structure recovery and the
controlled cross-system replication, not the discovery that parameters can be sloppy.

**Magnitude borrowing is meta-learning, not mixed-effects.** When a per-system magnitude is
unrecoverable, the framework sources it from a cross-system prior by warm-started, few-shot
adaptation (in the lineage of MAML, Finn et al.; Reptile) transported across a federation
(FedAvg, McMahan et al.) — not by fitting population fixed effects with individual random effects.
The system shares *structure* and borrows *magnitudes*; it never pools them into a single
hierarchical regression, so non-linear mixed-effects modelling is not the relevant neighbour
despite the surface resemblance of "borrow from a cohort."

**Two axes of departure.** Against all of the above the work differs on two axes that, together,
are the contribution:

1. *Typed population, not single semantics.* Existing discovery recovers one privileged
   relationship type; we maintain a competing population of fifteen. Single-relationship
   discovery — causal discovery being its most-developed instance, because causal is the hardest
   — is the special case, not the parent.
2. *Marker, not target.* Every structure-learning method treats the recovered graph as the
   *object of interest* — the thing one wanted. We treat it as a *marker* of a latent
   organizational identity, a lossy indicator of an unobserved invariant, which no discovery
   method does. This is the deeper departure, and it is what ties the method back to the theory:
   the graph grows with more data and more variables, while the identity it marks does not.

The epistemology is borrowed with acknowledgment. Treating identity as a latent inferred from
convergent markers is the logic of construct validity (Cronbach & Meehl); defining it by its
invariance group follows Klein's Erlangen program; and the term *organizational identity* is taken
from organization theory (Albert & Whetten) and given a dynamical-systems meaning here.

---

## 7. Discussion

### 7.1 The scarcity-paradox resolution, made concrete

The hierarchy gives the governance rule operational teeth. A per-patient twin may state form
and direction confidently ("inflammation tends to drive this patient's fatigue"; "glucose
harms this patient's β-cells") because those are recoverable. It must label every slow
magnitude as cohort-derived ("how *fast*, we estimate from people like you, not yet from
you"), because those are not. Magnitude supply is then a separate pipeline — a meta-learned
warm-start prior, adapted few-shot and transported across a federation without raw data,
reported with uncertainty that widens under scarcity — rather than a free per-patient
estimate. The theory thus does not forbid mechanistic, decision-grade twins; it specifies
the provenance every quantity must carry.

### 7.2 Why a controlled biological test matters

The macroeconomic results cannot, on their own, distinguish "form is recoverable" from "our
estimator is lucky," because there is no ground-truth graph and no way to compute parameter
identifiability exactly. The biological twin removes both ambiguities. Its generative
equations are known, so recovery is scored against truth; it is differentiable, so
identifiability is the exact sensitivity, not an estimator's variance. The cost is that the
generator and the recovery target share a model — there is no model mismatch — so the result
is a statement about *identifiability in principle*, the cleanest possible form of the claim,
and explicitly not a statement about real patients.

### 7.3 Clinical reading

Each head's hierarchy maps onto a familiar clinical intuition. In adaptive cancer therapy,
the contained resistant clone's growth rate is the decisive unknown and is precisely the
parameter one cannot measure while the clone is suppressed — the dilemma the strategy is
built around. In diabetes, the direction "hyperglycaemia damages β-cells" is available long
before an individual's damage *rate*. In fibromyalgia, the gate-control couplings and the
descending-inhibition strength are identifiable, but the central-sensitization rate — how
fast wind-up builds — is the sloppy magnitude. In each case the theory predicts which
clinical quantity is per-patient and which must be borrowed.

---

## 8. Limitations

*Macroeconomic domain.*

- **No ground-truth graph on real data.** The macroeconomic recovery is scored against
  *plausibility* and a synthetic benchmark, not a known real generative graph; the engine
  measures Granger-predictive recovery, not interventional identification (a non-causal shock
  propagates through the discovered graph as readily as a real one).
- **Calibration-dependent and baseline-competitive.** Raw engine confidence is uncalibrated
  (41% null FPR); only the post-hoc permutation/FDR/stability calibration is defensible, and
  even then simple sparse baselines (graphical lasso, correlation+AR) are close — the engine's
  edge is first-ground-truth rank and breadth, not blanket accuracy.
- **Annual frequency, small N.** ≈34 observations per country; graph-conditioning helps only
  above ~200 effective observations, and differences between methods are frequently inside
  bootstrap confidence intervals.

*Biological domain.*

- **Synthetic ground truth.** All biological results are simulation-generated and labelled as
  such. They are mechanistic-generalisation evidence, not clinical validity; no number here
  should be used on a patient. A clinical test requires the same battery on real cohort data
  and is gated on data access by design.
- **The generator fits itself.** The magnitude forward is the exact generating model, so the
  result bounds identifiability *in principle*; real data would add model mismatch.
- **Heterogeneous "slow" parameters.** Diabetes' slow magnitude rises in identifiability with
  horizon; the oncology and fibromyalgia slow magnitudes are closer to structurally swamped
  (flat, near-zero sensitivity). Both are valid for the hierarchy claim, but they are
  different phenomena and we do not conflate them.
- **Sloppiness is established.** Stiff/sloppy parameter spectra are well known in systems
  biology; our novelty is the unification with scarcity-limited structure recovery and the
  controlled cross-system replication, not the discovery that parameters can be sloppy.
- **Form-recovery precision.** Form F1 plateaus below 1.0 for the multi-variable heads
  because the engine confirms indirect edges (correlations between children of a common
  driver). The robust claim is form F1 ≫ shuffle F1 ≈ 0, not form F1 ≈ 1.
- **Shuffle leaks at large N.** The per-variable shuffle null is ≈0 in almost all cells but
  leaks to a moderate value in isolated large-N cases (fibromyalgia, the former CNS head),
  where heavy-tailed marginals can yield spurious correlational edges.
- **No single validated fibromyalgia ODE.** Unlike diabetes (Topp), fibromyalgia lacks a
  gold-standard quantitative model; the central-sensitization block is a literature-grounded
  extension of the published gate-control loop, documented as such, with time in model units.
- **Three seeds.** Each head is summarised over three independently seeded patients; the
  across-seed 95% interval is reported in Section 5.2. Form F1 carries zero seed variance, but the
  magnitude intervals are wide at n=3 — the stiff/slow separation is significant at every horizon
  except autoimmune's smallest (N=200), where the intervals overlap. Larger seed counts would
  tighten these intervals.

*Financial-markets domain.*

- **Observational, not interventional.** As in macroeconomics, recovery is Granger-predictive
  and the offline effects are do-calculus on observational data; there are no interventions, and
  the do-calculus identification rests on the usual unconfoundedness assumptions given the
  adjustment set.
- **The exploitability failure is confounded, deliberately.** The finding that the recovered
  effect cannot be traded profitably conflates three causes we cannot separate here: genuine
  market efficiency, retail-scale transaction costs, and a trade-derived feature set with no
  limit-order-book depth (no true microprice or queue imbalance). It is evidence that *this*
  structure is unexploitable under *these* costs, not a claim that no microstructure edge exists
  for any participant.
- **Single asset, short window.** One instrument (BTC/USD) over six days of five-second bars.
  Breadth across assets, venues, and regimes is future work; the domain establishes the pattern,
  not its universality across markets.
- **Discovered orientation is less stable than discovered structure.** The typed graph is stable
  enough to read the relation *types* off reliably, but the discovered *parents* of a specific
  target flicker between runs at the observation caps required to keep the non-vectorised engine
  tractable (discovery is quadratic in panel width). The type-level claims are robust; the
  node-level adjustment set at small caps is not, and we lean on the offline arm's own adjustment
  where a specific effect is estimated.

---

## 9. Conclusion

We introduced **Organizational Identity Theory for Dynamic Data**: a framing of what is
recoverable from scarce, drifting systems as a partially persistent organizational identity — a
latent continuity inferred from *markers*, chief among them the topological-conjugacy class of a
system's flow and its recoverable projection, the typed dependency graph — distinct from the
magnitudes that drift within it. We supported the theory in three domains. In
**macroeconomics**, on real federated time series across seven economies, the recovered
structure helps shallow consumers (type-aware features +4–7%) while progressively deeper
magnitude-hungry consumers fail monotonically (a graph neural network +96% over a naive
baseline) — the scarcity paradox, measured. In **biology**, on a mechanistic twin that serves
as its own ground truth, a streaming engine recovers the known coupling structure across four
organ systems while a temporal-shuffle null collapses; identifiability separates into a stiff
tier recoverable from a handful of observations and a slow/sloppy tier that is not; and an
offline do-calculus engine recovers a known causal effect that naive estimation biases
four-fold. In **financial markets**, on six days of real Bitcoin microstructure, the same
engine — pointed blind at the order-flow panel — autonomously recovers and correctly *types*
the relationship graph, the online-form/offline-magnitude split holds against an efficient
market (no confidence threshold certifies the directional edge with a clean shuffle null, yet
the offline engine recovers a robust order-flow → return effect, placebo p < 0.001), and the
scarcity paradox turns literal: the effect is transient and below transaction cost at every
horizon, so a magnitude-hungry trading strategy loses while the disciplined engine abstains —
and the engine's own typed discovery points to the one recoverable magnitude here, a
realized-volatility forecast reaching out-of-sample R² 0.40. The honest form of the result is a recoverability hierarchy rather than a flat
form-versus-magnitude split, with the non-recoverability of slow magnitudes as the
load-bearing, cohort-borrowing-justifying claim. The same machinery that recovers structure
should therefore *refuse* to estimate slow magnitudes per-system, and source them instead
from a cohort, with uncertainty that widens under scarcity.

We present this as the **foundational paper** of the theory, not its last word. The three
domains here were chosen to be complementary — real-world breadth (macroeconomics), controlled
ground truth (biology), and a priced adversarial test (financial markets) — and to establish
the framework: definitions, the seven rules of identity, hypotheses,
falsification criteria, and a reusable recovery / identifiability / shuffle-control battery.
Throughout, we treated the recovered graphs, motifs, and fingerprints as *markers* of a latent
organizational identity, never as the identity itself. The immediate next step — the programme's
**first empirical paper** — is the decisive test of that latent: whether the markers *concord*
(H3), run with the positive (the Topp oracle) and negative (independent noise) controls of
Section 3.7. Beyond it the programme has two natural axes of extension. *Depth*: carry the
biological battery to real patient cohorts — the
clinical test the synthetic-honesty rule reserves. *Breadth*: carry the same battery to
further domains in which systems drift under scarcity — engineered and physical sensor
systems, ecological and climate dynamics, neural recordings — each a new opportunity to
confirm the recoverability hierarchy or to falsify it. A theory of what is recoverable should
be judged by how widely its single prediction — form and stiff magnitudes recover, slow and
sloppy magnitudes do not — continues to hold; that adjudication is the work this paper begins.

---

## References

1. Topp B., Promislow K., De Vries G., Miura R.M., Finegood D.T. (2000). A model of β-cell
   mass, insulin, and glucose kinetics: pathways to diabetes. *J. Theor. Biol.* 206:605–619.
2. Zhang J., Cunningham J.J., Brown J.S., Gatenby R.A. (2017). Integrating evolutionary
   dynamics into treatment of metastatic castrate-resistant prostate cancer. *Nat. Commun.*
   8:1816.
3. West J. et al. (2022). Towards multidrug adaptive therapy. *eLife* 11:e76284.
4. Melzack R., Wall P.D. (1965). Pain mechanisms: a new theory. *Science* 150:971–979.
5. Britton N.F., Skevington S.M. (1989). A mathematical model of the gate control theory of
   pain. *J. Theor. Biol.* 137:91–105.
6. Staud R. et al. Slow temporal summation of pain for assessment of central pain
   sensitivity and clinical pain of fibromyalgia patients. *PLoS One* (PMC3928405).
7. Vélez de Mendizábal N. et al. (2011). Modeling the effector–regulatory T cell
   cross-regulation reveals the intrinsic character of relapses in multiple sclerosis. *BMC
   Syst. Biol.* 5:114.
8. Raj A., Kuceyeski A., Weiner M. (2012). A network diffusion model of disease progression
   in dementia. *Neuron* 73:1204–1215.
9. Fornari S., Schäfer A., Jucker M., Goriely A., Kuhl E. (2019). Prion-like spreading of
   Alzheimer's disease within the brain's connectome. *J. R. Soc. Interface* 16:20190356.
10. Transtrum M.K., Machta B.B., Brown K.S., Daniels B.C., Myers C.R., Sethna J.P. (2015).
    Perspective: Sloppiness and emergent theories in physics, biology, and beyond. *J. Chem.
    Phys.* 143:010901.
11. Benjamini Y., Hochberg Y. (1995). Controlling the false discovery rate. *J. R. Stat.
    Soc. B* 57:289–300.
12. Friedman J., Hastie T., Tibshirani R. (2008). Sparse inverse covariance estimation with
    the graphical lasso. *Biostatistics* 9:432–441.
13. Phipson B., Smyth G.K. (2010). Permutation P-values should never be zero. *Stat. Appl.
    Genet. Mol. Biol.* 9:Article 39.
14. Granger C.W.J. (1969). Investigating causal relations by econometric models and
    cross-spectral methods. *Econometrica* 37:424–438.
15. McMahan H.B. et al. (2017). Communication-efficient learning of deep networks from
    decentralized data. *AISTATS* (FedAvg).
16. Ansari A.F. et al. (2024). Chronos: learning the language of time series. *arXiv:2403.07815*.
17. Albert S., Whetten D.A. (1985). Organizational identity. *Research in Organizational
    Behavior* 7:263–295.
18. Cronbach L.J., Meehl P.E. (1955). Construct validity in psychological tests. *Psychological
    Bulletin* 52:281–302.
19. Klein F. (1893). A comparative review of recent researches in geometry [the Erlangen
    Program]. *Bull. New York Math. Soc.* 2:215–249.
20. Zhao X., Lynch J.G., Chen Q. (2010). Reconsidering Baron and Kenny: myths and truths about
    mediation analysis. *J. Consumer Research* 37:197–206.

---

*Reproducibility.* The biological results are produced by `biotwin/validation/` —
`recovery_bridge.py` (online Granger bridge and sensitivity), `dissociation.py` (diabetes
hierarchy), `heads.py` (oncology / fibromyalgia / autoimmune sweeps and the oncology
breakpoint), `causal_offline.py` (the offline DoWhy/EconML magnitude arm and the
confounded-cohort effect recovery, built on `scarcity.causal`), and `identity.py` (the
attractor-fingerprint measurement of Section 5.6). Disease heads are in `biotwin/disease/`. Per-head result tables are written to `biotwin/validation/RESULTS.md`
and the accompanying JSON files.
