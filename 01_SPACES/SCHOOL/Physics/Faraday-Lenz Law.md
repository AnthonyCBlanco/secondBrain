### Idea
We already know from [[Sources of Magnetic Field]] that a moving charge (a current) creates a [[Magnetic Field and Magnetic Forces|Magnetic Field]]. **Faraday's Law** asks the reverse question: *can a magnetic field create a current?*

Hold a magnet still next to a coil of wire and nothing happens, no matter how strong the magnet is. Move the magnet, though, and current suddenly flows! The secret is **change**. A steady magnetic field does nothing to a circuit, but a **changing magnetic flux** through a loop creates an [[Current, Resistance, and Electromotive Force|Electromotive Force (EMF)]] that pushes charges around the loop.

**Lenz's Law** tells us *which way* that induced current flows: nature hates change, so **the induced current always fights the change in magnetic flux that caused it**. Together, they form the **Faraday-Lenz Law**, the third of Maxwell's four equations and the principle behind almost every power plant, generator, transformer, and wireless charger on Earth.

### Formally: Magnetic Flux and Faraday's Law
First, the **Magnetic Flux ($\Phi_B$)** through an open surface $S$ measures how much magnetic field pierces through it ( via a [[Surface Integrals|surface integral]]):
$$ \Phi_B = \iint_S \vec{B} \cdot d\vec{A} \quad \text{(for a flat loop in a uniform field: } \Phi_B = BA\cos\theta \text{)} $$
- **Units**: **Webers (Wb)**, where $1 \text{ Wb} = 1 \ \text{T}\cdot\text{m}^2$.
- $\theta$ is the angle between $\vec{B}$ and the **normal vector** $\vec{A}$ perpendicular to the loop's face ($\theta = 0^\circ$ when $\vec{B}$ points straight through the loop).

**The Faraday-Lenz Law:**
Whenever the magnetic flux through a loop changes with time, an EMF ($\mathcal{E}$) is induced around the loop:
$$ \mathcal{E} = -\frac{d\Phi_B}{dt} $$
For a tightly wound coil of $N$ turns, each turn gets the same flux change, so their EMFs add up:
$$ \mathcal{E} = -N\frac{d\Phi_B}{dt} $$
If the loop is a closed conductor with resistance $R$, this induced EMF drives an **induced current**:
$$ I_{\text{ind}} = \frac{|\mathcal{E}|}{R} = \frac{N}{R}\left|\frac{d\Phi_B}{dt}\right| $$

**Three Ways to Change the Flux ($\Phi_B = BA\cos\theta$):**
1. **Change $B(t)$**: Crank the magnetic field strength up or down, or move a magnet closer to / farther from the loop.
2. **Change $A(t)$**: Stretch, shrink, or slide the loop into or out of the field.
3. **Change $\theta(t)$**: Rotate the loop inside the field (this is how **AC generators** spin mechanical work into electricity!).

### Lenz's Law (The Minus Sign)
The minus sign in $\mathcal{E} = -\frac{d\Phi_B}{dt}$ is **Lenz's Law**:
> An induced current always flows in the direction that creates an **induced magnetic field ($\vec{B}_{\text{ind}}$)** opposing the *change* in magnetic flux through the loop.

*(Careful: it opposes the **change** in flux, $\Delta \Phi_B$, not the original magnetic field itself!)*

**4-Step Recipe for Finding the Direction of Induced Current:**
1. **Find the direction of the external $\vec{B}$** piercing the loop (e.g., into the page $\otimes$ or out of the page $\odot$).
2. **Ask how the flux $\Phi_B$ is changing:** is it **increasing** or **decreasing**?
3. **Determine the direction of $\vec{B}_{\text{ind}}$:**
   - If $\Phi_B$ is **increasing**, $\vec{B}_{\text{ind}}$ points **opposite** to $\vec{B}$ to fight the increase.
   - If $\Phi_B$ is **decreasing**, $\vec{B}_{\text{ind}}$ points **in the same direction** as $\vec{B}$ to prop it back up.
4. **Use the Right-Hand Rule:** Point your right thumb along $\vec{B}_{\text{ind}}$, and your fingers curl in the direction of the **induced current**.

**Why Lenz's Law Must Be True:**
It's really [[Conservation of Energy]] in disguise. If the induced current helped the flux grow instead of fighting it, that extra flux would induce even more current, which would create even more flux, giving you a runaway explosion of free energy from a tiny nudge.

### Motional EMF
Instead of changing the magnetic field, you can induce an EMF by moving a conductor through a steady magnetic field $\vec{B}$.

**Moving Rod:**
Picture a metal rod of length $L$ sliding at speed $v$ perpendicular to a uniform magnetic field $B$.
1. The free charges inside the rod move with it, so they feel a magnetic force $\vec{F}_B = q\vec{v} \times \vec{B}$ pushing positive charges to one end of the rod and negative charges to the other.
2. That charge separation creates an internal [[Electric Fields|Electric Field]] $E$ along the rod until the electric force $qE$ balances the magnetic force $qvB$, giving $E = vB$.
3. The potential difference (motional EMF) between the ends of the rod is:
$$ \mathcal{E} = vBL $$

