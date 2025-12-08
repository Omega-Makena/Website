---
title: Scarcity System Overview
description: How I design machine learning systems when data, capital, and time are constrained.
section: Scarcity
date: 2025-01-10
links:
  - title: Research Log · Origin
    url: /research-log/scarcity/2025-01-origin
    description: First decisions and uncertainties in the finance track.
  - title: Library · Federated Learning
    url: /library/learning-paradigms/federated-learning
    description: Primer on the paradigm used for data-sparse collaboration.
---

### What Scarcity is

Scarcity is a design system for building ML products when the inputs are limited: few labels, partial visibility, regulatory drag, or thin budgets. Instead of fighting constraints, each layer of the system makes them explicit and uses them to guide architecture choices.

### Architecture

1. **Signals** — Identify the smallest reliable observables and codify data availability, privacy, and drift assumptions.  
2. **Learning core** — Pick the paradigm that respects those constraints (federated/online/meta-learning). Favor modularity over monoliths.  
3. **Experiment rail** — A repeatable loop for testing hypotheses with cheap counterfactuals and simulated scarcity.  
4. **Governance** — Guardrails for compliance, ethics, and operational risk baked into the pipeline.  
5. **Feedback** — Close the loop: deploy, observe failure, tighten the constraint model.

### Components

- **Constraint ledger** — A living document listing data/compute/legal limits per project.  
- **Pattern library** — Reusable templates for onboarding new data sources, simulating gaps, and cold-start strategies.  
- **Resilience checks** — Automated checks that fail fast when assumptions break (missing clients, skew, latency).  
- **Narrative layer** — How insights are communicated to stakeholders without leaking sensitive detail.

### Implementations (current focus)

- **Finance** — Retail brokerage data with uneven participation. Goal: stable inference despite intermittent contributors.  
- **Policy** — Resource-allocation simulations without collecting individual-level data.  
- **Experiments** — Synthetic scarcity drills to stress-test deployment choices.

Each implementation documents:

- The problem being constrained  
- Which Scarcity component is exercised  
- What worked, what broke, and what to change next  
- References back to the Research Log and Library entries

### Limitations

Scarcity does not remove the need for good data; it makes the lack of it a first-class citizen. It slows down upfront, accelerates later by reducing dead ends, and depends on honest logging of failures.

### FAQ

- **Is this only for finance?** No. Finance is the proving ground; the same constraint-first approach extends to macro and policy work.  
- **Where are the results?** See the Research Log for in-progress thinking and the Library for distilled teaching notes.  
- **How do you engage?** Work With Me is reserved for collaborations that align with the constraint model—mentorship, consulting, or joint experiments.
