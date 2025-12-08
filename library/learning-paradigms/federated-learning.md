---
title: Federated Learning - What It Is, Approaches, Algorithms, and How to Train One
description: A comprehensive guide to Federated Learning, covering its approaches, algorithms, training process, and practical applications in privacy-preserving machine learning.
section: Library
date: 2025-11-29
links:
  - title: Scarcity Overview
    url: /scarcity/overview
    description: How the constraint system chooses paradigms.
  - title: Research Log · Origin
    url: /research-log/scarcity/2025-01-origin
    description: First experiment thread that uses federated participation.
---

# Federated Learning: What It Is, Approaches, Algorithms, and How to Train One

Federated Learning (FL) is a machine learning paradigm that enables multiple devices or organizations to collaboratively train a shared model without exchanging their raw data. Each participant (often called a client) trains a local model on its private dataset and only shares model updates, such as gradients or weights, with a central aggregator or with peers in a decentralized setup. This makes it possible to build high-performing global models while preserving privacy, reducing data transfer, and allowing data to remain distributed where it is generated.

The concept was first popularized by Google in 2016 for applications like Gboard's keyboard prediction, where models are trained across millions of mobile devices. Since then, it has evolved into a powerful framework used in healthcare, finance, IoT systems, and cross-institutional collaborations.

## Why Federated Learning Matters

* **Data privacy:** Sensitive data stays on local devices or servers.
* **Regulatory compliance:** Meets data protection standards such as GDPR and HIPAA.
* **Efficiency:** Reduces central data storage needs.
* **Inclusivity:** Allows participation from different entities with different data types.
* **Scalability:** Supports millions of edge devices with intermittent connectivity.

## Approaches to Federated Learning

Federated Learning can be categorized based on how data is distributed and how clients interact. Below are the major approaches and their characteristics.

| **Approach**                               | **Data Distribution**                 | **Typical Clients**                     | **Aggregation Style**           | **Advantages**         | **Challenges / Limitations**    | **Use Cases**                    |
| ------------------------------------------ | ------------------------------------- | --------------------------------------- | ------------------------------- | ---------------------- | ------------------------------- | -------------------------------- |
| **Horizontal FL (Sample-based)**           | Same features, different samples      | Devices or branches with similar schema | FedAvg / FedProx                | Simple, scalable       | Data heterogeneity (non-IID)    | Banking, hospitals, education    |
| **Vertical FL (Feature-based)**            | Same samples, different features      | Institutions sharing users              | Secure gradient aggregation     | Richer combined data   | Requires secure alignment       | Bank + e-commerce collaborations |
| **Federated Transfer Learning (FTL)**      | Different samples, different features | Cross-domain institutions               | Domain adaptation + fine-tuning | Transfers knowledge    | Low sample overlap              | Cross-industry projects          |
| **Cross-Silo FL**                          | Few reliable institutions             | Banks, agencies                         | Centralized or hierarchical     | Stable, regulated      | Governance overhead             | Institutional partnerships       |
| **Cross-Device FL**                        | Many small devices                    | Smartphones, IoT                        | Decentralized / asynchronous    | Highly scalable        | Connectivity and reliability    | Gboard, Siri, wearables          |
| **Asynchronous FL**                        | Unaligned updates                     | Any client type                         | Incremental aggregation         | Faster convergence     | Model staleness                 | Edge learning, mobile FL         |
| **Hierarchical FL**                        | Multi-level aggregation               | Regional clusters                       | Tiered aggregation              | Low communication cost | System complexity               | Smart cities, health networks    |
| **Personalized FL (PFL)**                  | Any data type                         | All clients                             | Meta-learning or interpolation  | Custom local models    | Hard to balance personalization | Healthcare, education            |
| **Federated Reinforcement Learning (FRL)** | Policy learning                       | Multi-agent systems                     | Shared policy updates           | Collaborative control  | Instability                     | Smart traffic, robotics          |
| **Secure FL**                              | Any                                   | All                                     | Encrypted updates               | Strong privacy         | Heavy computation               | Finance, healthcare              |

## Common Federated Learning Algorithms

Federated Learning has diverse algorithms tailored for different data distributions, communication patterns, and system architectures.

### 1. Federated Averaging (FedAvg)

