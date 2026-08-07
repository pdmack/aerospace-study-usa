# Aerospace Engineering — Research Landscape

This document maps what aerospace engineering actually contains. Read it to get a feel for which sub-field pulls — not to make a final decision, but to notice where your attention goes.

---

## Electric Propulsion

**What it is:** Spacecraft thrusters that use electric fields to accelerate ions to extremely high velocities. No combustion. Examples: ion drives, Hall thrusters, plasma thrusters.

**Why it matters:** Chemical rockets are efficient for getting off the ground but wasteful in deep space. Electric propulsion uses far less propellant for the same velocity change — critical for long-duration missions, satellite station-keeping, and deep space exploration. NASA's Dawn spacecraft used ion propulsion to orbit both Vesta and Ceres. Every large commercial satellite uses electric propulsion for station-keeping.

**What the research looks like:** Plasma physics, electromagnetism, fluid dynamics at low pressures, materials science (electrodes erode). Heavy simulation and experimental work. Understanding how plasma behaves in magnetic fields is core — this is where the physics background is directly useful. The field sits at the intersection of plasma physics and engineering.

**Your background here:** Strong. Plasma physics is physics. The mathematical toolkit transfers directly.

**Who is doing it:** Princeton (the legacy of Edgar Choueiri's Electric Propulsion and Plasma Dynamics Lab), Michigan (PEPL lab, one of the most active in the country), MIT, Georgia Tech, Colorado.

---

## Astrodynamics and Orbital Mechanics

**What it is:** The mathematics of motion in space. How to get from Earth to the Moon, to Mars, to an asteroid. How to design satellite constellations. How to avoid debris. How to optimize low-thrust trajectories over months or years.

**Why it matters:** Every mission starts here. You can have the best spacecraft in the world and it goes nowhere without the trajectory. As cislunar space becomes crowded — with Artemis, commercial landers, planned lunar stations — traffic management becomes a serious engineering and mathematical problem.

**What the research looks like:** Differential equations, optimization theory, dynamical systems, numerical methods. Very mathematical. The physics intuition required is classical mechanics and gravity — foundational, not exotic. This is perhaps the most direct translation from a physics background.

**Your background here:** Very strong. Classical mechanics is physics. The mathematical maturity from string theory coursework is more than sufficient.

**Who is doing it:** CU Boulder (exceptional, space-focused culture), UT Austin, Purdue, Cornell, MIT, JPL (not a university but the world's premier astrodynamics institution, and many professors have JPL ties).

---

## Space Propulsion — Chemical

**What it is:** Traditional rocket engines. Combustion of fuel and oxidizer to produce thrust. The Saturn V, the Falcon 9, the Raptor engine on Starship.

**Why it matters:** Still the only way to get significant mass off Earth's surface. SpaceX's reusability revolution has changed the economics but not the underlying physics. The Raptor engine (methane/liquid oxygen) represents the current state of the art.

**What the research looks like:** Combustion chemistry, thermodynamics, fluid dynamics, heat transfer, materials at extreme temperatures. More engineering-adjacent than electric propulsion. Requires a stronger engineering fundamentals base.

**Your background here:** Moderate gap. The physics is there but the combustion and thermodynamics background isn't. Bridgeable in a master's program.

**Who is doing it:** Purdue (long tradition), Georgia Tech, Caltech GALCIT, Penn State, UT Austin.

---

## Hypersonics

**What it is:** Flight at Mach 5 and above. Reentry vehicles (capsules coming back from orbit), hypersonic glide vehicles, proposed high-speed civil transport. The physics changes at these speeds — air dissociates and ionizes, heat loads become extreme.

**Why it matters:** Military interest is very high right now — hypersonic glide vehicles are a major area of defense investment globally. Reentry physics is critical for every crewed mission return. Future high-speed commercial transport is a long-term ambition.

**What the research looks like:** High-temperature gas dynamics, aerothermodynamics, computational fluid dynamics, materials under extreme heat. Highly computational. Some plasma physics at the edges (ionized flow around reentry vehicles).

**Your background here:** Partial. The high-temperature plasma physics connects to your background; the aerodynamics and structures less so.

**Who is doing it:** Georgia Tech, UT Austin, Maryland, Caltech, Texas A&M, AFRL (Air Force Research Lab).

---

## Space Environment and Space Weather

**What it is:** The physical environment that spacecraft operate in — radiation belts, solar wind, geomagnetic storms, atmospheric drag at low orbit, plasma interactions with satellite surfaces.

**Why it matters:** The space environment damages spacecraft. Radiation degrades electronics. Charged particles cause surface charging. Atmospheric drag slowly deorbits satellites. Predicting and understanding these effects is increasingly important as satellite constellations grow and cislunar space becomes operational.

**What the research looks like:** Space plasma physics, magnetohydrodynamics, radiation physics, atmospheric science. This is physics with an engineering application layer — understanding the environment so you can design for it.

**Your background here:** Very strong. This is applied plasma and space physics. The theoretical physics training from NBI is directly relevant.

**Who is doing it:** Michigan (strong space weather group), CU Boulder, MIT Haystack Observatory, UCLA, Boston University. Also national labs: Los Alamos, Goddard.

---

## Spacecraft Systems and Mission Design

**What it is:** Integrating all the pieces — propulsion, power, thermal control, communications, attitude control, structures — into a working spacecraft. Mission architecture: deciding what to build, how to orbit, how to operate.

**Why it matters:** The systems level is where missions succeed or fail. A beautiful propulsion system means nothing if the thermal design lets it cook. CubeSats and SmallSats have democratized this — a university team can now design, build, and launch a working satellite.

**What the research looks like:** Systems engineering, optimization, trade studies, simulation. Broad rather than deep. More engineering management in flavor than physics.

**Your background here:** Indirect. Your analytical skills transfer; the domain knowledge doesn't.

**Who is doing it:** MIT AeroAstro, Stanford, CU Boulder, Cal Poly (SmallSats), Georgia Tech.

---

## Autonomy and Guidance, Navigation, and Control (GNC)

**What it is:** Getting spacecraft (and aircraft) to navigate and operate independently. Autonomous rendezvous and docking, Mars rover navigation, autonomous landing, formation flying of satellite swarms.

**Why it matters:** Deep space missions can't be operated in real time from Earth — signal delays make autonomy essential. Autonomous rendezvous is critical for on-orbit servicing. The Ingenuity helicopter on Mars was a landmark in autonomous flight on another world.

**What the research looks like:** Control theory, estimation theory (Kalman filtering), machine learning, robotics. Mathematical but applied. Strong connections to AI/ML research.

**Your background here:** Moderate. Strong in the mathematical foundations; the control systems domain is new.

**Who is doing it:** MIT, Stanford, Caltech JPL connections, Carnegie Mellon, UT Austin.

---

## Where your background lands

| Sub-field | Your physics background | Gap to bridge |
|---|---|---|
| Electric Propulsion | Direct — plasma physics | Experimental lab skills |
| Astrodynamics | Very direct — classical mechanics, math | Domain vocabulary |
| Space Environment | Very direct — space plasma physics | Atmospheric/radiation specifics |
| Hypersonics | Partial — high-temp plasma at edges | Aerodynamics, gas dynamics |
| Chemical Propulsion | Indirect | Combustion, thermodynamics |
| Spacecraft Systems | Indirect | Systems engineering breadth |
| Autonomy / GNC | Mathematical foundations | Control theory, estimation |

The top three are where you'd arrive the least behind. Any good master's program covers the gaps — but starting in your strength makes the first year easier and the research better.

---

## What's moving right now

A few things that weren't on anyone's radar five years ago:

**Cislunar space** — The region between Earth and the Moon is becoming operational. Artemis, commercial lunar landers, proposed Gateway station. Astrodynamics for this regime (complex three-body dynamics) is an active research area.

**In-space servicing** — Satellites that repair, refuel, and upgrade other satellites. Changes the economics of the entire industry. Requires precision GNC and docking.

**Nuclear propulsion revival** — NASA and DARPA are both funding nuclear thermal propulsion seriously for the first time since the 1970s. High specific impulse for deep space. Academic programs at Purdue, Maryland, and Idaho National Lab are active.

**Satellite mega-constellations** — Starlink (6,000+ satellites), OneWeb, Amazon Kuiper. Orbit design, collision avoidance, deorbit at end-of-life are active research areas. Raising significant space debris concerns.

**Reusability at scale** — SpaceX Starship aims for full and rapid reusability. The engineering challenges — thermal protection, propellant loading, structural fatigue — are active research questions.

---

*Next: programs.md — which institutions own which of these areas.*
