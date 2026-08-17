---
name: Harnessing machine learning for the design and structural classification of periodic mesoporous silica
speakers:
- Andrew Mawbey
track: Session 7
authors:
- A. Mawbey
- T. Stavert
- J. Cardona
- M. Jorge
affiliations:
- 1. Department of Chemical and Process Engineering, University of Strathclyde, 75 Montrose Street, Glasgow G1 1XJ, UK
email: a.mawbey@strath.ac.uk
abstract_source: Mawbey1.docx
---

### Abstract

Understanding the self-assembly process involved in producing ordered mesoporous silica (OMS) is vital to both improve control over the molecular structure and guide the design of sustainable manufacturing of these materials. Whilst the use of ammonium surfactants (e.g. cetyltrimethylammonium bromide, CTAB) produces a highly ordered OMS with a variety of potential applications (separations, catalysis, drug delivery, etc.) [1], the economic and environmental limitations of this surfactant impose limits on its large-scale industrial use. Efforts have been made to use more environmentally friendly amine surfactants, such as dodecylamine (DDA), but this invariably has led to a much lower degree of order in the resulting porous structures [2].

This work employs coarse-grained molecular dynamics to investigate a mixed surfactant approach, combining amine surfactants with a small quantity of ammonium surfactant to improve OMS sustainability whilst retaining a high degree of structural order. Initial results, shown in Figure 1, indicate that the addition of ammonium surfactants has a significant impact on silica structure, highlighting the potential for these systems to unlock the sustainability of OMS materials.

![Figure from Mawbey1.docx]({{ '/assets/abstracts/mawbey-harnessing-machine-learning-for-the-design-and-structural-cl/figure-1.png' | relative_url }})

Figure 1 – Simulated configurations of surfactant (blue) and silica (yellow) at a pH of 10.5. With a surfactant fraction as DDA of (a) 1, showing a clear lamellar phase; (b) 0.75, showing a disordered lamellar phase; (c) 0.5, showing a disordered hexagonal phase; (d) 0.25, showing a more ordered hexagonal phase.

To overcome the limitations of manual structural classification and quantify the simulated materials degree of order, we have developed a machine learning classification model using the PointNet architecture [3]. The model successfully classifies common OMS structures to a high degree of accuracy (up to 99%). Crucially, through use of a dynamic subcloud sampling technique, this model captures the emergence of local order within larger-scale self-assembly trajectories.

These tools work together to promote a quantifiable strategy for greener OMS synthesis through the computational design.

### References

[1] J. G. Croissant, Y. Fatieiev, A. Almalik, and N. M. Khashab, Adv Healthc Mater, vol. 7, Page (2018).

[2] A. Centi, J. R. H. Manning, V. Srivastava, S. van Meurs, S. V. Patwardhan, and M. Jorge, Mater Horiz, vol. 6, pp. 10277-1033 (2019).

[3] C. R. Qi, H. Su, K. Mo and L. J. Guibas, Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, July 21-26, Honolulu, USA, 2017, pp. 652–660
