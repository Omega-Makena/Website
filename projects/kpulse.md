---
title: KPulse Intelligence
date: 2026-04-05
description: Social sensing system for monitoring public sentiment and emerging threats.
---

# Pulse Intelligence Architecture

Pulse Intelligence turns multi-source social, economic, and institutional signals into decision-support intelligence for public-sector and institutional teams.

## 1. End-to-End Pulse Computation Graph

```mermaid
flowchart TD
    A[Platform Scrapers\nX · Telegram · Reddit · Facebook · News] --> B[Ingestion Orchestrator\nDeduplicate · Timestamp normalization · Geo hints]
    B --> C[Content Canonicalizer\nLanguage normalize · Entity extraction · Topic tagging]
    C --> D[LLM + Rule Hybrid Classifier\nThreat tier · Intent · Confidence]
    D --> E[Signal Scoring Layer\n15 detector families]
    E --> F[PulseState Builder\nScarcityVector · ActorStress · BondStrength]
    F --> G[Index Engine\n8 composite indices]
    G --> H[ThreatIndexReport\nOverall level + rationale]
    H --> I[Shock Mapping\nGDP · Inflation · Trade · FX · Confidence]
    I --> J[SFC / Research SFC Simulations]
    H --> K[Executive Dashboard tiles]
    H --> L[Admin escalation queues]
    H --> M[Archive + trend storage]
```

## 2. Core Calculation Stages

### Stage A — Ingestion Quality Control
Each raw event is assigned a quality weight based on source reliability history, duplicate density, parsing completeness, and geo confidence. 

### Stage B — Detector Scoring (15 Families)
The detector layer transforms each normalized post into detector intensities:

1. **Distress family**: food/water/health stress markers.
2. **Anger and escalation family**: aggression, mobilization language, urgency verbs.
3. **Institutional legitimacy family**: governance rejection and trust erosion signals.
4. **Identity polarization family**: group-framing and exclusion language.
5. **Information warfare family**: rumor, contradiction, synthetic amplification patterns.

### Stage C — Temporal Smoothing and Burst Control
To avoid overreaction to one-off spikes, each detector stream is smoothed with exponentially weighted moving averages and burst clamps.

### Stage D — PulseState Assembly
PulseState is assembled from grouped detector vectors:

- **ScarcityVector** from distress, access, service-breakdown indicators.
- **ActorStress** from institutional conflict, mobilization, and pressure cues.
- **BondStrength** from trust and cohesion evidence (inverted for risk).

## 3. Threat Indices and Scoring

The platform computes 8 multiple domain indices and then synthesizes an overall threat level.

```mermaid
flowchart LR
    S[Processed Signal Streams] --> I1[Social Cohesion Index]
    S --> I2[Institutional Pressure Index]
    S --> I3[Mobilization Index]
    S --> I4[Information Integrity Index]
    S --> I5[Economic Stress Index]
    S --> I6[Security Friction Index]
    I1 & I2 & I3 & I4 & I5 & I6 --> O[Overall Threat Level]
```

## 4. How Pulse Feeds the Simulation Layer

Pulse outputs are transformed into scenario-ready shock vectors for the downstream KShield simulation layers.

```mermaid
flowchart TD
    A[ThreatIndexReport] --> B[Shock Mapper]
    B --> C1[Demand confidence shock]
    B --> C2[Supply disruption shock]
    B --> C3[Inflation pressure shock]
    B --> C4[Trade/external balance shock]
    B --> C5[Institutional friction shock]
    C1 & C2 & C3 & C4 & C5 --> D[SFCConfig shock_vectors]
    D --> E[SFCEconomy / ResearchSFCEconomy projections]
    E --> F[Policy recommendation views]
```
