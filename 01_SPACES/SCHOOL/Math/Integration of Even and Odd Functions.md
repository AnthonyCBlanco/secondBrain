### Idea
Many integrals become much easier to evaluate when the integrand has **symmetry**.  
Functions that are **even** or **odd** exhibit predictable behavior over symmetric intervals, and this allows us to simplify definite integrals drastically.

Understanding these symmetry properties helps avoid unnecessary computation.

---

### Definitions

#### Even Function  
A function $f(x)$ is **even** if:  
$$
f(-x) = f(x)
$$  
Graphically, an even function is symmetric about the **y-axis**.

Examples:  
- $f(x) = x^2$  
- $f(x) = \cos x$  
- $f(x) = |x|$

---

#### Odd Function  
A function $f(x)$ is **odd** if:  
$$
f(-x) = -f(x)
$$  
Graphically, an odd function is symmetric about the **origin**.

Examples:  
- $f(x) = x^3$  
- $f(x) = \sin x$  
- $f(x) = x$

---

### Properties of Symmetric Integrals

#### 1. Integrals of Even Functions  
If $f(x)$ is even, then:

$$
\int_{-a}^{a} f(x)\,dx = 2 \int_{0}^{a} f(x)\,dx
$$

**Reason:**  
Area on the left side of the y-axis is the same as area on the right side.

---

#### 2. Integrals of Odd Functions  
If $f(x)$ is odd, then:

$$
\int_{-a}^{a} f(x)\,dx = 0
$$

**Reason:**  
The positive area on $(0, a)$ cancels perfectly with the negative area on $(-a, 0)$.

---

### Why These Rules Work

Using substitution $u = -x$, we find:

For odd functions:
$$
\int_{-a}^a f(x)\,dx 
= \int_a^{-a} f(-u)(-du)
= \int_{-a}^a -f(u)\,du = 0
$$

For even functions:
$$
\int_{-a}^a f(x)\,dx 
= 2\int_0^a f(x)\,dx
$$

---

### Examples

#### Example 1: Even Function  
Evaluate:
$$
\int_{-3}^3 (4x^2 + 2)\,dx
$$

Since $4x^2 + 2$ is even:  
$$
2 \int_{0}^3 (4x^2 + 2)\,dx
$$

Compute:
$$
2\left[\frac{4x^3}{3} + 2x\right]_0^3 
= 2\left[\frac{108}{3} + 6\right]
= 2(36 + 6)
= 84
$$

---

#### Example 2: Odd Function  
Evaluate:
$$
\int_{-5}^5 (x^3 - x)\,dx
$$

The function $x^3 - x$ is **odd**.

Thus:
$$
\int_{-5}^5 (x^3 - x)\,dx = 0
$$

---

### Practical Uses
- Quickly determine if a symmetric integral is zero.
- Cut computation time in half by integrating from $0$ to $a$.
- Recognize symmetry in trigonometric integrals.

---

### Common Trigonometric Symmetry

| Function | Symmetry | Notes |
|-----------|------------|--------|
| $\sin x$ | Odd | Integral over $[-a, a]$ is 0 |
| $\cos x$ | Even | Integral doubles from 0 to $a$ |
| $\tan x$ | Odd | Defined on symmetric intervals excluding discontinuities |
| $\sec x$ | Even | Useful in symmetric trig integrals |

---

### Concept Summary

| Concept | Formula | Meaning |
|----------|-----------|-----------|
| Even function | $f(-x) = f(x)$ | y-axis symmetry |
| Odd function | $f(-x) = -f(x)$ | Origin symmetry |
| Even integral rule | $\int_{-a}^{a} f(x) dx = 2\int_0^a f(x)\,dx$ | Double right-side area |
| Odd integral rule | $\int_{-a}^{a} f(x) dx = 0$ | Areas cancel |

---

### Related Notes
- [[Indefinite Integration]]
- [[Definite Integrals]]
- [[Riemann Sums]]
- [[Fundamental Theorem of Calculus]]
- [[Integration by Substitution]]

---

#math #calculus #integrals #symmetry
