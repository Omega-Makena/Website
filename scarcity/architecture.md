---
title: Architecture
description: The layered architecture of SCARCITY.
date: 2025-12-23
---

# Architecture

The **SCARCITY** core library follows a layered architecture with clear separation of concerns.

### System Diagram

```mermaid
graph TD
    App[Application Layer] --> FMI[FMI Service]
    App --> Sim[Simulation]
    App --> Meta[Meta-Learning]
    
    subgraph "Core Runtime"
        FMI --> Fed[Federation Layer]
        Fed --> Eng[Engine Layer (MPIE)]
        Eng --> Stream[Stream Processing]
        
        Note[Runtime Bus & Telemetry] -.-> Eng
        Note -.-> Fed
        
        DRG[Resource Governor] -.-> Eng
        DRG -.-> FMI
    end
    
    Stream --> Ops[Core Operators]
```

---

### Component Interaction Flow

1.  **Data Ingestion**
    Stream sources feed data windows to the engine via the `StreamSource`.

2.  **Path Exploration**
    **MPIE** proposes and evaluates candidate paths using bandit algorithms (UCB).

3.  **Federation**
    Successful paths are packaged into `PathPacks` and shared across domains via the **Federation Coordinator**.

4.  **Meta-Learning**
    Cross-domain patterns are learned and applied to the global model prior.

5.  **Resource Management**
    **DRG** monitors system resources (CPU, RAM) and throttles the Engine or FMI layer adaptation.

6.  **Simulation**
    Agent-based models provide what-if analysis capabilities to predict system behavior.
