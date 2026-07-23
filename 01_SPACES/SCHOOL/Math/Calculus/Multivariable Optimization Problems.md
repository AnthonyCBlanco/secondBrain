### Idea
Just as we find maximums and minimums of single-variable functions to solve optimization problems, we can optimize [[Multivariable Functions|multivariable functions]] $z = f(x, y)$. This involves locating local extrema (peaks and valleys) and saddle points.

### Finding Critical Points
The first step in finding local extrema is to locate the **critical points**. For a function $f(x, y)$, a point $(a, b)$ is a critical point if:
1. The [[Gradient Vector]] is zero: $\nabla f(a, b) = \langle 0, 0 \rangle$ 
   (Meaning both [[Partial Derivative|partial derivatives]] $f_x(a, b) = 0$ and $f_y(a, b) = 0$)
2. Or, at least one of the partial derivatives does not exist at $(a, b)$.

At these points, the tangent plane is completely horizontal (or undefined).

### The Second Partials Test
Once you have found a critical point $(a, b)$, you must determine whether it is a local maximum, a local minimum, or a saddle point. We do this using the **Second Partials Test**, which relies on the discriminant (or Hessian determinant), denoted as $D$:

$$
D(x, y) = f_{xx}(x, y) \cdot f_{yy}(x, y) - [f_{xy}(x, y)]^2
$$

**To classify the critical point $(a, b)$:**
Evaluate $D$ at the point $(a, b)$:
1. **Local Minimum:** If $D(a, b) > 0$ and $f_{xx}(a, b) > 0$. (The surface curves upwards in all directions like a bowl).
2. **Local Maximum:** If $D(a, b) > 0$ and $f_{xx}(a, b) < 0$. (The surface curves downwards in all directions like a hill).
3. **Saddle Point:** If $D(a, b) < 0$. (The surface curves up in one direction and down in another, resembling a horse saddle).
4. **Inconclusive:** If $D(a, b) = 0$, the test fails, and you must use another method to determine the behavior.

*(Note: In cases 1 and 2 where $D > 0$, $f_{xx}$ and $f_{yy}$ will always have the same sign, so you can check either one).*

### Absolute Extrema on a Closed Domain
To find the absolute maximum and absolute minimum of a continuous function on a closed and bounded set $D$:
1. Find the values of $f$ at all critical points *inside* $D$.
2. Find the maximum and minimum values of $f$ on the *boundary* of $D$ (this usually involves turning the boundary into a single-variable function or using [[Lagrange Multipliers]]).
3. Compare all the values found in steps 1 and 2. The largest is the absolute maximum; the smallest is the absolute minimum.

### Related
- [[Partial Derivative]]
- [[Gradient Vector]]
- [[The Derivative]]

#math/calculus #summer2026
