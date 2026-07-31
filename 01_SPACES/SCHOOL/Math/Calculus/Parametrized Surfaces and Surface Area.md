### Idea
To describe a 1D curve in 3D space, we use a [[Vector Valued Functions|vector-valued function]] with a single parameter: $\vec{r}(t)$. 
However, to describe a 2D sheet or **Surface** bending through 3D space, a single parameter is not enough. We need two parameters, typically called $u$ and $v$.

### Parametrized Surfaces
A parametrized surface is defined by a vector function of two variables:
$$ \vec{r}(u, v) = \langle x(u, v), y(u, v), z(u, v) \rangle $$
As $u$ and $v$ vary across a 2D region $D$ (in the $uv$-plane), the tip of the vector $\vec{r}$ sweeps out a surface $S$ in 3D space.

**Grid Curves:**
If you hold $v$ constant and let $u$ vary, $\vec{r}$ traces out a 1D curve on the surface. If you hold $u$ constant and let $v$ vary, it traces out a different curve. Together, these form a mesh or "grid" that perfectly maps the surface.

### The Normal Vector
To calculate anything useful about a surface (like area or flux), we need to find its **normal vector** (the vector pointing straight out, perpendicular to the surface).
1. Find the tangent vector along the $u$-grid curve by taking the [[Partial Derivative]] with respect to $u$: 
   $$ \vec{r}_u = \left\langle \frac{\partial x}{\partial u}, \frac{\partial y}{\partial u}, \frac{\partial z}{\partial u} \right\rangle $$
2. Find the tangent vector along the $v$-grid curve:
   $$ \vec{r}_v = \left\langle \frac{\partial x}{\partial v}, \frac{\partial y}{\partial v}, \frac{\partial z}{\partial v} \right\rangle $$
3. Take the **cross product** of these two tangent vectors to get the normal vector to the surface:
   $$ \vec{n} = \vec{r}_u \times \vec{r}_v $$

### Surface Area Formula
The magnitude of that normal vector, $|\vec{r}_u \times \vec{r}_v|$, represents the microscopic area of the tiny parallelogram formed by the two tangent vectors. 

To find the total **Surface Area** of the surface $S$, we simply add up all those microscopic parallelograms using a [[Double Integral]] over the region $D$:
$$
A(S) = \iint_D |\vec{r}_u \times \vec{r}_v| \, dA
$$
*(Where $dA = du \, dv$)*.

---

### Special Case: Surfaces given by $z = f(x, y)$
Very often, a surface isn't given as a complex parameterization, but simply as a standard function like $z = x^2 + y^2$. 
In this case, the easiest parameterization is just to use $x$ and $y$ themselves as the parameters:
$$ \vec{r}(x, y) = \langle x, y, f(x, y) \rangle $$

If you run this through the cross-product process above, the magnitude $|\vec{r}_x \times \vec{r}_y|$ always simplifies to a very clean, specific formula:
$$ |\vec{r}_x \times \vec{r}_y| = \sqrt{1 + (f_x)^2 + (f_y)^2} $$

So, the **Surface Area** for a standard function $z = f(x, y)$ over a region $D$ in the $xy$-plane is:
$$
A(S) = \iint_D \sqrt{1 + \left(\frac{\partial z}{\partial x}\right)^2 + \left(\frac{\partial z}{\partial y}\right)^2} \, dA
$$

### Related
- [[Double Integral]]
- [[Partial Derivative]]
- [[Vector Valued Functions]]

#math/calculus #summer2026
