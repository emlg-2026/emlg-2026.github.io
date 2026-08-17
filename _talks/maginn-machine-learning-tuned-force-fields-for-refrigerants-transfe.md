---
name: 'Machine-learning-tuned force fields for refrigerants: transferability across thermophysical properties, state points, and liquid interfaces'
speakers:
- Ed Maginn
track: Session 8
authors:
- B. P. Agbodekhe
- E. J. Maginn
affiliations:
- Department of Chemical and Biomolecular Engineering, University of Notre Dame, Notre Dame, IN 46556, USA
email: ed@nd.edu
abstract_source: Maginn-EMLG-JMLG-abstract.docx
---

### Authors

B. P. Agbodekhe, E. J. Maginn

### Affiliations

Department of Chemical and Biomolecular Engineering, University of Notre Dame, Notre Dame, IN 46556, USA  

**Contact:** [ed@nd.edu](mailto:ed@nd.edu)

### Abstract

Hydrofluorocarbon refrigerants used in heating, ventilation, air conditioning, and refrigeration (HVACR) systems have high global warming potential and are being phased out under the Kigali Amendment to the Montreal Protocol. Meeting this challenge requires both the discovery of low-GWP replacement mixtures and the reclamation of legacy refrigerants, the latter requiring separation of azeotropic and near-azeotropic mixtures. Because reliable experimental data for the relevant mixtures and conditions are scarce, molecular simulation is an indispensable predictive tool in this effort, but its fidelity rests on the accuracy and transferability of the underlying force fields (FFs). One promising approach optimizes the non-bonded (Lennard-Jones) parameters of an FF against experimental vapor-liquid equilibria (VLE) data via a machine-learning protocol, while retaining the bonded parameters and partial charges of a standard classical FF such as GAFF [1-3]. Two questions follow: do such VLE-tuned FFs transfer to properties and thermodynamic states absent from the tuning set, and do they extend to mixtures and interfaces?

We address these questions through an extensive, multi-property validation of new FFs we have developed for seven refrigerants spanning three chemical classes [4,5]. For difluoromethane (R-32) and pentafluoroethane (R-125), four near-degenerate VLE-tuned candidate FFs per molecule were evaluated against eleven thermophysical, transport, and structural properties not used in tuning, each at several state points. The VLE-tuned models proved highly transferable, generally outperforming an expert-tuned FF for R-32 and GAFF for R-125. Properties absent from the tuning resolved differences that VLE data alone could not, enabling a robust ranking of otherwise indistinguishable parameter sets. We then test generality across five additional refrigerants (R-50, R-170, R-14, R-134a, and R-143a), adding two new tests: the surface tension and properties at subcooled liquid states far from the VLE manifold. The new FFs capture surface-tension trends well, with quantitative agreement within ~10% for four of the five fluids and retain near-saturation predictive quality at subcooled conditions. Tuning only the Lennard-Jones parameters while preserving the classical physics-based functional form thus yields models that transfer across property types, chemical classes, and thermodynamic conditions, providing a foundation for simulating the mixtures and interfaces central to refrigerant reclamation and a circular HVACR economy.

### References

[1] B. J. Befort, R. S. DeFever, G. M. Tow, A. W. Dowling, and E. J. Maginn, J. Chem. Inf. Model., 61, 4400 (2021).

[2] N. Wang, M. N. Carlozo, E. Marin-Rimoldi, B. J. Befort, A. W. Dowling, and E. J. Maginn, J. Chem. Theory Comput., 19, 4546 (2023).

[3] M. N. Carlozo, N. Wang, A. W. Dowling, and E. J. Maginn, Digit. Discov., 5, 1650 (2026).

[4] B. Agbodekhe, E. Marin-Rimoldi, Y. Zhang, A. W. Dowling, and E. J. Maginn, J. Chem. Eng. Data, 69, 427 (2024).

[5] B. Agbodekhe and E. J. Maginn, in preparation (2026).
