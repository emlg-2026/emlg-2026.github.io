---
name: A Multifidelity Monte Carlo Approach for Simulating the Diffusion Coefficient of Water
speakers:
- Tom Frömbgen
track: Session 4
authors:
- T. Frömbgen
- A. Kuhn
- J. Dölz
- B. Kirchner
affiliations:
- 1. Mulliken Center for Theoretical Chemistry, University of Bonn, Beringstraße 4, 53115 Bonn, Germany
- 2. Institute for Numerical Simulation, University of Bonn, Friedrich-Hirzebruch-Allee 7, 53115 Bonn, Germany
email: tomfroe@uni-bonn.de
abstract_source: Frömbgen1.docx
---

### Authors

T. Frömbgen<sup>1</sup>, A. Kuhn<sup>2</sup>, J. Dölz<sup>2</sup>, B. Kirchner<sup>1</sup>

### Affiliations

1. Mulliken Center for Theoretical Chemistry, University of Bonn, Beringstraße 4, 53115 Bonn, Germany  
2. Institute for Numerical Simulation, University of Bonn, Friedrich-Hirzebruch-Allee 7, 53115 Bonn, Germany  

**Contact:** [tomfroe@uni-bonn.de](mailto:tomfroe@uni-bonn.de)

### Abstract

Self-diffusion coefficients computed from molecular dynamics simulations are known to suffer from systematic finite-size effects. To mitigate this dependence, additive correction terms have been proposed. [1,2] More recently, the OrthoBoXY approach [3] introduced tetragonal simulation boxes with specific aspect ratios for which the correction term vanishes.

In this contribution, we present an alternative strategy: a multifidelity Monte Carlo framework for the computation of diffusion coefficients of water that explicitly exploits, rather than corrects for, the size dependence. [4] Multifidelity methods, originally developed in the field of uncertainty quantification, combine computational models that evaluate the same quantity of interest—in this case the diffusion coefficient—at different levels of accuracy and computational cost. [5] In our framework, the model hierarchy is defined by the size of the simulation boxes. Water is represented by a rigid three-point model, and uncertainties in the non-bonded force-field parameters, namely the Lennard-Jones parameters and partial charges, are propagated through the simulations.

To assess the capabilities of the proposed framework, we conduct a large-scale study involving six computational models, three parameter calibrations, cubic and tetragonal simulation box geometries, and two sets of perturbed force-field parameters. Our results demonstrate that computational speed-ups of up to one order of magnitude can be achieved when successive models exhibit only small differences in their correlations with the high-fidelity model. Furthermore, nearly all combinations of high- and low-fidelity models outperform simulations relying exclusively on a single high-fidelity model, highlighting the robustness and efficiency of the multifidelity approach.

### References

[1] B. Dünweg and K. Kremer, J. Chem. Phys., 99, 6983–6997 (1993).

[2] I.-C. Yeh and G. Hummer, J. Phys. Chem. B, 108, 15873–15879 (2004).

[3] J. Busch and D. Paschek, J. Phys. Chem. B, 127, 7983–7987 (2023).

[4] T. Frömbgen, A. Kuhn, J. Dölz, and B. Kirchner, J. Chem. Phys., 164, 024504 (2026).

[5] B. Peherstorfer, K. Willcox, and M. Gunzburger, SIAM Rev., 60, 550–59 (2018).
