**### Idea
Just as the [[Electric Fields|Electric Field]] ($\vec{E}$) represents the Force *per unit charge*, the **Electric Potential** ($V$) represents the Potential Energy *per unit charge*. 

Often referred to simply as **Voltage**, it tells us how much "work" would be required to move a positive test charge from infinitely far away and push it to a specific point inside an electric field. 

Think of electric potential like the "height" or "elevation" of a hill. The electric field is the steepness pushing you down, and the electric potential is how high up the hill you are.

### Formally
Electric Potential ($V$) is defined as the electric potential energy ($U$) divided by the test charge ($q_0$):
$$
V = \frac{U}{q_0}
$$
Because energy is measured in Joules and charge in Coulombs, Electric Potential is measured in **Joules per Coulomb (J/C)**, which is given the special name **Volts (V)**.

The electric potential created by a single point charge $q$ at a distance $r$ is:
$$
V = k \frac{q}{r}
$$

### The Superposition Principle (The Easy Way!)
Unlike Electric Force and Electric Fields, Electric Potential is a **scalar quantity** (it has no direction, just a number). 

This makes calculating the total potential of a system incredibly easy. If you have 5 charges, you don't need to break anything into $x$ and $y$ vectors! You simply calculate the potential for each charge and add them up like standard algebra:
$$ V_{net} = V_1 + V_2 + V_3 + \dots $$
*(Make sure to keep the negative signs for negative charges!)*

### Connection to Calculus
Because the electrostatic field is a [[Conservative Vector Fields|Conservative Vector Field]], the path you take to move a charge doesn't matter. You can calculate the difference in electric potential ($\Delta V$) between point A and point B by taking a [[Line Integrals|line integral]] of the electric field:
$$ \Delta V = V_B - V_A = -\int_A^B \vec{E} \cdot d\vec{r} $$

Conversely, if you already know the scalar potential function $V(x,y,z)$, you can easily find the Electric Field by taking the negative [[Gradient Vector|gradient]]:
$$ \vec{E} = -\nabla V $$
*(The negative sign simply means that the electric field always points "downhill", towards lower potential).*

### Equipotential Surfaces
An **Equipotential Surface** is a topographical map of the electric field. It is a line or surface where the electric potential is exactly the same everywhere.
1. **Zero Work**: Moving a charge anywhere along an equipotential line requires zero work (because $\Delta V = 0$).
2. **Perpendicularity**: Equipotential lines are always perfectly perpendicular ($90^\circ$) to Electric Field lines.

### Related
- [[Electric Fields]]
- [[Conservative Vector Fields]]
- [[Line Integrals]]
- [[Gradient Vector]]

#physics #electromagnetism
