---
name: AI-Enabled Discovery of Deep Eutectic Solvents and Their Chemical Space
speakers:
- Dinis Abranches
track: Session 8
authors:
- João P. Santos
- Filipe H. B. Sosa
- Dinis O. Abranches
- João A. P. Coutinho
affiliations:
- 1. CICECO—Aveiro Institute of Materials, Department of Chemistry, University of Aveiro, 3810-193 Aveiro, Portugal
email: jdinis@ua.pt
abstract_source: Abranches2.docx
---

### Authors

João P. Santos<sup>1</sup>, Filipe H. B. Sosa<sup>1</sup>, Dinis O. Abranches<sup>1</sup>, João A. P. Coutinho<sup>1</sup>

### Affiliations

1. CICECO—Aveiro Institute of Materials, Department of Chemistry, University of Aveiro, 3810-193 Aveiro, Portugal  

**Contact:** [jdinis@ua.pt](mailto:jdinis@ua.pt)

### Abstract

Deep eutectic solvents (DESs), binary liquid mixtures noted for their strong intermolecular interactions, have emerged as promising green alternatives to traditional organic solvents. The design of these novel solvents is complex, as their properties do not simply reflect the weighted average of their precursors. Incorporating low molecular weight compounds, such as water, to reduce viscosity or modulate other properties is a common practice. This leads to an overly complex and extensive DES design space, where the number, chemical nature, and relative composition of precursors must be carefully tuned [1]. Machine learning (ML), with its innate ability to correlate variables, presents a promising alternative to trial-and-error approaches in the design of DESs.

In this work, Gaussian processes (GPs) [2] were used to fit and predict several physicochemical properties of DESs, namely density, viscosity, and melting temperature. Experimental data was collected from the literature, including over 400 unique DES combinations and more than 4000 independent data points. Each dataset was carefully split into training, validation, and testing sets to determine the optimal GP architecture and hyperparameters for each physicochemical property. Coefficients of determination exceeding 0.95 were achieved for all studied properties, including viscosity, which spanned values over eight orders of magnitude, and melting temperature, which encompassed a range of nearly 700 K. Using the trained GP models, new DES-based lubricants were designed by exploring the sigma profile space of DESs. The GPs suggested novel combinations of precursors not present in the original database to achieve desired viscosities and melting temperatures. These novel DESs were experimentally prepared and characterized for the first time in this work. Viscosity and tribological properties were also measured, which surpassed common standards in the literature for low and high operational temperatures, effectively leading to DES formulations suitable for lubricant applications.

### Acknowledgements

This work was developed within the scope of the project CICECO-Aveiro Institute of Materials, UID/50011/2025 (DOI 10.54499/UID/50011/2025) & LA/P/0006/2020 (DOI 10.54499/LA/P/0006/2020), financed by national funds through the FCT/MCTES (PIDDAC). Filipe Sosa acknowledges FCT (CEECIND/07209/2022).

### References

[1] D. O. Abranches and J. A. P. Coutinho. Annual Review of Chemical and Biomolecular Engineering 14 (2023): 141-163.

[2] D. O. Abranches, E. J. Maginn, Y. J. Colón, Proc. Natl. Acad. Sci. U.S.A., vol. 121 (2024), e2404676121.
