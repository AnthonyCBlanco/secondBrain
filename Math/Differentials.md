### Idea

A **differential** represents an infinitesimally small change in a variable.  
When a function $y = f(x)$ changes due to a small change $dx$ in $x$, the corresponding change in $y$ can be approximated by its **differential** $dy$.

The differential provides a **linear approximation** of how much $y$ changes based on how fast it changes (its derivative).

---

### Definition

If $y = f(x)$ is a differentiable function, then:

$$
dy = f'(x) \, dx
$$

Here:

- $dx$ represents an independent small change in $x$  
- $dy$ represents the corresponding change in $y$ predicted by the tangent line  
- The ratio $\frac{dy}{dx}$ equals the derivative $f'(x)$  

---

### Concept Summary

- Differentials are not actual changes but **approximations** of small changes.
- They are foundational in **linearization**, **error estimation**, and **differential equations**.
- For very small $dx$, the approximation $dy \approx \Delta y$ becomes accurate.

---

### Example

Let $y = x^3$.  
Then $dy = 3x^2 \, dx$.

If $x = 2$ and $dx = 0.1$:

$$
dy = 3(2)^2(0.1) = 1.2
$$

So the approximate change in $y$ is $1.2$, meaning when $x$ increases from $2$ to $2.1$, $y$ increases by about $1.2$.

---

### Linear Approximation

Differentials give the linear approximation formula:

$$
f(x + \Delta x) \approx f(x) + f'(x) \, \Delta x
$$

Or equivalently, using differentials:

$$
\Delta y \approx dy
$$

---

### Related Notes

- [[The Derivative]]
- [[The Chain Rule]]
- [[Implicit Differentiation]]

---

#math #calculus #differentiation #concepts
