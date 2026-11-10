### Idea
From the [[Faraday-Lenz Law]], a **changing magnetic flux** through a loop induces an EMF. Now apply that to a coil of wire carrying its *own* current: if that current changes, its own magnetic field changes, which changes the flux through itself, which induces an EMF that **fights the change**. This is **Inductance**.

Think of an inductor as the **"inertia" of a circuit**. Just like a heavy object resists changes in its velocity, an inductor resists changes in current:
- Try to **increase** the current, and the inductor pushes back.
- Try to **cut** the current, and the inductor tries to keep it flowing (that's why yanking a plug can cause a spark).
- If the current is **steady**, the inductor does nothing at all and acts like a plain wire.

Inductance shows up in two flavors:
- **Mutual Inductance**: a changing current in one coil induces an EMF in a **neighboring** coil (how transformers and wireless chargers work).
- **Self-Inductance**: a changing current in a coil induces an EMF in **itself**.

### Formally: Mutual Inductance
When two coils sit near each other, a changing current $i_1$ in coil 1 creates a changing magnetic flux through coil 2, inducing an EMF in coil 2:
$$ \mathcal{E}_2 = -M \frac{di_1}{dt} \qquad \mathcal{E}_1 = -M \frac{di_2}{dt} $$
**Mutual Inductance ($M$):**
$$ M = \frac{N_2 \Phi_{B2}}{i_1} = \frac{N_1 \Phi_{B1}}{i_2} $$
- **Units**: **Henry (H)**, where $1 \text{ H} = 1 \ \text{Wb/A} = 1 \ \text{V}\cdot\text{s/A} = 1 \ \Omega\cdot\text{s}$.
- *Note: $M$ is the same in both directions. Coil 1 affects coil 2 exactly as much as coil 2 affects coil 1. Like capacitance, $M$ depends only on **geometry** (shape, size, number of turns, and how close the coils are).*

### Self-Inductance
A single coil with $N$ turns carrying current $i$ has a self-inductance:
$$ L = \frac{N \Phi_B}{i} $$
When the current changes, the coil induces a **back EMF** in itself:
$$ \mathcal{E} = -L \frac{di}{dt} $$
*(The minus sign is Lenz's Law: the induced EMF always opposes the **change** in current, not the current itself.)*

**Inductor Sign Convention (for Kirchhoff's Loop Rule):**
Walking through an inductor in the direction of the current, the potential change is:
$$ \Delta V = -L \frac{di}{dt} $$
- Current **increasing** ($\frac{di}{dt} > 0$): the inductor acts like a battery pushing **against** the current (potential drops).
- Current **decreasing** ($\frac{di}{dt} < 0$): the inductor acts like a battery pushing **with** the current (potential rises).

**Self-Inductance of a Solenoid / Toroid:**
Using $B = \mu_0 n I$ from [[Sources of Magnetic Field]] (where $n = N/l$):
$$ L = \frac{\mu_0 N^2 A}{l} \quad \text{(solenoid of length } l \text{, area } A\text{)} $$
$$ L = \frac{\mu_0 N^2 A}{2\pi r} \quad \text{(toroid with average radius } r\text{)} $$
*(Inductance grows with $N^2$: doubling the number of turns quadruples the inductance. Stuffing an iron core inside multiplies it further by the relative permeability $K_m$.)*

### Magnetic Field Energy
It takes work to build up current in an inductor against its back EMF. That energy is stored in the inductor's **magnetic field**:
$$ U = \frac{1}{2} L I^2 $$
*(Compare this to a capacitor's $U = \frac{1}{2}CV^2$ from [[Capacitance and Dielectrics]]. Capacitors store energy in **electric** fields, and inductors store energy in **magnetic** fields.)*

**Magnetic Energy Density:**
$$ u = \frac{B^2}{2\mu_0} $$
*(The magnetic twin of the electric energy density $u = \frac{1}{2}\varepsilon_0 E^2$ from [[Capacitors]]. Wherever there's a $\vec{B}$ field, there's stored energy.)*

### R-L Circuits
An inductor in series with a resistor means current can't jump to its final value instantly. Instead, it rises (or decays) **exponentially**, just like the charge in an R-C circuit (see [[Direct-Current Circuits]]).

**Time Constant ($\tau$):**
$$ \tau = \frac{L}{R} $$
- **Units**: seconds.
- After one time constant, the current has reached about **63%** of its final value (or decayed to about **37%**).

**Current Growth** (battery $\mathcal{E}$ switched on at $t = 0$):
$$ i(t) = \frac{\mathcal{E}}{R}\left(1 - e^{-(R/L)t}\right) $$

**Current Decay** (battery removed, starting with current $I_0$):
$$ i(t) = I_0 \, e^{-(R/L)t} $$

**Quick Intuition:**
- At $t = 0$ (just after switching on), the inductor acts like a **broken wire**: it blocks the sudden change, so $i = 0$.
- At $t \to \infty$ (steady state), the inductor acts like a **plain wire**: the current is constant, so there's no back EMF.
*(This is the exact **opposite** of a capacitor!)*

**Connection to Calculus:**
Applying the loop rule gives a separable differential equation. For current growth:
$$ \mathcal{E} - iR - L\frac{di}{dt} = 0 \quad \Rightarrow \quad \frac{di}{dt} = \frac{\mathcal{E}}{L} - \frac{R}{L}i $$

| | R-C Circuit | R-L Circuit |
|---|---|---|
| **Time Constant** | $\tau = RC$ | $\tau = L/R$ |
| **At $t = 0$** | Capacitor = plain wire | Inductor = broken wire |
| **At $t \to \infty$** | Capacitor = broken wire | Inductor = plain wire |
| **Stores Energy In** | Electric field, $\frac{1}{2}CV^2$ | Magnetic field, $\frac{1}{2}LI^2$ |

### L-C Circuits (Electrical Oscillations)
Connect a charged capacitor to an inductor (with no resistor) and the energy **sloshes back and forth** forever:
1. The capacitor discharges, pushing current through the inductor. Energy moves from the **electric field** into the **magnetic field**.
2. Once the capacitor is empty, the inductor keeps the current flowing (it resists the change!), recharging the capacitor with the **opposite** polarity.
3. The process reverses and repeats.

This is the electrical version of a mass on a spring (see [[Oscillatory Motion]]). The loop rule gives the simple harmonic motion equation:
$$ \frac{d^2q}{dt^2} + \frac{1}{LC}q = 0 $$
**Solution:**
$$ q(t) = Q\cos(\omega t + \phi) $$
**Angular Frequency:**
$$ \omega = \frac{1}{\sqrt{LC}} $$

**Energy Conservation:**
The total energy is constant, just traded between the two components:
$$ \frac{1}{2}Li^2 + \frac{q^2}{2C} = \frac{Q^2}{2C} $$

| Mass-Spring System | L-C Circuit |
|---|---|
| Displacement $x$ | Charge $q$ |
| Velocity $v$ | Current $i$ |
| Mass $m$ | Inductance $L$ |
| Spring constant $k$ | $1/C$ |
| $\omega = \sqrt{k/m}$ | $\omega = 1/\sqrt{LC}$ |
| Kinetic energy $\frac{1}{2}mv^2$ | Magnetic energy $\frac{1}{2}Li^2$ |
| Spring potential energy $\frac{1}{2}kx^2$ | Electric energy $\frac{q^2}{2C}$ |

### L-R-C Series Circuits (Damped Oscillations)
Real circuits always have some resistance, which turns energy into heat every cycle. So the oscillations slowly **die out**, just like a mass on a spring with friction:
$$ L\frac{d^2q}{dt^2} + R\frac{dq}{dt} + \frac{1}{C}q = 0 $$
For small resistance (**underdamped**), the charge oscillates with shrinking amplitude:
$$ q(t) = A e^{-(R/2L)t}\cos(\omega' t + \phi) \qquad \omega' = \sqrt{\frac{1}{LC} - \frac{R^2}{4L^2}} $$

**Three Damping Cases:**
- **Underdamped** ($R^2 < 4L/C$): oscillates while slowly dying out.
- **Critically Damped** ($R^2 = 4L/C$): returns to zero as fast as possible with no oscillation.
- **Overdamped** ($R^2 > 4L/C$): slowly creeps back to zero with no oscillation.

### Related
- [[Faraday-Lenz Law]]
- [[Sources of Magnetic Field]]
- [[Magnetic Field and Magnetic Forces]]
- [[Direct-Current Circuits]]
- [[Capacitors]]
- [[Capacitance and Dielectrics]]
- [[Oscillatory Motion]]

#physics #electromagnetism #circuits #magnetism
