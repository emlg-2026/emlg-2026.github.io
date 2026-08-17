---
name: Predicting Partition Coefficients of Biomolecules in Aqueous Biphasic Systems
speakers:
- Margarida Pinhão
track: Session 8
authors:
- A. Margarida D. Pinhão
- B. Emanuel V. Capela
- C. João A. P. Coutinho
- D. Mara G. Freire
- E. Dinis O. Abranches
affiliations:
- 1. CICECO-Aveiro Institute of Materials, Department of Chemistry, University of Aveiro, Portugal
email: margaridapinhao@ua.pt
abstract_source: Pinhão1.docx
---

### Authors

A. Margarida D. Pinhão<sup>1</sup>, B. Emanuel V. Capela<sup>1</sup>, C. João A. P. Coutinho<sup>1</sup>, D. Mara G. Freire<sup>1</sup>, E. Dinis O. Abranches<sup>1</sup>

### Affiliations

1. CICECO-Aveiro Institute of Materials, Department of Chemistry, University of Aveiro, Portugal  

**Contact:** [margaridapinhao@ua.pt](mailto:margaridapinhao@ua.pt)

### Abstract

Aqueous Biphasic Systems (ABSs) have emerged as a viable approach in the purification of biomolecules without loss of biological activity. Unlike traditional water-organic biphasic systems, ABSs consist of two immiscible aqueous phases and are non-toxic, non-flammable, and biocompatible. Ionic liquids (ILs) are often used as ABS constituents to better control biomolecule-solvent interactions and enhance separation performance. However, given the vast library of ILs, the selection of suitable systems for each target biomolecule relies on laborious trial-and-error campaigns. Machine learning (ML), particularly Gaussian process (GP) models have been shown to be capable of predicting physicochemical properties of materials and emerge as a viable alternative to help design IL- based ABSs.

In this work, GP models were developed to predict the partitioning behaviour of several biomolecules, such as caffeine, nicotine, phenylalanine, gallic acid and levodopa, in different polyethylene glycol-dextran (PEG-DEX) ABSs. Sigma profiles, molecular descriptors derived from quantum chemistry calculations, were employed. The GP models were able to predict the partition coefficients of all biomolecules across several different ABSs. Overall, coefficients of determination of 0.99 and 0.85 were attained for the training and testing sets, respectively. The testing set consisted of novel ABSs never seen before by the model, highlighting its predictive and generalization capability. The methodology developed in this work significantly accelerates the design of separation and purification processes based on ABSs, guiding the experimental design and reducing trial and error screening.

![Figure from Pinhão1.docx]({{ '/assets/abstracts/pinhao-predicting-partition-coefficients-of-biomolecules-in-aqueous/figure-1.png' | relative_url }})

Figure 1 – Sigma profiles of all the Ionic Liquids added as adjuvants to the Aqueous Biphasic Systems, used as input to the Gaussian Process model to predict the relative Partition Coefficients of the solutes in the DEX-rich, bottom phase, achieving R-Squared values of 0.99 and 0.85 for the training and testing sets, respectively.
