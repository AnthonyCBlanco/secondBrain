### Idea
While rectangular coordinates $(x, y, z)$ are great for boxes and planes, they make describing curves and rounded surfaces extremely complicated. When dealing with symmetries in 3D space, we rely on two alternative coordinate systems: **Cylindrical** and **Spherical** coordinates.

---

### Cylindrical Coordinates $(r, \theta, z)$
Think of cylindrical coordinates as simply **Polar Coordinates** extended into 3D space by adding a standard $z$-axis. 
- $r$ = distance from the origin to the point's projection on the $xy$-plane.
- $\theta$ = angle in the $xy$-plane (just like polar).
- $z$ = vertical height (same as rectangular $z$).

**Converting to Rectangular:**
$$ x = r \cos \theta $$
$$ y = r \sin \theta $$
$$ z = z $$

**Converting from Rectangular:**
$$ r^2 = x^2 + y^2 $$
$$ \tan \theta = \frac{y}{x} $$
$$ z = z $$

**When to use:** Use cylindrical coordinates when dealing with cylinders, cones, or any objects that possess symmetry around the $z$-axis.
**Integration Volume Element:** When setting up a [[Triple Integral]], the volume element $dV$ becomes:
$$ dV = r \, dz \, dr \, d\theta $$

---

### Spherical Coordinates $(\rho, \theta, \phi)$
Spherical coordinates define a point in 3D space using one distance and two angles, similar to how we define locations on Earth using latitude and longitude.
- $\rho$ (rho) = straight-line distance from the origin to the point.
- $\theta$ (theta) = the exact same angle $\theta$ from polar/cylindrical coordinates (sweeping around the $xy$-plane).
- $\phi$ (phi) = the angle sweeping *down* from the positive $z$-axis.

**Converting to Rectangular:**
$$ x = \rho \sin \phi \cos \theta $$
$$ y = \rho \sin \phi \sin \theta $$
$$ z = \rho \cos \phi $$

**Converting from Rectangular:**
$$ \rho^2 = x^2 + y^2 + z^2 $$
$$ \tan \theta = \frac{y}{x} $$
$$ \cos \phi = \frac{z}{\rho} = \frac{z}{\sqrt{x^2 + y^2 + z^2}} $$

**Standard Restrictions:**
- Distance cannot be negative: $\rho \ge 0$
- Full sweep around the xy-plane: $0 \le \theta \le 2\pi$
- From the "north pole" to the "south pole": $0 \le \phi \le \pi$

**When to use:** Use spherical coordinates when dealing with spheres, hemispheres, or cones originating at the origin.
**Integration Volume Element:** When setting up a [[Triple Integral]], the volume element $dV$ requires the Jacobian determinant and becomes:
$$ dV = \rho^2 \sin \phi \, d\rho \, d\theta \, d\phi $$

### Related
- [[Triple Integral]]
- [[Double Integral]]

#math/calculus #summer2026
