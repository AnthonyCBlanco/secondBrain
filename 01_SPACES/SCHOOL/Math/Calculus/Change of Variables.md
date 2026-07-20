### Idea
In single-variable calculus, we use $u$-substitution to simplify integrals. **Change of Variables** is the exact same concept extended to [[Double Integral|double]] and [[Triple Integral|triple integrals]]. We use it when the region of integration is too awkward to describe in standard $(x, y)$ coordinates, or when the integrand itself is too complex.

By defining new variables (usually $u$ and $v$), we map a complicated region $R$ in the $xy$-plane to a much simpler region $S$ (often a rectangle) in the $uv$-plane.

### The Jacobian Determinant
When we change variables, we can't just swap $dx \, dy$ for $du \, dv$. We have to account for how the transformation stretches or shrinks the area. We do this by multiplying by the absolute value of the **[[Jacobian Matrix|Jacobian Determinate]]**, denoted as $J(u, v)$ or $\frac{\partial(x, y)}{\partial(u, v)}$.

For a transformation $x = g(u, v)$ and $y = h(u, v)$, the Jacobian is the determinant of the matrix of partial derivatives:
$$
J(u, v) = \frac{\partial(x, y)}{\partial(u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}
$$

### The Formula
The general formula for a change of variables in a double integral is:
$$
\iint_R f(x, y) \, dx \, dy = \iint_S f(x(u, v), y(u, v)) \left| \frac{\partial(x, y)}{\partial(u, v)} \right| \, du \, dv
$$

*Note: You must use the **absolute value** of the Jacobian determinant, because area cannot be negative.*

### Connection to Coordinate Systems
If you have ever converted an integral to polar coordinates, you have already used a Change of Variables!
When you let $x = r \cos \theta$ and $y = r \sin \theta$, the variables are $(r, \theta)$. If you calculate the Jacobian determinant for this transformation, it comes out exactly to $r$. 

This is why $dx \, dy$ becomes $r \, dr \, d\theta$. The same principle applies to the $dV$ elements in [[Cylindrical and Spherical Coordinates]].

### Triple Integrals
The concept scales perfectly to 3D. If you transform $(x, y, z)$ into $(u, v, w)$, the Jacobian is simply a $3 \times 3$ determinant of all nine partial derivatives:
$$
\frac{\partial(x, y, z)}{\partial(u, v, w)} = \begin{vmatrix} 
x_u & x_v & x_w \\ 
y_u & y_v & y_w \\ 
z_u & z_v & z_w 
\end{vmatrix}
$$
And the integral becomes:
$$
\iiint_R f(x, y, z) \, dV = \iiint_S f(x(u,v,w), y(u,v,w), z(u,v,w)) \left| \frac{\partial(x, y, z)}{\partial(u, v, w)} \right| \, du \, dv \, dw
$$

### Related
- [[Double Integral]]
- [[Triple Integral]]
- [[Cylindrical and Spherical Coordinates]]

#math/calculus #summer2026
