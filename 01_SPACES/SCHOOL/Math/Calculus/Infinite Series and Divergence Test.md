## Infinite Series and Divergence Test

### Idea
An infinite series is the formal sum of the infinite sequence of numbers: $\sum_{n=1}^\infty a_n = a_1 + a_2 + a_3 + \dots$. Because an infinite number of additions cannot be performed directly, the sum of a series is defined as the limit of its sequence of finite partial sums $S_N = \sum_{n=1}^N a_n$.

If the sequence of partial sums $\{S_N\}$ converges to a finite number $S$, the infinite series is said to **converge** and its sum is $S$. If $\{S_N\}$ diverges, the series has no finite sum. The **Divergence Test** ($n$-th term test) is the primary first-line diagnostic: if the individual terms $a_n$ do not approach zero as $n \to \infty$, the partial sums cannot stabilize, and the series must diverge.

### Formally
#### Infinite Series and Partial Sums
For a sequence $\{a_n\}_{n=1}^\infty$, the $N$-th partial sum is:
$$S_N = \sum_{n=1}^N a_n = a_1 + a_2 + \dots + a_N$$
The infinite series $\sum_{n=1}^\infty a_n$ **converges** to the sum $S \in \mathbb{R}$ if:
$$\sum_{n=1}^\infty a_n = \lim_{N \to \infty} S_N = S$$
If $\lim_{N\to\infty} S_N$ fails to exist or is infinite, the series **diverges**.

#### The Divergence Test ($n$-th Term Test for Divergence)
$$\text{If } \lim_{n \to \infty} a_n \neq 0 \text{ or does not exist, then } \sum_{n=1}^\infty a_n \text{ diverges.}$$

#### Crucial Caution (The Converse is False)
If $\lim_{n\to\infty} a_n = 0$, the Divergence Test is **inconclusive**. The series may converge or diverge. For example, the harmonic series $\sum_{n=1}^\infty \frac{1}{n}$ diverges even though $\lim_{n\to\infty} \frac{1}{n} = 0$.

#### Geometric Series
$$\sum_{n=1}^\infty a r^{n-1} = a + ar + ar^2 + \dots = \begin{cases} \displaystyle \frac{a}{1 - r} & \text{if } |r| < 1 \\ \text{diverges} & \text{if } |r| \ge 1 \quad (a \neq 0) \end{cases}$$

#### Telescoping Series
A series in which consecutive terms cancel in the partial sums:
$$S_N = \sum_{n=1}^N (b_n - b_{n+1}) = b_1 - b_{N+1} \implies \sum_{n=1}^\infty (b_n - b_{n+1}) = b_1 - \lim_{N\to\infty} b_{N+1}$$

### Example
Determine whether the series converges or diverges, and if it converges, compute its exact sum:
$$\sum_{n=1}^\infty \frac{3}{n(n+3)}$$

**Step 1: Check the Divergence Test**
$$\lim_{n\to\infty} a_n = \lim_{n\to\infty} \frac{3}{n(n+3)} = 0$$
The Divergence Test is inconclusive, so we analyze the partial sums.

**Step 2: Decompose the general term using partial fractions**
$$\frac{3}{n(n+3)} = \frac{A}{n} + \frac{B}{n+3} \implies 3 = A(n+3) + Bn$$
- Setting $n = 0 \implies 3 = 3A \implies A = 1$.
- Setting $n = -3 \implies 3 = -3B \implies B = -1$.
Thus, $a_n = \frac{1}{n} - \frac{1}{n+3}$.

**Step 3: Expand the $N$-th partial sum $S_N$ to observe telescoping cancellation**
$$S_N = \sum_{n=1}^N \left( \frac{1}{n} - \frac{1}{n+3} \right)$$
$$= \left( 1 - \frac{1}{4} \right) + \left( \frac{1}{2} - \frac{1}{5} \right) + \left( \frac{1}{3} - \frac{1}{6} \right) + \left( \frac{1}{4} - \frac{1}{7} \right) + \dots + \left( \frac{1}{N-2} - \frac{1}{N+1} \right) + \left( \frac{1}{N-1} - \frac{1}{N+2} \right) + \left( \frac{1}{N} - \frac{1}{N+3} \right)$$

All intermediate terms cancel, leaving the first three positive terms and the last three negative terms:
$$S_N = 1 + \frac{1}{2} + \frac{1}{3} - \frac{1}{N+1} - \frac{1}{N+2} - \frac{1}{N+3} = \frac{11}{6} - \left( \frac{1}{N+1} + \frac{1}{N+2} + \frac{1}{N+3} \right)$$

**Step 4: Take the limit of $S_N$ as $N \to \infty$**
$$\lim_{N\to\infty} S_N = \frac{11}{6} - (0 + 0 + 0) = \frac{11}{6}$$

**Step 5: Conclusion**
The series **converges** to the exact sum $\frac{11}{6}$.

### Related
- [[Sequences and Limits]]
- [[Sigma Notation]]
- [[Limits at Infinity]]
- [[Integral and Comparison Tests]]
- [[Partial Fractions]]
- [[Geometric Series]]

---
#math/calculus #spring2026
