### Idea
Just like electric charges create an [[Electric Fields|Electric Field]], **moving** charges create a **Magnetic Field** ($\vec{B}$). And just like an electric field pushes on charges, a magnetic field pushes on **moving** charges.

That word *moving* is the big difference. A magnetic field completely ignores a charge sitting still. It only acts on charges in motion, and it pushes them **sideways**, perpendicular to both the field and the direction they're moving.

Some key differences from electricity:
- **No magnetic monopoles.** Every magnet has a North and a South pole. Cut a bar magnet in half and you just get two smaller magnets, each with its own N and S. You can never isolate a lone "north charge."
- **Field lines form closed loops.** Outside a magnet they run from N to S, and inside the magnet they continue from S back to N. They never start or stop anywhere.

### Formally: The Magnetic Force on a Moving Charge
A charge $q$ moving with velocity $\vec{v}$ through a magnetic field $\vec{B}$ feels a force given by a [[Vectors In Physics|cross product]]:
$$ \vec{F} = q\vec{v} \times \vec{B} $$
**Magnitude:**
$$ F = |q| v B \sin\phi $$
*(Where $\phi$ is the angle between $\vec{v}$ and $\vec{B}$.)*

- **Units**: The magnetic field is measured in **Tesla (T)**, where $1 \text{ T} = 1 \ \text{N}/(\text{A}\cdot\text{m})$.
- *Note: 1 Tesla is a strong field. Earth's magnetic field is only about $5 \times 10^{-5}$ T, so the smaller unit **Gauss** is also common ($1 \text{ G} = 10^{-4} \text{ T}$).*

**Key Consequences:**
1. If $\vec{v}$ is **parallel** to $\vec{B}$ ($\phi = 0^\circ$ or $180^\circ$), the force is **zero**.
2. The force is **maximum** when $\vec{v} \perp \vec{B}$ ($\phi = 90^\circ$).
3. The force is always **perpendicular to the velocity**, so **magnetic forces do no work**. They can change a particle's *direction* but never its *speed* or [[Work and Energy|kinetic energy]].

**Right-Hand Rule:**
Point your fingers along $\vec{v}$, curl them toward $\vec{B}$, and your thumb points along $\vec{F}$ for a **positive** charge. For a **negative** charge (like an electron), flip the direction.

**Diagram Notation:**
- $\odot$ (dot) = field pointing **out of** the page (like the tip of an arrow coming at you)
- $\otimes$ (cross) = field pointing **into** the page (like the tail feathers of an arrow flying away)

### Magnetic Flux and Gauss's Law for Magnetism
**Magnetic Flux ($\Phi_B$)** measures how much magnetic field passes through a surface, just like electric flux:
$$ \Phi_B = \int \vec{B} \cdot d\vec{A} \quad \text{(uniform field: } \Phi_B = BA\cos\phi \text{)} $$
- **Units**: **Webers (Wb)**, where $1 \text{ Wb} = 1 \ \text{T}\cdot\text{m}^2$.

Because there are no magnetic monopoles, every field line that enters a closed surface must also leave it. So the net magnetic flux through **any** closed surface is always zero:
$$ \oint \vec{B} \cdot d\vec{A} = 0 $$
*(Compare to [[Gauss's Law]] for electricity, where the right side is $Q_{enc}/\varepsilon_0$. For magnetism, there's no "enclosed magnetic charge" to put there.)*

### Motion of Charged Particles in a Magnetic Field
When a charged particle moves **perpendicular** to a uniform magnetic field, the magnetic force acts as a centripetal force, so the particle moves in a perfect circle (see [[Circular Motion]]).

Setting the magnetic force equal to the centripetal force:
$$ |q|vB = \frac{mv^2}{R} $$
**Radius of the orbit:**
$$ R = \frac{mv}{|q|B} $$
**Angular speed (cyclotron frequency):**
$$ \omega = \frac{v}{R} = \frac{|q|B}{m} $$
*(Notice $\omega$ doesn't depend on speed! Faster particles move in bigger circles, but they all complete a lap in the same time. This is the principle behind the **cyclotron** particle accelerator.)*

**Helical Motion:**
If the velocity has a component **parallel** to $\vec{B}$, that part is unaffected, so the particle drifts along the field while circling around it, tracing out a **helix** (a spring shape).

### Applications: Crossed Fields
**Velocity Selector:**
Set up an electric field and a magnetic field perpendicular to each other so their forces on a moving charge point in opposite directions. Only particles with exactly the right speed feel zero net force and pass straight through:
$$ qE = qvB \quad \Rightarrow \quad v = \frac{E}{B} $$

**Mass Spectrometer:**
Send particles through a velocity selector (so they all have the same $v$), then into a pure magnetic field. Since $R = \frac{mv}{|q|B}$, heavier particles curve in wider circles, which lets you sort atoms by mass.

### Magnetic Force on a Current-Carrying Wire
A current is just a bunch of moving charges, so a wire carrying current through a magnetic field feels a force:
$$ \vec{F} = I\vec{L} \times \vec{B} $$
**Magnitude:**
$$ F = ILB\sin\phi $$
*(Where $\vec{L}$ points along the wire in the direction of the current, and $L$ is the length of wire inside the field.)*

For a curved wire or non-uniform field, break it into tiny pieces and integrate:
$$ d\vec{F} = I \, d\vec{l} \times \vec{B} $$

### Force and Torque on a Current Loop
Put a loop of current in a uniform magnetic field and the **net force is zero** (the forces on opposite sides cancel out), but there **is** a net [[Torque]] that tries to twist the loop.

**Magnetic Dipole Moment ($\vec{\mu}$):**
$$ \mu = IA $$
*(Where $A$ is the loop's area. The direction of $\vec{\mu}$ is perpendicular to the loop, found by curling your right-hand fingers along the current; your thumb points along $\vec{\mu}$. For $N$ turns of wire, $\mu = NIA$.)*

**Torque on the Loop:**
$$ \vec{\tau} = \vec{\mu} \times \vec{B} \qquad \tau = \mu B \sin\phi $$

**Potential Energy:**
$$ U = -\vec{\mu} \cdot \vec{B} = -\mu B\cos\phi $$
- **Lowest energy** (stable): $\vec{\mu}$ lines up **with** $\vec{B}$.
- **Highest energy** (unstable): $\vec{\mu}$ points **against** $\vec{B}$.

*(These equations look just like the electric dipole equations $\vec{\tau} = \vec{p} \times \vec{E}$ and $U = -\vec{p}\cdot\vec{E}$ from [[Dipole Moment]]. A current loop is the magnetic version of an electric dipole.)*

**Application, the DC Motor:**
The torque on a current loop is what spins an electric motor. A device called a **commutator** flips the current direction every half turn so the torque keeps pushing the loop the same way around.

### The Hall Effect
When a current flows through a conductor sitting in a magnetic field, the magnetic force pushes the moving charges toward one side of the conductor. Charge builds up on that side, creating a small measurable voltage across the conductor's width, called the **Hall voltage**.
- The **sign** of the Hall voltage reveals whether the charge carriers are positive or negative. (This is how we first confirmed that the charge carriers in metals are electrons!)
- The **size** of the Hall voltage can be used to measure magnetic field strength or the charge carrier density $n$.

### Related
- [[Sources of Magnetic Field]]
- [[Electric Fields]]
- [[Dipole Moment]]
- [[Torque]]
- [[Circular Motion]]
- [[Gauss's Law]]
- [[Vectors In Physics]]
- [[Current, Resistance, and Electromotive Force]]

#physics #electromagnetism #magnetism
