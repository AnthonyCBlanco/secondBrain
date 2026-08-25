## Volume by Cylindrical Shells

### Idea
The method of cylindrical shells computes the volume of a solid of revolution by slicing the region **parallel** to the axis of revolution into thin, concentric cylindrical shells.

When a thin cylindrical shell of radius $r$, height $h$, and infinitesimal thickness $\Delta r$ is unrolled flat, it forms a rectangular slab with volume $dV = 2\pi r \cdot h \cdot dr$ (circumference $\times$ height $\times$ thickness). 

This method is particularly advantageous when integrating using disks or washers would require solving difficult equations for the inverse function, or would force the region to be split into multiple separate integrals.

### Formally
#### Rotation About a Vertical Axis (e.g., $y$-axis or line $x = k$)
Because slices are parallel to the vertical axis, shell thickness is $dx$, necessitating integration with respect to $x$:
$$V = 2\pi \int_a^b (\text{shell radius})(\text{shell height}) \, dx = 2\pi \int_a^b r(x) h(x) \, dx$$
- For rotation about the $y$-axis ($x = 0$): $r(x) = x$, and $h(x) = f_{\text{top}}(x) - g_{\text{bottom}}(x)$:
  $$V = 2\pi \int_a^b x [f(x) - g(x)] \, dx$$
- For rotation about the line $x = k$: $r(x) = |x - k|$.

#### Rotation About a Horizontal Axis (e.g., $x$-axis or line $y = c$)
Because slices are parallel to the horizontal axis, shell thickness is $dy$, necessitating integration with respect to $y$:
$$V = 2\pi \int_c^d (\text{shell radius})(\text{shell height}) \, dy = 2\pi \int_c^d r(y) h(y) \, dy$$
- For rotation about the $x$-axis ($y = 0$): $r(y) = y$, and $h(y) = f_{\text{right}}(y) - g_{\text{left}}(y)$:
  $$V = 2\pi \int_c^d y [f(y) - g(y)] \, dy$$
- For rotation about the line $y = c$: $r(y) = |y - c|$.

#### Method Comparison Summary
| Method | Slice Orientation to Axis | Variable for Vertical Axis | Variable for Horizontal Axis |
| :--- | :--- | :--- | :--- |
| **Disks / Washers** | Perpendicular ($\perp$) | Integrate with respect to $y$ ($dy$) | Integrate with respect to $x$ ($dx$) |
| **Cylindrical Shells** | Parallel ($\parallel$) | Integrate with respect to $x$ ($dx$) | Integrate with respect to $y$ ($dy$) |

### Example
Find the volume of the solid obtained by rotating the region bounded by $y = 2x^2 - x^3$ and $y = 0$ about the $y$-axis.

**Step 1: Determine the region boundaries**
Find the $x$-intercepts by setting $y = 0$:
$$2x^2 - x^3 = 0 \implies x^2(2 - x) = 0 \implies x = 0 \quad \text{to} \quad x = 2$$

**Step 2: Identify shell parameters for rotation about the $y$-axis**
- Radius: $r(x) = x$
- Height: $h(x) = (2x^2 - x^3) - 0 = 2x^2 - x^3$

**Step 3: Set up the cylindrical shell integral**
$$V = 2\pi \int_0^2 x(2x^2 - x^3) \, dx = 2\pi \int_0^2 (2x^3 - x^4) \, dx$$

**Step 4: Evaluate the integral**
$$V = 2\pi \left[ \frac{2x^4}{4} - \frac{x^5}{5} \right]_0^2 = 2\pi \left[ \frac{x^4}{2} - \frac{x^5}{5} \right]_0^2$$
$$= 2\pi \left( \frac{2^4}{2} - \frac{2^5}{5} \right) = 2\pi \left( 8 - \frac{32}{5} \right) = 2\pi \left( \frac{40 - 32}{5} \right) = 2\pi \left( \frac{8}{5} \right) = \frac{16\pi}{5}$$

**Step 5: Conclusion**
The volume of the solid is $\frac{16\pi}{5}$ cubic units.

### Related
- [[Volume by Disks and Washers]]
- [[Definite Integrals]]
- [[Fundamental Theorem of Calculus]]
- [[Integration by Parts]]
- [[Triple Integral]]

---
#math/calculus #spring2026
