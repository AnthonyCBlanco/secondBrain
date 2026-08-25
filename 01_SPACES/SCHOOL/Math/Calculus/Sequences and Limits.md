## Sequences and Limits

### Idea
An infinite sequence is an ordered, countably infinite progression of real numbers indexed by the natural numbers: $a_1, a_2, a_3, \dots, a_n, \dots$. Rather than summing the terms, the study of sequences investigates their asymptotic behavior as $n \to \infty$.

Intuitively, if the numbers $a_n$ cluster indefinitely close to a single finite target value $L$ as $n$ grows without bound, the sequence **converges** to $L$. If the sequence oscillates without settling (such as $(-1)^n$) or grows without bound (such as $n^2$), it **diverges**. Sequences form the foundational discrete scaffolding upon which continuous infinite series and function expansions are constructed.

### Formally
#### Formal Definitions
- **Sequence:** A real sequence is a function $a: \mathbb{N} \to \mathbb{R}$, denoted $\{a_n\}_{n=1}^\infty$ or simply $\{a_n\}$, where $a(n) = a_n$.
- **Convergence & Limit ($\varepsilon-N$ Definition):** A sequence $\{a_n\}$ converges to a limit $L \in \mathbb{R}$, written $\lim_{n \to \infty} a_n = L$, if for every $\varepsilon > 0$, there exists an integer $N \in \mathbb{N}$ such that:
  $$|a_n - L| < \varepsilon \quad \text{for all } n > N$$
  If no such finite $L$ exists, the sequence **diverges**.

#### Sequence Limit Properties and Theorems
1. **Algebraic Limit Laws:** If $\lim_{n\to\infty} a_n = L$ and $\lim_{n\to\infty} b_n = M$, then:
   - $\lim_{n\to\infty} (c a_n + d b_n) = c L + d M$
   - $\lim_{n\to\infty} (a_n b_n) = L M$
   - $\lim_{n\to\infty} \frac{a_n}{b_n} = \frac{L}{M} \quad (M \neq 0, b_n \neq 0)$
   - $\lim_{n\to\infty} (a_n)^p = L^p \quad (p > 0, L > 0)$
2. **Continuous Function Theorem:** If $\lim_{n\to\infty} a_n = L$ and $f$ is continuous at $L$, then $\lim_{n\to\infty} f(a_n) = f(L)$.
3. **Squeeze Theorem for Sequences:** If $a_n \le b_n \le c_n$ for all $n \ge N_0$ and $\lim_{n\to\infty} a_n = \lim_{n\to\infty} c_n = L$, then $\lim_{n\to\infty} b_n = L$.
4. **Absolute Value Theorem:** If $\lim_{n\to\infty} |a_n| = 0$, then $\lim_{n\to\infty} a_n = 0$.
5. **Geometric Sequence Limit:**
   $$\lim_{n\to\infty} r^n = \begin{cases} 0 & \text{if } |r| < 1 \\ 1 & \text{if } r = 1 \\ \text{diverges} & \text{if } r > 1 \text{ or } r \le -1 \end{cases}$$
6. **Monotone Convergence Theorem:** Every bounded, monotonic sequence is convergent:
   - If $\{a_n\}$ is non-decreasing ($a_n \le a_{n+1}$) and bounded above ($a_n \le M$), then $\lim_{n\to\infty} a_n = \sup \{a_n\}$.
   - If $\{a_n\}$ is non-increasing ($a_n \ge a_{n+1}$) and bounded below ($a_n \ge m$), then $\lim_{n\to\infty} a_n = \inf \{a_n\}$.

### Example
Determine whether the sequence $\{a_n\}_{n=1}^\infty$ defined by
$$a_n = \frac{4n^2 + (-1)^n \ln(n)}{3n^2 + 5n}$$
converges or diverges. If it converges, find its limit.

**Step 1: Divide numerator and denominator by the dominant power $n^2$**
$$a_n = \frac{4 + (-1)^n \frac{\ln(n)}{n^2}}{3 + \frac{5}{n}}$$

**Step 2: Analyze the asymptotic behavior of the oscillatory term via the Squeeze Theorem**
Since $-1 \le (-1)^n \le 1$ and $\ln(n) > 0$ for $n \ge 2$:
$$-\frac{\ln(n)}{n^2} \le (-1)^n \frac{\ln(n)}{n^2} \le \frac{\ln(n)}{n^2}$$

Evaluate the bounding limit using L'Hôpital's Rule on the associated continuous function $f(x) = \frac{\ln x}{x^2}$:
$$\lim_{x\to\infty} \frac{\ln x}{x^2} = \lim_{x\to\infty} \frac{\frac{1}{x}}{2x} = \lim_{x\to\infty} \frac{1}{2x^2} = 0$$

By the Squeeze Theorem for Sequences, $\lim_{n\to\infty} (-1)^n \frac{\ln(n)}{n^2} = 0$.

**Step 3: Evaluate the algebraic limit**
$$\lim_{n\to\infty} a_n = \frac{4 + 0}{3 + 0} = \frac{4}{3}$$

**Step 4: Conclusion**
The sequence **converges** to $\frac{4}{3}$.

### Related
- [[Limits]]
- [[Limits at Infinity]]
- [[Continuity and Limits]]
- [[The squeeze theorem]]
- [[Infinite Series and Divergence Test]]
- [[Sigma Notation]]
- [[Basics Of Calculus]]

---
#math/calculus #spring2026
