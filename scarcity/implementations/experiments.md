---
title: Experiments
description: Synthetic drills to break Scarcity assumptions before production.
section: Scarcity
date: 2025-01-11
links:
  - title: Research Log
    url: /research-log
    description: Live notes from these drills.
---

**Problem**  
Find failure modes fast—simulate scarcity rather than wait for production outages.

**Scarcity components exercised**  
Simulation harness, resilience checks, aggregation patterns under stress.

**What worked**  
Client dropout simulations revealed stale-update risks early; bandwidth throttling forced payload compression plans.

**What failed**  
Adversarial update tests are incomplete; need better poisoning detection before rollout.

**Next steps**  
Add poisoning scenarios, automate staleness decay, and link outcomes directly into the constraint ledger.
