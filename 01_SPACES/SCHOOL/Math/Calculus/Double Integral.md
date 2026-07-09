### Idea
Just as a standard single [[Definite Integrals|definite integral]] $\int_a^b f(x) \, dx$ calculates the **area** under a curve in 2D space, a **Double Integral** calculates the **volume** under a surface $z = f(x, y)$ over a specific region $R$ in the $xy$-plane. 

If the function you are integrating is simply $f(x, y) = 1$, then the double integral calculates the **area** of the 2D region $R$ itself.

### Formally
The double integral of a function $f(x,y)$ over a region $R$ in the $xy$-plane is denoted as:
$$
\iint_R f(x, y) \, dA
$$
Here, $dA$ represents a tiny element of area. Depending on the coordinate system, $dA$ could be $dx \, dy$ or $dy \, dx$ (in rectangular coordinates) or $r \, dr \, d\theta$ (in polar coordinates).

### Evaluating Double Integrals: Fubini's Theorem
To compute a double integral, we evaluate it as an **iterated integral** (integrating one variable at a time, treating the other as a constant). **Fubini's Theorem** states that if $f(x, y)$ is continuous on a rectangular region $R = [a, b] \times [c, d]$ (meaning $a \le x \le b$ and $c \le y \le d$), you can integrate in either order:

$$
\iint_R f(x, y) \, dA = \int_a^b \int_c^d f(x, y) \, dy \, dx = \int_c^d \int_a^b f(x, y) \, dx \, dy
$$
*Note: Always evaluate from the inside out. In $\int \int f(x, y) \, dy \, dx$, you integrate with respect to $y$ first, and then $x$.*

### Integrating Over General Regions
When the region $R$ is not a perfect rectangle, the bounds of the inner integral will be functions instead of constants.

**Type I Regions (Vertically Simple):**
The region is bounded by constants on the $x$-axis ($a \le x \le b$) and by functions of $x$ on the top and bottom ($g_1(x) \le y \le g_2(x)$). 
You must integrate with respect to $y$ first:
$$
\iint_R f(x, y) \, dA = \int_a^b \int_{g_1(x)}^{g_2(x)} f(x, y) \, dy \, dx
$$

**Type II Regions (Horizontally Simple):**
The region is bounded by constants on the $y$-axis ($c \le y \le d$) and by functions of $y$ on the left and right ($h_1(y) \le x \le h_2(y)$).
You must integrate with respect to $x$ first:
$$
\iint_R f(x, y) \, dA = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x, y) \, dx \, dy
$$
### Integrating Using Polar Coordinates
When the region of integration $R$ is circular (like a disk or a ring) or the integrand involves $x^2 + y^2$, it is often much easier to switch to **Polar Coordinates** $(r, \theta)$.

**The Transformation:**
To convert the integral, substitute every $x$ and $y$ with their polar equivalents:
- $x = r \cos(\theta)$
- $y = r \sin(\theta)$
- $x^2 + y^2 = r^2$

**The Area Element ($dA$):**
The most critical step in the conversion is changing the area element $dA$. In polar coordinates, **$dA = r \, dr \, d\theta$**. You must multiply the integrand by this extra $r$ (the Jacobian determinant).

**The Formula:**
$$
\iint_R f(x, y) \, dA = \int_{\alpha}^{\beta} \int_{h_1(\theta)}^{h_2(\theta)} f(r\cos\theta, r\sin\theta) \, r \, dr \, d\theta
$$
Here, $r$ spans from the inner boundary $h_1(\theta)$ to the outer boundary $h_2(\theta)$, and the angle $\theta$ spans from $\alpha$ to $\beta$.

### Example
**Evaluate $\iint_R xy \, dA$ where $R$ is the rectangular region defined by $0 \le x \le 2$ and $1 \le y \le 3$.**

1. Set up the iterated integral (we will do $dy \, dx$, but $dx \, dy$ works identically due to Fubini's Theorem):
   $$ \int_0^2 \int_1^3 xy \, dy \, dx $$

2. Evaluate the **inner** integral with respect to $y$ (treat $x$ as a constant):
   $$ \int_1^3 xy \, dy = x \left[ \frac{y^2}{2} \right]_1^3 = x \left( \frac{9}{2} - \frac{1}{2} \right) = x \left( \frac{8}{2} \right) = 4x $$

3. Evaluate the **outer** integral with respect to $x$:
   $$ \int_0^2 4x \, dx = \left[ 2x^2 \right]_0^2 = 2(2)^2 - 2(0)^2 = 8 $$

The volume under the surface $z = xy$ over the rectangle $R$ is **$8$**.

### Related
- [[Definite Integrals]]
- [[Multivariable Functions]]
- [[Area by Limit Definition]]

#math/calculus #summer2026