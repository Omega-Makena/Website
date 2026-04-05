---
title: "The Three Contracts of Risk Governance"
description: Defining the exact JSON specifications needed for institutions to share meaning without sharing raw data.
date: 2026-04-05
---

# The Base Interfaces of Federated Risk

To achieve a true "Federated National Risk Coordination Layer," standardizing how information is passed is more critical than the algorithms running underneath. Raw data must never be shared—only the *meaning* and *interpretation* of that data. 

To govern this, we introduce three core mathematical and structural contracts.

## 1. The Signal Contract (Institution → Federation)
This is the single most important interface. It standardizes how a Treasury department and a Health department report stress to each other, using a common temporal and geospatial matrix.

```json
{
  "signal_id": "uuid",
  "producer_org": "Ministry of Health",
  "domain": "health",
  "indicator": "hospital_bed_capacity",
  "geo": { "level": "county", "code": "047" },
  "window": { "start": "2026-04-01T00:00:00Z", "end": "2026-04-07T00:00:00Z" },
  "anomaly_score": 0.85,
  "trend_velocity": 0.2,
  "confidence": 0.9,
  "data_latency_hours": 24.0,
  "quality_flags": ["missingness", "revision"],
  "sensitivity": "restricted",
  "provenance": { "method": "ml", "model_version": "v1.2.0" }
}
```
**Why it matters:** Notice that there is no sensitive patient data included. The federation only receives the *anomaly score*, *trend velocity*, and *confidence degree*.

## 2. The Coordination Trigger Contract (Engine → Conveners)
When the Cross-Layer Interpretation Engine detects systemic alignment across independent fields, it translates those signals into actionable triggers for the Executive layer.

```json
{
  "trigger_id": "uuid",
  "time": "2026-04-08T12:00:00Z",
  "geo": { "level": "county", "code": "047" },
  "severity": 0.92,
  "confidence": 0.88,
  "supporting_domains": ["econ", "health", "infra"],
  "supporting_signals": ["sig_123", "sig_456"],
  "rationale": {
    "convergence": 0.89,
    "persistence": 0.95,
    "coherence": 0.81,
    "acceleration": 0.40
  },
  "recommended_action": "REVIEW",
  "constraints": ["classified_dependencies"]
}
```

## 3. The Action & Feedback Contract (Conveners → Engine)
The system requires a closed-loop. Once a coordination trigger is escalated and action is taken, the system logs the intervention to verify if the risk actually damped over the following weeks.

```json
{
  "action_id": "uuid",
  "trigger_id": "uuid",
  "owner": "National Security Secretariat",
  "action_type": "resource_shift",
  "scope": { "geo": { "level": "county", "code": "047" }, "time_horizon_days": 14 },
  "expected_effects": [
    { "domain": "health", "indicator": "anomaly_score", "direction": "down", "target_delta": 0.3 }
  ],
  "status": "in_progress"
}
```

These three contracts form the backbone of cross-institutional collaboration.
