---
title: "SCARCITY Components"
date: "2025-01-01"
description: "Deep dive into the algorithms and math."
---

# Core Algorithms & Components

SCARCITY implements custom algorithms for causal discovery, resource management, and privacy-preserving federation.

## 1. Multi-Path Inference Engine (MPIE)

The MPIE uses a multi-stage pipeline to discover causal structures from streaming data: `Encoder → Controller → Evaluator`.

### Controller Algorithm
The controller generates and scores candidate causal paths based on strength, stability, and novelty.

```python
def compute_path_score(path: Path, encoded: EncodedFeatures) -> float:
    """
    Score = α·strength + β·stability + γ·novelty
    """
    strength = compute_strength(path, encoded)
    stability = compute_stability(path, encoded)
    novelty = compute_novelty(path, history)
    
    return 0.4*strength + 0.4*stability + 0.2*novelty
```

### Evaluator Algorithm

We use **Bootstrap Resampling** to validate candidate paths, ensuring statistical significance before adding them to the hypergraph.

-----

## 2. Dynamic Resource Governor (DRG)

The DRG prevents system overload by using a **PID Controller** to regulate processing rates based on CPU and Memory feedback.

### Control Policy

```python
def compute_action(self, profile: ResourceProfile) -> Action:
    # Compute error for each resource
    cpu_error = self.cpu_threshold - profile.cpu_percent
    
    # Compute PID output
    cpu_output = (
        self.Kp * cpu_error +
        self.Ki * self.cpu_integral +
        self.Kd * self.cpu_derivative
    )
    
    if cpu_output < -10: return Action.THROTTLE_HEAVY
    elif cpu_output > 10: return Action.INCREASE_RATE
    else: return Action.MAINTAIN
```

-----

## 3. Federation Layer

SCARCITY supports decentralized learning using **Federated Averaging (FedAvg)** and **Differential Privacy**.

### Differential Privacy

To protect sensitive data, Gaussian noise is added to model weights before sharing:

$$ \sigma = \frac{\sqrt{2 \ln(1.25/\delta)} \cdot \Delta f}{\epsilon} $$

```python
def add_privacy_noise(weights, epsilon=1.0, delta=1e-5):
    sigma = np.sqrt(2 * np.log(1.25 / delta)) * sensitivity / epsilon
    noise = np.random.normal(0, sigma, weights.shape)
    return weights + noise
```
