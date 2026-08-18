---
name: Development of a prediction method of a solvent configuration
speakers: []
authors:
- based on Extended Molecular Ornstein-Zernike theory Y. Matsui
- N. Yoshida
affiliations:
- 1. Graduate school of informatics Nagoya University Aichi Japan
email: matsui.yusei.h0@s.mail.nagoya-u.ac.jp
abstract_source: Matsui1.docx
---

### Abstract

Solvent is essential for the structure and function of biomolecules. Determining the solvation structure around biomolecules is crucial for understanding their roles. The Extended Molecular Ornstein-Zernike (XMOZ) theory describes the solvation structure around a complex solute molecule as a six-dimensional distribution function of both position and orientation [1]. While this distribution function is certainly useful for understanding the solvation, determining an explicit molecular configuration identical to that obtained from X-ray or neutron diffraction experiments would also be of substantial value. In this study, we developed a prediction method of a solvent configuration based on XMOZ theory (Figure 1). Since our method is a straightforward extension of the “Placevent method” which is based on three-dimensional reference interaction site model (3D-RISM) theory [2], we refer to it as the “Molecular Placevent” method.

In the Molecular Placevent method, explicit solvent molecules are placed through an iterative procedure. In each iteration, the position and orientation corresponding to the maximum of the distribution function are identified, an explicit solvent molecule is placed at that position and orientation, and the density corresponding to the placed molecule is subtracted from the original distribution function. The density-subtraction region is defined as the positions corresponding to an isotropic region centered at the position of the maximum point and all orientations. The isotropic region is determined such that the integrated three-dimensional population function within the region corresponds to a single solvent molecule.

To demonstrate the performance, the molecular placevent method was applied to some protein systems and predicted solvent configurations were compared to neutron diffraction or joint X-ray/neutron data. The predicted positions and orientations of water molecules directly coordinated to the protein or ligand were in good agreement with the experimental results. A detailed discussion on the performance of the proposed method will be presented at the conference.

![Figure from Matsui1.docx]({{ '/assets/posters/development-of-a-prediction-method-of-a-solvent-configuration/figure-1.png' | relative_url }})

Since molecular placevent method can determine solvent configurations including hydrogen atoms, it will be highly useful for elucidating the role of solvent, especially water, in biochemical systems where the application of neutron diffraction is challenging.

### References

[1] R. Ishizuka, N. Yoshida, J. Chem. Phys., 139, 084119 (2013).

[2] D. J. Sindhikara, N. Yoshida, F. Hirata, J. Comput. Chem., 33, 1536 (2012).
