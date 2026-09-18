---
title: StocksKE
date: 2026-08-24
description: News-driven prediction system for short-term price impact on the Nairobi Securities Exchange (NSE).
---

# StocksKE — NSE News-to-Market Impact Engine

StocksKE is a news-driven prediction system for short-term price impact on the Nairobi Securities Exchange (NSE).

Its central architectural idea is to separate perception from reasoning.

* **LLM**: What happened?
* **Knowledge graph**: Who else should be affected, and how?

The LLM therefore does not need to encode the entire financial relationship network.

## What it does

StocksKE consumes Kenyan financial/news sources and produces predictions for affected NSE companies:

* Direction
* Expected magnitude
* Confidence
* Propagation/audit path

For example, an event involving Boeing aircraft can affect Kenya Airways even when Kenya Airways is never mentioned in the original article.

The system discovers this through the knowledge graph.

## How it works

The main pipeline is:

`News → Relevance Filter → LLM Extraction → Validation → Graph Propagation → Price Alignment → Backtest`

### 1. News collection
RSS feeds from Kenyan news sources are collected, article bodies extracted, and cross-run duplicates removed.

### 2. Relevance filtering
Before calling the LLM, articles are filtered for NSE/macro relevance. This reduces unnecessary LLM calls.

### 3. Event extraction
An LLM converts the article into a structured source event, identifying things such as:
* Event type
* Severity
* Source entities
* Direction

The LLM is only responsible for understanding the event.

### 4. Validation
Extracted tickers and fields are validated to prevent hallucinated company mappings.

### 5. Knowledge-graph propagation
The graph propagates the event through relationships between:
* Companies
* Sectors
* Products
* Macro/commodity drivers

Relationships include:
* Competitors
* Suppliers
* Products
* Sector membership
* Drivers
* Data-derived co-movement

Each propagation step applies signed impact, decay and confidence.

### 6. Market alignment
Predictions are compared against realized NSE prices.

The current architecture works with daily closes, supporting D / D+1 / D+3 / D+5 horizons.

### 7. Evaluation
The harness evaluates predictions using abnormal returns and compares them against baselines.

## How the knowledge graph is built

The graph isn't solely hardcoded. It combines:

* Curated company/product/driver relationships
* Historical price co-movement
* Article entity co-occurrence
* Validated driver relationships

These are consolidated into a graph artifact consumed by production.

## Example

**Event:**
Ethiopian Airlines crash

The extractor identifies the event and its severity.

The graph then reasons:
`Ethiopian Airlines → Boeing 737 MAX → Kenya Airways`

Therefore:
`KQ → negative impact`

The important architectural point is that the LLM didn't have to know that Kenya Airways operates Boeing aircraft. That relationship lives in the graph.

## Production architecture

The production layer uses:

* **FastAPI** for the service/API
* **Celery** for asynchronous processing
* **Postgres/TimescaleDB** for production data
* **Alerts** for prediction outputs

The pipeline remains independently executable for evaluation and research.

## Key limitations

The documentation explicitly identifies several limitations:

* Daily prices cannot support the original 1-hour prediction horizon.
* Corporate actions use a heuristic rather than a true adjusted-close feed.
* Some driver exposures remain curated and unvalidated.
* Calibration currently uses synthetic defaults until fitted to real NSE labels.
* Historical backtesting requires archived news; RSS is primarily suitable for live/forward evaluation.
* Extraction quality depends significantly on the selected LLM.
