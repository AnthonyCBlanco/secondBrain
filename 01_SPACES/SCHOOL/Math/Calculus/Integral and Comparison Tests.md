## Integral and Comparison Tests

### Idea
For series with strictly positive terms ($a_n > 0$), the sequence of partial sums is strictly monotonically increasing. Consequently, such series converge if and only if their partial sums remain bounded above.

We test boundedness by comparing the series with a continuous improper integral (the Integral Test) or with a known benchmark series whose convergence behavior is already established (the Comparison Tests). 
- The **Integral Test** equates the discrete summation to the continuous area under a positive, decreasing curve.
- The **Direct Comparison Test (DCT)** establishes term-by-term inequalities against known series.
- The **Limit Comparison Test (LCT)** simplifies complex algebraic expressions by analyzing the limiting ratio of dominant asymptotic terms.

### Formally
#### 1. The Integral Test
Let $f(x)$ be a continuous, positive, and decreasing function on $[1, \infty)$ such that $f(n) = a_n$ for all integers $n \ge 1$. Then:
$$\sum_{n=1}^\infty a_n \text{ converges if and only if } \int_1^\infty f(x)\,dx \text{ converges.}$$

#### Integral Test Remainder Estimate
If $\sum_{n=1}^\infty a_n = S$ converges and $R_N = S - S_N$ is the remainder after $N$ terms:
$$\int_{N+1}^\infty f(x)\,dx \le R_N \le \int_N^\infty f(x)\,dx$$

#### 2. The $p$-Series Test
$$\sum_{n=1}^\infty \frac{1}{n^p} = \frac{1}{1^p} + \frac{1}{2^p} + \frac{1}{3^p} + \dots \begin{cases} \text{converges} & \text{if } p > 1 \\ \text{diverges} & \text{if } p \le 1 \end{cases}$$

#### 3. Direct Comparison Test (DCT)
Let $\sum a_n$ and $\sum b_n$ be series with positive terms ($a_n, b_n > 0$) such that $a_n \le b_n$ for all $n \ge N_0$:
1. If $\sum b_n$ converges, then $\sum a_n$ converges.
2. If $\sum a_n$ diverges, then $\sum b_n$ diverges.

#### 4. Limit Comparison Test (LCT)
Let $a_n > 0$ and $b_n > 0$ for all $n$. Evaluate the limit:
$$c = \lim_{n \to \infty} \frac{a_n}{b_n}$$
1. If $0 < c < \infty$, then **both $\sum a_n$ and $\sum b_n$ converge or both diverge**.
2. If $c = 0$ and $\sum b_n$ converges, then $\sum a_n$ converges.
3. If $c = \infty$ and $\sum b_n$ diverges, then $\sum a_n$ diverges.

### Example
Determine the convergence or divergence of the series:
$$\sum_{n=1}^\infty \frac{n^2 + 2\sqrt{n}}{4n^4 - 3n^2 + 1}$$

**Step 1: Identify dominant terms for large $n$**
$$a_n = \frac{n^2 + 2\sqrt{n}}{4n^4 - 3n^2 + 1} \approx \frac{n^2}{4n^4} = \frac{1}{4n^2}$$

**Step 2: Choose comparison benchmark series $b_n$**
Let $b_n = \frac{1}{n^2}$.
The series $\sum_{n=1}^\infty \frac{1}{n^2}$ is a $p$-series with $p = 2 > 1$, which is known to **converge**.

**Step 3: Compute the limit ratio $c$ for the Limit Comparison Test**
$$c = \lim_{n\to\infty} \frac{a_n}{b_n} = \lim_{n\to\infty} \frac{\frac{n^2 + 2\sqrt{n}}{4n^4 - 3n^2 + 1}}{\frac{1}{n^2}} = \lim_{n\to\infty} \frac{n^4 + 2n^{5/2}}{4n^4 - 3n^2 + 1}$$

Divide the numerator and denominator by $n^4$:
$$c = \lim_{n\to\infty} \frac{1 + 2n^{-3/2}}{4 - 3n^{-2} + n^{-4}} = \frac{1 + 0}{4 - 0 + 0} = \frac{1}{4}$$

**Step 4: Conclusion**
Since $c = \frac{1}{4}$ is finite and positive ($0 < c < \infty$), and the comparison series $\sum \frac{1}{n^2}$ converges, by the **Limit Comparison Test**, the series:
$$\sum_{n=1}^\infty \frac{n^2 + 2\sqrt{n}}{4n^4 - 3n^2 + 1} \quad \text{\textbf{converges}}.$$

### Related
- [[Infinite Series and Divergence Test]]
- [[Improper Integrals]]
- [[Definite Integrals]]
- [[Sequences and Limits]]
- [[Alternating Series and Absolute Convergence]]
- [[Ratio and Root Tests]]

---
#math/calculus #spring2026
