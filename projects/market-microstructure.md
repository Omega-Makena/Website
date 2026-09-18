---
title: High-Frequency Market Microstructure
date: 2026-06-10
description: Quantitative research in Bitcoin order flow and market dynamics.
category: Quantitative Research
---

# High-Frequency Market Microstructure

### Quantitative Research in Bitcoin Order Flow and Market Dynamics

This project investigates **high-frequency market microstructure** using Bitcoin trade data, with a particular focus on how order flow relates to short-horizon returns and volatility.

The study also serves as one of the real-data validation environments for **Scarcity**, testing its relationship-discovery machinery against a rapidly evolving financial system where dependencies can be short-lived, regime-dependent, and difficult to exploit after execution costs.

Unlike the controlled synthetic and mechanistic experiments, the market structure here is not known in advance.

The engine is pointed at the data and asked to determine what relationships exist, what form they take, and whether any discovered information survives out-of-sample and economic evaluation.

---

# 1. The Market Data

The experiment uses approximately **six days of Bitcoin trade-level data**.

From roughly:

* **6 million signed trades**
* approximately **100,000 five-second bars**

the research constructs a high-frequency representation of market activity.

The short aggregation interval preserves substantially more temporal structure than conventional daily financial data while keeping the problem computationally tractable for streaming analysis.

The data contains information derived from trade direction, trade intensity, and subsequent market behavior.

Importantly, the discovery stage was conducted **without specifying a target or adjustment set in advance**.

The system was therefore not simply asked to confirm a predetermined trading hypothesis.

---

# 2. Streaming Market-Structure Discovery

The central experiment uses Scarcity's streaming relationship-discovery engine.

The engine processes the market observations sequentially and maintains a living graph of candidate relationships.

Rather than treating every dependency as correlation, the discovery layer evaluates multiple relationship classes.

In this experiment it recovered a **29-edge typed relationship graph**.

The important result was not simply the number of edges.

It was that the engine distinguished relationships with materially different interpretations.

For example, it separated:

**Trade intensity → next-return magnitude**

from

**Order-flow imbalance ↔ return**

and assigned them different relationship types.

The former was identified as a **functional relationship**, while the latter was identified as **correlational**.

That distinction matters because both variables can be statistically related while carrying very different information about how the market behaves.

---

# 3. Order Flow and Short-Horizon Returns

A central question was whether order flow contains information about subsequent price movement.

The research found a measurable relationship between **order-flow imbalance and subsequent returns**.

The relationship was then examined beyond the initial discovery stage.

The offline causal arm recovered a robust **order-flow → return effect**, with a placebo test producing:

**p < 0.001**

This establishes that the relationship was not simply discarded as an artefact of the initial discovery process.

But the research did not stop at statistical significance.

The next question was whether the relationship could actually support a high-frequency trading decision.

---

# 4. Statistical Relationship ≠ Trading Edge

This became one of the most important findings of the study.

A relationship can be:

* statistically detectable,
* reproducible over some interval,
* and still economically unusable.

The discovered directional relationship was **transient** and did not provide sufficient economic value after transaction costs under the tested trading setup.

The resulting HFT strategy therefore **abstained from trading the directional edge**.

That behavior is deliberate.

The system does not convert every statistically significant relationship into a position.

The decision pipeline was:

**Trade Data**

→ **Order-Flow Construction**

→ **Streaming Relationship Discovery**

→ **Typed Market Graph**

→ **Signal Evaluation**

→ **Out-of-Sample Testing**

→ **Execution / Cost Analysis**

→ **Trading Decision**

The final stage is allowed to produce **no trade**.

That is an important distinction between relationship discovery and trading.

---

# 5. Volatility Contains Different Information

The directional result was not the only predictive structure found in the market.

A separate relationship involving order flow and **future return magnitude / volatility** proved more persistent.

The research used this structure to construct a realized-volatility forecasting model.

The resulting forecast reached approximately:

**Out-of-sample R² = 0.40**

This provides an interesting contrast.

The same market can contain information that is useful for forecasting **how much the market will move** without providing a sufficiently persistent signal for predicting **which direction it will move** after trading costs.

The typed relationship graph makes this distinction explicit rather than treating both as generic predictive associations.

---

# 6. Why the Typing Matters

The financial experiment was particularly useful for testing whether relationship discovery could identify **different forms of dependence in the same system**.

Consider two observations:

### Directional relationship

Order-flow imbalance is associated with subsequent return.

