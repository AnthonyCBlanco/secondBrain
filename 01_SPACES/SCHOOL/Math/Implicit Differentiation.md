# Implicit Differentiation

Implicit differentiation is used when a function is defined **implicitly** rather than explicitly (e.g., $y$ is not isolated). In such cases, $y$ is treated as a function of $x$, and we apply the **chain rule** when differentiating terms involving $y$.

---

## Key Idea
- Differentiate both sides of the equation with respect to $x$.
- Apply the **chain rule**: whenever you differentiate $y$ with respect to $x$, you must multiply by $\frac{dy}{dx}$.
- Solve for $\frac{dy}{dx}$ at the end.

---

## General Steps
1. Start with an equation involving $x$ and $y$.
2. Differentiate both sides w.r.t. $x$.
3. Collect all terms involving $\frac{dy}{dx}$.
4. Solve for $\frac{dy}{dx}$.

---

## Example 1
Differentiate the equation:

$$
x^2 + y^2 = 25
$$

**Solution:**

$$
\frac{d}{dx}(x^2 + y^2) = \frac{d}{dx}(25)
$$

$$
2x + 2y \frac{dy}{dx} = 0
$$

Solve for $\frac{dy}{dx}$:

$$
\frac{dy}{dx} = -\frac{x}{y}
$$

---

## Example 2
Differentiate:

$$
xy + y^3 = 10
$$

**Solution:**

$$
\frac{d}{dx}(xy) + \frac{d}{dx}(y^3) = \frac{d}{dx}(10)
$$

Apply product and chain rule:

$$
x \frac{dy}{dx} + y + 3y^2 \frac{dy}{dx} = 0
$$

Group $\frac{dy}{dx}$ terms:

$$
(x + 3y^2)\frac{dy}{dx} + y = 0
$$

Solve:

$$
\frac{dy}{dx} = -\frac{y}{x + 3y^2}
$$

---

## Applications
- **Curves defined implicitly** (circles, ellipses, etc.).
- **Related rates problems** where multiple variables change with time.
- **Non-explicit functions** where isolating $y$ is impossible or messy.

---

### Links
- [[The Chain Rule]]
- [[The Derivative]]


#calculus #derivatives
