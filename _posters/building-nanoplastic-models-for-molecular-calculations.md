---
name: Building Nanoplastic Models for Molecular Calculations
speakers: []
authors:
- B. Szabó
- P. Zaby
- L. Dick
- K. Drysch
- Y. Dawer
- W. Reckien
- B. Kirchner
- O. Hollóczki1*
affiliations:
- 1. University of Debrecen
- 2. University of Bonn
email: holloczki.oldamur@science.unideb.hu
abstract_source: Szabo1.docx
---

### Abstract

Molecular simulations of plastic nanoparticles have become increasingly important in uncovering the toxicity of micro- and nanoplastics. Modeling nanoplastics requires realistic starting structures, otherwise the simulations may produce faulty results. Building such structures most often relies on folding multiple polymer chains into a tightly entangled particle, which is a complex task and necessitates careful optimization. Here we present a systematic workflow that employs a simulated annealing approach to generate low-energy nanoplastic models. The resulting structures are further refined through semiempirical quantum chemical geometry optimizations with the GFN2-xTB method, followed by benchmark single-point energy calculations using both GGA and hybrid DFT functionals. We demonstrate the effectiveness of this protocol on six types of plastics: polyethylene, polypropylene, polystyrene, nylon-66 and polyurethane.

The most stable geometries obtained (Figure 1) show notable agreement with previously reported theoretical and experimental structures. Polyethylene, for instance, forms a highly ordered arrangement, with long chain segments predominantly in trans conformation, similarly to the crystal structure of this polymer. In contrast, polypropylene and polystyrene exhibit helical chain geometries characterized by alternating gauche and trans configurations along the backbone. For nylon-66, folding is more complex due to hydrogen bonding between amide groups, leading to parallel chains connected through hydrogen-bond networks within the particle. Finally, all optimized structures are made publicly available in an online repository, with the aim of supporting and advancing future simulation studies, including enabling ensemble-based investigations [1].

![Figure from Szabo1.docx]({{ '/assets/posters/building-nanoplastic-models-for-molecular-calculations/figure-1.jpeg' | relative_url }})

Figure 1 – 3D structure of the obtained most stable plastic models

### References

[1] B. Szabó, P. Zaby, L. Dick, K. Drysch, Y. Dawer, W. Reckien, A. Udvardy, F. Neese, B. Kirchner, O. Hollóczki, J. Phys. Chem. B, 130, 2, 881–893 (2026).
