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

The **actual change** in the function’s value for a finite change in $x$ is:

$$
\Delta y = f(x + \Delta x) - f(x)
$$

This represents the **true** (nonlinear) change in $y$ as $x$ changes by $\Delta x$.

For very small $\Delta x$, the differential $dy$ closely approximates this actual change:

$$
dy \approx \Delta y
$$

---

### Understanding $\Delta y$ vs. $dy$

| Symbol | Meaning | Interpretation |
|:--|:--|:--|
| $\Delta y$ | Actual change in $y$ | The true difference in function values, $f(x + \Delta x) - f(x)$ |
| $dy$ | Differential (approximate change) | The change predicted by the tangent line using $f'(x)$ |

- $\Delta y$ measures **how much the function actually changes**  
- $dy$ measures **how much the tangent line predicts it should change**  
- For very small $\Delta x$, the two become nearly identical  

---

### Concept Summary

- Differentials are **approximations** of small changes in a function’s output.  
- $\Delta y$ measures the **true** change, while $dy$ measures the **approximate** change.  
- For small intervals, $dy \approx \Delta y$.  
- This relationship is central to **error estimation**, **linearization**, and **calculus-based modeling**.  

---

### Example

Let $y = x^3$.  
Then $dy = 3x^2 \, dx$.

If $x = 2$ and $dx = 0.1$:

$$
dy = 3(2)^2(0.1) = 1.2
$$

Now compute the actual change:

$$
\Delta y = f(2.1) - f(2) = (2.1)^3 - (2)^3 = 9.261 - 8 = 1.261
$$

Comparing both:
- $dy = 1.2$  
- $\Delta y = 1.261$  

→ The differential **slightly underestimates** the true change, but is close — showing its value as an approximation.

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
- [[Linearization]]

---

#math #calculus #differentiation #concepts
