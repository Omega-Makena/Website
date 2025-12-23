---
title: Simulation Engine
description: Agent-based modeling and visualization.
date: 2025-12-23
---

# Simulation Engine

The **Simulation Engine** allows you to create Digital Twins of your deployment environment. It runs agent-based models to predict how the system will behave under stress.

---

### Core Concepts

#### Agent Registry
The central directory of all entities in the simulation.
-   **Agents**: Nodes in the graph (Servers, Models, Data Sources).
-   **Edges**: Connections between them (Network links, dependencies).

#### Dynamics Engine
The "Physics Engine" of the simulation.
-   Calculates how agents affect each other over time.
-   Applies "Shocks" (e.g., Latency spikes, Node failures) to test resilience.

---

### Visualization

The engine renders the state of the hypergraph in 3D using force-directed layouts.

*   **Nodes**: Represent physical agents or logical domains.
*   **Edges**: Represent data flow or causal influence.
*   **Colors**: Indicate stability (Green=Stable, Red=Volatile).
*   **Position**: Determined by the strength of causal relationships.
