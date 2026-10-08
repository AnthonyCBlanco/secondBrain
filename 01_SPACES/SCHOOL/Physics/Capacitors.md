### Idea
A **Capacitor** is basically a "charge bucket" for a circuit. It's made of two conductors (usually plates) separated by an insulator. Hook it up to a battery and the battery pulls electrons off one plate and piles them onto the other, leaving the plates with equal and opposite charges ($+Q$ and $-Q$). The capacitor holds that charge and its energy until the circuit lets it go.

Think of it like a water tower: the battery pumps water (charge) up into the tank, and the tank holds that "pressure" (voltage) until you open the valve and it all rushes out at once. That quick dump of energy is why capacitors power camera flashes, defibrillators, and smooth out power supplies.

*(For the basics of capacitance, energy storage, and dielectrics, see [[Capacitance and Dielectrics]].)*

### Formally
Every capacitor follows the same core relationship:
$$ C = \frac{Q}{\Delta V} $$
*(Where $Q$ is the charge on **one** plate and $\Delta V$ is the [[Electric Potential|potential difference]] between the plates. Measured in **Farads (F)**.)*

**The General Recipe for Finding $C$:**
Capacitance depends only on **geometry**. For any shape:
1. Pretend the conductors carry charge $+Q$ and $-Q$.
2. Use [[Gauss's Law]] to find the [[Electric Fields|Electric Field]] $\vec{E}$ between them.
3. Integrate to get the potential difference: $\Delta V = -\int \vec{E} \cdot d\vec{r}$
4. Divide: $C = Q / \Delta V$ (the $Q$ always cancels!)

### Common Capacitor Geometries
| Type | Capacitance | Variables |
|---|---|---|
| **Parallel-Plate** | $C = \dfrac{\varepsilon_0 A}{d}$ | $A$ = plate area, $d$ = gap |
| **Cylindrical** | $C = \dfrac{2\pi\varepsilon_0 L}{\ln(b/a)}$ | $L$ = length, $a$ = inner radius, $b$ = outer radius |
| **Spherical** | $C = 4\pi\varepsilon_0 \dfrac{ab}{b-a}$ | $a$ = inner radius, $b$ = outer radius |
| **Isolated Sphere** | $C = 4\pi\varepsilon_0 R$ | $R$ = radius (second "plate" is at infinity) |

*(Where $\varepsilon_0 = 8.85 \times 10^{-12} \ \text{C}^2/\text{N}\cdot\text{m}^2$ and $k = \frac{1}{4\pi\varepsilon_0}$.)*

**Example: Deriving the Parallel-Plate Formula**
- From Gauss's Law, the field between two large plates is uniform: $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{\varepsilon_0 A}$
- Potential difference across the gap: $\Delta V = Ed = \dfrac{Qd}{\varepsilon_0 A}$
- So: $C = \dfrac{Q}{\Delta V} = \dfrac{\varepsilon_0 A}{d}$ ✅

### Combining Capacitors
Capacitors combine the **opposite** way resistors do, so be careful not to mix them up!

**Parallel (side-by-side):**
- Every capacitor gets the **same voltage** ($\Delta V$).
- The charges add up: $Q_{total} = Q_1 + Q_2 + \dots$
$$ C_{eq} = C_1 + C_2 + C_3 + \dots $$
*(Parallel = effectively one giant plate with more area, so capacitance goes **up**.)*

**Series (end-to-end):**
- Every capacitor holds the **same charge** ($Q$), since charge can't leak through the gaps.
- The voltages add up: $\Delta V_{total} = \Delta V_1 + \Delta V_2 + \dots$
$$ \frac{1}{C_{eq}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \dots $$
*(Series = effectively one capacitor with a wider gap, so capacitance goes **down**. $C_{eq}$ is always smaller than the smallest capacitor.)*

**Shortcut for two in series:**
$$ C_{eq} = \frac{C_1 C_2}{C_1 + C_2} $$

### Energy Density
The energy in a capacitor actually lives **in the electric field** between the plates. Dividing the stored energy $U = \frac{1}{2}C(\Delta V)^2$ by the volume between the plates ($Ad$) gives the **energy density** ($u$):
$$ u = \frac{U}{\text{Volume}} = \frac{1}{2}\varepsilon_0 E^2 $$
*(This holds for **any** electric field, not just inside capacitors. Wherever there is an $\vec{E}$ field, there is stored energy.)*

### Problem-Solving Tips
1. **Battery connected?** Then $\Delta V$ stays **constant**. Changing the geometry changes $Q$.
2. **Battery disconnected?** Then $Q$ stays **constant** (the charge has nowhere to go). Changing the geometry changes $\Delta V$.
3. For complicated networks, collapse them step by step: combine the innermost series/parallel groups first, then work outward.
4. To find the charge or voltage on each capacitor, work **backwards** from the fully simplified $C_{eq}$.

### Related
- [[Capacitance and Dielectrics]]
- [[Electric Potential]]
- [[Electric Fields]]
- [[Gauss's Law]]
- [[Coulomb's Law]]

#physics #electromagnetism #circuits
