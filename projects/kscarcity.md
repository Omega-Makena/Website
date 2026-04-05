---
title: KScarcity Architecture
date: 2026-04-05
description: Unified national-level platform for real-time overview and simulation.
---

# KScarcity Unified Platform

KScarcity is a unified national-level platform that gives the government a real-time overview of policies, sectoral activities, and institutional operations. 

It analyzes data across sectoral, institutional, and national layers, trains machine learning models in real time, explains the five W's and one H, simulates risks and policy responses, and allows collaboration for planning and preparing for future shocks. Essentially, it integrates monitoring, analysis, and simulation tailored to a country's needs.

---

## 1. Full System Data Flow

```mermaid
flowchart LR
    subgraph RAW["Raw Data Sources"]
        R1[Twitter / X]
        R2[Facebook / Telegram]
        R3[News Feeds]
        R4[World Bank / KNBS]
        R5[Institution CSVs]
    end

    subgraph PULSE["Pulse Engine"]
        P1[Scrapers]
        P2[NLP Pipeline]
        P3[15 Signal Detectors]
        P4[PulseState\nScarcityVector · ActorStress · BondStrength]
        P5[8 Threat Indices\nPI · LEI · MRS · ECI · IWI · SFI · ECR · ETM]
        P6[ShockGenerator\nGDP · Inflation · Trade · FX · Confidence]
    end

    subgraph SCARCITY["Scarcity Engine"]
        S1[Online Discovery Engine\n15 Hypotheses]
        S2[LearnedSFCEconomy]
        S3[Meta-Learning Agent\nReptile Optimizer]
        S4[DRG — Dynamic Resource Governor]
        S5[RRCF Anomaly Detector]
        S6[Bayes VARX Forecaster]
    end

    subgraph SIM["Simulation Layer"]
        M1[SFCEconomy\nBase Macro]
        M2[ResearchSFCEconomy\nHeterogeneous · Open · Financial · IO]
        M3[SectorSimulator\n6 Sectors × 20+ Indicators]
        M4[Shock Templates\n380+]
        M5[5–10 Year Projections]
    end

    subgraph FED["Aegis Federation"]
        F1[Institution Nodes]
        F2[Gossip Consensus]
        F3[Global Meta-Aggregation]
    end

    subgraph UI["Dashboards"]
        U1[K-SHIELD]
        U2[Institution Portal]
        U3[SENTINEL]
    end

    R1 & R2 & R3 --> P1
    P1 --> P2 --> P3 --> P4 --> P5 --> P6
    P6 --> M3
    P5 --> U3

    R4 & R5 --> S1
    S1 --> S2
    S2 --> M1 & M2
    S3 --> S2
    S4 --> S2
    S5 --> S6

    M2 --> M3 --> M4 --> M5
    M5 --> U1 & U2

    F1 --> F2 --> F3 --> S3
    R5 --> F1
```

---

## 2. Scarcity Engine — Online Learning Architecture

```mermaid
flowchart TD
    subgraph Preprocessing["Pre-Processing"]
        A1[Raw Stream] --> A2[Online Winsorization\n5th–95th percentile clipping]
        A2 --> A3[Online MAD\nMedian Absolute Deviation]
        A3 --> A4[Huber Loss\nGradient Clipping]
    end

    subgraph Encoding["Sketching & Encoding"]
        A4 --> B1[CountSketch + FFT\nPolynomial Approximation]
        B1 --> B2[Tensor Sketch\nKronecker Product Compression]
        B2 --> B3[Top-K Sparse Attention\nFP16 Transformer-style]
        B3 --> B4[Lag Positional Encodings]
    end

    subgraph Hypotheses["15 Competing Hypotheses (Online)"]
        B4 --> C1[Causal — Granger Augmented Ridge]
        B4 --> C2[Correlational — Welford Pearson]
        B4 --> C3[Temporal — Recursive Least Squares VAR-p]
        B4 --> C4[Functional — Online Polynomial RLS]
        B4 --> C5[Equilibrium — Kalman Mean Reversion]
        B4 --> C6[Compositional — Sum Constraints MAE]
        B4 --> C7[Competitive — CV Zero-Sum Detection]
        B4 --> C8[Synergistic — Interaction Term Regression]
        B4 --> C9[Probabilistic — Cohen's d Distribution Shift]
        B4 --> C10[Structural — ICC Hierarchical]
        B4 --> C11[Mediating — Baron-Kenny]
        B4 --> C12[Moderating — Conditional Effects]
        B4 --> C13[Graph — Network Density]
        B4 --> C14[Similarity — Online K-Means]
        B4 --> C15[Logical — Boolean Gate Rules]
    end

    subgraph Arbitration["Arbitration & Validation"]
        C1 & C2 & C3 & C4 & C5 & C6 & C7 & C8 & C9 & C10 & C11 & C12 & C13 & C14 & C15 --> D1[HypothesisArbiter\nParsimony + Conflict Resolution]
        D1 --> D2[Page-Hinkley\nConcept Drift Detection]
        D2 --> D3[Bootstrap CI\nConfidence Intervals]
        D3 --> D4[Spearman Concordance\nSign-Agreement Validation]
    end

    subgraph Output["Knowledge Output"]
        D4 --> E1[Causal Knowledge Graph\nEdge strengths + confidence]
        D4 --> E2[RRCF Anomaly Detector]
        D4 --> E3[Bayes VARX Forecaster]
        E1 --> E4[LearnedSFCEconomy]
        E2 & E3 --> E5[DRG — Assurance Levels\nHIGH · MEDIUM · LOW · FALLBACK]
    end
```

