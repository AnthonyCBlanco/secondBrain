### Idea
So far, charges have mostly been sitting still (electrostatics). Now they **move**. When charges flow through a conductor, that flow is called **Electric Current**.

Think of a circuit like a water system:
- **Current ($I$)** is how much water flows past a point each second.
- **Voltage / EMF ($\mathcal{E}$)** is the pump that creates the pressure pushing the water around.
- **Resistance ($R$)** is how narrow or clogged the pipe is, which fights the flow.

A battery doesn't "create" charge. It acts as a **charge pump**, raising charges to a higher [[Electric Potential|potential]] so they can flow back down through the circuit and do useful work (light a bulb, spin a motor) along the way.

### Formally: Current
**Electric Current ($I$)** is the rate at which charge flows through a cross-sectional area:
$$ I = \frac{dQ}{dt} $$
- **Units**: **Amperes (A)**, where $1 \text{ A} = 1 \text{ C/s}$.
- **Conventional Current** points in the direction **positive** charges would move (from $+$ to $-$ outside the battery). In real metal wires, the electrons actually move the *opposite* way, but the math works out identically.

**Microscopic View (Drift Velocity):**
Electrons in a wire bounce around randomly at very high speeds, but an [[Electric Fields|Electric Field]] gives them a slow overall "drift" in one direction:
$$ I = n q v_d A $$
*(Where $n$ = number of charge carriers per volume, $q$ = charge per carrier, $v_d$ = drift velocity, $A$ = cross-sectional area.)*
- *Note: Drift velocity is shockingly slow, around $10^{-4}$ m/s! The light turns on instantly because the **field** travels through the wire at nearly the speed of light, pushing all the electrons at once.*

**Current Density ($\vec{J}$):** current per unit area.
$$ J = \frac{I}{A} = n q v_d $$

### Resistivity and Resistance
**Resistivity ($\rho$)** is a property of the **material** itself: how strongly it resists current.
$$ \rho = \frac{E}{J} $$
- **Units**: Ohm-meters ($\Omega \cdot \text{m}$).
- Conductors (copper, silver) have tiny $\rho$. Insulators (glass, rubber) have huge $\rho$.

**Resistance ($R$)** depends on the material **and** the shape of the wire:
$$ R = \frac{\rho L}{A} $$
*(Where $L$ is length and $A$ is cross-sectional area. Longer wire = more resistance, thicker wire = less resistance.)*

**Temperature Dependence:**
For most metals, resistivity increases as they heat up (atoms vibrate more and get in the electrons' way):
$$ \rho(T) = \rho_0 \left[ 1 + \alpha (T - T_0) \right] $$
*(Where $\alpha$ is the temperature coefficient of resistivity.)*

### Ohm's Law
The most important circuit equation:
$$ V = IR $$
- **Units**: Resistance is measured in **Ohms ($\Omega$)**, where $1 \ \Omega = 1 \text{ V/A}$.
- *Note: Ohm's Law isn't a universal law of nature. It only applies to **ohmic** materials, where $R$ stays constant. Diodes and light bulb filaments are **non-ohmic** (their $V$ vs. $I$ graph isn't a straight line).*

### Electromotive Force (EMF)
**EMF ($\mathcal{E}$)** is the energy per unit charge a source (battery, generator) supplies to push charge around the circuit. Despite the name, **it's not a force**. It's measured in **Volts**.

**Internal Resistance ($r$):**
Real batteries aren't perfect. The chemicals inside resist current a little bit, so some voltage is "lost" inside the battery itself. The voltage you actually measure across the battery's terminals is:
$$ V_{ab} = \mathcal{E} - Ir $$
- With **no current** flowing (open circuit), $V_{ab} = \mathcal{E}$.
- The more current you draw, the more the terminal voltage drops.

**Full Circuit with Internal Resistance:**
For a battery connected to an external resistor $R$:
$$ I = \frac{\mathcal{E}}{R + r} $$

### Energy and Power in Circuits
As charge flows "downhill" through a resistor, its potential energy is turned into heat (this is why wires and bulbs get hot). The **rate** of energy conversion is **Power ($P$)**:
$$ P = IV $$
For a resistor, plug in Ohm's Law to get the other two forms:
$$ P = I^2 R = \frac{V^2}{R} $$
- **Units**: **Watts (W)**, where $1 \text{ W} = 1 \text{ J/s}$.

**Power from a real battery:**
$$ P_{\text{delivered}} = \mathcal{E}I - I^2 r $$
*(The battery generates $\mathcal{E}I$, but wastes $I^2 r$ as heat on its own internal resistance.)*

### Related
- [[Direct-Current Circuits]]
- [[Electric Potential]]
- [[Electric Fields]]
- [[Capacitors]]
- [[Work and Energy]]

#physics #electromagnetism #circuits
