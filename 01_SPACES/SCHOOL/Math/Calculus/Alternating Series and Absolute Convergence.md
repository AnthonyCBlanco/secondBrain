## Alternating Series and Absolute Convergence

### Idea
When the terms of an infinite series alternate in sign (positive, negative, positive, ...), consecutive terms cancel each other out. This destructive interference enables series to converge even when the individual term magnitudes do not decay rapidly enough to satisfy positive-term convergence tests.

Convergent series are classified into two fundamentally different categories:
1. **Absolute Convergence:** The series of absolute values converges ($\sum |a_n| < \infty$). These series converge purely through the rapid decay of term magnitudes and are unconditionally invariant under any rearrangement of terms.
2. **Conditional Convergence:** The series converges ($\sum a_n < \infty$), but the series of absolute values diverges ($\sum |a_n| = \infty$). Convergence depends entirely on sign cancellation, and by Riemann's Rearrangement Theorem, reordering terms can alter the sum to any real number or cause divergence.

### Formally
#### Definitions and Fundamental Theorems
- **Alternating Series Form:**
  $$\sum_{n=1}^\infty (-1)^{n-1} b_n \quad \text{or} \quad \sum_{n=1}^\infty (-1)^n b_n \quad \text{where } b_n > 0$$
- **The Alternating Series Test (AST / Leibniz's Theorem):** An alternating series $\sum (-1)^{n-1} b_n$ converges if:
  1. $b_{n+1} \le b_n$ for all $n \ge N_0$ (the sequence $\{b_n\}$ is eventually monotonically decreasing), and
  2. $\lim_{n \to \infty} b_n = 0$.
- **Alternating Series Estimation Theorem:** If $S = \sum_{n=1}^\infty (-1)^{n-1} b_n$ converges by AST, the truncation error $R_N = S - S_N$ is bounded by the magnitude of the first omitted term:
  $$|R_N| = |S - S_N| \le b_{N+1}$$
  Moreover, $R_N$ has the same sign as the first omitted term $(-1)^N b_{N+1}$.
- **Absolute vs. Conditional Convergence:**
  - $\sum a_n$ is **absolutely convergent** if $\sum |a_n|$ converges.
  - $\sum a_n$ is **conditionally convergent** if $\sum a_n$ converges but $\sum |a_n|$ diverges.
- **Absolute Convergence Implication Theorem:**
  $$\text{If } \sum_{n=1}^\infty |a_n| \text{ converges, then } \sum_{n=1}^\infty a_n \text{ converges.}$$
- **Riemann Rearrangement Theorem:** If $\sum a_n$ is conditionally convergent, for any target value $M \in \mathbb{R} \cup \{-\infty, \infty\}$, there exists a permutation $\sigma: \mathbb{N} \to \mathbb{N}$ such that $\sum_{n=1}^\infty a_{\sigma(n)} = M$.

### Example
Determine whether the series is **absolutely convergent**, **conditionally convergent**, or **divergent**:
$$\sum_{n=1}^\infty \frac{(-1)^{n-1} n}{3n^2 + 2}$$

**Step 1: Test for Absolute Convergence ($\sum |a_n|$)**
Consider the series of absolute values:
$$\sum_{n=1}^\infty \left| \frac{(-1)^{n-1} n}{3n^2 + 2} \right| = \sum_{n=1}^\infty \frac{n}{3n^2 + 2}$$

Apply the Limit Comparison Test with the harmonic series $\sum \frac{1}{n}$:
$$c = \lim_{n\to\infty} \frac{\frac{n}{3n^2+2}}{\frac{1}{n}} = \lim_{n\to\infty} \frac{n^2}{3n^2 + 2} = \frac{1}{3}$$
Since $0 < \frac{1}{3} < \infty$ and $\sum \frac{1}{n}$ diverges ($p$-series with $p=1$), $\sum_{n=1}^\infty \frac{n}{3n^2+2}$ **diverges**.
Thus, the original series is **not absolutely convergent**.

**Step 2: Test for Convergence using the Alternating Series Test**
Let $b_n = \frac{n}{3n^2 + 2} > 0$.
1. **Check if $\{b_n\}$ is decreasing:** Consider the continuous function $f(x) = \frac{x}{3x^2 + 2}$:
   $$f'(x) = \frac{(1)(3x^2+2) - x(6x)}{(3x^2+2)^2} = \frac{2 - 3x^2}{(3x^2+2)^2}$$
   For $x \ge 1$, $2 - 3x^2 < 0 \implies f'(x) < 0$. Thus, $b_{n+1} < b_n$ for all $n \ge 1$.
2. **Check the limit:**
   $$\lim_{n\to\infty} b_n = \lim_{n\to\infty} \frac{n}{3n^2 + 2} = 0$$

Both hypotheses of AST are satisfied, so $\sum_{n=1}^\infty \frac{(-1)^{n-1} n}{3n^2 + 2}$ converges.

**Step 3: Conclusion**
Because the series converges but fails to converge absolutely, it is **conditionally convergent**.

### Related
- [[Infinite Series and Divergence Test]]
- [[Integral and Comparison Tests]]
- [[Ratio and Root Tests]]
- [[Power Series and Radius of Convergence]]
- [[Sequences and Limits]]

---
#math/calculus #spring2026
