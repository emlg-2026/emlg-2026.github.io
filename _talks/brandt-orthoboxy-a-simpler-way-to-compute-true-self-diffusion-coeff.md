---
name: 'OrthoBoXY: A Simpler Way to Compute True Self-Diffusion Coefficients and Viscosities from MD Simulations'
speakers:
- Marcel Brandt
track: Session 4
authors:
- M. Brandt
- D. Paschek
- R. Ludwig
affiliations:
- 1. University of Rostock, Albert-Einstein-Str. 27, 18059 Rostock, Germany
- 2. Leibniz Institute of Catalysis, Albert-Einstein-Str. 29A, 18059 Rostock, Germany
email: marcel.brandt@uni-rostock.de
abstract_source: Brandt1.docx
---

### Authors

M. Brandt<sup>1</sup>, D. Paschek<sup>1</sup>, R. Ludwig<sup>1</sup><sup>,2</sup>

### Affiliations

1. University of Rostock, Albert-Einstein-Str. 27, 18059 Rostock, Germany  
2. Leibniz Institute of Catalysis, Albert-Einstein-Str. 29A, 18059 Rostock, Germany  

**Contact:** [marcel.brandt@uni-rostock.de](mailto:marcel.brandt@uni-rostock.de)

### Abstract

Self-diffusion coefficients calculated from molecular dynamics (MD) simulations with periodic boundary conditions are known to exhibit a system size-dependence. The deviation from the “true” system size-independent self-diffusion coefficient can be calculated via a correction term to the simulated self-diffusion coefficient. This correction, known as the Yeh-Hummer correction, requires the knowledge of the viscosity and shows a 1/L dependency, where L is the length of a cubic simulation box. [1]

When stretching the box along the z-axis, we obtain an orthorhombic system where the self-diffusion coefficient becomes direction-dependent. By employing a hydrodynamic model, it is possible to exactly determine the difference between the simulated and the “true” self-diffusion coefficient for varying box size ratios. Interestingly, at a so-called “magic” ratio the hydrodynamic effects cancel each other out and the correction vanishes in the x- and y-direction. The OrthoBoXY method now uses simulation boxes with this “magic” box size ratio of Lz/Lx = Lz/Ly = 2.793… in order to obtain the “true” system size-independent self-diffusion coefficients in the x- and y-direction. Moreover, the still system size-dependent self-diffusion coefficient in the z-direction can be used to determine the viscosity. [2,3]

MD simulations of a variety of molecular liquids, ionic liquids and liquid mixtures have demonstrated the accuracy of this approach for systems where the Yeh-Hummer correction holds true. However, there are some systems known to not be described properly by this correction. For example, electrolyte solutions show a smaller deviation from the “true” self-diffusion coefficient than predicted by the Yeh-Hummer correction, i.e. the self-diffusion coefficient is overcorrected. In our recent work, we use the OrthoBoXY method to investigate the system size-dependence of these systems.

### References

[1] I.-C. Yeh, G. Hummer, J. Phys. Chem. B, 108, 15873–15879 (2004).

[2] J. Busch, D. Paschek, J. Phys. Chem. B, 127, 7983–7987 (2023).

[3] J. Busch, D. Paschek, J. Phys. Chem. B, 128, 1040–1052 (2024).
