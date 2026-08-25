## Polar Coordinates and Curves

### Idea
While Cartesian coordinates identify points using orthogonal rectilinear displacements $(x, y)$, the polar coordinate system locates points in the plane via radial distance and angular direction $(r, \theta)$. The directed distance $r$ is measured from a fixed central point (the **pole**), and the directed angle $\theta$ is measured counterclockwise from a reference ray (the **polar axis**).

Polar coordinates provide an elegant framework for analyzing figures with central or rotational symmetry, such as circles, cardioids, multi-petaled rose curves, lemniscates, and spirals. Tangent slopes and calculus properties are analyzed by treating $\theta$ as a parameter within the coordinate conversion formulas.

### Formally
#### Coordinate Definitions and Conversions
- **Polar Coordinates $(r, \theta)$:**
  - $r$: directed radial distance from pole to $P$. (If $r < 0$, $P$ lies $|r|$ units along the opposite ray $\theta + \pi$).
  - $\theta$: directed angle from the polar axis.
- **Conversion Equations:**
  $$\begin{aligned}
  x &= r\cos\theta, & y &= r\sin\theta \\
  r^2 &= x^2 + y^2, & \tan\theta &= \frac{y}{x} \quad (x \neq 0)
  \end{aligned}$$

#### Tangent Slope to a Polar Curve $r = f(\theta)$
Treating $\theta$ as a parameter with $x = f(\theta)\cos\theta$ and $y = f(\theta)\sin\theta$:
$$\frac{dy}{dx} = \frac{\frac{dy}{d\theta}}{\frac{dx}{d\theta}} = \frac{\frac{dr}{d\theta}\sin\theta + r\cos\theta}{\frac{dr}{d\theta}\cos\theta - r\sin\theta} = \frac{f'(\theta)\sin\theta + f(\theta)\cos\theta}{f'(\theta)\cos\theta - f(\theta)\sin\theta}$$

- **Tangents at the Pole:** If $r = f(\alpha) = 0$ and $f'(\alpha) \neq 0$:
  $$\frac{dy}{dx} = \frac{f'(\alpha)\sin\alpha}{f'(\alpha)\cos\alpha} = \tan\alpha$$
  The line $\theta = \alpha$ is the tangent line to the curve at the origin.

#### Symmetry Tests
1. **Symmetry about the Polar Axis ($x$-axis):** Unchanged under $(r, \theta) \to (r, -\theta)$ or $(-r, \pi - \theta)$.
2. **Symmetry about $\theta = \frac{\pi}{2}$ ($y$-axis):** Unchanged under $(r, \theta) \to (r, \pi - \theta)$ or $(-r, -\theta)$.
3. **Symmetry about the Pole:** Unchanged under $(r, \theta) \to (-r, \theta)$ or $(r, \theta + \pi)$.

#### Canonical Polar Curve Families
- **Circles:** $r = a$, $r = 2a\cos\theta$, $r = 2a\sin\theta$
- **Limaçons:** $r = a \pm b\cos\theta$, $r = a \pm b\sin\theta$ ($a = b \implies$ cardioid)
- **Rose Curves:** $r = a\cos(n\theta)$, $r = a\sin(n\theta)$ ($n$ odd $\implies n$ petals; $n$ even $\implies 2n$ petals)
- **Lemniscates:** $r^2 = a^2\cos(2\theta)$, $r^2 = a^2\sin(2\theta)$
- **Spirals:** $r = a\theta$ (Archimedean), $r = ae^{b\theta}$ (Logarithmic)

### Example
Consider the cardioid $r = 1 + \cos\theta$.
1. Confirm its symmetry about the polar axis.
2. Find all values of $\theta \in [0, 2\pi)$ where the tangent line is horizontal.
3. Find the slope of the tangent line at $\theta = \frac{\pi}{3}$.

**Part 1: Symmetry Test**
Substitute $(r, -\theta)$ into $r = 1 + \cos\theta$:
$$r = 1 + \cos(-\theta) = 1 + \cos\theta$$
Since $\cos(-\theta) = \cos\theta$, the equation is invariant. The curve is **symmetric about the polar axis**.

**Part 2: Horizontal Tangents**
Horizontal tangents occur when $\frac{dy}{d\theta} = 0$ while $\frac{dx}{d\theta} \neq 0$.
Given $r = 1 + \cos\theta \implies \frac{dr}{d\theta} = -\sin\theta$:
$$\frac{dy}{d\theta} = (-\sin\theta)\sin\theta + (1 + \cos\theta)\cos\theta = -\sin^2\theta + \cos\theta + \cos^2\theta$$
$$= -(1 - \cos^2\theta) + \cos\theta + \cos^2\theta = 2\cos^2\theta + \cos\theta - 1$$

Factor the quadratic in $\cos\theta$:
$$(2\cos\theta - 1)(\cos\theta + 1) = 0$$
- $2\cos\theta - 1 = 0 \implies \cos\theta = \frac{1}{2} \implies \theta = \frac{\pi}{3}, \frac{5\pi}{3}$
- $\cos\theta + 1 = 0 \implies \cos\theta = -1 \implies \theta = \pi$

Check $\frac{dx}{d\theta} = -\sin\theta(2\cos\theta + 1)$:
- At $\theta = \frac{\pi}{3}$, $\frac{dx}{d\theta} = -\frac{\sqrt{3}}{2}(2) = -\sqrt{3} \neq 0$.
- At $\theta = \frac{5\pi}{3}$, $\frac{dx}{d\theta} = \frac{\sqrt{3}}{2}(2) = \sqrt{3} \neq 0$.

Thus, horizontal tangents occur at **$\theta = \frac{\pi}{3}$ and $\theta = \frac{5\pi}{3}$**.

**Part 3: Slope at $\theta = \pi/3$**
$$\frac{dy}{dx}\Bigg|_{\theta=\pi/3} = \frac{0}{-\sqrt{3}} = 0$$
The tangent line is horizontal (slope $0$).

### Related
- [[Parametric Equations and Calculus]]
- [[Calculus in Polar Coordinates]]
- [[Trigonometric Identities]]
- [[Conic Sections in Polar Form]]
- [[Polar Coordinate System]]
- [[Graph of Polar Equations]]

---
#math/calculus #spring2026
