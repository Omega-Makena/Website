---
title: Scarcity Components
description: The reusable pieces that make constraint-driven ML shippable.
section: Scarcity
date: 2025-01-11
links:
  - title: Architecture
    url: /scarcity/architecture
    description: How the pieces fit together.
  - title: Implementations
    url: /scarcity/implementations
    description: Where components are exercised.
---

- **Constraint ledger** — Captures data access, privacy, compute, and regulatory limits per project.  
- **Onboarding template** — Standard checklist for new data sources or partners; defines schemas, consent, and failure modes.  
- **Simulation harness** — Tools to mimic scarcity: missing clients, skewed updates, noisy labels, throttled bandwidth.  
- **Aggregation patterns** — FedAvg + reliability weighting, secure aggregation, DP noise hooks.  
- **Resilience checks** — Health probes for participation rate, gradient divergence, stale updates, and latency budgets.  
- **Narrative layer** — How results are communicated without leaking sensitive detail; bridges to Library and Writing.
