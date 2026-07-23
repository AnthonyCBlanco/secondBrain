### Idea
While a [[Double Integral]] calculates the volume under a 2D surface, a **Triple Integral** evaluates a function $f(x, y, z)$ over a 3D solid region $E$. 

Conceptually, this calculates a 4-dimensional "hypervolume," which is hard to visualize. However, practically, it is extremely useful in physics and engineering. For example, if $f(x, y, z)$ represents the density of a solid at any given point, the triple integral gives you the total **mass** of the solid.

If the function being integrated is simply $f(x, y, z) = 1$, then the triple integral calculates the **volume** of the 3D region $E$.

### Formally
The triple integral of a function $f(x, y, z)$ over a solid region $E$ is denoted as:
$$
\iiint_E f(x, y, z) \, dV
$$
Here, $dV$ represents a tiny element of volume. In standard rectangular coordinates, $dV = dx \, dy \, dz$ (or any combination thereof).

### Evaluating Triple Integrals: Fubini's Theorem
To compute a triple integral, we evaluate it as an **iterated integral**. If $f$ is continuous on a rectangular solid box $E = [a, b] \times [c, d] \times [r, s]$ (meaning $a \le x \le b$, $c \le y \le d$, and $r \le z \le s$), you can integrate in any order (there are $3! = 6$ possible orders).

$$
\iiint_E f(x, y, z) \, dV = \int_r^s \int_c^d \int_a^b f(x, y, z) \, dx \, dy \, dz
$$
*Remember to evaluate from the inside out.*

### Integrating Over General Solid Regions
When the region $E$ is not a simple rectangular box, the bounds of the inner integrals will be functions of the outer variables.

The most common approach is a **Type 1 Solid Region**, where the solid is bounded above and below by two surfaces, $z = u_2(x, y)$ and $z = u_1(x, y)$, and its projection onto the $xy$-plane is a 2D region $D$.
You evaluate $z$ first, and then evaluate the remaining [[Double Integral|double integral]] over the 2D region $D$:
$$
\iiint_E f(x, y, z) \, dV = \iint_D \left[ \int_{u_1(x, y)}^{u_2(x, y)} f(x, y, z) \, dz \right] dA
$$
The remaining $dA$ can then be integrated as $dx \, dy$ or $dy \, dx$ just like a normal [[Double Integral|double integral]].

### Alternative Coordinate Systems
Just as double integrals are sometimes easier in polar coordinates, triple integrals over spherical or cylindrical regions are often easier to evaluate using different coordinate systems. You must swap the volume element $dV$:

1. **Cylindrical Coordinates:** (Great for cylinders, cones, or symmetry around the z-axis)
   $x = r \cos \theta$, $y = r \sin \theta$, $z = z$
   **$dV = r \, dz \, dr \, d\theta$**

2. **Spherical Coordinates:** (Great for spheres or cones originating at the origin)
   $x = \rho \sin \phi \cos \theta$, $y = \rho \sin \phi \sin \theta$, $z = \rho \cos \phi$
   **$dV = \rho^2 \sin \phi \, d\rho \, d\theta \, d\phi$**

### Example
**Evaluate $\int_0^1 \int_0^2 \int_0^3 xyz \, dz \, dy \, dx$**

1. Evaluate the inner integral with respect to $z$ (treating $x$ and $y$ as constants):
   $$ \int_0^3 xyz \, dz = xy \left[ \frac{z^2}{2} \right]_0^3 = xy \left( \frac{9}{2} - 0 \right) = \frac{9}{2}xy $$
2. Substitute back and evaluate the middle integral with respect to $y$ (treating $x$ as a constant):
   $$ \int_0^2 \frac{9}{2}xy \, dy = \frac{9}{2}x \left[ \frac{y^2}{2} \right]_0^2 = \frac{9}{2}x \left( \frac{4}{2} \right) = \frac{9}{2}x (2) = 9x $$
3. Substitute back and evaluate the outer integral with respect to $x$:
   $$ \int_0^1 9x \, dx = \left[ \frac{9x^2}{2} \right]_0^1 = \frac{9}{2} $$

The result is $\frac{9}{2}$.

### Related
- [[Double Integral]]
- [[Definite Integrals]]

#math/calculus #summer2026
