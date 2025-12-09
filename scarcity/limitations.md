---
title: "SCARCITY Limitations & Roadmap"
date: "2025-01-01"
description: "Transparency about what is missing or in progress."
---

# Limitations & Roadmap

We believe in transparency regarding the current state of the SCARCITY framework.

## Current Limitations

### 1. Hardware Utilization
* **GPU Acceleration**: While the architecture supports GPU hooks, the current version primarily utilizes CPU for the core MPIE loops. GPU offloading is currently experimental.
* **Memory Footprint**: The hypergraph store can grow significantly with long-running sessions (500MB - 2GB), requiring periodic pruning.

### 2. Privacy Mechanisms
* **Differential Privacy**: The current implementation supports basic Gaussian noise addition ($\epsilon, \delta$). Advanced mechanisms like Secure Multi-Party Computation (SMPC) are not yet implemented.

## Roadmap & Future Work

### 🚧 In Progress
* **Advanced Privacy**: Integrating homomorphic encryption for secure model aggregation.
* **Distributed Simulation**: Expanding the simulation engine to support distributed agent-based modeling across multiple nodes.
* **Enhanced Meta-Learning**: Improving the 5-tier meta-learning hierarchy for faster adaptation.

### 📋 Planned Features
* **Full GPU Acceleration**: moving tensor operations to CUDA for faster causal discovery.
* **Kubernetes Support**: Native Helm charts for deploying the Federation layer on K8s clusters.
* **Model Export**: Standardized ONNX export for causal graphs.
