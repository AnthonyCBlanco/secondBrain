### Idea
A **Capacitor** is an electronic component designed to store electric charge and electrical potential energy. The most basic design (a parallel-plate capacitor) consists of two conductive metal plates separated by a small gap. When connected to a battery, one plate fills with positive charge and the other with negative charge, creating a strong uniform [[Electric Fields|Electric Field]] between them.

### Formally: Capacitance
**Capacitance ($C$)** is a measure of how much charge a capacitor can store per unit of voltage. 
$$ C = \frac{Q}{V} \quad \text{or} \quad Q = CV $$
- **Units**: Capacitance is measured in **Farads (F)**, which is equivalent to one Coulomb per Volt. 
- *Note: A 1-Farad capacitor is monstrously huge. Most electronics use microfarads ($\mu\text{F}$) or picofarads ($\text{pF}$).*

**For a Parallel-Plate Capacitor:**
The capacitance depends entirely on the physical geometry of the plates, not the battery attached to it:
$$ C = \varepsilon_0 \frac{A}{d} $$
*(Where $A$ is the area of the plates, and $d$ is the distance between them. Bigger plates or a smaller gap = more capacitance).*

### Energy Stored in a Capacitor
The work done by the battery to push charges onto the plates is stored as potential energy ($U$) inside the electric field between the plates:
$$ U = \frac{1}{2} C V^2 = \frac{Q^2}{2C} $$

### Dielectrics (The Dipole Moment Hack)
Instead of leaving the gap between the plates empty, engineers stuff it with an insulating material called a **Dielectric** (like plastic, glass, or ceramic). Why? It dramatically increases the capacitance!

Here is how it works:
1. The insulating material is full of molecules that act like tiny electric dipoles (see [[Dipole Moment]]).
2. When the capacitor charges up, the main electric field forces all these tiny molecular dipoles to twist and align themselves.
3. This alignment creates a secondary, internal electric field that points in the *opposite* direction, partially cancelling out the main electric field.
4. Because the overall electric field is weakened, the [[Electric Potential|Voltage]] between the plates drops ($V = Ed$).
5. Since $C = Q/V$, a massive drop in voltage means the capacitor can now hold significantly more charge for the same battery!

**Dielectric Formula:**
If you insert a dielectric into a capacitor, the new capacitance is multiplied by a dimensionless number called the **dielectric constant ($\kappa$)**:
$$ C = \kappa C_0 $$
*(For a vacuum, $\kappa = 1$. For water, $\kappa \approx 80$, meaning it can hold 80x more charge!)*

### Related
- [[Electric Potential]]
- [[Electric Fields]]
- [[Dipole Moment]]

#physics #electromagnetism #circuits