- **How it works**: Clients train locally, then send model updates to a server which averages them. This produces a global model without centralized data.
- **Best for**: Homogeneous data and when clients are relatively reliable.
- **Challenges**: Non-IID data and inconsistent client participation can slow convergence or cause divergence.

### 2. FedProx

- **How it works**: Adds a proximal term to the loss function to limit how much client updates diverge from the global model. This stabilizes training in heterogeneous environments.
- **Best for**: Non-IID data distributions.
- **Challenges**: Requires careful tuning of the proximal coefficient (μ).

### 3. SCAFFOLD

- **How it works**: Uses control variates to correct the drift between client updates and the global model.
- **Best for**: Reducing variance caused by client drift.
- **Challenges**: Increased computational and communication overhead.

### 4. FedNova

- **How it works**: Normalizes client updates to address objective inconsistency.
- **Best for**: Reducing client drift and ensuring convergence.
- **Challenges**: Requires consistent scaling across clients.

### 5. Personalized Federated Learning (pFedMe, FedPer, FedBABU)

- **How it works**: Allows clients to adapt the global model to their specific data through fine-tuning or personalized layers.
- **Best for**: Highly heterogeneous data where clients have unique characteristics.
- **Challenges**: Balancing personalization with the shared global model.

### 6. Federated Reinforcement Learning

- **How it works**: Collaboratively trains RL agents across multiple environments without sharing raw experience data.
- **Best for**: Multi-agent systems and robotics.
- **Challenges**: Synchronization and stability in training.

## Training a Federated Learning Model

### Step 1: Define the Task and Data Distribution

- Identify the types of clients, their data, and connectivity patterns.
- Determine whether the data is IID or non-IID.
- Set evaluation criteria that account for client diversity.

### Step 2: Choose a Federated Learning Paradigm

- **Centralized**: A single aggregation server. Simpler but has a single point of failure.
- **Hierarchical**: Multiple aggregation layers (regional servers). Better scalability and resilience.
- **Decentralized**: Peer-to-peer aggregation. No central authority, but requires robust consensus mechanisms.

### Step 3: Select Algorithms and Security Measures

- Start with FedAvg, then consider FedProx or SCAFFOLD if heterogeneity is high.
- Implement secure aggregation to protect model updates.
- Apply differential privacy when dealing with sensitive data.

### Step 4: Handle System Constraints

- Account for intermittent connectivity and varying client compute power.
- Implement client selection to avoid stragglers.
- Use compression and quantization to reduce communication overhead.

### Step 5: Monitor and Iterate

- Track client participation rates, model convergence, and fairness metrics.
- Use validation sets that reflect client diversity.
- Iterate on algorithms and hyperparameters based on observed performance.

## Practical Applications

### Healthcare

- Collaborative model training across hospitals without sharing patient data.
- Improved diagnostic models through diverse datasets.

### Finance

- Fraud detection across banks without exposing sensitive transaction data.
- Credit scoring models that respect privacy regulations.

### Smart Devices and IoT

- On-device personalization for voice assistants.
- Collaborative anomaly detection in sensor networks.

## Challenges in Federated Learning

1. **Non-IID Data**: Data distributions vary widely across clients, complicating model convergence.
2. **Communication Costs**: Limited bandwidth and device constraints can hinder training.
3. **Security and Privacy**: Malicious clients may poison updates; secure aggregation and anomaly detection are crucial.
4. **Client Availability**: Participants may frequently disconnect or have unreliable connections.
5. **Evaluation**: Assessing model performance without centralized data is challenging.

## Future Trends

- **Personalization**: More focus on client-specific models.
- **Decentralization**: Reduced reliance on central servers through peer-to-peer methods.
- **Efficient Communication**: Advanced compression and quantization techniques.
- **Robustness**: Defenses against poisoning and backdoor attacks.
- **Regulatory Alignment**: Compliance frameworks for cross-border federated learning.

## Conclusion

Federated Learning represents a powerful approach to collaborative model training under privacy and data availability constraints. By carefully choosing algorithms, handling system limitations, and prioritizing security, organizations can build robust models while keeping data decentralized. In domains like finance, healthcare, and IoT, federated learning is not just a theoretical concept—it is already proving its value.
