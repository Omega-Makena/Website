---
title: Scarcity
date: 2026-04-05
description: A research framework for discovering structural relationships under data scarcity.
category: Independent Research
---

# Scarcity

### Structure Before Scale

**Scarcity** is a research framework for discovering structural relationships in dynamic multivariate data when observations are limited.

It started with a practical problem in macroeconomic modelling: some of the datasets I was working with had only a few dozen observations per variable. There was not enough data to reliably estimate everything I wanted the model to know.

So I changed the question.

Instead of asking a model to learn the whole system from sparse observations, **what if we first recovered the structure of the system itself?**

That became Scarcity.

> [!NOTE]
> **Ecosystem Context:** Scarcity is the core computational engine and theoretical framework that powers several applied platforms. It provides the causal discovery layer for [KShield](/projects/kshield/), which models national economies; [KScarcity](/projects/kscarcity/), a macroscopic orchestration platform; and the [NSE Insight](/projects/nse-insight) market-intelligence system. You can explore the [internal architecture of the Scarcity engine here](/scarcity/architecture/).

---

## What Scarcity Does

Scarcity processes data as a stream and builds a **typed, evolving relationship graph** of the system.

It does not assume that every dependency is a correlation. It can represent different kinds of relationships between variables and track whether those relationships become stronger, weaker, or disappear as new observations arrive.

The discovered structure can then be used as a prior or representation for other models.

The basic loop is:

**observe → discover structure → evaluate → maintain → reuse**

The aim is not to replace statistical or machine-learning models.

It is to give them information about **how the system is organized** before asking them to learn everything from the observations themselves.

---

## Why It Exists

Most machine-learning workflows treat limited data as a reason to use a simpler model, stronger regularization, or more prior information.

Scarcity explores a different possibility:

> **Some of the information we need may be in the organization of the system rather than in the number of observations.**

That idea is especially interesting in systems where observations are expensive, irregular, noisy, or constantly changing.

---

## The Research

The research began with macroeconomic data and expanded into several substantially different environments.

### Macroeconomics

The original test case used annual indicators for East African economies, with roughly 34 observations per variable.

Scarcity's calibrated discovery process substantially improved the ranking and false-positive behavior of recovered relationships under this constraint.

The downstream results were mixed—which is important. Some shallow structure-aware consumers improved over raw lag features, while deeper consumers degraded and simple persistence remained difficult to beat.

### Financial Markets

Scarcity was subsequently tested on high-frequency Bitcoin trade and order-flow data.

The streaming engine recovered a typed market graph and was used to distinguish different forms of order-flow and volatility relationships. The study also tested whether discovered relationships translated into economically useful trading signals.

They did not all do so.

A statistically detectable relationship was not automatically treated as a tradable edge.

### Biological Systems

Scarcity's structural discovery machinery is also used inside **BioTwin**, an experimental continuous-time biological modelling environment.

Controlled mechanistic experiments test whether known biological structure can be recovered from sparse, heterogeneous observations across multiple biological scales.

These experiments are validation environments for the framework. They are not claims of clinical validation.

---

## The Paper

The research is documented in:

### *Scarcity: A Streaming Relationship-Discovery and Federated-Learning Framework for Multivariate Time Series Under Data Scarcity*

The paper describes the framework, its statistical calibration, relationship model, federated setting, benchmarks, and domain experiments.

**[Read the Paper]**

This is a research manuscript / preprint. The results are empirical and bounded by the experiments reported in the work.

---

## The Software

Scarcity is also implemented as a Python package.

### Install

```bash
pip install scarcity
```

The package contains the framework itself rather than a simplified demonstration of the idea.

The research and software evolve together: experiments inform the framework, while the framework provides the environment in which those experiments can be reproduced and extended.

**[View the Repository]**

---

## What I Am Actually Testing

The central claim under investigation is narrower than “Scarcity solves data scarcity.”

It is:

> **When observations are scarce, some useful information about a system may survive in its structure even when its magnitudes are difficult to estimate reliably.**

The research is therefore testing three separate questions:

**Can structure be discovered?**

**Can it be distinguished from noise?**

**Does using that structure actually improve another task?**

Scarcity has produced evidence for some of these questions and negative or inconclusive results for others.

That distinction is part of the work.

---

## Current Status

Scarcity is an **active independent research programme with an implemented software framework and accompanying research paper**.

The main research phase is now focused less on adding capability and more on consolidating the evidence, documenting failure modes, preserving benchmarks, and establishing where the underlying idea holds—and where it does not.

**Structure survives when magnitudes do not.**
