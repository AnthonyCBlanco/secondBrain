### Idea
When dealing with [[Vector Fields]], we often want to measure two distinct physical behaviors relative to a path or a boundary: how much of the field pushes *along* the path, and how much of the field pierces *through* the boundary.

### Flow and Circulation
**Flow** measures how much of a vector field $\vec{F}$ points in the same direction as a curve $C$. It calculates the "work" done moving along that path.
You calculate Flow by taking the dot product of the vector field and the tangent vector of the curve, which is exactly a standard [[Line Integrals|line integral]]:
$$ \text{Flow} = \int_C \vec{F} \cdot d\vec{r} = \int_C \vec{F} \cdot \vec{T} \, ds $$

**Circulation:** If the curve $C$ is a *closed loop* (starting and ending at the same point), the flow is specifically called **Circulation**. It measures how much the vector field rotates around that loop.
$$ \text{Circulation} = \oint_C \vec{F} \cdot d\vec{r} $$

### Flux
**Flux** measures how much of a vector field $\vec{F}$ pierces *through* or flows *across* a boundary. 
You calculate Flux by taking the dot product of the vector field and the **normal vector** (the vector pointing perpendicularly outward from the boundary).

**2D Flux (Across a curve):**
In 2D, flux measures how much fluid is crossing a curve $C$. Instead of the tangent vector $\vec{T}$, we use the outward normal vector $\vec{n}$:
$$ \text{2D Flux} = \int_C \vec{F} \cdot \vec{n} \, ds $$
*(If $\vec{F} = \langle P, Q \rangle$, this is often calculated as $\int_C P \, dy - Q \, dx$).*

**3D Flux (Across a surface):**
In 3D, flux measures how much fluid or energy is passing through a 2D surface $S$ (like a sail catching wind). This requires a **Surface Integral**:
$$ \text{3D Flux} = \iint_S \vec{F} \cdot d\vec{S} = \iint_S \vec{F} \cdot \vec{n} \, dS $$

### Related
- [[Line Integrals]]
- [[Green's Theorem]]
- [[The Divergence Theorem]]
- [[Vector Fields]]

#math/calculus #summer2026
