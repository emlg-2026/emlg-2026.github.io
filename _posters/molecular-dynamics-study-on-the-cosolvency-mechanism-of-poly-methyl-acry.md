---
number: 19
name: Molecular Dynamics Study on the Cosolvency Mechanism of Poly(methyl acrylate) in Ethanol/Water Mixtures
speakers: []
authors:
- I. Takahashi
- Y. Yasuda
- M. Kato
- and K. Fujimoto
affiliations:
- 1. Grad. Sch. of Life Sci., Ritsumeikan Univ., 1-1-1 Nojihigashi, Kusatsu, Shiga 525-8577, Japan
- 2. Grad. Sch. of Frontier Sci., The Univ. of Tokyo, 5-1-5 Kashiwanoha, Kashiwa, Chiba 277-8561, Japan
- 3. Dept. of Appl. Chem., Coll. of Life Sci., Ritsumeikan Univ., 1-1-1 Nojihigashi, Kusatsu, Shiga 525-8577, Japan
- 4. Dept. of Chem. and Mater. Eng., Fac. of Chem., Mater. and Bioeng., Kansai Univ., 3-3-35 Yamate-cho, Suita, Osaka 564-8680, Japan
email: k-fuji@kansai-u.ac.jp
abstract_source: Takahashi1.docx
---

### Abstract

Polymeric materials are widely used in both everyday applications and as advanced functional materials, and solubility is a critical factor governing their properties. When polymers are employed in biomedical applications — such as dentures, bone cement, and contact lenses — dissolution in biological environments may lead to mechanical degradation and leaching of potentially harmful substances. Polymer solubility has conventionally been evaluated using Hansen solubility parameters (HSP) [1], which describe solute–solvent interactions in terms of dispersion forces, polarity, and hydrogen bonding. However, acrylic polymers are known to exhibit an anomalous cosolvency phenomenon: they show low solubility in pure water or pure ethanol individually, yet dissolve readily in ethanol/water mixtures at 80 vol% ethanol [2]. This behavior cannot be explained by conventional solubility indices based on pairwise solute–solvent interactions, and a molecular-level mechanistic understanding is therefore required. In this study, we perform molecular dynamics (MD) simulations of a single polymer chain in ethanol/water mixtures and discuss the molecular origin of polymer dissolution stability based on the solvation structure between the polymer and solvent. Poly(methyl acrylate) (PMA) was used as a structurally simpler analogue of poly(methyl methacrylate), for which cosolvency has been well investigated [2].

A 580-mer single-chain PMA was constructed and mixed into ethanol/water solutions at 0, 20, 40, 60, 70, 80, 90, and 100% (v/v) ethanol using PACKMOL. All MD simulations were performed using GROMACS-2022 [3] (double precision) with OPLS-AA [4] force field for PMA and ethanol, and TIP4P [5] model for water. To generate initial polymer conformations spanning from globule to coil states, NPT simulations were performed at 300 K for solvents and 400 K for PMA, 1 bar for 50 ns, yielding structures with normalized radii of gyration () of 0.4, 0.7, 1.0, and 1.3. Two sets of simulations were then conducted:

(1) Equilibrium conformation analysis.

Polymer chains with = 0.4, 0.7, 1.0, and 1.3 were each dissolved in 0, 40, 80, and 100% (v/v) ethanol solution, and simulated at 363.15 K and 1 bar. The equilibrium chain conformations were compared across solvent compositions. The resulting of the polymer increased with increasing alcohol concentration.

(2) Solvation structure analysis.

An extended chain ( = 1.3) was dissolved in 0, 20, 40, 60, 70, 80, 90, and 100% (v/v) ethanol solution. Simulations were performed at 363.15 K and 1 bar with the polymer backbone restrained, allowing analysis of the solvation structure around the dissolved polymer chain as a function of ethanol content.

### References

[1] C. M. Hansen, The Three Dimensional Solubility Parameter and Solvent Diffusion Coefficient: Their Importance in Surface Coating Formulation. Copenhagen (1967). [2] J. M. G. Cowie, M. A. Mohsin and I. J. MuCwen, polymer, 28, 1569 (1987). [3] S. Pall et al., J. Chem. Phys. 153, 134110 (2020). [4] W. J. Jorgensen, D. S. Maxwell, J. TiradoRives, J. Am. Chem. Soc. 118, 11225 (1996). [5] W. J. Jorgensen et al., J. Chem. Phys., 79, 926 (1983).
