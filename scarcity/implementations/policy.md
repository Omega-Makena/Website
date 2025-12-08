---
title: Policy Implementation
description: Resource allocation experiments without collecting personal data.
section: Scarcity
date: 2025-01-11
links:
  - title: Components
    url: /scarcity/components
    description: Templates and guardrails used here.
---

**Problem**  
Design allocation strategies for public resources while avoiding individual-level data collection.

**Scarcity components exercised**  
Constraint ledger (privacy mandates), simulation harness (policy scenarios without PII), governance (auditability and rollback), narrative layer (communicating fairness without revealing microdata).

**What worked**  
Synthetic populations enabled quick iteration; clear governance steps built trust with stakeholders.

**What failed**  
Some fairness metrics were unstable on synthetic data; sensitivity to assumption changes was under-documented.

**Next steps**  
Harden fairness evaluation, add stress tests for assumption shifts, log decision rationale per run.
