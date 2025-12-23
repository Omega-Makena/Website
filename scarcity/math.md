---
title: Mathematical Foundations
description: Algorithms and theoretical basis of SCARCITY.
date: 2025-12-23
---

# Mathematical Foundations

### 1. Bandit Algorithms (UCB)

We use **Upper Confidence Bound** to balance exploration and exploitation.

`UCB_i(t) = μ_i(t) + c · √(ln(t) / n_i(t)) + γ · D_i(t) - η · C_i(t)`

*   **μ_i(t)**: Empirical Mean Reward.
*   **c**: Confidence parameter (Exploration).
*   **D_i(t)**: Diversity Score.
*   **C_i(t)**: Computational Cost.

---

### 2. Diversity Scoring

To ensure the model learns diverse features, we penalize redundancy using Inverse Coverage.

`D_i = 1 / √(1 + c_i)`

*   **c_i**: Coverage count (How many times has variable *i* been used?).

---

### 3. Reward Shaping

The reward signal *r* is not just accuracy; it is a composite of multiple objectives:

`r = α · gain + β · diversity - γ · latency - δ · cost`

---

### 4. Meta-Learning (Reptile)

We use the **Online Reptile** update rule for fast adaptation:

`θ_t+1 = θ_t + α_t · (φ_i - θ_t)`

*   **Adaptive Learning Rate**:
    The rate *α* decays over time but boosts when high rewards are found.

    `α_t = α_0 · e^(-λt) · (1 + β · reward_t)`

---

### 5. Sketch Operators

**Polynomial Sketch**
Approximates polynomial expansion using CountSketch (Memory efficient).

`poly_sketch(x, d) ≈ Σ (|S| ≤ d) c_S · Π_(i ∈ S) x_i`

**Tensor Sketch**
Approximates the Kronecker product `x₁ ⊗ x₂` using hash-based convolution.
