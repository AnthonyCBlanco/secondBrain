### Idea
The previous note covered what a magnetic field **does** to moving charges. This note covers where magnetic fields **come from**.

The answer is simple: **moving charges create magnetic fields.** That's it. Every magnetic field in the universe comes from moving charge, whether it's current flowing in a wire or the electrons spinning and orbiting inside the atoms of a fridge magnet.

The big picture:
- A **straight wire** carrying current creates a magnetic field that **circles around** the wire.
- A **loop** of wire bunches those circles together into a field that looks like a little bar magnet.
- Stack many loops into a **solenoid** (a coil) and you get a strong, uniform field inside: an **electromagnet**.

*(For the force a magnetic field exerts, see [[Magnetic Field and Magnetic Forces]].)*

### Formally: Field of a Moving Point Charge
A single point charge $q$ moving with velocity $\vec{v}$ creates a magnetic field at a distance $r$:
$$ \vec{B} = \frac{\mu_0}{4\pi} \frac{q\vec{v} \times \hat{r}}{r^2} $$
- $\mu_0 = 4\pi \times 10^{-7} \ \text{T}\cdot\text{m/A}$ is the **permeability of free space** (the magnetic version of $\varepsilon_0$).
- *Note: Like [[Coulomb's Law]], the field falls off as $1/r^2$. Unlike the electric field, it's **zero** directly ahead of or behind the charge (where $\vec{v} \parallel \hat{r}$), and it's strongest off to the sides.*

### The Biot-Savart Law
To find the field from a current, chop the wire into tiny segments $d\vec{l}$, find each one's contribution, and add them all up:
$$ d\vec{B} = \frac{\mu_0}{4\pi} \frac{I \, d\vec{l} \times \hat{r}}{r^2} $$
$$ \vec{B} = \frac{\mu_0}{4\pi} \int \frac{I \, d\vec{l} \times \hat{r}}{r^2} $$
*(This is the magnetic version of building up an electric field from tiny bits of charge $dq$. It always works, but the integral can be painful. When there's lots of symmetry, Ampère's Law is much easier.)*

### Field of a Long Straight Wire
Using Biot-Savart on an infinitely long straight wire:
$$ B = \frac{\mu_0 I}{2\pi r} $$
*(Where $r$ is the perpendicular distance from the wire. The field gets weaker as $1/r$, not $1/r^2$.)*

**Right-Hand Grip Rule:**
Grab the wire with your right hand, thumb pointing along the current. Your fingers curl in the direction of the magnetic field lines, which form **circles** around the wire.

### Force Between Two Parallel Wires
Each wire creates a magnetic field, and the other wire's current feels a force in that field. The force per unit length between two parallel wires a distance $r$ apart is:
$$ \frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi r} $$
- Currents in the **same** direction: wires **attract**.
- Currents in **opposite** directions: wires **repel**.
*(Opposite of electric charges, where like charges repel!)*

### Field of a Circular Current Loop
On the central axis of a loop of radius $a$, at a distance $x$ from its center:
$$ B_x = \frac{\mu_0 I a^2}{2(x^2 + a^2)^{3/2}} $$
**At the very center** of the loop ($x = 0$):
$$ B = \frac{\mu_0 I}{2a} \quad \text{(for } N \text{ turns: } B = \frac{\mu_0 N I}{2a} \text{)} $$
*(Far away from the loop, its field looks exactly like a bar magnet's. That's why a current loop is called a **magnetic dipole**, with dipole moment $\mu = IA$.)*

### Ampère's Law
For situations with lots of symmetry, **Ampère's Law** is the shortcut, the same way [[Gauss's Law]] is the shortcut for electric fields.

Pick any closed loop (called an **Amperian loop**). The [[Line Integrals|line integral]] of $\vec{B}$ around that loop equals $\mu_0$ times the current passing through it:
$$ \oint \vec{B} \cdot d\vec{l} = \mu_0 I_{encl} $$

