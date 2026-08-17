---
name: Tuning the water models to elucidate the effect of ATP to disordered proteins in high ATP concentration
speakers:
- Toshifumi Mori
track: Session 11
authors:
- Toshifumi Mori
- Norio Yoshida
affiliations:
- 1. Graduate School of Engineering, Kyoto University
- 2. Graduate School of Informatics, Nagoya University
email: toshi_mori@moleng.kyoto-u.ac.jp
abstract_source: Mori1.docx
---

### Abstract

ATP plays a fundamental role as an energy currency in biomolecular systems. The concentration of ATP in cells is yet much higher than what is needed for proteins to function. It has recently been realized that ATP in high concentration can dissolve protein aggregates and regulate liquid-liquid phase separations, indicating the role of ATP as a hydrotrope [1]. To understand its underlying molecular mechanism, molecular dynaimics (MD) simulations have been applied to study the ATP-protein interactions. Yet, ATP molecules in MD simulations with classical force fields tend to over-aggregate compared to experimental dissociation constants [2], and aggregation of ATP molecules can negatively affect the protein-ATP interactions. We anticipated that this over-aggregation is partly due to the TIP3P water model, which is widely used but has been known to fail in properly describing protein unfolded state, e.g., shows over-compact character.

To this end, we examined different water models to see how the over-aggregation of ATP molecules can be controlled. In particular, we compared TIP4P-D and OPC against TIP3P, which are designed to improve the behavior of the protein unfolded state. Our MD simulations on the ATP in ~15 mM concentration showed that ATP aggregates to a single cluster in the TIP3P water, whereas dynamic changes in the ATP cluster size were observed in the TIP4P-D and OPC waters. This indicates that ATP over-aggregation can be reduced by changing the water model.

Next, by simulating the ATP-protein interaction for the disordered protein α-Synuclein, we found that water model also has a large impact on the ATP-protein interactions. In particular, ATP bound to the protein was almost fully preserved once formed in the TIP3P water, whereas repeating binding/unbinding from the protein was observed in the TIP4P-D and OPC waters.

These results indicate the importance of water models in describing the ATP-protein interaction in high ATP concentration and also suggests that the interaction can be tuned by choosing the appropriate water model [3].

![Figure from Mori1.docx]({{ '/assets/abstracts/mori-tuning-the-water-models-to-elucidate-the-effect-of-atp-to-di/figure-1.png' | relative_url }})

Figure 1 – Summary of ATP-protein interactions. (a) Characteristic snapshot, (b) distribution of cluster sizes, and (c) distances between ATP and residues in α-Synuclein along the trajectories.

### References

[1] A. Patel et al., Science, 356, 753-756 (2017).

[2] J. Mehringer et al., Cell Reports Phys. Sci., 2, 100343 (2021).

[3] T. Mori and N. Yoshida, J. Chem. Phys. 159, 035102 (2023).
