---
title: Federated Model Interface (FMI)
description: High-level orchestration for federated learning workflows.
date: 2025-12-23
---

# Federated Model Interface (FMI)

The **FMI** is the high-level API that ties all the components together for Federated Learning. It serves as the gateway for all external model communication.

---

### The Pipeline

When a packet arrives from a peer, it goes through 4 stages:

1.  **Validation**
    *   Checks cryptographic signature.
    *   Verifies schema version.
    *   Checks sender Trust Score.

2.  **Routing**
    *   Assigns the packet to the correct Peer Cohort.
    *   Filters based on domain relevance.

3.  **Aggregation**
    *   Combines the parameters with local knowledge.
    *   Uses **FedAvg** or **Adaptive Weighted Averaging**.

4.  **Emission**
    *   Notifies subscribers (Engine/Meta-Learner) of the new state.

---

### DRG Integration

The FMI automatically degrades performance (gracefully) when resources are tight:

*   **Low Bandwidth?** -> Switch to `Q8` (8-bit) quantization.
*   **High Latency?** -> Suspend Proof-of-Path (POP) verification.
*   **High VRAM?** -> Defer aggregation until memory clears.
*   **Resources OK?** -> Restore full precision (`FP32`).
