title: Measuring and Mitigating Bias in Machine Learning Systems
date: 2024-08-25
category: My Papers
author: Omega Makena
description: Research on developing frameworks for identifying and reducing algorithmic bias in AI systems.

---

## Motivation

As machine learning systems increasingly influence critical decisions—from loan approvals to criminal justice to hiring—ensuring these systems are fair and equitable becomes paramount. My research focuses on developing practical frameworks for measuring and mitigating bias in ML systems.

### The Challenge of Fairness

Fairness in ML isn't a solved problem for several reasons:

1. **Multiple definitions**: Different mathematical definitions of fairness can be mutually exclusive
2. **Data reflects historical bias**: Training on historical data can perpetuate or amplify existing societal biases
3. **Intersectionality**: Bias can manifest differently across intersecting protected attributes
4. **Deployment challenges**: Even "fair" models can produce unfair outcomes in practice

### Research Questions

This work addresses three primary questions:

**Q1**: How can we comprehensively measure bias across different fairness definitions?

**Q2**: What interventions most effectively reduce bias while maintaining model utility?

**Q3**: How do fairness guarantees hold up under distribution shift and in real-world deployment?

## Methodology

### 1. Comprehensive Fairness Metrics

I developed a unified framework evaluating models across multiple fairness criteria:

**Group Fairness Metrics**:
- Demographic parity: \(P(\hat{Y}=1|A=0) = P(\hat{Y}=1|A=1)\)
- Equalized odds: \(P(\hat{Y}=1|Y=y, A=a)\) equal across groups
- Equal opportunity: Equalized true positive rates

**Individual Fairness Metrics**:
- Similar individuals receive similar predictions
- Counterfactual fairness: Predictions don't change if sensitive attributes change

**Calibration**:
- Predictions are calibrated across groups
- \(P(Y=1|\hat{Y}=p, A=a) = p\) for all groups

### 2. Bias Mitigation Techniques

I compared three categories of interventions:

**Pre-processing**: Modifying training data
- Reweighting samples
- Learning fair representations
- Synthetic data augmentation

**In-processing**: Modifying learning algorithm
- Adversarial debiasing
- Fairness constraints in optimization
- Multi-objective learning balancing accuracy and fairness

**Post-processing**: Modifying model outputs
- Threshold optimization per group
- Calibration adjustments
- Reject option classification

### 3. Robustness Analysis

Critical contribution: analyzing how fairness degrades under:
- Distribution shift between training and deployment
- Data drift over time
- Adversarial manipulation
- Subgroup variations

## Key Findings

### Finding 1: No Free Lunch

Trade-offs between different fairness metrics are real and unavoidable. Satisfying demographic parity often conflicts with equalized odds. The choice depends on the specific application and stakeholder values.

**Implication**: Fairness interventions must be context-specific, not one-size-fits-all.

### Finding 2: In-Processing Works Best

In-processing methods (incorporating fairness during training) generally outperformed pre- and post-processing approaches, achieving better accuracy-fairness trade-offs.

**Explanation**: Optimizing for both objectives jointly allows the model to learn representations that naturally balance accuracy and fairness.

### Finding 3: Intersectionality Matters

Standard fairness metrics often miss bias affecting intersectional subgroups (e.g., Black women vs. general gender or race categories).

**Solution**: Developed metrics specifically targeting intersectional fairness, though this increases complexity and data requirements.

### Finding 4: Fairness Degrades Under Shift

Perhaps most concerning: models fair on training data can become significantly biased under distribution shift.

**Mitigation**: Regularization techniques and robust optimization can improve fairness stability, but ongoing monitoring is essential.

## Practical Framework

Based on this research, I propose a deployment framework:

**Phase 1: Audit**
1. Identify protected attributes and potential harms
2. Measure bias across multiple metrics
3. Analyze intersectional fairness
4. Document findings and trade-offs

**Phase 2: Intervention**
1. Select appropriate mitigation technique based on constraints
2. Implement with explicit fairness objectives
3. Validate on held-out data
4. Test robustness under distribution shift

**Phase 3: Monitor**
1. Deploy with continuous monitoring
2. Track fairness metrics in production
3. Alert on metric degradation
4. Regularly retrain and audit

## Limitations and Future Work

This research has important limitations:

1. **Protected attributes**: Often unavailable or imperfectly measured
2. **Proxy discrimination**: Models can use proxies for protected attributes
3. **Causality**: Observational fairness metrics don't capture causal mechanisms
4. **Stakeholder values**: Technical solutions don't address whose fairness definition should prevail

Future directions:

- Causal frameworks for fairness
- Fairness under missing or noisy sensitive attributes
- Multi-stakeholder fairness negotiation mechanisms
- Long-term societal impacts beyond immediate decisions

## Conclusion

Algorithmic fairness is fundamentally a sociotechnical challenge requiring technical rigor **and** engagement with affected communities, policymakers, and domain experts.

The tools and frameworks developed in this research provide practitioners with concrete methods for measuring and improving fairness, but they're not a substitute for careful ethical reasoning about how AI systems should be deployed in high-stakes contexts.

### Code and Data

Implementation and experiments available at: [github.com/Omega-Makena/AI-equity](https://github.com/Omega-Makena/AI-equity)

### Acknowledgments

This research benefited from discussions with ethicists, policymakers, and community advocates. Technical solutions must be informed by lived experience and normative values.

---

*This post summarizes ongoing research. Formal publication details forthcoming.*



