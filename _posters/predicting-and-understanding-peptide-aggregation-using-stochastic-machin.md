---
number: 1
name: Predicting and Understanding Peptide Aggregation using Stochastic Machine Learning
speakers: []
authors:
- João P. Santos
- Pavel Zelenovskii
- Filipe Figueiredo
- Dinis O. Abranches
affiliations:
- 1. CICECO—Aveiro Institute of Materials, Department of Chemistry, University of Aveiro, 3810-193 Aveiro, Portugal
- 2. Department of Physics & CICECO−Aveiro Institute of Materials, University of Aveiro, Aveiro, 3810-193, Portugal
email: jdinis@ua.pt
abstract_source: Abranches1.docx
---

### Abstract

Peptides can self-assemble into ordered nanostructures such as nanofibers, nanotubes, or sheets. They are promising functional elements for energy harvesting and energy storage systems, and are inherently eco-friendly [1]. Unfortunately, the peptide space is too vast to explore using costly and time-consuming experimental or computational (e.g., molecular dynamics) trial-and-error approaches. As such, a method to convert the discrete set of all synthesizable peptides to a continuous mathematical space, navigable through simple optimization procedures, is proposed in this work based on sigma profiles [2].

The aggregation propensity of all possible dipeptides (400) and tripeptides (8000) in water was taken from the literature, estimated using computational simulations. This dataset was split into training and testing sets using stratified sampling. The training data was used to fit a Gaussian process (GP) model, followed by making predictions for peptides never seen before by the model (testing set). The GP model exhibited remarkable performance, attaining testing set coefficients of determination of 0.87 for dipeptides and 0.85 for tripeptides. To minimize model data requirements, GPs were combined with the stochastic frameworks of active learning and Bayesian optimization. This demonstrated that GPs serve as laboratory companions, suggesting amino acid combinations that maximize peptide self-aggregation with only a handful of training examples. All in all, this work establishes a new paradigm on digital molecular spaces for peptides and their efficient navigation by exploiting sigma profiles.

### Acknowledgements

This work was developed within the scope of the project CICECO-Aveiro Institute of Materials, UID/50011/2025 (DOI 10.54499/UID/50011/2025) & LA/P/0006/2020 (DOI 10.54499/LA/P/0006/2020), financed by national funds through the FCT/MCTES (PIDDAC).

### References

[1] P. S. Zelenovskii, K. Romanyuk, M. S. Liberato, P. Brandao, et al., Funct. Mater., vol. 31 (2021), 2102524.

[2] D. O. Abranches, E. J. Maginn, Y. J. Colón, Proc. Natl. Acad. Sci. U.S.A., vol. 121 (2024), e2404676121.
