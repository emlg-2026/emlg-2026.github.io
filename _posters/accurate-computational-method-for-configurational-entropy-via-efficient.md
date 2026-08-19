---
number: 7
name: Accurate computational method for configurational entropy via efficient solvation free energy calculation
speakers: []
authors:
- R. Kaji
- S. Hervø-Hansen
- K. Kasahara
- N. Matubayasi
affiliations:
- 1. Graduate school of Engineering Science, The University of Osaka
email: kaji-ry@cheng.es.osaka-u.ac.jp
abstract_source: kaji.docx
---

### Abstract

Introduction Configurational entropy reflecting the flexibility of molecular structures is a crucial quantity for understanding biological processes such as protein folding and ligand binding. In statistical mechanics, configurational entropy is defined using the probability density function of molecular coordinates as

Direct computation of configurational entropy is generally difficult because of the high dimensionality of molecular conformation space, and therefore several approximate computational methods have been proposed [1]. In this study, we propose an accurate computational method to evaluate the change in configurational entropy of molecules in solution from molecular dynamics (MD) simulations based on solvation free energy calculations.

Theory In solution, the configurational-entropy change of a solute molecule can be expressed as

where is the intramolecular potential energy of the solute, is the solvation free energy at a fixed configuration of the solute, and is the free-energy change. can be calculated from the free-energy change of the isolated solute and the change in the solvation free energy. Based on this relationship, configurational-entropy changes can be rigorously evaluated by combining MD simulations in solution, vacuum, and solvation free energy calculations. However, as the flexibility of target solute molecules increases, the computation of solvation free energy with solute being flexible () becomes challenging. In this work, we constructed an efficient scheme based on an error minimization method to realize an accurate estimation of through the values for a small number of configurations.

Results and Discussion Configurational-entropy changes were calculated for linear alkanes and alkanediols from bent to extended states, and for carboxylic acids from syn to anti conformations in water. Figure 1 shows the configurational-entropy changes together with the corresponding free energy and energetic contribution. For linear alkanes and alkanediols, configurational-entropy changes increased with alkyl chain length, destabilizing the extended state. In butanoic acid, the syn conformation is stabilized mainly by energetic contributions. In contrast, in o-anisic acid, the configurational entropy of the anti conformation was more than 1 kcal/mol smaller than that of the syn conformation because of restricted rotational degrees of freedom induced by intramolecular hydrogen bond formation between the carboxyl and methoxy groups. Comparison with the quasi-harmonic approximation (QHA) showed that configurational entropy changes of linear alkanes and alkanediols are significantly larger with QHA than with the present method, indicating strong anharmonicity in these systems.

![Figure 1 – The changes in configurational entropy, free-energy, and energetic contribution.]({{ '/assets/posters/accurate-computational-method-for-configurational-entropy-via-efficient/figure-1.emf' | relative_url }})

*Figure 1 – The changes in configurational entropy, free-energy, and energetic contribution.*

### References

[1] S. Hikiri, T. Yoshidome, and M. Ikeguchi, J. Chem. Theory Comput., 12, 5990 (2016).

[2] S. Hervø-Hansen, K. Okita, K. Kasahara, and N. Matubayasi, J. Chem. Theory Comput., 21, 1064 (2025).
