## Parametric Equations and Calculus

### Idea
Parametric equations define the coordinates $x$ and $y$ of a plane curve independently as functions of a third variable, the parameter $t$ (often representing time): $x = f(t), y = g(t)$.

This formulation liberates curves from the single-valued "vertical line test" constraint of Cartesian functions $y = f(x)$, allowing the modeling of closed loops, self-intersecting figures, cycloids, spirals, planetary orbits, and directional particle paths. 

Calculus on parametric curves provides formulas for tangent slopes $\frac{dy}{dx}$, concavity $\frac{d^2y}{dx^2}$, total arc length, surface area of revolution, and area under the curve.

### Formally
#### 1. Parametric Derivatives
Let $x = f(t)$ and $y = g(t)$ be differentiable functions of $t$:
- **First Derivative (Tangent Slope):**
  $$\frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} = \frac{g'(t)}{f'(t)} \quad (\text{provided } f'(t) \neq 0)$$
  - *Horizontal Tangent:* $\frac{dy}{dt} = 0$ while $\frac{dx}{dt} \neq 0$.
  - *Vertical Tangent:* $\frac{dx}{dt} = 0$ while $\frac{dy}{dt} \neq 0$.
- **Second Derivative (Concavity):**
  $$\frac{d^2y}{dx^2} = \frac{d}{dx}\left( \frac{dy}{dx} \right) = \frac{\frac{d}{dt}\left( \frac{dy}{dx} \right)}{\frac{dx}{dt}}$$

#### 2. Parametric Arc Length
If the curve is traversed exactly once without retracing as $t$ increases from $\alpha$ to $\beta$:
$$L = \int_\alpha^\beta \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

#### 3. Surface Area of Revolution
- **Rotation about the $x$-axis ($y(t) \ge 0$):**
  $$S_x = \int_\alpha^\beta 2\pi y(t) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$
- **Rotation about the $y$-axis ($x(t) \ge 0$):**
  $$S_y = \int_\alpha^\beta 2\pi x(t) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$

#### 4. Area Under a Parametric Curve
$$A = \int_\alpha^\beta y(t) x'(t) \, dt$$

### Example
Consider the cycloid parameterized by:
$$x = 2(t - \sin t), \quad y = 2(1 - \cos t), \quad 0 \le t \le 2\pi$$
1. Find the equation of the tangent line to the curve at $t = \frac{\pi}{3}$.
2. Determine the concavity $\frac{d^2y}{dx^2}$ at $t = \frac{\pi}{3}$.
3. Calculate the total arc length $L$ of one full arch ($t \in [0, 2\pi]$).

**Part 1: Tangent Line Equation at $t = \pi/3$**
Compute the parametric derivatives:
$$\frac{dx}{dt} = 2(1 - \cos t), \quad \frac{dy}{dt} = 2\sin t$$
Evaluate at $t = \frac{\pi}{3}$:
$$x\left(\frac{\pi}{3}\right) = 2\left(\frac{\pi}{3} - \frac{\sqrt{3}}{2}\right) = \frac{2\pi}{3} - \sqrt{3}, \quad y\left(\frac{\pi}{3}\right) = 2\left(1 - \frac{1}{2}\right) = 1$$
$$\frac{dy}{dx} = \frac{2\sin(\pi/3)}{2(1 - \cos(\pi/3))} = \frac{\sqrt{3}/2}{1/2} = \sqrt{3}$$

Equation of the tangent line:
$$y - 1 = \sqrt{3}\left(x - \left(\frac{2\pi}{3} - \sqrt{3}\right)\right) \implies y = \sqrt{3}x - \frac{2\pi\sqrt{3}}{3} + 4$$

**Part 2: Second Derivative and Concavity**
$$\frac{dy}{dx} = \frac{\sin t}{1 - \cos t}$$
$$\frac{d}{dt}\left(\frac{dy}{dx}\right) = \frac{\cos t(1 - \cos t) - \sin t(\sin t)}{(1 - \cos t)^2} = \frac{\cos t - 1}{(1 - \cos t)^2} = -\frac{1}{1 - \cos t}$$
$$\frac{d^2y}{dx^2} = \frac{-\frac{1}{1 - \cos t}}{2(1 - \cos t)} = -\frac{1}{2(1 - \cos t)^2}$$
At $t = \frac{\pi}{3}$:
$$\frac{d^2y}{dx^2} = -\frac{1}{2(1 - 1/2)^2} = -\frac{1}{2(1/4)} = -2 < 0 \implies \text{\textbf{concave down}}.$$

**Part 3: Total Arc Length of One Arch**
$$\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 = 4(1 - \cos t)^2 + 4\sin^2 t = 8(1 - \cos t) = 16\sin^2\left(\frac{t}{2}\right)$$
$$L = \int_0^{2\pi} 4\sin\left(\frac{t}{2}\right) \, dt = \left[ -8\cos\left(\frac{t}{2}\right) \right]_0^{2\pi} = -8(-1) - (-8(1)) = 16$$

### Related
- [[The Derivative]]
- [[The Chain Rule]]
- [[Arc Length]]
- [[Surface Area of Revolution]]
- [[Calculus of Vector-Valued Functions]]
- [[Vector Valued Functions]]
- [[Polar Coordinates and Curves]]
- [[Definite Integrals]]

---
#math/calculus #spring2026
