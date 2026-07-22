### Idea
Divergence and Curl are two operations that analyze the behavior of [[Vector Fields]]. Both are calculated using the "Del" operator:
$$ \nabla = \left\langle \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right\rangle $$
While the [[Gradient Vector]] applies $\nabla$ to a *scalar* function to create a vector field, Divergence and Curl apply $\nabla$ to *vector fields* using the dot product and cross product.

---

### Divergence ($\nabla \cdot \vec{F}$)
**Divergence** measures the tendency of a fluid to collect or disperse at a point. It tells you whether a point acts as a "source" (fluid expanding out) or a "sink" (fluid compressing in).

**Formula:**
Divergence is the **dot product** of the Del operator and the vector field $\vec{F} = \langle P, Q, R \rangle$. 
*Crucially, the divergence of a vector field produces a **scalar** (a single number).*
$$
\text{div } \vec{F} = \nabla \cdot \vec{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}
$$

**Interpretations:**
- $\text{div } \vec{F} > 0$: The point is a **source** (expansion / gas expanding).
- $\text{div } \vec{F} < 0$: The point is a **sink** (compression / gas condensing).
- $\text{div } \vec{F} = 0$: The fluid is **incompressible** (whatever flows in must flow out).

---

### Curl ($\nabla \times \vec{F}$)
**Curl** measures the rotation or "swirl" of a vector field. If you were to drop a microscopic paddlewheel into a fluid flow, the curl tells you how fast the wheel would spin and the axis around which it would rotate.

**Formula:**
Curl is the **cross product** of the Del operator and the vector field. 
*Crucially, the curl of a vector field produces another **vector**.*
$$
\text{curl } \vec{F} = \nabla \times \vec{F} = \begin{vmatrix} 
\hat{i} & \hat{j} & \hat{k} \\ 
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ 
P & Q & R 
\end{vmatrix}
$$
$$
\text{curl } \vec{F} = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right)\hat{i} - \left( \frac{\partial R}{\partial x} - \frac{\partial P}{\partial z} \right)\hat{j} + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)\hat{k}
$$

**Interpretations:**
- The resulting vector points exactly along the **axis of rotation** (following the right-hand rule).
- The magnitude of the vector represents the **speed of rotation**.
- If $\text{curl } \vec{F} = \vec{0}$ everywhere, the vector field is said to be **irrotational**.

*(Note: For a 2D vector field $\vec{F} = \langle P, Q \rangle$, the curl is often given as just the scalar $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$, which represents rotation in the xy-plane around the invisible z-axis).*

---

### Two Critical Identities
There are two extremely important theorems connecting gradient, curl, and divergence. They are often used to prove properties about conservative vector fields.

1. **The curl of a gradient field is zero:** 
   $$ \text{curl}(\nabla f) = \vec{0} $$
   *(Meaning: all conservative vector fields are irrotational).*
2. **The divergence of a curl field is zero:** 
   $$ \text{div}(\text{curl } \vec{F}) = 0 $$
   *(Meaning: rotational fields are incompressible).*

### Related
- [[Vector Fields]]
- [[Gradient Vector]]
- [[Partial Derivative]]

#math/calculus #summer2026
