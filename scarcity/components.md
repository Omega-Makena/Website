---
title: Core Components
description: Module structure and key exports.
date: 2025-12-23
---

# Core Components

The framework is organized into specific modules, each handling a distinct part of the scarce-resource learning pipeline.

---

### Module Breakdown

The package layout follows a domain-driven design:

*   **`engine/`**: **Multi-Path Inference Engine**.
    Contains the Bandit algorithms and path orchestrators.
*   **`federation/`**: **Decentralized Learning**.
    Manage peer discovery, trust scoring, and packet exchange.
*   **`meta/`**: **Meta-Learning**.
    Algorithms for cross-domain knowledge transfer (Reptile).
*   **`simulation/`**: **3D Simulation**.
    Tools for 'What-If' analysis and agent-based modeling.
*   **`governor/`**: **DRG**.
    The "nervous system" that monitors CPU/RAM and throttles operations.
*   **`stream/`**: **Stream Processing**.
    Adaptive data ingestion with backpressure.

---

### Key Interfaces

The primary interface classes you will interact with:

*   **`MPIEOrchestrator`**: The main brain for online inference.
*   **`FederationCoordinator`**: The networking interface.
*   **`DynamicResourceGovernor`**: The resource guard.