**Sliding Bar on Conducting Rails:**
If that rod slides along U-shaped rails with total resistance $R$, the loop area grows at rate $\frac{dA}{dt} = Lv$, so Faraday's Law gives the exact same result:
$$ |\mathcal{E}| = \frac{d\Phi_B}{dt} = B\frac{dA}{dt} = BLv \quad \Rightarrow \quad I = \frac{BLv}{R} $$
Because the induced current flows through a magnetic field, the bar feels a magnetic drag force $\vec{F} = I\vec{L} \times \vec{B}$ pointing **opposite to its velocity**:
$$ F_{\text{drag}} = ILB = \frac{B^2 L^2 v}{R} $$
*(To keep the bar moving at constant speed $v$, you have to pull it with force $F_{\text{drag}}$, and the mechanical power you put in, $P = Fv = \frac{B^2L^2v^2}{R}$, equals the electrical power $I^2R$ dissipated as heat in the resistor!)*

**General Motional EMF:**
For any conductor moving with velocity $\vec{v}$ through a magnetic field $\vec{B}$:
$$ \mathcal{E} = \oint (\vec{v} \times \vec{B}) \cdot d\vec{l} $$

### Induced Electric Fields (General Form of Faraday's Law)
What if there's no wire loop at all, just empty space where $\vec{B}$ is changing? Faraday's Law says an EMF is *still* induced! That means a changing magnetic field creates an **induced Electric Field ($\vec{E}_{\text{ind}}$)** that swirls in closed loops, even in a vacuum.

Since EMF is the [[Line Integrals|line integral]] of the electric field around a closed path, the full Maxwell-equation form of Faraday's Law is:
$$ \oint_{\partial S} \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt} \iint_S \vec{B} \cdot d\vec{A} $$

**Differential Form:**
Applying [[Stokes' Theorem]] turns the line integral into the [[Divergence and Curl|curl]] of $\vec{E}$:
$$ \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t} $$

**Electrostatic vs. Induced Electric Fields:**
This induced electric field behaves very differently from the electrostatic field of stationary charges:

| Property | Electrostatic $\vec{E}$ (from charges) | Induced $\vec{E}$ (from changing $\vec{B}$) |
|---|---|---|
| **Source** | Electric charges ($\nabla \cdot \vec{E} = \rho/\varepsilon_0$) | Changing magnetic field ($\nabla \times \vec{E} = -\partial\vec{B}/\partial t$) |
| **Field Lines** | Start on $+$ charges, end on $-$ charges | Form continuous **closed loops** (no start or end) |
| **Conservative?** | **Yes** ([[Conservative Vector Fields|conservative]]): $\oint \vec{E}\cdot d\vec{l} = 0$ | **No** (non-conservative): $\oint \vec{E}\cdot d\vec{l} = -\frac{d\Phi_B}{dt}$ |
| **Electric Potential $V$** | Well-defined ($V_B - V_A$ is path-independent) | Not well-defined around a loop (work depends on path) |

**Cylindrical Symmetry Shortcut:**
Inside a long solenoid of radius $R$ whose uniform field $B(t)$ is changing, the induced electric field lines are circles concentric with the solenoid. By symmetry, $\oint \vec{E}\cdot d\vec{l} = E(2\pi r)$, giving:
- **Inside ($r < R$):** $E(2\pi r) = \pi r^2 \left|\frac{dB}{dt}\right| \implies E = \frac{r}{2}\left|\frac{dB}{dt}\right|$ *(grows linearly with $r$)*
- **Outside ($r > R$):** $E(2\pi r) = \pi R^2 \left|\frac{dB}{dt}\right| \implies E = \frac{R^2}{2r}\left|\frac{dB}{dt}\right|$ *(falls off as $1/r$)*

### Generators and Back EMF
**AC Generator:**
A coil of $N$ turns and area $A$ spinning at constant angular speed $\omega$ inside a uniform magnetic field $B$ has angle $\theta(t) = \omega t$. Its flux is $\Phi_B = BA\cos(\omega t)$, so Faraday's Law gives a sinusoidal alternating EMF:
$$ \mathcal{E}(t) = -N\frac{d\Phi_B}{dt} = NBA\omega \sin(\omega t) $$

**Eddy Currents and Magnetic Braking:**
When a solid piece of metal moves through a magnetic field (or a magnet moves past a conductor like a copper plate), the changing flux induces swirling whirlpools of current inside the metal called **eddy currents**.
- By Lenz's Law, these eddy currents create a magnetic field that **opposes the motion**, producing a smooth, contactless braking force (**magnetic braking**, used in trains, roller coasters, and gym equipment).
- Eddy currents also dissipate energy as heat ($I^2R$), which is how **induction stoves** heat up metal pots without a flame. To *prevent* wasted heat in transformers and motors, iron cores are built from thin insulated sheets (**laminations**) that block large eddy-current loops.

### Related
- [[Inductance]]
- [[Magnetic Field and Magnetic Forces]]
- [[Sources of Magnetic Field]]
- [[Current, Resistance, and Electromotive Force]]
- [[Electric Fields]]
- [[Gauss's Law]]
- [[Conservation of Energy]]
- [[Surface Integrals]]
- [[Line Integrals]]
- [[Stokes' Theorem]]
- [[Divergence and Curl]]
- [[Conservative Vector Fields]]
- [[Thursday November 2nd|Chapter 29 Lecture Notes]]

#physics #electromagnetism #magnetism
