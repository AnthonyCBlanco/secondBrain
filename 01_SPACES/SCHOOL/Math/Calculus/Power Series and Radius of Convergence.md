## Power Series and Radius of Convergence

### Idea
A power series is an "infinite polynomial" centered at a fixed real point $x = a$. Unlike classical algebraic polynomials that are defined over all real numbers, a power series generally converges only on a specific domain of $x$ values.

The set of all $x$ values for which the series converges is called its **Interval of Convergence ($I$)**, and half the width of this interval is the **Radius of Convergence ($R$)**. Inside the open disk $|x - a| < R$, the power series defines a smooth, continuous, and infinitely differentiable function that can be integrated and differentiated term-by-term, preserving the exact same radius of convergence.

### Formally
#### Power Series Definition
A power series centered at $x = a$ has the form:
$$\sum_{n=0}^\infty c_n (x - a)^n = c_0 + c_1(x - a) + c_2(x - a)^2 + c_3(x - a)^3 + \dots$$
where $c_n \in \mathbb{R}$ are constant coefficients and $a \in \mathbb{R}$ is the center.

#### Fundamental Convergence Trichotomy Theorem
For any power series $\sum c_n (x - a)^n$, exactly one of the following three conditions holds:
1. The series converges **only at the center** $x = a$ ($R = 0$, $I = \{a\}$).
2. The series converges **for all real numbers** $x \in \mathbb{R}$ ($R = \infty$, $I = (-\infty, \infty)$).
3. There exists a finite positive number $R > 0$ such that the series converges absolutely for $|x - a| < R$ and diverges for $|x - a| > R$.

#### The Interval of Convergence ($I$)
When $R > 0$, the interval of convergence consists of $(a - R, a + R)$ together with any endpoints where the series converges:
$$(a - R, a + R), \quad [a - R, a + R), \quad (a - R, a + R], \quad \text{or} \quad [a - R, a + R]$$
Endpoints must **always be tested independently** using non-power-series tests (AST, Integral Test, Comparison Tests).

#### Calculating the Radius of Convergence
Applying the Ratio Test:
$$L = \lim_{n\to\infty} \left| \frac{c_{n+1}(x - a)^{n+1}}{c_n(x - a)^n} \right| = |x - a| \lim_{n\to\infty} \left| \frac{c_{n+1}}{c_n} \right| < 1 \implies R = \frac{1}{\lim_{n\to\infty} \left|\frac{c_{n+1}}{c_n}\right|}$$

#### Term-by-Term Calculus Operations
If $f(x) = \sum_{n=0}^\infty c_n (x - a)^n$ has radius of convergence $R > 0$:
1. **Differentiation:**
   $$f'(x) = \frac{d}{dx}\left[ \sum_{n=0}^\infty c_n (x - a)^n \right] = \sum_{n=1}^\infty n c_n (x - a)^{n-1}$$
2. **Integration:**
   $$\int f(x) \, dx = C + \sum_{n=0}^\infty \frac{c_n}{n + 1} (x - a)^{n+1}$$
Both derived series share the **exact same radius of convergence $R$**.

### Example
Find the radius of convergence $R$ and the exact interval of convergence $I$ for the power series:
$$\sum_{n=1}^\infty \frac{(-1)^n (x - 3)^n}{n \cdot 4^n}$$

**Step 1: Apply the Ratio Test for the Radius of Convergence**
Let $u_n = \frac{(-1)^n (x - 3)^n}{n \cdot 4^n}$. Compute $\lim_{n\to\infty} \left| \frac{u_{n+1}}{u_n} \right|$:
$$\lim_{n\to\infty} \left| \frac{(-1)^{n+1}(x - 3)^{n+1}}{(n + 1) 4^{n+1}} \cdot \frac{n \cdot 4^n}{(-1)^n (x - 3)^n} \right| = \lim_{n\to\infty} \frac{|x - 3|}{4} \cdot \frac{n}{n + 1} = \frac{|x - 3|}{4}$$

Set the ratio strictly less than 1 for absolute convergence:
$$\frac{|x - 3|}{4} < 1 \iff |x - 3| < 4$$
Thus, the **Radius of Convergence is $R = 4$**.

**Step 2: Determine the open interval of convergence**
$$|x - 3| < 4 \implies -4 < x - 3 < 4 \implies -1 < x < 7$$

**Step 3: Test endpoints individually**
- **Endpoint $x = 7$:**
  $$\sum_{n=1}^\infty \frac{(-1)^n (7 - 3)^n}{n \cdot 4^n} = \sum_{n=1}^\infty \frac{(-1)^n 4^n}{n \cdot 4^n} = \sum_{n=1}^\infty \frac{(-1)^n}{n}$$
  This is the alternating harmonic series, which **converges** by the Alternating Series Test.
- **Endpoint $x = -1$:**
  $$\sum_{n=1}^\infty \frac{(-1)^n (-1 - 3)^n}{n \cdot 4^n} = \sum_{n=1}^\infty \frac{(-1)^n (-4)^n}{n \cdot 4^n} = \sum_{n=1}^\infty \frac{(-1)^n (-1)^n 4^n}{n \cdot 4^n} = \sum_{n=1}^\infty \frac{1}{n}$$
  This is the harmonic series ($p$-series with $p = 1$), which **diverges**.

**Step 4: Conclusion**
- **Radius of Convergence:** $R = 4$
- **Interval of Convergence:** $I = (-1, 7]$

### Related
- [[Ratio and Root Tests]]
- [[Taylor and Maclaurin Series]]
- [[Infinite Series and Divergence Test]]
- [[The Derivative]]
- [[Definite Integrals]]
- [[Indefinite Integration]]

---
#math/calculus #spring2026
