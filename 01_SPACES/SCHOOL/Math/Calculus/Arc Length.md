## Arc Length

### Idea
Arc length is the measure of the exact geometric distance along a continuous, smooth curve between two defined points.

The fundamental formula is derived by subdividing the curve into infinitesimal straight-line segments. Applying the Pythagorean theorem to each microscopic triangle with horizontal run $dx$ and vertical rise $dy$ yields the differential arc length element $dL = \sqrt{(dx)^2 + (dy)^2}$. 

Summing these infinitesimal hypotenuses via definite integration accounts for the curve's continuously varying slope and yields the exact total curve length.

### Formally
#### Differential Arc Length Element
$$dL = \sqrt{dx^2 + dy^2}$$

#### Explicit Function $y = f(x)$ on $[a, b]$
Assuming $f'(x)$ is continuous on $[a, b]$:
$$dL = \sqrt{1 + \left(\frac{dy}{dx}\right)^2} dx = \sqrt{1 + [f'(x)]^2} \, dx$$
$$L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$$

#### Explicit Function $x = g(y)$ on $[c, d]$
Assuming $g'(y)$ is continuous on $[c, d]$:
$$dL = \sqrt{\left(\frac{dx}{dy}\right)^2 + 1} dy = \sqrt{1 + [g'(y)]^2} \, dy$$
$$L = \int_c^d \sqrt{1 + [g'(y)]^2} \, dy$$

#### Parametric Curve $x = x(t), y = y(t)$ on $[\alpha, \beta]$
$$L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

#### Arc Length Function (Distance Accumulation)
$$s(x) = \int_a^x \sqrt{1 + [f'(t)]^2} \, dt \implies \frac{ds}{dx} = \sqrt{1 + [f'(x)]^2}$$

### Example
Find the exact arc length of the curve $y = \frac{2}{3}x^{3/2}$ from $x = 0$ to $x = 3$.

**Step 1: Compute the derivative of $y$**
$$f'(x) = \frac{d}{dx}\left[ \frac{2}{3}x^{3/2} \right] = \frac{2}{3} \cdot \frac{3}{2} x^{1/2} = \sqrt{x}$$

**Step 2: Form the expression $1 + [f'(x)]^2$**
$$[f'(x)]^2 = (\sqrt{x})^2 = x \implies 1 + [f'(x)]^2 = 1 + x$$

**Step 3: Set up the arc length integral**
$$L = \int_0^3 \sqrt{1 + x} \, dx$$

**Step 4: Evaluate using the power rule for integration**
Let $u = 1 + x \implies du = dx$:
$$L = \left[ \frac{2}{3}(1 + x)^{3/2} \right]_0^3 = \frac{2}{3}(1 + 3)^{3/2} - \frac{2}{3}(1 + 0)^{3/2}$$
$$= \frac{2}{3}(4^{3/2} - 1^{3/2}) = \frac{2}{3}(8 - 1) = \frac{2}{3}(7) = \frac{14}{3}$$

**Step 5: Conclusion**
The total arc length of the curve is $\frac{14}{3}$ units.

### Related
- [[The Derivative]]
- [[Definite Integrals]]
- [[Fundamental Theorem of Calculus]]
- [[Surface Area of Revolution]]
- [[Parametric Equations and Calculus]]
- [[Line Integrals]]

---
#math/calculus #spring2026
