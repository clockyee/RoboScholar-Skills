# Robotics Venue Notes

Use this reference when the manuscript concerns robotics, embodied AI, evolutionary robotics, artificial life, morphology-control co-design, bio-inspired systems, soft robotics, swarm robotics, or robot learning.

## Venue Families

- **Robotics strong-recognition venues**: IEEE Transactions on Robotics, The International Journal of Robotics Research, IEEE Robotics and Automation Letters, Science Robotics, Robotics and Autonomous Systems, Autonomous Robots, Soft Robotics.
- **Evolutionary computation / ALife-adjacent venues**: Swarm and Evolutionary Computation, IEEE Transactions on Evolutionary Computation, Artificial Life, Adaptive Behavior.
- **Bio-inspired / biomimetics venues**: Bioinspiration & Biomimetics, Biomimetics, Advanced Intelligent Systems, Advanced Bionics. Check CAS/SCI carefully; some may not satisfy strict CAS 1/2 requirements.
- **Magazine-style venues**: IEEE Robotics & Automation Magazine can have high recognition and IF, but check whether the article must be accessible magazine style and whether CAS partition satisfies the user's hard requirement.

## Fit Heuristics

- Simulation-only embodied evolution is usually more plausible for Swarm and Evolutionary Computation or IEEE Transactions on Evolutionary Computation than for T-RO/IJRR/Science Robotics.
- Robotics and Autonomous Systems can be a strong fit if the manuscript clearly maps simulation assumptions to robot systems and includes credible robotics baselines.
- RA-L is short and robotics-facing; prefer it when the contribution can be compressed and ideally supported by a physical prototype, video, or high-fidelity robot simulation.
- T-RO/IJRR/Science Robotics are stretch targets unless the work has strong real-robot evidence, system novelty, or broadly important robotics theory.
- Soft Robotics requires a soft, compliant, deformable, or variable-morphology physical system; a generic morphology-plasticity simulation is usually not enough.

## Common Robotics Revision Gaps

- Add real robot, small prototype, or bench-top validation when targeting robotics-first venues.
- Explain the reality gap: morphology parameters, mass, friction, actuation limits, sensing, power consumption, and controller update rates.
- Include videos or high-quality system images when the journal expects robot demonstrations.
- Compare against robotics baselines, not only evolutionary computation baselines.
- Report robustness across seeds, environments, initial states, sensor noise, and dynamics perturbations.
