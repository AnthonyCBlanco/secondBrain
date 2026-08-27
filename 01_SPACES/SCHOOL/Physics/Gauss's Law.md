### Idea
**Gauss's Law** is the first of Maxwell's famous equations of electromagnetism. It provides a profound, elegant relationship between the electric charge in a region and the [[Electric Fields|Electric Field]] it creates.

The core idea is simple: If you trap some charge inside an imaginary 3D bubble (a "Gaussian surface"), the total amount of electric field lines piercing out through that bubble (the [[Surface Integrals|flux]]) depends *only* on the total amount of charge trapped inside. **Charges completely outside the bubble do not affect the net flux.**

While fundamentally equivalent to [[Coulomb's Law]], Gauss's Law provides a massive shortcut for calculating electric fields when dealing with highly symmetrical charge distributions (like infinite lines, flat planes, or solid spheres).

### Formally (Integral Form)
Gauss's law states that the net electric flux ($\Phi_E$) passing through any closed surface is equal to the total net charge enclosed inside that surface ($Q_{enc}$), divided by the permittivity of free space ($\varepsilon_0$).

$$
\Phi_E = \oint_S \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\varepsilon_0}
$$

**Variables:**
- **$\oint_S$**: A closed [[Surface Integrals|surface integral]] over your imaginary "Gaussian surface".
- **$\vec{E}$**: The electric field vector.
- **$d\vec{A}$**: The outward-pointing normal area vector.
- **$Q_{enc}$**: The total net charge completely trapped inside the boundary.
- **$\varepsilon_0$**: Permittivity of free space ($\approx 8.85 \times 10^{-12} \, \text{C}^2 / (\text{N}\cdot\text{m}^2)$).

### Differential Form
Using [[The Divergence Theorem]], we can also write Gauss's Law in its differential form, which states that the divergence of the electric field at any specific point is proportional to the local charge density ($\rho$) at that point:
$$
\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}
$$

### Applying Gauss's Law
To actually use the integral equation to solve for the electric field $\vec{E}$, you must be very clever about drawing your imaginary Gaussian surface. You must pick a shape (usually a sphere or a cylinder) that perfectly matches the symmetry of the charge distribution so that:
1. $\vec{E}$ is perfectly parallel to $d\vec{A}$ everywhere on the surface (making the dot product just $E \cdot dA$).
2. The magnitude of $\vec{E}$ is absolutely constant everywhere on the surface.

If you do this right, $\vec{E}$ is pulled completely out of the integral!
$$ \oint_S \vec{E} \cdot d\vec{A} = E \oint_S dA = E(\text{Total Surface Area}) = \frac{Q_{enc}}{\varepsilon_0} $$

### Rule of Conductors
One of the most famous applications of Gauss's Law is proving how conductors behave in electrostatic equilibrium:
1. **The electric field inside a solid conductor is always zero** ($\vec{E} = 0$). If it wasn't zero, the free electrons would instantly move until they cancelled it out.
2. Because $\vec{E} = 0$ inside, Gauss's law dictates that $Q_{enc} = 0$ inside. Therefore, **any excess charge placed on a solid conductor resides entirely on its outer surface**. 

### Related
- [[Electric Fields]]
- [[Coulomb's Law]]
- [[Surface Integrals]]
- [[The Divergence Theorem]]

#physics #electromagnetism
