---
title: Engine Layer (MPIE)
description: Multi-Path Inference Engine documentation.
date: 2025-12-23
---

# Engine Layer (MPIE)

The **Multi-Path Inference Engine (MPIE)** is the core component responsible for online learning and adaptive inference. It operates through:
- **Bandit-based path exploration**: Discovers optimal computation paths dynamically.
- **Resource-aware execution**: Adapts to available CPU/RAM in real-time.

### MPIEOrchestrator

The main orchestrator coordinates the online inference pipeline. It ensures that the system never blocks and only maintains bounded state.

#### Processing Pipeline

1.  **Proposal Phase**
    The Controller analyzes current context and proposes candidate paths/pipelines using **UCB** or **Thompson Sampling**.

2.  **Evaluation Phase**
    The Evaluator runs candidates on the data window, scores performance (Accuracy, Latency), and computes confidence intervals.

3.  **Selection Phase**
    The system selects the best path based on Reward (**R**) and Cost (**C**), enforcing diversity penalties to avoid local optima.

4.  **Update Phase**
    Results are fed back into the Bandit model to update arm statistics (**μ**, **σ**).

---

### BanditRouter (Controller)

Implements the decision-making policy. It balances exploration (trying new things) and exploitation (sticking to what works).

#### The Algorithm

The controller uses **Upper Confidence Bound (UCB)** with diversity bonuses. It optimizes for:

`UCB(arm) = μ(arm) + τ · √(2ln(T) / n(arm)) + γ · D(arm) - η · C(arm)`

**Variables**:
*   **μ(arm)**: Mean reward observed so far.
*   **τ**: Temperature parameter (Controls exploration).
*   **γ**: Diversity weight.
*   **η**: Cost weight (Penalizes slow paths).
*   **D(arm)**: Diversity score.
*   **C(arm)**: Cost estimate.

#### Key Features

-   **Drift Detection**: Detects if data distribution changes using Page-Hinkley tests.
-   **Resource Awareness**: Adjusts exploration budget based on DRG signals.

---

### Evaluator

Scores the candidate paths produced by the Controller.

#### Evaluation Metrics

-   **Gain**: Improvement in **R²** or reduction in NLL.
-   **Confidence Interval**: Verifies result significance.
-   **Stability**: How consistent the result is.
-   **Cost**: Execution time.
