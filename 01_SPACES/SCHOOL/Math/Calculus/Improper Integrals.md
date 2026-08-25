## Improper Integrals

### Idea
A standard Riemann definite integral $\int_a^b f(x)\,dx$ requires both a bounded interval $[a, b]$ and a bounded, continuous (or piecewise continuous) integrand $f(x)$. 

Improper integrals generalize definite integration to scenarios where one or both limits of integration are infinite (Type 1), or where the integrand exhibits an infinite discontinuity (vertical asymptote) within or at the boundaries of the interval of integration (Type 2). 

These integrals are evaluated by formulating them as limits of proper definite integrals. If the corresponding limit exists and equals a finite real number, the improper integral **converges** to that value; if the limit fails to exist or approaches $\pm \infty$, the integral **diverges**.

### Formally
#### Type 1: Infinite Intervals of Integration
1. **Upper Bound Infinite:** If $f(x)$ is continuous on $[a, \infty)$:
   $$\int_a^\infty f(x) \, dx = \lim_{t \to \infty} \int_a^t f(x) \, dx$$
2. **Lower Bound Infinite:** If $f(x)$ is continuous on $(-\infty, b]$:
   $$\int_{-\infty}^b f(x) \, dx = \lim_{t \to -\infty} \int_t^b f(x) \, dx$$
3. **Both Bounds Infinite:** If $f(x)$ is continuous on $(-\infty, \infty)$, choose any real number $c$:
   $$\int_{-\infty}^\infty f(x) \, dx = \int_{-\infty}^c f(x) \, dx + \int_c^\infty f(x) \, dx = \lim_{s \to -\infty} \int_s^c f(x) \, dx + \lim_{t \to \infty} \int_c^t f(x) \, dx$$
   *(The integral converges if and only if both individual limits converge independently).*

#### Type 2: Discontinuous / Unbounded Integrands
1. **Discontinuity at Upper Bound $b$:** If $f(x)$ is continuous on $[a, b)$ and discontinuous at $b$:
   $$\int_a^b f(x) \, dx = \lim_{t \to b^-} \int_a^t f(x) \, dx$$
2. **Discontinuity at Lower Bound $a$:** If $f(x)$ is continuous on $(a, b]$ and discontinuous at $a$:
   $$\int_a^b f(x) \, dx = \lim_{t \to a^+} \int_t^b f(x) \, dx$$
3. **Interior Discontinuity at $c \in (a, b)$:**
   $$\int_a^b f(x) \, dx = \lim_{s \to c^-} \int_a^s f(x) \, dx + \lim_{t \to c^+} \int_t^b f(x) \, dx$$

#### The Canonical $p$-Integral Benchmark
$$\int_1^\infty \frac{1}{x^p} \, dx = \begin{cases} \displaystyle \frac{1}{p - 1} & \text{if } p > 1 \quad (\text{Converges}) \\ \text{Diverges} & \text{if } p \le 1 \end{cases}$$
$$\int_0^1 \frac{1}{x^p} \, dx = \begin{cases} \displaystyle \frac{1}{1 - p} & \text{if } p < 1 \quad (\text{Converges}) \\ \text{Diverges} & \text{if } p \ge 1 \end{cases}$$

#### Direct Comparison Test for Improper Integrals
Let $f(x)$ and $g(x)$ be continuous functions satisfying $0 \le f(x) \le g(x)$ for all $x \ge a$:
1. If $\int_a^\infty g(x) \, dx$ converges, then $\int_a^\infty f(x) \, dx$ converges.
2. If $\int_a^\infty f(x) \, dx$ diverges, then $\int_a^\infty g(x) \, dx$ diverges.

### Example
Evaluate the improper integral and determine whether it converges or diverges:
$$\int_1^\infty \frac{1}{x^2} \, dx$$

**Step 1: Express as the limit of a proper definite integral**
$$\int_1^\infty \frac{1}{x^2} \, dx = \lim_{t \to \infty} \int_1^t x^{-2} \, dx$$

**Step 2: Evaluate the definite integral using the power rule**
$$\int_1^t x^{-2} \, dx = \left[ -\frac{1}{x} \right]_1^t = \left( -\frac{1}{t} - \left( -\frac{1}{1} \right) \right) = 1 - \frac{1}{t}$$

**Step 3: Evaluate the limit as $t \to \infty$**
$$\lim_{t \to \infty} \left( 1 - \frac{1}{t} \right) = 1 - 0 = 1$$

**Step 4: Conclusion**
The improper integral **converges**, and its exact value is $1$.

### Related
- [[Definite Integrals]]
- [[Limits at Infinity]]
- [[One-Sided Limits]]
- [[Fundamental Theorem of Calculus]]
- [[Integral and Comparison Tests]]
- [[Infinite Series and Divergence Test]]
- [[Partial Fractions]]

---
#math/calculus #spring2026
