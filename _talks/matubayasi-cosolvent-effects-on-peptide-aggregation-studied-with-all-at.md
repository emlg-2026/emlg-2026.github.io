---
name: Cosolvent Effects on Peptide Aggregation Studied with All-Atom MD and a Solvation Theory
speakers:
- Nobuyuki Matubayasi
track: Session 10
authors:
- Nobuyuki Matubayasi
affiliations:
- Graduate School of Engineering Science, Osaka University, Osaka 560-8531 Japan
email: nobuyuki@cheng.es.osaka-u.ac.jp
abstract_source: Abstract_Matubayasi.docx
---

### Abstract

Solvent affects strongly the structures of biomolecules. The aggregation state of a biomolecule can then be modulated by the solvent environment, and indeed, it is considered that cosolvents act to regulate the structures and aggregation tendencies of proteins in biological systems. This work addresses the molecular mechanism of the effects of ATP (adenosine triphosphate) on peptide aggregation from the energetic standpoint by combining all-atom MD simulation and a solvation theory [1,2]. ATP is present in cells at concentrations much higher than required for its biological reactions as the energy source, and it has been shown experimentally that ATP acts as a cosolvent to inhibit the aggregation of proteins and peptides [3]. The aggregation core of amyloid b was employed as a model peptide, and the changes in the equilibria between the dissociated and aggregate states of the peptide induced by addition of ATP as a cosolvent was examined in comparison to the case of urea cosolvent.

The equilibrium of n-mer formation from n monomers (1-mers) is determined by the excess chemical potential of the n-mer (n = 1 for 1-mer). The change in the equilibrium constant upon addition of the cosolvent at a concentration of c is then given by the corresponding changes in for the species involved. The cosolvent-induced change in is expressed exactly as

![Figure from Abstract_Matubayasi.docx]({{ '/assets/abstracts/matubayasi-cosolvent-effects-on-peptide-aggregation-studied-with-all-at/figure-1.emf' | relative_url }})

![Figure from Abstract_Matubayasi.docx]({{ '/assets/abstracts/matubayasi-cosolvent-effects-on-peptide-aggregation-studied-with-all-at/figure-2.emf' | relative_url }})

due to the variational theorem, where is the cosolvent-induced change in the solvation free energy averaged over the solute structures sampled in the pure-water solvent. In , the contributions are absent from the changes in the peptide structures (configurational entropies) and the peptide-peptide interactions. The force fields were Amber03w and TIP4P/2005.

![aggregation number nFigure 1. Cosolvent-induced changes in the solvation free energies per monomer averaged over the structures of peptide or its n-mer sampled in the pure-water solvent.]({{ '/assets/abstracts/matubayasi-cosolvent-effects-on-peptide-aggregation-studied-with-all-at/figure-3.emf' | relative_url }})

*aggregation number nFigure 1. Cosolvent-induced changes in the solvation free energies per monomer averaged over the structures of peptide or its n-mer sampled in the pure-water solvent.*

![aggregation number nFigure 1. Cosolvent-induced changes in the solvation free energies per monomer averaged over the structures of peptide or its n-mer sampled in the pure-water solvent.]({{ '/assets/abstracts/matubayasi-cosolvent-effects-on-peptide-aggregation-studied-with-all-at/figure-4.emf' | relative_url }})

*aggregation number nFigure 1. Cosolvent-induced changes in the solvation free energies per monomer averaged over the structures of peptide or its n-mer sampled in the pure-water solvent.*

Figure 1 shows as a function of the aggregation number n. Each n-mer is stabilized upon addition of ATP or urea, and the extent of stabilization is stronger at small n. This means that ATP and urea favor the 1-mer, leading to the inhibition of aggregation by virtue of the above equation. It can also be shown that ATP is more effective for the inhibition by two orders of magnitude compared with urea at similar concentrations. Through the decomposition of free energy, it is revealed that the aggregation is inhibited by the van der Waals interaction both for ATP and urea. Although the electrostatic interaction with the highly charged ATP is strong, it is essentially cancelled by the loss of interactions with water. The observed features of energetics are common between ATP and urea, indicative of the non-specificity of the ATP’s (and urea’s) effects of aggregate inhibition.

### References

T. M. Do, D. Horinek, and N. Matubayasi, Phys. Chem. Chem. Phys., 26, 11880 (2024).

T. M. Do, N. Matubayasi, and D. Horinek, Phys. Chem. Chem. Phys., 27, 6325 (2025).

A. Patel, L. Malinovska, S. Saha, J. Wang, S. Alberti, Y. Krishnan, and A. A. Hyman, Science, 356, 753 (2017).
