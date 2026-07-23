### Idea
A standard [[Definite Integrals|definite integral]] $\int_a^b f(x) \, dx$ calculates the area under a curve, but it restricts us to integrating along a perfectly straight line on the $x$-axis from $a$ to $b$. 

A **Line Integral** (sometimes called a path integral or curve integral) generalizes this concept. It allows us to integrate a function over a curved path $C$ winding through 2D or 3D space. 

There are two main types of line integrals: those over scalar functions, and those over vector fields.

---

### Line Integrals of Scalar Functions
Imagine a path $C$ painted on the ground. Above this path hovers a surface $z = f(x, y)$. If you hang a curtain from the surface down to the path $C$, the line integral calculates the total **area of that wavy curtain**.

**Notation:**
$$ \int_C f(x, y) \, ds $$
Here, $ds$ represents a tiny element of arc length along the curve.

**How to Evaluate:**
1. **Parameterize the curve $C$:** Write it as a [[Vector Valued Functions|vector-valued function]] $\vec{r}(t) = \langle x(t), y(t) \rangle$ for some range $a \le t \le b$.
2. **Find the magnitude of the derivative:** $ds$ becomes $|\vec{r}'(t)| \, dt$.
3. **Substitute into the integral:** Replace all $x$'s and $y$'s in the function with your parameterized $x(t)$ and $y(t)$, and integrate from $a$ to $b$:
   $$ \int_C f(x,y) \, ds = \int_a^b f(x(t), y(t)) |\vec{r}'(t)| \, dt $$

*(Note: If $f(x, y) = 1$, the integral simply calculates the total arc length of the curve $C$).*

---

### Line Integrals of Vector Fields
This is the most common application in physics. If $\vec{F}$ is a force field (like wind or gravity), the line integral calculates the total **work** done by the field pushing an object along the path $C$. It effectively sums up how much of the vector field points in the same direction as your path at every given moment.

**Notation:**
$$ \int_C \vec{F} \cdot d\vec{r} $$
*(Sometimes written in terms of the unit tangent vector as $\int_C \vec{F} \cdot \vec{T} \, ds$).*

**Alternate Notation (Differential Form):**
Since $\vec{F} = \langle P, Q \rangle$ and $d\vec{r} = \langle dx, dy \rangle$, their dot product leads to a very common alternative way to write the exact same integral:
$$ \int_C P \, dx + Q \, dy $$

**How to Evaluate:**
1. **Parameterize the curve $C$:** $\vec{r}(t) = \langle x(t), y(t) \rangle$ for $a \le t \le b$.
2. **Find the derivative vector:** $d\vec{r}$ becomes $\vec{r}'(t) \, dt$.
3. **Substitute and take the dot product:** Plug your parameterized equations into the vector field $\vec{F}$, take the dot product with $\vec{r}'(t)$, and integrate:
   $$ \int_C \vec{F} \cdot d\vec{r} = \int_a^b \vec{F}(\vec{r}(t)) \cdot \vec{r}'(t) \, dt $$

---

### The Fundamental Theorem of Line Integrals
Line integrals can be notoriously tedious to calculate. However, if your vector field $\vec{F}$ happens to be a [[Conservative Vector Fields|Conservative Vector Field]] (meaning $\vec{F} = \nabla f$), you can bypass the entire parameterization process!

If the field is conservative, the line integral is **path independent**. It does not matter how winding or crazy the curve $C$ is, the work done only depends on where you start and where you end:
$$
\int_C \nabla f \cdot d\vec{r} = f(\vec{r}(b)) - f(\vec{r}(a))
$$
Just evaluate the potential function $f$ at the ending point and subtract its value at the starting point.

### Related
- [[Definite Integrals]]
- [[Vector Fields]]
- [[Conservative Vector Fields]]
- [[Vector Valued Functions]]

#math/calculus #summer2026
