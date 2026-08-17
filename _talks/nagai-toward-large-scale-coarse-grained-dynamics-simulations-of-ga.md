---
name: Toward large-scale coarse-grained dynamics simulations of gas diffusion aided by machine-learning in realistic systems
speakers:
- Tetsuro Nagai
track: Session 9
authors:
- Tetsuro Nagai
- Zhiye Tang
- Yoshitake Sakae
- Tatsuya Yamada
- Nobuaki Kikkawa
- Ryosuke Jinnouchi
- Kumiko Nomura
- Masayuki Kimura
- and Susumu Okazaki
affiliations:
- 1. Research Institute for Interdisciplinary Science, Okayama University, Japan
- 2. Institute for Molecular Science, Japan
- 3. Center for Management of Information Technologies, Kagoshima University, Japan
- 4. Research Organization for Information Science and Technology, Japan
- 5. Toyota Central R&D Labs., Inc., Japan
- 6. Toyota Motor Corporation, Japan
- 7. Graduate School of Nanobioscience, Yokohama City University, Japan
email: tnagai@okayama-u.ac.jp
abstract_source: Nagai1.docx
---

### Abstract

Mass transport within heterogeneous media is a widespread phenomenon observed in various physical, chemical, and biological systems. Examples of such heterogeneous media include gas separation membranes for carbon capture, polymer electrolyte membranes, and the cathode catalyst layers of fuel cells. Molecular diffusion is key to understanding mass transport and molecular dynamics (MD) simulations are a powerful tool for examining the diffusion process in atomistic detail. However, the timescales associated with molecular diffusion in heterogeneous systems often exceed those accessible by conventional all-atom MD simulations, thereby limiting the direct applicability of MD to these problems.

One promising strategy to overcome this limitation is to construct coarse-grained dynamics of the diffusing molecules. For this purpose, we proposed the dynamic Monte Carlo (MC) approach [1], which can effectively generate long-time trajectories of diffusing molecules. The dynamic MC method requires the free energy landscape and position-dependent diffusion constant of a diffusing molecule as input and these input quantities can be obtained from MD simulations. This approach was demonstrated in applications to hydrogen gas diffusion through polymer electrolyte membranes [2,3]. In addition to reproducing gas permeability at various water uptakes, we clarified the molecular-level mechanism of the gas permeation.

However, the evaluation of input quantities for an entire large-scale system, such as a 100 nm-scale cathode catalyst layer model, using MD calculations is computationally prohibitive. To address this issue, we adopted the machine learning (ML) approach. We employed support vector regression (SVR) with the smooth overlap of atomic positions (SOAP) kernel to predict the input quantities from local chemical structures [4]. The ML model can be trained using a small subset of the input quantities or those obtained for smaller or more tractable systems resembling the large-scale system in question. We can thus circumvent the evaluation of the input quantities in the entire system.

In this presentation, we introduce our recent efforts to apply our methodology to oxygen gas transport in the large-scale, realistic all-atom cathode catalyst layer model constructed based on experimental structural information. This work helps establish a common framework for evaluating mass transport in spatially heterogeneous systems.

### References

[1] T. Nagai et al., J. Chem. Phys. 156, 154506 (2022).

[2] T. Nagai and Susumu Okazaki, J. Chem. Phys. 157, 054502 (2022).

[3] T. Nagai et al., J. Chem. Phys. 156, 044507 (2022).

[4] T. Nagai et al., J. Chem. Theory Comput. 21, 2598–2611 (2025).
