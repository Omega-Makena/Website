---
title: Overview
description: High-level introduction to the Scarcity framework — an online relationship-discovery engine for data that drifts under scarcity.
date: 2025-12-23
---

# Overview

**Scarcity** is a general online **relationship-discovery engine** — an automated statistician for multivariate data streams. You feed it one row at a time; it learns *which relationships currently hold* between the variables and hands that structure downstream as a continuously-updated knowledge graph. It is not specific to any one field; macroeconomics was simply the first domain it was applied to.

Around that engine sits a full runtime for learning under scarcity — few samples, high noise, constant drift: federation so nodes can learn together without sharing raw data, meta-learning so magnitudes can be borrowed across systems, and dynamic resource governance so the whole thing runs within a device's compute budget. "Scarcity" names both regimes — scarce *data* and scarce *compute* — and the framework is built to work under each.

Scarcity is also the framework from which [**Organizational Identity Theory**](/projects/organizational-identity-theory/) emerged: the finding that a system's *form* — the structure this engine recovers — survives scarcity while its *magnitudes* do not.

---

### Key Features

*   **Relationship-Discovery Engine**
    A living population of 15 typed relational hypotheses (causal, correlational, functional, temporal, mediating, and more). Each must survive the data stream or die; survivors are calibrated against permutation nulls with false-discovery control, so noise is not reported as structure.

*   **Multi-Path Inference Engine (MPIE)**
    Online bandit-based path exploration with UCB/Thompson sampling. Automatically finds the best calculation path.

*   **Federated Learning**
    Decentralized model aggregation with differential privacy preservation. Learn from data without seeing it.

*   **Meta-Learning**
    Cross-domain adaptation using online **Reptile** optimization. Transfer knowledge between different environments.

*   **Dynamic Resource Governance (DRG)**
    Adaptive resource allocation based on system telemetry. If CPU usage spikes, the model shrinks.

*   **Real-time Simulation**
    Agent-based modeling with 3D visualization to stress-test policies.

*   **Stream Processing**
    Continuous data ingestion with backpressure control (PI-Controller).

*   **Event-Driven Architecture**
    Asynchronous `pub/sub` communication fabric for non-blocking operations.

---

### Version Information

*   **Version**: `1.0.0`
*   **Author**: Omega Makena
*   **License**: Apache-2.0 (See LICENSE file)
