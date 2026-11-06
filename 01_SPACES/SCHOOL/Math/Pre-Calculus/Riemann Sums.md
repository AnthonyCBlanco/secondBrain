---
date: 2026-11-05
aliases:
  - Riemann Sum
  - Riemann Sums
  - Definite Integral Limit Definition
tags:
  - math/calculus
  - math/integration
---
# Riemann Sums

> [!abstract] Core Concept
> A **Riemann sum** approximates the signed area between a function $f(x)$ and the $x$-axis over a closed interval $[a, b]$ by partitioning the region into $n$ vertical rectangles and summing their areas. Taking the limit as the width of the widest subinterval approaches zero yields the exact **definite integral**.

---

## 1. Formal Definition & Partitioning

Let $f(x)$ be defined on a closed interval $[a, b]$.

1. **Partition ($P$):** Divide $[a, b]$ into $n$ subintervals using points:
   $$a = x_0 < x_1 < x_2 < \dots < x_{n-1} < x_n = b$$
2. **Subinterval Width ($\Delta x_i$):** The width of the $i$-th subinterval $[x_{i-1}, x_i]$ is $\Delta x_i = x_i - x_{i-1}$.
   - For a **regular (uniform) partition**, all rectangles have equal width:
     $$\Delta x = \frac{b - a}{n}, \qquad x_i = a + i\Delta x$$
3. **Sample Point ($x_i^*$):** Choose any evaluation point $x_i^* \in [x_{i-1}, x_i]$ to determine the height $f(x_i^*)$ of the $i$-th rectangle.

### General Riemann Sum Formula
$$S_n = \sum_{i=1}^{n} f(x_i^*) \, \Delta x_i$$

---

## 2. Standard Approximation Methods (Uniform $\Delta x$)

| Method | Sample Point $x_i^*$ | Formula ($i = 1 \dots n$) | Monotonic Behavior |
| :--- | :--- | :--- | :--- |
| **Left Riemann Sum ($L_n$)** | Left endpoint: $x_{i-1}$ | $$\Delta x \sum_{i=1}^{n} f(a + (i-1)\Delta x)$$ | **Underestimates** if $f$ is increasing;<br>**Overestimates** if $f$ is decreasing. |
| **Right Riemann Sum ($R_n$)** | Right endpoint: $x_i$ | $$\Delta x \sum_{i=1}^{n} f(a + i\Delta x)$$ | **Overestimates** if $f$ is increasing;<br>**Underestimates** if $f$ is decreasing. |
| **Midpoint Rule ($M_n$)** | Midpoint: $\bar{x}_i = \frac{x_{i-1} + x_i}{2}$ | $$\Delta x \sum_{i=1}^{n} f\!\left(a + \left(i - \tfrac{1}{2}\right)\Delta x\right)$$ | More accurate ($O(n^{-2})$ error); concavity dictates over/underestimate. |
| **Upper Sum ($U_n$)** | $\sup_{[x_{i-1}, x_i]} f(x)$ | $$\sum_{i=1}^{n} M_i \, \Delta x_i$$ | Always $\ge \int_a^b f(x)\,dx$ (Darboux upper bound). |
| **Lower Sum ($L_n^*$)** | $\inf_{[x_{i-1}, x_i]} f(x)$ | $$\sum_{i=1}^{n} m_i \, \Delta x_i$$ | Always $\le \int_a^b f(x)\,dx$ (Darboux lower bound). |

> [!tip] Concavity & Midpoint Error
> - If $f''(x) > 0$ (**concave up**), the Midpoint Rule **underestimates** the integral (tangent line sits below the curve).
> - If $f''(x) < 0$ (**concave down**), the Midpoint Rule **overestimates** the integral.

---

## 3. Connection to the Definite Integral

Let $\|P\| = \max_{1 \le i \le n} \Delta x_i$ denote the **norm (mesh)** of the partition. A function $f$ is **Riemann integrable** on $[a, b]$ if the limit of the Riemann sums exists and is independent of the choice of sample points $x_i^*$:

$$\int_a^b f(x)\,dx = \lim_{\|P\| \to 0} \sum_{i=1}^{n} f(x_i^*) \, \Delta x_i$$

For a **uniform partition** ($\Delta x = \frac{b-a}{n}$), using Right Endpoints gives the standard limit calculation form:
$$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f\!\left(a + i\frac{b-a}{n}\right)\frac{b-a}{n}$$

> [!important] Signed Area Interpretation
> - Where $f(x) > 0$, $f(x_i^*)\Delta x > 0$ contributes **positive** area.
> - Where $f(x) < 0$, $f(x_i^*)\Delta x < 0$ contributes **negative** area.
> - Therefore, the limit computes **net signed area** ($\text{Area}_{\text{above}} - \text{Area}_{\text{below}}$), not total geometric area $\int_a^b |f(x)|\,dx$.

---

## 4. Essential Summation Identities

To evaluate $\lim_{n \to \infty} R_n$ algebraically, factor out terms independent of $i$ and apply closed-form power sums:

$$\sum_{i=1}^{n} c = cn \qquad \sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6} \qquad \sum_{i=1}^{n} i^3 = \left[\frac{n(n+1)}{2}\right]^2$$

---

## 5. Worked Limit Example

> [!example] Evaluate $\displaystyle \int_0^2 x^2\,dx$ using the Limit of a Right Riemann Sum
> 1. **Find $\Delta x$ and $x_i$:**
>    $$\Delta x = \frac{2 - 0}{n} = \frac{2}{n}, \qquad x_i = 0 + i\Delta x = \frac{2i}{n}$$
> 2. **Set up $R_n$:**
>    $$R_n = \sum_{i=1}^{n} f(x_i)\Delta x = \sum_{i=1}^{n} \left(\frac{2i}{n}\right)^2 \left(\frac{2}{n}\right) = \frac{8}{n^3} \sum_{i=1}^{n} i^2$$
> 3. **Substitute power sum identity:**
>    $$R_n = \frac{8}{n^3} \cdot \frac{n(n+1)(2n+1)}{6} = \frac{4}{3} \cdot \frac{2n^3 + 3n^2 + n}{n^3} = \frac{4}{3}\left(2 + \frac{3}{n} + \frac{1}{n^2}\right)$$
> 4. **Take the limit as $n \to \infty$:**
>    $$\int_0^2 x^2\,dx = \lim_{n \to \infty} \frac{4}{3}\left(2 + \frac{3}{n} + \frac{1}{n^2}\right) = \frac{8}{3}$$

---

## 6. Multivariable Extension (Double Riemann Sums)

In Calculus III, partitioning a rectangular domain $R = [a, b] \times [c, d]$ into $m \times n$ subrectangles of area $\Delta A = \Delta x \Delta y$ extends Riemann sums to volumes under a surface $z = f(x, y)$:

$$\iint_R f(x, y)\,dA = \lim_{m, n \to \infty} \sum_{i=1}^{m} \sum_{j=1}^{n} f(x_{ij}^*, y_{ij}^*) \, \Delta A$$

---

## Related Notes
- [[Fundamental Theorem of Calculus]]
- [[Numerical Integration - Trapezoidal and Simpson's Rules]]
- [[Double Integrals over Rectangular Regions]]