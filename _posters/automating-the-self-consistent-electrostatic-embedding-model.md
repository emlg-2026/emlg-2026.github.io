---
name: Automating the Self-Consistent Electrostatic Embedding Model
speakers: []
authors:
- Z. Macpherson
- L. Lue
- M. Jorge
affiliations:
- 1. University of Strathclyde, Glasgow, G1 1XJ
email: zoe.macpherson.2018@uni.strath.ac.uk
abstract_source: Macpherson1.docx
---

### Abstract

The ability of molecular simulations to reliably predict thermodynamic and transport properties depends crucially on the quality of underlying force field models, which describe the bonded and non-bonded interactions of molecules. Emulating experimental observations has allowed us to design these models over the past 50 years to study previously inaccessible chemistry. The most widely used force fields are nonpolarisable, and consequently fail to capture polarisation effects, resulting in systematic deviations in properties such as the dielectric constant. This raises questions about model performance in areas relevant to drug discovery, eg predicting solvation, transfer or binding free energies. Such deviations can be mitigated through post facto polarisation corrections;[1] however, knowledge of the liquid phase dipole moment, a quantity related to polarisation, is required.

Our research group developed Self-Consistent Electrostatic Embedding (SCEE): a computationally efficient approach combining classical molecular simulations with ab initio calculations to accurately capture polarisation effects.[2] Previously applied to various polar solvents, we have automated this approach within a new Python workflow, enabling dipole moment calculations at unprecedented accuracy across a wide range of molecules.[3,4] We demonstrate Automated SCEE through two test cases: i) wide exploration of the phase space of water, including liquid, vapour and supercritical states;[5] ii) dipole moment calculation of substituted aromatic molecules in the liquid phase, by far the largest molecules to which this approach has been applied. Our results reveal new connections between the liquid dipole moment and local interactions, particularly hydrogen bonding.

### References

[1] M. Jorge and L. Lue, (2019): The Dielectric Constant: Reconciling Simulation and Experiment, J. Chem. Phys., 150,084108

[2] M. Jorge, J. R. B Gomes, and A. W. Milne, (2021): Self Consistent Electrostatic Embedding for Liquid Phase Polarisation, J. Mol. Liq., 114550

[3] M. Jorge, M. C. Barrera, A. W. Milne, C. Ringrose and D. J. Cole, (2023): What Is the Optimal Dipole Moment for Nonpolarisable Models of Liquids?, J. Chem. Theo. And Comp., 1790-1804

[4] M. Jorge, J. R. B. Gomes, and M. C. Barrera, (2022): The Dipole Moment of Alcohols in the Liquid Phase and In Solution, J. Mol. Liq., 356, 119033

[5] Z. Macpherson, J. R.B. Gomes, M. Jorge and L. Lue (2024): The Dipole Moment of Supercritical Water – Local vs Mean-field Polarisation Contributions, Mol Phys, e2381574., DOI: 10.1080/00268976.2024.2381574
