---
title: API Reference
description: Quick reference for key exports and usage.
date: 2025-12-23
---

# API Reference

The Scarcity API is designed to be modular. You interact with the high-level Orchestrators, while the Runtime handles the complexity.

---

### Engine Layer

**`MPIEOrchestrator`**
The main entry point. Coordinates the entire inference lifecycle.

**`BanditRouter`**
The decision brain. Controls path proposal and exploration budgets.

---

### Federation Layer

**`FederationCoordinator`**
Manages the mesh network, peer discovery, and trust scoring.

**`PathPack`**
The standard data unit for knowledge transfer. Contains the causal graph and weights.

---

### Simulation Engine

**`SimulationEngine`**
Runs the agent-based model. Controls the clock and event loop.

**`What-If Manager`**
Triggers counterfactual scenario analyses (e.g., "What if Node A goes offline?").

---

### Dynamic Resource Governor

**`DynamicResourceGovernor`**
The monitor. Starts the sensing loop and executes policies.

---

### Runtime

**`EventBus`**
The central nervous system. Provides global `pub/sub` access for all components.
