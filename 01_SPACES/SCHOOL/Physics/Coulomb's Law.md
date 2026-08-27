### Idea
**Coulomb's Law** is the fundamental principle of electrostatics. It quantifies the amount of electrostatic force between two electrically charged particles. 

The core intuition is simple: **Like charges repel, and opposite charges attract.** 
The force between two charges is directly proportional to the amount of charge they have, and it gets exponentially weaker the further apart they are (following an inverse-square law, much like gravity).

### Formally
The magnitude of the electrostatic force $F$ between two point charges is given by:
$$
F = k \frac{|q_1 q_2|}{r^2}
$$

To describe it as a vector field indicating direction (where a positive force indicates repulsion and a negative force indicates attraction), we use the vector form:
$$
\vec{F} = k \frac{q_1 q_2}{r^2} \hat{r}
$$

**Variables:**
- **$\vec{F}$**: Electrostatic force (measured in Newtons, $N$).
- **$q_1, q_2$**: The quantities of the two charges (measured in Coulombs, $C$).
- **$r$**: The distance between the centers of the two charges (measured in meters).
- **$\hat{r}$**: The unit vector pointing from one charge to the other.
- **$k$**: Coulomb's constant, $k \approx 8.99 \times 10^9 \, \text{N}\cdot\text{m}^2/\text{C}^2$. 
  *(Note: $k$ is often expanded as $k = \frac{1}{4\pi\varepsilon_0}$, where $\varepsilon_0$ is the permittivity of free space).*

### The Superposition Principle
Coulomb's Law technically only calculates the force between *two* isolated charges. If you have a system of three or more charges, you must use the **Principle of Superposition**. 
This principle states that the net force on any specific charge is simply the **vector sum** of all the individual forces acting upon it from the surrounding charges:
$$ \vec{F}_{net} = \vec{F}_1 + \vec{F}_2 + \dots + \vec{F}_n $$
*(You cannot just add the magnitudes; you must break them into $x$ and $y$ components and add the vectors!)*

### Example
**If two electrons are separated by a distance of $1 \text{ nm}$ ($1 \times 10^{-9} \text{ m}$), what is the repulsive force between them?**

1. Identify the charge of an electron: $q_1 = q_2 = -1.6 \times 10^{-19} \text{ C}$.
2. Plug into the magnitude formula:
   $$ F = (8.99 \times 10^9) \frac{|(-1.6 \times 10^{-19})(-1.6 \times 10^{-19})|}{(1 \times 10^{-9})^2} $$
   $$ F = (8.99 \times 10^9) \frac{2.56 \times 10^{-38}}{1 \times 10^{-18}} $$
   $$ F \approx 2.3 \times 10^{-10} \text{ N} $$
This might seem like a tiny force, but because the mass of an electron is so incredibly small, this force results in an absolutely massive acceleration!

### Related
- [[Electric Fields]] (coming soon)
- [[Conservative Vector Fields]] (The electrostatic force field is conservative, meaning it is path-independent and has a potential function!)

#physics #electromagnetism