---

## 3. Institution Dashboard — Navigation Structure

```mermaid
flowchart TD
    L[Landing Page\n5 Ws — Who · What · When · Where · Why] --> A

    A[Institution Portal Login\nSector + Invite Code + Password] --> B{Role}

    B --> C[Executive Dashboard]
    B --> D[Admin Governance Console]
    B --> E[Developer Dashboard]
    B --> F[Local / Spoke Dashboard]

    C --> C1[National Briefing\nThreat Intelligence · Social Signals]
    C --> C2[Sector Reports\n7 Sectors — status grid always visible]
    C --> C3[Command & Control\nActive Operations]
    C --> C4[Policy Simulator\nScenario design + projections]
    C --> C5[Collaboration Room\nCross-institution messaging]
    C --> C6[Archive\nHistorical reports]
    C --> C7[Analytics Pillars\nSO WHAT · COMPARED TO WHAT · WHERE EXACTLY\nWHAT SHOULD I DO · DID IT WORK]

    D --> D1[Pending Approvals\nInstitution registration review]
    D --> D2[Audit Logs\nFull approval audit trail]
    D --> D3[Topology Injection\nLevel 1/2 agency hierarchy]
    D --> D4[FL Dashboard\nFederated learning round management]
    D --> D5[Admin Data Schemas\nStructured project tracking]

    E --> E1[Model Quality\nDRG assurance levels]
    E --> E2[Causal Adapter\nDiscovery engine inspection]
    E --> E3[Technical Metrics\nLatency · throughput · hypothesis counts]

    F --> F1[County Analytics\nLocalized indicators]
    F --> F2[Cost of Delay\nKES billions — Do Nothing · Act Early · Price of Late]
    F --> F3[Data Upload\nCSV → FL training trigger]
    F --> F4[Report Export\nPDF · ZIP · CSV]
```

---

## 4. DRG Assurance Levels

```mermaid
flowchart TD
    A[Projection Request] --> B{Discovery Confidence}

    B -->|≥ 0.85 + recent data| C[HIGH\nReliable for policy decisions]
    B -->|0.65–0.85| D[MEDIUM\nDirectionally correct\nQuantitative uncertainty]
    B -->|< 0.65 or stale| E[LOW\nIndicative only\nManual review recommended]
    B -->|Discovery failed| F[FALLBACK\nHardcoded SFC baselines]

    C --> G[LearnedSFCEconomy\nFull discovered relationships]
    D --> H[Blended: Learned + Hardcoded\nWeighted by confidence]
    E --> I[LearnedSFCEconomy\nwith wide confidence bands]
    F --> J[BaselineSFCEconomy\nStatic Kenya 2022 calibration]

    style C fill:#1a6b3c,color:#fff
    style D fill:#b8860b,color:#fff
    style E fill:#b5290e,color:#fff
    style F fill:#555,color:#fff
```

---

## 5. Component Interaction Map (Low-Level)

