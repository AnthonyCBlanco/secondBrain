### Idea
The **Gradient Vector** (often just called the "gradient") is a fundamental concept in multivariable calculus. For a scalar function $f$, the gradient vector packages all of its [[Partial Derivative|partial derivatives]] into a single vector field. 

It is denoted by $\nabla f$ (read as "del f").

### Formally
For a function of two variables $f(x, y)$, the gradient vector is defined as:
$$
\nabla f(x, y) = \langle f_x(x, y), f_y(x, y) \rangle = \frac{\partial f}{\partial x} \hat{i} + \frac{\partial f}{\partial y} \hat{j}
$$

For a function of three variables $f(x, y, z)$, the gradient vector is:
$$
\nabla f(x, y, z) = \langle f_x, f_y, f_z \rangle = \frac{\partial f}{\partial x} \hat{i} + \frac{\partial f}{\partial y} \hat{j} + \frac{\partial f}{\partial z} \hat{k}
$$

### Key Geometric Properties
The gradient vector has several extremely important geometric meanings:
1. **Direction of Maximum Increase**: Evaluated at a specific point, $\nabla f$ points in the direction of the greatest rate of increase of the function.
2. **Maximum Rate of Change**: The magnitude of the gradient vector, $|\nabla f|$, is equal to that maximum rate of change.
3. **Direction of Maximum Decrease**: The negative gradient, $-\nabla f$, points in the direction of the greatest rate of decrease (steepest descent).
4. **Orthogonality to Level Sets**: The gradient vector at any point is **perpendicular (normal)** to the level curve $f(x, y) = c$ (or level surface $f(x, y, z) = c$) passing through that point.

### Example
Let $f(x, y) = x^2 y^3$. Find the gradient vector at the point $(1, 2)$.

1. Find the partial derivatives:
   $f_x = 2xy^3$
   $f_y = 3x^2y^2$
2. Form the gradient vector:
   $\nabla f(x, y) = \langle 2xy^3, 3x^2y^2 \rangle$
3. Evaluate at $(1, 2)$:
   $\nabla f(1, 2) = \langle 2(1)(2)^3, 3(1)^2(2)^2 \rangle = \langle 16, 12 \rangle$

Therefore, at $(1, 2)$, the function increases most rapidly in the direction of the vector $\langle 16, 12 \rangle$, and the rate of that increase is $\sqrt{16^2 + 12^2} = \sqrt{256 + 144} = \sqrt{400} = 20$.

### Related
- [[Partial Derivative]]
- [[Directional Derivatives]]
- [[Multivariable Functions]]

#math/calculus #summer2026
