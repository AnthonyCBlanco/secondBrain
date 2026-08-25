## Taylor and Maclaurin Series

### Idea
Taylor and Maclaurin series represent smooth, infinitely differentiable functions as infinite power series whose coefficients are generated from the function's higher-order derivatives evaluated at a single anchor point $x = a$.

Truncating a Taylor series generates a **Taylor polynomial** $T_n(x)$, which provides the optimal local polynomial approximation of degree $n$ near the center. This framework enables the evaluation and approximation of transcendental functions ($e^x, \sin x, \ln x, \arctan x$) with rigorous error bounds via Taylor's Inequality, and enables the definite integration of non-elementary functions.

### Formally
#### Taylor and Maclaurin Series Definitions
- **Taylor Series centered at $x = a$:** If $f(x)$ has derivatives of all orders at $x = a$:
  $$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!} (x - a)^n = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \frac{f'''(a)}{3!}(x - a)^3 + \dots$$
- **Maclaurin Series (centered at $a = 0$):**
  $$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} x^n = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f'''(0)}{3!}x^3 + \dots$$

#### Taylor Polynomial of Degree $n$
$$T_n(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x - a)^k$$

#### Taylor's Inequality (Remainder Bound)
Let $f(x) = T_n(x) + R_n(x)$. If $|f^{(n+1)}(x)| \le M$ for all $|x - a| \le d$, the remainder $R_n(x)$ satisfies:
$$|R_n(x)| \le \frac{M}{(n + 1)!} |x - a|^{n+1} \quad \text{for } |x - a| \le d$$

#### Fundamental Canonical Maclaurin Series Table
$$\begin{aligned}
\frac{1}{1 - x} &= \sum_{n=0}^\infty x^n = 1 + x + x^2 + x^3 + \dots & R = 1, \quad I = (-1, 1) \\
e^x &= \sum_{n=0}^\infty \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots & R = \infty, \quad I = (-\infty, \infty) \\
\sin x &= \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots & R = \infty, \quad I = (-\infty, \infty) \\
\cos x &= \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots & R = \infty, \quad I = (-\infty, \infty) \\
\ln(1 + x) &= \sum_{n=1}^\infty \frac{(-1)^{n-1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots & R = 1, \quad I = (-1, 1] \\
\arctan x &= \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{2n+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \dots & R = 1, \quad I = [-1, 1]
\end{aligned}$$

### Example
1. Find the Maclaurin series for $f(x) = x^3 \cos(2x^2)$ in sigma notation.
2. Use the first two non-zero terms to approximate $\int_0^{0.5} x^3 \cos(2x^2)\,dx$ and determine an error bound.

**Part 1: Series Derivation**
Start with the standard series for $\cos(u) = \sum_{n=0}^\infty \frac{(-1)^n u^{2n}}{(2n)!}$.
Substitute $u = 2x^2$:
$$\cos(2x^2) = \sum_{n=0}^\infty \frac{(-1)^n (2x^2)^{2n}}{(2n)!} = \sum_{n=0}^\infty \frac{(-1)^n 2^{2n} x^{4n}}{(2n)!}$$

Multiply through by $x^3$:
$$f(x) = x^3 \cos(2x^2) = \sum_{n=0}^\infty \frac{(-1)^n 2^{2n} x^{4n+3}}{(2n)!} = x^3 - 2x^7 + \frac{2}{3}x^{11} - \dots$$

**Part 2: Definite Integral Approximation & Error Estimation**
Integrate term-by-term:
$$\int_0^{0.5} \left( x^3 - 2x^7 + \frac{2}{3}x^{11} - \dots \right) dx = \left[ \frac{x^4}{4} - \frac{x^8}{4} + \frac{x^{12}}{18} - \dots \right]_0^{0.5}$$

Evaluate using the first two terms at $x = 0.5 = \frac{1}{2}$:
$$\text{Estimate} \approx \frac{(1/2)^4}{4} - \frac{(1/2)^8}{4} = \frac{1}{64} - \frac{1}{1024} = \frac{15}{1024} \approx 0.0146484$$

By the Alternating Series Estimation Theorem, the truncation error is bounded by the magnitude of the next omitted term:
$$|R_2| \le \frac{(1/2)^{12}}{18} = \frac{1}{4096 \times 18} = \frac{1}{73728} \approx 1.356 \times 10^{-5}$$

### Related
- [[Power Series and Radius of Convergence]]
- [[The Derivative]]
- [[Linearization]]
- [[Integration by Parts]]
- [[Indefinite Integration]]
- [[Limits]]

---
#math/calculus #spring2026
