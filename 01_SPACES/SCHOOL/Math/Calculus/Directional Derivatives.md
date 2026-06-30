### Idea
While partial derivatives measure the rate of change of a function strictly along the $x$-axis or $y$-axis, **Directional Derivatives** generalize this concept. They allow us to find the rate of change of a multivariable function $z = f(x, y)$ in **any** given direction.

If you are standing on a hilly surface (represented by $f(x, y)$), the directional derivative tells you the slope of the hill if you were to walk in a specific direction $\vec{v}$.

### Formally
The directional derivative of a function $f(x,y)$ at a point $(x_0, y_0)$ in the direction of a **unit vector** $\vec{u} = \langle a, b \rangle$ is denoted as $D_{\vec{u}}f(x_0, y_0)$ and is defined by the limit:
$$
D_{\vec{u}} f(x_0, y_0) = \lim_{h \to 0} \frac{f(x_0 + ah, y_0 + bh) - f(x_0, y_0)}{h}
$$

### Computation Using the Gradient
Using the limit definition is tedious. Thankfully, if $f$ is a differentiable function, we can compute the directional derivative easily using the **Gradient Vector** ($\nabla f$):

$$
D_{\vec{u}} f(x, y) = \nabla f(x, y) \cdot \vec{u}
$$

**Important Steps:**
1. Find the gradient vector: $\nabla f = \langle f_x, f_y \rangle$.
2. Ensure your direction vector is a **unit vector**. If you are given a vector $\vec{v}$ that is not a unit vector, you must normalize it: $\vec{u} = \frac{\vec{v}}{|\vec{v}|}$.
3. Take the dot product of the gradient and the unit vector.

### Example
**Find the directional derivative of $f(x, y) = x^2y$ at the point $(1, 2)$ in the direction of $\vec{v} = \langle 3, 4 \rangle$.**

1. **Find the gradient vector:**
   $f_x = 2xy$
   $f_y = x^2$
   $\nabla f(x,y) = \langle 2xy, x^2 \rangle$

2. **Evaluate the gradient at the point $(1, 2)$:**
   $\nabla f(1, 2) = \langle 2(1)(2), (1)^2 \rangle = \langle 4, 1 \rangle$

3. **Find the unit vector $\vec{u}$ for the given direction:**
   The magnitude of $\vec{v}$ is $|\vec{v}| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$.
   So, $\vec{u} = \frac{1}{5}\langle 3, 4 \rangle = \langle \frac{3}{5}, \frac{4}{5} \rangle$.

4. **Compute the dot product:**
   $$
   D_{\vec{u}} f(1, 2) = \nabla f(1, 2) \cdot \vec{u} = \langle 4, 1 \rangle \cdot \langle \frac{3}{5}, \frac{4}{5} \rangle
   $$
   $$
   D_{\vec{u}} f(1, 2) = 4\left(\frac{3}{5}\right) + 1\left(\frac{4}{5}\right) = \frac{12}{5} + \frac{4}{5} = \frac{16}{5}
   $$

### Properties of the Directional Derivative
Since $D_{\vec{u}} f = \nabla f \cdot \vec{u} = |\nabla f| |\vec{u}| \cos(\theta) = |\nabla f| \cos(\theta)$ (where $\theta$ is the angle between the gradient and the direction vector):
- **Maximum Rate of Change:** Occurs when $\theta = 0$ (moving in the exact same direction as the gradient). The maximum value is $|\nabla f|$.
- **Minimum Rate of Change:** Occurs when $\theta = \pi$ (moving in the exact opposite direction of the gradient). The minimum value is $-|\nabla f|$.
- **Zero Rate of Change:** Occurs when $\theta = \pi/2$ (moving perpendicular to the gradient, along a level curve).

#math/calculus #summer2026
