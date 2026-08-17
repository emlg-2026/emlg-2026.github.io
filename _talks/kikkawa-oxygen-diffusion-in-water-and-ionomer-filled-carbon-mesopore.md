---
name: Oxygen Diffusion in Water- and Ionomer-filled Carbon Mesopores
speakers:
- Nobuaki Kikkawa
track: Session 9
authors:
- N. Kikkawa
- R. Jinnouchi
- T. Nagai
- S. Okazaki
- M. Kimura
affiliations:
- 1. Toyota Central R&D Labs., Inc.
- 2. Okayama University
- 3. Yokohama City University
- 4. Toyota Motor Corporation
email: kikkawa@mosk.tytlabs.co.jp
abstract_source: Kikkawa1.docx
---

### Abstract

Mesoporous carbon is a promising cathode catalyst support for polymer electrolyte fuel cells [1], as it can both mitigate catalyst poisoning by ionomer and reduce oxygen transport resistance at the ionomer-catalyst interface. However, oxygen transport resistance is also significantly affected by additional factors, including long diffusion pathways and blockage within pores by liquid water and ionomer. Therefore, optimizing the pore structure is essential to minimize overall transport resistance. To support such optimization, we have conducted molecular dynamics (MD) simulations to analyse oxygen transport within mesopores [2]. Considering the diversity of pore sizes, filing materials, and occupancies in actual fuel cells, we systematically investigated the effects of these factors on oxygen diffusion using an in-house automated tool for generating molecular systems [3, 4]. As a result of the comprehensive analysis, as shown in Figure 1a, the oxygen diffusion coefficient followed the order: low occupancy > water-filled > ionomer-filled conditions. Interestingly, in the water-filled conditions, the diffusion coefficient was comparable to that in bulk water, whereas under ionomer-filled conditions, it was approximately one order of magnitude lower than that in bulk ionomer. Oxygen diffusion in ionomer-filled pores is extremely slow, making it difficult to analyze by MD simulations alone. To address this limitation, we employed a combined approach of free energy landscape calculation and kinetic Monte Carlo simulations [5, 6] to additionally investigate the long-time dynamics of oxygen diffusion. The analysis revealed that oxygen diffusion is hindered by the trapping of oxygen molecules in voids formed near the pore walls (Figure 1b).

a)b)

![Figure from Kikkawa1.docx]({{ '/assets/abstracts/kikkawa-oxygen-diffusion-in-water-and-ionomer-filled-carbon-mesopore/figure-1.png' | relative_url }})

![Figure from Kikkawa1.docx]({{ '/assets/abstracts/kikkawa-oxygen-diffusion-in-water-and-ionomer-filled-carbon-mesopore/figure-2.png' | relative_url }})

Figure 1 – a) Snapshots (cross-sectional views are shown for pore systems) and oxygen diffusion coefficients in various conditions. b) Diffusion mechanism in ionomer-filled mesopores.

### References

[1] K. Kodama, et al., Nat. Nanotechnol., 16, 140 (2021).

[2] N. Kikkawa and M. Kimura, Langmuir, 40, 1674 (2024).

[3] N. Kikkawa and R. Jinnouchi, J. Phys. Chem. C, 126, 11518 (2022).

[4] N. Kikkawa, et al., ACS Appl. Mater. Interfaces, 14, 53744 (2022).

[5] T. Nagai, A. Yoshimori, S. Okazaki, J. Chem. Phys., 156, 154506 (2022).

[6] T. Nagai and S. Okazaki, J. Chem. Phys., 157, 054502 (2022).
