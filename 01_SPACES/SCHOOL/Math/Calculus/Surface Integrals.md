### Idea
Just as a line integral generalizes a standard 1D integral to a curved path, a **Surface Integral** generalizes a [[Double Integral]] to a curved 2D surface $S$ floating in 3D space. 

Instead of integrating over a perfectly flat region in the $xy$-plane, we are adding up values across a wavy, curved sheet. There are two main types of surface integrals: those for scalar functions, and those for vector fields.

---

### Surface Integrals of Scalar Functions
If you have a thin curved sheet of metal, and $f(x, y, z)$ represents the density at any given point, the surface integral calculates the total **mass** of the sheet. 
*(If $f(x, y, z) = 1$, it simply calculates the total Surface Area).*

**Notation:**
$$ \iint_S f(x, y, z) \, dS $$
*(Note the capital $S$, which distinguishes it from the lowercase $s$ arc length in line integrals).*

**How to Evaluate:**
To calculate this, you must project the curved surface $S$ down onto a flat region $D$ (usually in the $uv$-plane or $xy$-plane) and use the magnitude of the normal vector to account for the stretching.

Using a general parameterization $\vec{r}(u, v)$ (see [[Parametrized Surfaces and Surface Area]]):
$$ \iint_S f(x, y, z) \, dS = \iint_D f(\vec{r}(u, v)) |\vec{r}_u \times \vec{r}_v| \, dA $$

Using a standard function $z = g(x, y)$:
$$ \iint_S f(x, y, z) \, dS = \iint_D f(x, y, g(x,y)) \sqrt{1 + (g_x)^2 + (g_y)^2} \, dA $$

---

### Surface Integrals of Vector Fields (Flux)
This is the most common application in physics (like Gauss's Law in electromagnetism). If $\vec{F}$ is a vector field (like water flow or an electric field), the surface integral calculates the total [[Flow and Flux|Flux]]—how much of the field is piercing *through* the surface $S$.

**Notation:**
$$ \iint_S \vec{F} \cdot d\vec{S} \quad \text{or} \quad \iint_S \vec{F} \cdot \vec{n} \, dS $$
Where $\vec{n}$ is the unit normal vector pointing out of the surface.

**Orientation:**
To calculate flux, the surface must be **orientable**. You have to pick a "positive" side (usually "upward" for an open surface, or "outward" for a closed surface like a sphere). *You cannot calculate flux across a Möbius strip because it only has one side!*

**How to Evaluate:**
You evaluate this by taking the dot product of the vector field and the normal vector.

Using a general parameterization $\vec{r}(u, v)$:
$$ \iint_S \vec{F} \cdot d\vec{S} = \iint_D \vec{F}(\vec{r}(u, v)) \cdot (\vec{r}_u \times \vec{r}_v) \, dA $$
*(Make sure $\vec{r}_u \times \vec{r}_v$ points in the correct positive orientation! If it points the wrong way, just multiply by $-1$).*

Using a standard function $z = g(x, y)$ (oriented **upwards**):
If $\vec{F} = \langle P, Q, R \rangle$, the cross product simplifies heavily, and you can jump straight to this formula:
$$ \iint_S \vec{F} \cdot d\vec{S} = \iint_D (-P g_x - Q g_y + R) \, dA $$

### Related
- [[Parametrized Surfaces and Surface Area]]
- [[Flow and Flux]]
- [[Vector Fields]]
- [[Double Integral]]

#math/calculus #summer2026
