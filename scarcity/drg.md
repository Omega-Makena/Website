---
title: Resource Governor (DRG)
description: Dynamic resource management and adaptation.
date: 2025-12-23
---

# Dynamic Resource Governor (DRG)

The **DRG** acts as the system's "autonomic nervous system."
It constantly monitors hardware health and acts to keep the system stable.

---

### What it Monitors (Sensors)

The sensors sample metrics at 10Hz:

*   **CPU Usage**
    Total processor utilization.
*   **Memory Pressure**
    Available RAM vs Total RAM.
*   **VRAM (GPU)**
    Video memory utilization.
*   **I/O Throughput**
    Disk read/write speeds.

---

### How it Reacts (Policies)

The DRG uses a **Rule-Based Policy System** to trigger interventions when thresholds are crossed.

#### Default Constraints

1.  **Memory Pressure High (>85%)**
    *   **Action**: Reduce Batch Size.
    *   **Action**: Enable Compression.

2.  **CPU Overload (>95%)**
    *   **Action**: Lower Sampling Rate.
    *   **Action**: Suspend Federation updates.

3.  **Network Congestion**
    *   **Action**: Compress Packets (gzip/lz4).

---

### Actuators

When a policy triggers, the Actuators modify the runtime configuration on the fly, seamlessly downgrading fidelity to preserve uptime.