```
scarcity/engine/
┌──────────────────────────────────────────────────────────────────────┐
│  EventBus (runtime/bus.py)  — async pub/sub backbone                 │
│   "data_window"                ← new data row arrives                │
│   "scarcity.anomaly_detected"  → RRCF result                         │
│   "scarcity.forecasted_trends" → Bayes VARX result                   │
│   "scarcity.drg_extension_profile" → DRG risk profile                │
│                                                                      │
│  OnlineAnomalyDetector  (RRCF — streaming, no training phase)        │
│   Output: {anomaly_score: float, is_anomaly: bool, context: dict}    │
│                                                                      │
│  PredictiveForecaster  (GARCH-VARX — multi-variate + exogenous)      │
│   Output: {forecasts: List[float], variances, horizon}               │
│                                                                      │
│  OnlineDiscoveryEngine (engine_v2.py)                                 │
│   HypothesisPool → AdaptiveGrouper → HypothesisArbiter → MetaCtrl   │
│   .process_row(row) → update all hypotheses → arbitrate → promote    │
│   .get_knowledge_graph() → top-K confirmed relationships (JSON)      │
└──────────────────────────────────────────────────────────────────────┘

scarcity/simulation/
┌──────────────────────────────────────────────────────────────────────┐
│  SFCEconomy                                                          │
│   .step() → Consumption · Investment · Tax · Gov Spend · Net Exports │
│   .run(steps) → List[frame]                                          │
│   .apply_shock(type, magnitude)                                       │
│                                                                      │
│  ResearchSFCEconomy (wraps SFCEconomy)                               │
│   + HeterogeneousHouseholdEconomy (Q1–Q5 income quintiles)           │
│   + OpenEconomyModule (REER, reserves, trade balance)                │
│   + FinancialAcceleratorModule (credit cycles, LTV, leverage)        │
│   + IOStructureModule (agriculture, manufacturing, services, finance)│
│   + BayesianBeliefUpdater (shock probability distributions)          │
│   .stress_test(shocks) → shocked scenario outcomes                   │
│   .twin_deficit_analysis() → fiscal + current account positions      │
│   .external_vulnerability_index() → 0–1 reserve adequacy            │
│   .financial_stability_index() → 0–1 leverage + credit health       │
│                                                                      │
│  WhatIfManager                                                        │
│   .run_bootstrap(base_cfg, n=8, jitter_pct=8%)                       │
│   → (mean−std, mean+std) confidence interval tuple per dimension     │
└──────────────────────────────────────────────────────────────────────┘

kshiked/core/
┌──────────────────────────────────────────────────────────────────────┐
│  ScarcityBridge                                                       │
│   .train(data_path) → 306+ causal hypotheses from World Bank data    │
│   .create_learned_economy() → SFC with discovered relationships       │
│   .get_top_relationships(k) → ranked causal chains                   │
│   .get_confidence_map() → per-variable confidence scores (0–1)       │
│   .validate() → historical accuracy score + replay validation        │
│                                                                      │
│  EconomicGovernor                                                     │
│   Enforces resource stability constraints                            │
│   Transmits monetary/fiscal policy to SFC engine                     │
│                                                                      │
│  Shocks (Phase 4–5 Stochastic)                                        │
│   ImpulseShock      → exponential decay impulse                      │
│   OUProcessShock    → Ornstein-Uhlenbeck mean reversion              │
│   BrownianShock     → Geometric Brownian Motion                      │
│   MarkovSwitchingShock → Hamilton regime-switching                   │
│   JumpDiffusionShock → Poisson jump process                          │
│   StudentTShock     → fat-tailed shocks                              │
└──────────────────────────────────────────────────────────────────────┘

kshiked/federation/  (Aegis Protocol)
┌──────────────────────────────────────────────────────────────────────┐
│  AegisNode (extends FederationClientAgent)                           │
│   Security lattice: UNCLASSIFIED / RESTRICTED / SECRET / TOP_SECRET  │
│   Trust scoring per incoming packet                                   │
│   Graph merging from external nodes                                   │
│   CryptoSigner (Ed25519 signatures)                                   │
│                                                                      │
│  Cryptographic Secure Aggregation                                     │
│   Ed25519 long-term identity + X25519 ephemeral keys                 │
│   HKDF-SHA256 pairwise masking → summation cancellation              │
│   Q8 quantization before broadcast                                    │
│                                                                      │
│  Byzantine Defense Stack                                              │
│   1. Krum — reject outlier models by pairwise Euclidean distance      │
│   2. Multi-Krum — select k safest models                              │
│   3. Bulyan — Krum survivors → Trimmed-Mean (most hardened)          │
│   4. Coordinate-wise Trimmed Mean (top 10% + bottom 10% discarded)   │
└──────────────────────────────────────────────────────────────────────┘
```
