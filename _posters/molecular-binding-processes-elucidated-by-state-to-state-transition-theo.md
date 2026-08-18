---
name: Molecular Binding Processes Elucidated by State-to-State Transition Theory and Molecular Dynamics Simulation
speakers: []
authors:
- K. Kasahara
- R. Okabe
- C. A. Chang
- T. Mori
- and N. Matubayasi
affiliations:
- 1. Graduate School of Engineering Science, The University of Osaka
- 2. Department of Chemistry, University of California at Riverside
- 3. Graduate School of Engineering, Kyoto University
email: kasahara@cheng.es.osaka-u.ac.jp
abstract_source: Kasahara1.docx
---

### Abstract

The dynamics of proteins, including folding and unfolding as well as ligand binding and unbinding, proceed through a number of intermediate states, which are closely related to biological functions. To elucidate the structural dynamics of biological systems based on molecular dynamics (MD) simulations, the Markov state model (MSM)[1] has been widely utilized. This method enables the description of long-timescale dynamics of the target molecule based on transitions between states that characterize distinct stable structures. A practical limitation is the need to introduce a coarse-grained timescale, namely, a lag time, in computing transition probabilities. It is known that the resulting kinetic properties, such as rate constants, can be sensitive to the choice of the lag time.

![Figure 1 – Prediction of the time-correlation function (TCF) associated with the state change based on the short-timescale MD and IEPDYN[2] method.]({{ '/assets/abstracts/molecular-binding-processes-elucidated-by-state-to-state-transition-theo/figure-1.emf' | relative_url }})

*Figure 1 – Prediction of the time-correlation function (TCF) associated with the state change based on the short-timescale MD and IEPDYN[2] method.*

To overcome this limitation, we propose the integral-equation formalism of population dynamics (IEPDYN) to describe the population dynamics of distinct configurational states ()[2]. According to classical reaction dynamics theory, the probability density associated with a given state obeys the Liouville equation, including influx from and efflux to neighbouring states. By introducing a Markov approximation for the crossing of boundaries separating the states, one can derive tractable integral equations governing the state populations at time , , and the population flux from state to state at time , (Fig. 1). The time-dependent quantities appearing in these equations ( and ) are associated with the retention behaviours within a given state and the state-to-state transitions. Because these quantities depend only on a few states in the local neighbourhood of a given state, they can be computed using a set of short-timescale MD simulations. The population dynamics on long timescales can be predicted by solving the set of the integral equations of and . The IEPDYN method is formulated in continuous time and therefore does not rely on a lag time. Consequently, kinetic quantities obtained from IEPDYN are free from lag-time dependence.

We apply the IEPDYN method to the binding and unbinding kinetics of CH4/CH4, Na+/Cl−, and 18-crown-6-ether (crown ether)/K+ in water. For both kinetics, the time constants estimated from the IEPDYN method are comparable to those obtained from brute-force MD simulations. The required timescale of each MD trajectory in the IEPDYN method is approximately two orders of magnitude shorter than that in the brute-force MD approach in the crown ether/K+ system.

### References

[1] V. S. Pande, K. Beauchamp, and G. R. Bowman, Methods, 52, 99 (2010).

[2] K. Kasahara, R. Okabe, C. A. Chang, T. Mori, and N. Matubayasi, J. Chem. Phys., 164, 124112 (2026).
