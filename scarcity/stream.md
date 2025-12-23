---
title: Stream Processing
description: Adaptive data ingestion and rate control.
date: 2025-12-23
---

# Stream Processing

The Stream layer handles the firehose of incoming data. It ensures the Engine is never overwhelmed by using **Adaptive Backpressure**.

---

### Data Sources

The ingestor is capable of reading form multiple backends:
*   **CSV Files**: Chunked reading via Pandas.
*   **Async Iterators**: Python generators.
*   **Streaming APIs**: WebSockets / Kafka.

---

### Adaptive Rate Control (PI Controller)

We use a **Proportional-Integral (PI) Controller** to adjust the ingestion speed dynamically.

**Goal**: Maintain a constant latency of `100ms` per window.

#### Controls
1.  **Error Calculation**:
    Distance between Target Latency and Actual Latency.
2.  **Integral**:
    Accumulates error over time to correct systematic drift (e.g., a slowly clogging process).
3.  **Adjustment**:
    `Δt_next = Δt_base + Kp · error + Ki · integral`

If the engine is slow, the PI Controller **slows down** the stream automatically.
