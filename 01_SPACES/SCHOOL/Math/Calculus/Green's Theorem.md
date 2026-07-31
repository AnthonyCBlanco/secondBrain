### Idea
**Green's Theorem** is a fundamental theorem of calculus in 2D space. It creates a magical bridge between 1D [[Line Integrals]] (around a closed loop) and 2D [[Double Integral|Double Integrals]] (over the area enclosed by that loop).

Instead of tediously parameterizing a boundary curve to calculate work or flux, you can often just take a double integral over the inside shape!

### Requirements
To use Green's Theorem, your curve $C$ must be:
1. **Closed**: Starts and ends at the exact same point.
2. **Simple**: Does not cross over itself (no figure eights).
3. **Positively Oriented**: You must be traveling around the curve **counter-clockwise**. (Imagine walking along the curve; the enclosed region $D$ must always be on your left).

### The Two Forms of Green's Theorem
Green's Theorem has two different equations depending on what physical property you are trying to measure: Circulation or Flux.

#### 1. The Circulation (Curl) Form
This form relates the circulation of a vector field *around* the boundary $C$ to the sum of the microscopic rotation ([[Divergence and Curl|curl]]) everywhere *inside* the region $D$.
If $\vec{F} = \langle P, Q \rangle$:
$$ 
\oint_C \vec{F} \cdot d\vec{r} = \oint_C P \, dx + Q \, dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dA 
$$
*(Notice that the integrand on the right is exactly the 2D Curl!)*

#### 2. The Flux (Divergence) Form
This form relates the outward flux *across* the boundary $C$ to the sum of the microscopic expansion/compression ([[Divergence and Curl|divergence]]) everywhere *inside* the region $D$.
If $\vec{F} = \langle P, Q \rangle$:
$$ 
\oint_C \vec{F} \cdot \vec{n} \, ds = \oint_C P \, dy - Q \, dx = \iint_D \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} \right) dA 
$$
*(Notice that the integrand on the right is exactly the Divergence!)*

### Why is this useful?
Evaluating line integrals often requires nasty parameterizations containing sines and cosines. If the path is closed, you can instantly convert it into a double integral. Often, the resulting partial derivatives simplify the integrand dramatically, making it a trivial double integral to solve.

### Related
- [[Line Integrals]]
- [[Double Integral]]
- [[Flow and Flux]]
- [[Divergence and Curl]]

#math/calculus #summer2026