**Strategy:**
1. Choose an Amperian loop that matches the symmetry, so $\vec{B}$ is either constant and parallel to the path, or perpendicular to it (contributing zero).
2. Then the integral simplifies to $B \times (\text{length of path})$.
3. Find the current passing through your loop, and solve for $B$.

**Sign Convention:** Curl your right-hand fingers along the direction you walk around the loop. Currents in the direction of your thumb count as **positive**, and currents the other way count as **negative**.

| | Gauss's Law (Electric) | Ampère's Law (Magnetic) |
|---|---|---|
| **Integral Over** | Closed surface | Closed loop |
| **Source** | Enclosed charge $Q_{encl}$ | Enclosed current $I_{encl}$ |
| **Equation** | $\oint \vec{E}\cdot d\vec{A} = \frac{Q_{encl}}{\varepsilon_0}$ | $\oint \vec{B}\cdot d\vec{l} = \mu_0 I_{encl}$ |

### Applications of Ampère's Law
**Long Straight Wire (re-derived the easy way):**
Use a circle of radius $r$ around the wire: $B(2\pi r) = \mu_0 I \Rightarrow B = \dfrac{\mu_0 I}{2\pi r}$ ✅

**Inside a Thick Wire (radius $R$, uniform current):**
Only the fraction of the current inside radius $r$ counts:
$$ B = \frac{\mu_0 I r}{2\pi R^2} \quad (r < R) $$
*(The field grows linearly from zero at the center, peaks at the surface, then falls off as $1/r$ outside.)*

**Solenoid (long coil):**
Inside a long solenoid, the field is strong and uniform. Outside, it's nearly zero:
$$ B = \mu_0 n I $$
*(Where $n = N/L$ is the number of turns per unit length.)*

**Toroid (donut-shaped coil):**
The field is trapped entirely inside the donut:
$$ B = \frac{\mu_0 N I}{2\pi r} $$
*(Where $N$ is the total number of turns and $r$ is the distance from the toroid's center.)*

### Magnetic Materials
Inside atoms, orbiting and spinning electrons act like tiny current loops (magnetic dipoles). How these tiny dipoles respond to an outside field determines the material's magnetic behavior:
- **Paramagnetic** (aluminum, oxygen): The dipoles weakly line up **with** the field, slightly strengthening it. They are weakly attracted to magnets.
- **Diamagnetic** (water, copper, bismuth): The field induces dipoles pointing **against** it, slightly weakening it. They are weakly repelled by magnets.
- **Ferromagnetic** (iron, nickel, cobalt): The dipoles **strongly** line up in groups called **magnetic domains**, which can make the field hundreds or thousands of times stronger. These materials can stay magnetized after the outside field is removed, which is how permanent magnets work.

In a material, $\mu_0$ is replaced by the material's permeability $\mu = K_m \mu_0$, where $K_m$ is the **relative permeability** (similar to the dielectric constant $\kappa$ in [[Capacitance and Dielectrics]]).

### Displacement Current
Ampère's Law has a problem: it fails for a charging [[Capacitors|capacitor]]. Current flows in the wires, but no current actually crosses the gap between the plates.

Maxwell's fix: a **changing electric field** also acts as a source of magnetic field, just like a real current. He called it the **displacement current**:
$$ i_D = \varepsilon_0 \frac{d\Phi_E}{dt} $$
This gives the complete **Ampère-Maxwell Law**:
$$ \oint \vec{B}\cdot d\vec{l} = \mu_0 \left( i_C + \varepsilon_0 \frac{d\Phi_E}{dt} \right) $$
*(This was the missing piece that led Maxwell to predict that light is an electromagnetic wave!)*

### Related
- [[Magnetic Field and Magnetic Forces]]
- [[Gauss's Law]]
- [[Coulomb's Law]]
- [[Electric Fields]]
- [[Line Integrals]]
- [[Capacitors]]
- [[Capacitance and Dielectrics]]
- [[Current, Resistance, and Electromotive Force]]

#physics #electromagnetism #magnetism
