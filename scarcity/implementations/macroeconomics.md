---
title: Macroeconomics Implementation
description: Modeling macro signals without high-frequency proprietary data.
section: Scarcity
date: 2025-01-11
links:
  - title: Architecture
    url: /scarcity/architecture
    description: How constraint choices shape the pipeline.
---

**Problem**  
Forecast macro indicators with sparse, lagged public data and no access to private feeds.

**Scarcity components exercised**  
Constraint ledger (data latency + availability), experiment rail (nowcasting with synthetic gaps), narrative layer (communicating uncertainty ranges).

**What worked**  
Bootstrapping with proxy signals and robust uncertainty estimates kept forecasts honest.

**What failed**  
Seasonality adjustments were brittle when public releases slipped; models overreacted to noise in small series.

**Next steps**  
Test online-learning variants that adapt gracefully to release delays; expand proxy set and monitor drift aggressively.
