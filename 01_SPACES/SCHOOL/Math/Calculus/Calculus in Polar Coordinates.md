## Calculus in Polar Coordinates

### Idea
Calculus in polar coordinates enables the direct computation of areas enclosed by polar curves, areas trapped between overlapping polar graphs, and arc lengths along curved polar trajectories.

In Cartesian coordinates, area is accumulated by summing narrow vertical rectangular strips $\Delta A \approx y \Delta x$. In polar coordinates, area is accumulated by sweeping radial rays outward from the pole, summing infinitesimal **circular sectors** with area $\Delta A \approx \frac{1}{2} r^2 \Delta \theta$. Arc length is calculated by transforming polar differential elements into the Pythagorean metric $dL = \sqrt{r^2 + (r')^2} \, d\theta$.

### Formally
#### 1. Area of a Polar Region
For a continuous function $r = f(\theta) \ge 0$ bounded between radial rays $\theta = \alpha$ and $\theta = \beta$ with $0 \le \beta - \alpha \le 2\pi$:
$$A = \frac{1}{2}\int_\alpha^\beta [f(\theta)]^2 \, d\theta = \frac{1}{2}\int_\alpha^\beta r^2 \, d\theta$$

#### 2. Area Between Two Polar Curves
If $r_{\text{outer}} = f(\theta)$ and $r_{\text{inner}} = g(\theta)$ satisfy $f(\theta) \ge g(\theta) \ge 0$ on $[\alpha, \beta]$:
$$A = \frac{1}{2}\int_\alpha^\beta \left( [f(\theta)]^2 - [g(\theta)]^2 \right) d\theta$$

#### 3. Arc Length of a Polar Curve
For a polar curve $r = f(\theta)$ with continuous derivative $f'(\theta)$ on $[\alpha, \beta]$:
$$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta = \int_\alpha^\beta \sqrt{[f(\theta)]^2 + [f'(\theta)]^2} \, d\theta$$

#### 4. Surface Area of Revolution in Polar Coordinates
- **Rotation about the Polar Axis ($x$-axis, where $y = r\sin\theta \ge 0$):**
  $$S_{\text{polar}} = \int_\alpha^\beta 2\pi r\sin\theta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta$$
- **Rotation about the Vertical Line $\theta = \frac{\pi}{2}$ ($y$-axis, where $x = r\cos\theta \ge 0$):**
  $$S_{\pi/2} = \int_\alpha^\beta 2\pi r\cos\theta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta$$

### Example
Find the exact area $A$ of the region that lies **inside** the circle $r = 3\sin\theta$ and **outside** the cardioid $r = 1 + \sin\theta$.

**Step 1: Determine the intersection angles**
Set the two radii equal to find intersection points in $[0, \pi]$:
$$3\sin\theta = 1 + \sin\theta \implies 2\sin\theta = 1 \implies \sin\theta = \frac{1}{2}$$
The solutions in $[0, \pi]$ are:
$$\theta = \frac{\pi}{6} \quad \text{and} \quad \theta = \frac{5\pi}{6}$$
On $\left[\frac{\pi}{6}, \frac{5\pi}{6}\right]$, the circle is the outer boundary ($3\sin\theta \ge 1 + \sin\theta$).

**Step 2: Set up the polar area integral**
$$A = \frac{1}{2}\int_{\pi/6}^{5\pi/6} \left( (3\sin\theta)^2 - (1 + \sin\theta)^2 \right) d\theta$$

**Step 3: Expand and simplify the integrand**
$$(3\sin\theta)^2 - (1 + \sin\theta)^2 = 9\sin^2\theta - (1 + 2\sin\theta + \sin^2\theta) = 8\sin^2\theta - 2\sin\theta - 1$$
Using the half-angle identity $\sin^2\theta = \frac{1 - \cos(2\theta)}{2}$:
$$8\left(\frac{1 - \cos 2\theta}{2}\right) - 2\sin\theta - 1 = 4 - 4\cos 2\theta - 2\sin\theta - 1 = 3 - 4\cos 2\theta - 2\sin\theta$$

**Step 4: Evaluate the definite integral**
$$A = \frac{1}{2} \int_{\pi/6}^{5\pi/6} (3 - 4\cos 2\theta - 2\sin\theta) \, d\theta = \frac{1}{2} \left[ 3\theta - 2\sin(2\theta) + 2\cos\theta \right]_{\pi/6}^{5\pi/6}$$

Evaluate at the upper limit $\theta = \frac{5\pi}{6}$:
$$3\left(\frac{5\pi}{6}\right) - 2\sin\left(\frac{5\pi}{3}\right) + 2\cos\left(\frac{5\pi}{6}\right) = \frac{5\pi}{2} - 2\left(-\frac{\sqrt{3}}{2}\right) + 2\left(-\frac{\sqrt{3}}{2}\right) = \frac{5\pi}{2}$$

Evaluate at the lower limit $\theta = \frac{\pi}{6}$:
$$3\left(\frac{\pi}{6}\right) - 2\sin\left(\frac{\pi}{3}\right) + 2\cos\left(\frac{\pi}{6}\right) = \frac{\pi}{2} - 2\left(\frac{\sqrt{3}}{2}\right) + 2\left(\frac{\sqrt{3}}{2}\right) = \frac{\pi}{2}$$

Subtract limits:
$$A = \frac{1}{2} \left( \frac{5\pi}{2} - \frac{\pi}{2} \right) = \frac{1}{2}(2\pi) = \pi$$

**Step 5: Conclusion**
The exact area of the region is $\pi$ square units.

### Related
- [[Polar Coordinates and Curves]]
- [[Parametric Equations and Calculus]]
- [[Definite Integrals]]
- [[Arc Length]]
- [[Surface Area of Revolution]]
- [[Double Integral]]

---
#math/calculus #spring2026
