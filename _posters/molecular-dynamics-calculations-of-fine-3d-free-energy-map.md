---
name: Molecular Dynamics Calculations of Fine 3D Free Energy Map
speakers: []
authors:
- for Water Molecule Solved in Polymers and Lipid Bilayers K. Fujimoto
- Z. Tang
- T. Nagai
- W. Shinoda
- S. Okazaki
affiliations:
- 1. Kansai University, Suita, Osaka 564-8680, Japan
- 2. Institute for Molecular Science, Myodaiji, Okazaki 444-8585, Japan
- 3. Okayama University, Tsushima-naka, Okayama 700-8530, Japan
- 4. Yokohama City University, Kanazawa-ku, Yokohama 236-0027, Japan
email: okazaki.sus.oy@yokohama-cu.ac.jp
abstract_source: Okazaki1.docx
---

### Abstract

We developed an efficient calculation method for free energy of transfer of small molecules from vacuum to inside of the inhomogeneous media such as polymers and lipid bilayers. The method enables us to draw fine three dimensional (3D) free energy map consisting of one million meshes. The calculations adopted three techniques. First, the free energy was calculated according to Widom equation [1] combined with a new importance sampling method. Second, the method samples thousands of test molecules simultaneously, each of which follows single-particle canonical distribution independently of each other. The sampling was also accelerated by high-temperature sampling method. Computational cost of the method is much lower than that of the conventional particle insertion method based on inefficient random samplings.

The position-dependent free energy plays a central role in dynamic Monte Carlo calculations as reported in our previous papers [2-4]. Further, the fine free energy map must present abundant information about microscopic absorption mechanism such as spatial distribution of absorption points together with their stabilization energy. It also presents information about diffusion mechanism such as 3D diffusion path networks formed by spatially distributed free energy saddle points connected by slopes from the minimum points.

Here we applied the method to water molecule in two soft materials, amorphous polylactic acid (PLA) and dipalmitoyl phosphatidyl choline (DPPC) and obtained the fine 3D free energy map with 0.05 nm resolution as shown in Fig. 1. The former is a solid polyester in which water molecule can make hydrogen bonds with the ester groups. The latter forms a bilayer where lipid molecules are ordered though they are still flexible and mobile. Water molecules can diffuse in both media. However, the diffusion mechanism must be very different from each other reflecting the difference in free energy landscape as clearly shown in the figure.

![Figure from Okazaki1.docx]({{ '/assets/abstracts/molecular-dynamics-calculations-of-fine-3d-free-energy-map/figure-1.jpeg' | relative_url }})

![Figure from Okazaki1.docx]({{ '/assets/abstracts/molecular-dynamics-calculations-of-fine-3d-free-energy-map/figure-2.jpeg' | relative_url }})

![Figure 1 – Cross sections of the calculated 3D free energy of transfer of water molecule at kz=0 from vacuum to inside of the (left) PLA and (right) DPPC.]({{ '/assets/abstracts/molecular-dynamics-calculations-of-fine-3d-free-energy-map/figure-3.wmf' | relative_url }})

*Figure 1 – Cross sections of the calculated 3D free energy of transfer of water molecule at kz=0 from vacuum to inside of the (left) PLA and (right) DPPC.*

### References

[1] B. Widom, J. Chem. Phys. 39, 2808 (1963).

[2] T. Nagai, A. Yoshimori, S. Okazaki, J. Chem. Phys., 156, 154506 (2022).

[3] T. Nagai, S. Okazaki, J. Chem. Phys., 157, 054502 (2022).

[4] S. Okazaki, J. Chem. Phys., 160, 174111 (2024).
