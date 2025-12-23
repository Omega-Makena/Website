---
title: Runtime System
description: Event bus and asynchronous architecture.
date: 2025-12-23
---

# Runtime System

The runtime relies on a central **Event Bus** to decouple components.
This allows the Engine, DRG, and Federation layers to communicate without blocking each other.

---

### EventBus Architecture

An asynchronous `pub/sub` broker.

*   **Non-blocking**: Uses `asyncio` tasks for dispatch.
*   **Topic-based**: Components subscribe to specific channels.
*   **Resilient**: Automatic error isolation (one crasher doesn't kill the bus).

---

### Key Topics

| Topic | Description | Payload |
| :--- | :--- | :--- |
| **`data_window`** | New batch of data arrival | Data Tensor |
| **`resource_profile`** | Hardware health status | Dictionary (CPU, RAM) |
| **`engine.insight`** | Discovered causal path | Path Packet |
| **`federation.gossip`** | P2P message from peer | Federation Packet |
| **`meta_policy`** | New learning strategy | Policy Packet |
| **`simulation.tick`** | Sim world update | State Vector |
