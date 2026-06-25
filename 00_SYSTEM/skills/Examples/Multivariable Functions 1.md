### Idea
A **Multivariable Function** is a function that depends on more than one independent variable. Instead of just $y = f(x)$, we have situations where a value depends on two, three, or even $n$ inputs.

Common examples include:
- The area of a rectangle: $A(w, h) = w \cdot h$
- The volume of a cylinder: $V(r, h) = \pi r^2 h$
- Temperature at a location: $T(x, y, z, t)$ (depends on position and time)

---

### Formally
A function of two variables $f$ is a rule that assigns to each ordered pair of real numbers $(x, y)$ in a set $D$ (the **domain**) a unique real number denoted by $f(x, y)$.

#### Notation
- **Two variables**: $z = f(x, y)$
  - $x, y$ are **independent variables**.
  - $z$ is the **dependent variable**.
- **Three variables**: $w = f(x, y, z)$

---

### Domain and Range
The **Domain** is the set of all possible input points $(x, y)$ for which the function is defined.
The **Range** is the set of all resulting output values.

**Common Domain Restrictions:**
1. **Division by Zero**: Denominator cannot be zero.
2. **Square Roots (and even roots)**: Radicand must be $\ge 0$ (for real values).
3. **Logarithms**: Argument must be $> 0$.

#### Example
Find the domain of $f(x, y) = \frac{\sqrt{y - x^2}}{1 - x^2}$.
1. From the square root: $y - x^2 \ge 0 \Rightarrow y \ge x^2$.
2. From the denominator: $1 - x^2 \neq 0 \Rightarrow x \neq \pm 1$.
**Domain**: $D = \{(x, y) \mid y \ge x^2, x \neq \pm 1\}$.

---
### Visualization

#### Graphs
The graph of a function of two variables is a **surface** in 3D space. 
For each point $(x, y)$ in the domain, we plot the point $(x, y, f(x, y))$. These surfaces often involve [[Planes in Space]] or quadric surfaces.

#### Level Curves (Contour Maps)
Since 3D surfaces can be hard to draw, we often use **Level Curves**. 
A level curve of a function $f(x, y)$ is the set of all points $(x, y)$ where $f(x, y) = k$ (for some constant $k$).
- These are like topographic lines on a map showing elevation.
- If level curves are close together, the surface is steep.

#### Level Surfaces
For a function of three variables $f(x, y, z)$, the set $f(x, y, z) = k$ forms a **surface** in 3D space.

---

### Limits and Continuity
Limits in multivariable calculus are more complex than basic [[Limits]] because there are infinitely many paths to approach a point $(a, b)$ (unlike just left/right in 1D).

- **Limit existence**: For $\lim_{(x, y) \to (a, b)} f(x, y) = L$ to exist, the function must approach $L$ along **every possible path**.
- **Continuity**: Similar to [[Continuity and Limits]], a multivariable function is continuous if the limit at a point equals the function value at that point.
- **Strategy to show a limit does not exist**: Find two different paths (e.g., $x=0$ and $y=x$) that yield different limit values.

---

### Next Steps
Once we understand the behavior of these functions, we can look at how they change:
- [[Partial Derivative]] (Change along axes)
- [[Directional Derivatives]] (Change along any vector)
- [[Vector Valued Functions]] (Functions that output vectors instead of scalars)

---
### Related
- [[The Derivative]]
- [[Planes in Space]]
- [[Lines in Space]]

#math/calculus #summer2026

