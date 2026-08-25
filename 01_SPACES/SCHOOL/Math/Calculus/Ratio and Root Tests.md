## Ratio and Root Tests

### Idea
The Ratio and Root Tests evaluate the absolute convergence of an infinite series by comparing its asymptotic decay rate to that of a **geometric series**.

The **Ratio Test** analyzes the limiting ratio between consecutive terms $\left|\frac{a_{n+1}}{a_n}\right|$. It is the premier diagnostic tool whenever terms feature factorials ($n!$) or products of exponential sequences ($k^n$). 

The **Root Test** analyzes the limiting $n$-th root of terms $\sqrt[n]{|a_n|}$, making it exceptionally powerful when entire terms are raised to variable $n$-th powers $(f(n))^n$. 

If the limiting ratio or root is strictly less than 1, the series converges exponentially fast; if strictly greater than 1, the terms grow and the series diverges.

### Formally
#### 1. The Ratio Test
Let $\sum a_n$ be an infinite series with non-zero terms ($a_n \neq 0$). Evaluate the limit:
$$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$
1. If $L < 1$, the series $\sum a_n$ is **absolutely convergent** (and therefore convergent).
2. If $L > 1$ or $L = \infty$, the series $\sum a_n$ is **divergent**.
3. If $L = 1$, the test is **inconclusive** (the series may be absolutely convergent, conditionally convergent, or divergent; an alternative test must be applied).

#### 2. The Root Test
Let $\sum a_n$ be an infinite series. Evaluate the limit:
$$L = \lim_{n \to \infty} \sqrt[n]{|a_n|} = \lim_{n \to \infty} |a_n|^{1/n}$$
1. If $L < 1$, the series $\sum a_n$ is **absolutely convergent**.
2. If $L > 1$ or $L = \infty$, the series $\sum a_n$ is **divergent**.
3. If $L = 1$, the test is **inconclusive**.

#### Diagnostic Selection Heuristics
- **Factorials ($n!$, $(2n)!$):** Use the Ratio Test.
- **Exponential terms ($c^n$) mixed with polynomials:** Use the Ratio Test.
- **Outer $n$-th powers ($(g(n))^n$):** Use the Root Test.
- **Rational functions ($P(n)/Q(n)$) or algebraic radicals:** Ratio and Root Tests **always yield $L = 1$ (inconclusive)**; use the Limit Comparison Test instead.

### Example
Determine whether the series converges or diverges:
$$\sum_{n=1}^\infty \frac{n! \, 5^n}{(2n)!}$$

**Step 1: Set up the Ratio Test**
Because the general term features factorials, apply the Ratio Test:
$$a_n = \frac{n! \, 5^n}{(2n)!}, \quad a_{n+1} = \frac{(n+1)! \, 5^{n+1}}{(2(n+1))!} = \frac{(n+1)! \, 5^{n+1}}{(2n+2)!}$$

**Step 2: Simplify the ratio $\left| \frac{a_{n+1}}{a_n} \right|$**
$$\left| \frac{a_{n+1}}{a_n} \right| = \frac{(n+1)! \, 5^{n+1}}{(2n+2)!} \cdot \frac{(2n)!}{n! \, 5^n}$$
$$= \frac{(n+1)n! \cdot 5 \cdot 5^n}{(2n+2)(2n+1)(2n)!} \cdot \frac{(2n)!}{n! \, 5^n}$$
$$= \frac{5(n+1)}{(2n+2)(2n+1)} = \frac{5(n+1)}{2(n+1)(2n+1)} = \frac{5}{2(2n+1)}$$

**Step 3: Evaluate the limit as $n \to \infty$**
$$L = \lim_{n\to\infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n\to\infty} \frac{5}{4n + 2} = 0$$

**Step 4: Conclusion**
Since $L = 0 < 1$, by the **Ratio Test**, the series:
$$\sum_{n=1}^\infty \frac{n! \, 5^n}{(2n)!} \quad \text{\textbf{converges absolutely}}.$$

### Related
- [[Infinite Series and Divergence Test]]
- [[Alternating Series and Absolute Convergence]]
- [[Power Series and Radius of Convergence]]
- [[Taylor and Maclaurin Series]]
- [[Limits at Infinity]]

---
#math/calculus #spring2026
