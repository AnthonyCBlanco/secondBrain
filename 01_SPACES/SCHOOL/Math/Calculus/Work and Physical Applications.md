## Work and Physical Applications

### Idea
In physics, mechanical work is defined as the measure of energy transfer when an applied force causes a displacement. For a constant force, work is given by $W = F \cdot d$.

When the applied force varies continuously with position $x$, or when different portions of a physical system—such as liquid in a tank, a hanging cable, or an elastic spring—move across different distances, definite integration is required to sum the infinitesimal work elements $dW = F(x)\,dx$. 

Core Calculus 2 applications include:
1. **Hooke's Law:** Calculating work done in compressing or stretching elastic springs.
2. **Pumping Liquids:** Calculating total work required to empty fluid reservoirs against gravity.
3. **Hauling Heavy Cables:** Lifting flexible ropes or chains with non-negligible mass density.
4. **Hydrostatic Force:** Computing total fluid pressure force exerted on submerged vertical surfaces.

### Formally
#### General Definition of Work for Variable Force
$$W = \lim_{n \to \infty} \sum_{i=1}^n F(x_i^*) \Delta x = \int_a^b F(x) \, dx$$

#### 1. Hooke's Law for Springs
The restoring force required to hold a spring stretched $x$ units beyond its natural equilibrium length is:
$$F(x) = kx \quad (k = \text{spring constant})$$
The work done in stretching the spring from $x = a$ to $x = b$ is:
$$W = \int_a^b kx \, dx = \left[ \frac{1}{2}kx^2 \right]_a^b = \frac{1}{2}k(b^2 - a^2)$$

#### 2. Pumping Liquids from Tanks
For a horizontal cross-sectional fluid slice at height $y$ with thickness $\Delta y$:
- Cross-sectional area: $A(y)$
- Volume of slice: $\Delta V = A(y)\Delta y$
- Weight / Differential Force: $\Delta F = \rho g A(y)\Delta y$ (where $\rho$ is density, $g$ is gravitational acceleration)
- Displacement distance to exit: $d(y) = y_{\text{exit}} - y$
- Total Work Integral:
  $$W = \int_{y_{\text{bottom}}}^{y_{\text{top}}} \rho g A(y) (y_{\text{exit}} - y) \, dy$$

#### 3. Lifting Heavy Chains / Cables
For a hanging cable of length $L$ and linear weight density $\lambda$ (weight per unit length), the work required to pull the entire cable to the top is:
$$W = \int_0^L \lambda (L - x) \, dx = \frac{1}{2}\lambda L^2$$

#### 4. Hydrostatic Fluid Force on Vertical Plates
$$F_{\text{hydro}} = \int_c^d \rho g \cdot (\text{depth}(y)) \cdot (\text{width}(y)) \, dy$$

### Example
A force of $40\text{ N}$ is required to hold a spring stretched $0.1\text{ m}$ beyond its natural equilibrium length. Find the total work done in stretching the spring from $0.1\text{ m}$ to $0.2\text{ m}$ beyond its natural length.

**Step 1: Calculate the spring constant $k$ using Hooke's Law**
$$F = kx \implies 40 = k(0.1) \implies k = \frac{40}{0.1} = 400\text{ N/m}$$

**Step 2: Set up the work integral**
With $F(x) = 400x$, the work done stretching from $a = 0.1\text{ m}$ to $b = 0.2\text{ m}$ is:
$$W = \int_{0.1}^{0.2} 400x \, dx$$

**Step 3: Evaluate the definite integral**
$$W = \left[ 200x^2 \right]_{0.1}^{0.2} = 200\left( (0.2)^2 - (0.1)^2 \right)$$
$$= 200(0.04 - 0.01) = 200(0.03) = 6\text{ J}$$

**Step 4: Conclusion**
The total work done is $6\text{ Joules}$.

### Related
- [[Definite Integrals]]
- [[Fundamental Theorem of Calculus]]
- [[Indefinite Integration]]
- [[The Calculus of Motion]]
- [[Line Integrals]]
- [[Volume by Disks and Washers]]
- [[Improper Integrals]]

---
#math/calculus #spring2026