This is relevant to directional trading, but its usefulness depends heavily on persistence, latency, execution, and transaction costs.

### Volatility relationship

Trade activity is associated with the magnitude of subsequent returns.

This relationship can be useful for volatility forecasting even when the corresponding directional information is not economically exploitable.

A system that reports only “order flow correlates with returns” loses this distinction.

Scarcity instead represents the discovered relationship as a typed edge and carries that distinction into downstream analysis.

---

# 7. High-Frequency Trading as a Validation Environment

The HFT setting provides a particularly demanding environment for Scarcity.

Financial markets exhibit several properties that make relationship discovery difficult:

* observations arrive rapidly;
* relationships can decay quickly;
* market regimes change;
* many variables interact simultaneously;
* apparent relationships can disappear once execution costs are considered;
* statistical significance does not imply economic profitability.

This makes the market a useful test of the framework's central principle:

> **Recover structure, calibrate it, and refuse to invent an exploitable magnitude when the evidence does not support one.**

The HFT experiment therefore was not added simply to demonstrate that Scarcity could process financial data.

It tested whether the framework's distinction between **discovering a relationship** and **acting on a relationship** survives contact with a market where that distinction has immediate economic consequences.

---

# 8. Relationship to Scarcity

The financial-market study is part of the broader Scarcity validation programme.

The framework was originally motivated by scarce macroeconomic data, where annual observations can number only in the dozens.

Financial microstructure provides almost the opposite environment:

**many observations, extremely short horizons, rapidly changing relationships, and strong economic pressure to distinguish signal from noise.**

That contrast is useful.

In macroeconomics, the central difficulty is often insufficient observations.

In high-frequency markets, the problem is that abundant observations do not guarantee stable or economically exploitable relationships.

Scarcity is therefore being tested against two different meanings of difficult data:

> **too little information**

and

> **rapidly changing information whose useful lifetime may be extremely short.**

---

# 9. What the Experiment Shows

The study produces several distinct findings.

### 1. Market structure can be discovered without specifying the target first

The engine recovered a **29-edge typed graph** directly from the market stream without being given a predetermined target or adjustment set.

### 2. Different market relationships have different forms

The system distinguished functional volatility relationships from correlational directional relationships rather than treating them as one generic dependency.

### 3. Statistical significance does not imply economic profitability

The order-flow → return relationship was statistically supported, but the corresponding HFT strategy abstained because the edge was too transient relative to the tested transaction costs.

### 4. Predictive information can survive in magnitude even when direction does not

The realized-volatility model achieved approximately **OOS R² = 0.40**, showing useful information about future market movement magnitude.

### 5. Discovery and trading should remain separate decisions

The research pipeline deliberately allows:

**relationship discovered → relationship statistically supported → relationship economically rejected → no trade**

rather than forcing every discovered relationship into a trading strategy.

---

# 10. Limitations

The financial experiment has deliberately narrow scope.

**Single asset.**
The study uses Bitcoin rather than a multi-asset or multi-venue universe.

**Short observation period.**
The analysis covers approximately six days of market activity. It cannot establish that the discovered relationships persist across longer periods or different market regimes.

**Limited market-depth information.**
The feature set does not incorporate the full depth of a limit-order book, which restricts what can be inferred about execution and microstructure.

**Transaction-cost dependence.**
The strategy's abstention is conditional on the tested execution assumptions and costs. It does not establish that no profitable directional edge exists under other infrastructure, latency, fees, or execution conditions.

**Predictive rather than universal causal interpretation.**
The offline causal result is still bounded by observational-data assumptions. It should not be interpreted as establishing an intervention-level law of Bitcoin price formation.

**No claim of production HFT deployment.**
This is a substantial experimental quantitative research study, not a claim of operating a production market-making or HFT desk.

---

# Status

This is an **experimental quantitative research study in high-frequency market microstructure** and one of the real-data validation environments for Scarcity.

The research is sufficiently developed to evaluate:

* streaming relationship discovery,
* typed market structure,
* statistical calibration,
* predictive relationships,
* out-of-sample volatility forecasting,
* trading-strategy implications,
* and transaction-cost-aware decision making.

Its conclusions remain bounded by the asset, period, feature set, and execution assumptions used in the study.

The most useful result is not simply that an order-flow relationship was found.

It is that the research followed the relationship all the way through:

> **discover → type → validate → forecast → test economically → abstain when the edge is not worth trading.**

That distinction is central to the way I approach quantitative research.
