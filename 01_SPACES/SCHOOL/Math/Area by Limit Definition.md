# Area Under a Curve (Limit Definition)

### Idea

The **area under a curve** represents the **accumulated value** of a function over an interval.  
When the function $f(x)$ is positive on $[a, b]$, the area under its graph corresponds to the **region between the curve and the x-axis**.

Before defining the **definite integral**, we can approximate this area using **rectangular sums** and then take the **limit** as the rectangles become infinitely thin.

---

### Conceptual Overview

To find the area under $y = f(x)$ from $x = a$ to $x = b$, we:

1. Divide the interval $[a, b]$ into $n$ equal subintervals of width  
   $$
   \Delta x = \frac{b - a}{n}
   $$
2. Choose a sample point $x_i^*$ in each subinterval.  
3. Approximate the area using rectangles of height $f(x_i^*)$ and width $\Delta x$:
   $$
   A_n = \sum_{i=1}^{n} f(x_i^*) \, \Delta x
   $$
4. Take the **limit as $n \to \infty$** to obtain the exact area:
   $$
   A = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \, \Delta x
   $$

This is the **limit definition of the definite integral**.

---

### Formally

If $f(x)$ is continuous on $[a, b]$, the area under the curve is defined by:

$$
\text{Area} = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x
$$

where:
- $a$ = lower bound  
- $b$ = upper bound  
- $n$ = number of subintervals  
- $\Delta x = \frac{b - a}{n}$  
- $x_i^*$ = sample point in the $i^{\text{th}}$ subinterval

If we choose **right endpoints**, then:
$$
x_i^* = a + i\Delta x
$$

---

### Example — Area Under a Line

Find the area under $f(x) = x$ on $[0, 2]$ using the limit definition.

**Step 1:**  
$\Delta x = \frac{2 - 0}{n} = \frac{2}{n}$

**Step 2:**  
Using right endpoints, $x_i = 0 + i\Delta x = \frac{2i}{n}$

**Step 3:**  
Substitute into the sum:
$$
A_n = \sum_{i=1}^{n} f(x_i) \Delta x = \sum_{i=1}^{n} \left( \frac{2i}{n} \right) \left( \frac{2}{n} \right)
$$
$$
A_n = \frac{4}{n^2} \sum_{i=1}^{n} i
$$

**Step 4:**  
Use the formula $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$:
$$
A_n = \frac{4}{n^2} \cdot \frac{n(n+1)}{2} = 2\left(1 + \frac{1}{n}\right)
$$

**Step 5:**  
Take the limit as $n \to \infty$:
$$
A = \lim_{n \to \infty} 2\left(1 + \frac{1}{n}\right) = 2
$$

✅ Therefore, the area under $y = x$ on $[0, 2]$ is **2 square units**.

---

### Geometric Interpretation

Each rectangular sum approximates the area under the curve.  
As $n$ increases:
- $\Delta x$ becomes smaller,  
- the rectangles fit the curve more closely,  
- and the sum approaches the true area.  

In the limit, the sum becomes **exact**, forming the foundation for **definite integrals**.

---

### From Limit to Integral

The limit definition leads directly to the notation of the **definite integral**:

$$
\int_{a}^{b} f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x
$$

This expresses the same concept — the exact area under $f(x)$ on $[a, b]$.

---

### Concept Summary

| Concept | Formula / Description |
|----------|-----------------------|
| Subinterval Width | $\Delta x = \frac{b - a}{n}$ |
| Riemann Sum | $\displaystyle \sum_{i=1}^{n} f(x_i^*) \Delta x$ |
| Area (Limit Definition) | $\displaystyle A = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x$ |
| Definite Integral | $\displaystyle \int_{a}^{b} f(x)\,dx$ |
| Right Endpoint Rule | $x_i^* = a + i\Delta x$ |

---

### Related Notes

- [[Definite Integral]]
- [[Riemann Sums]]
- [[Sigma Notation]]
- [[Antiderivatives]]
- [[Fundamental Theorem of Calculus]]

---

#math #calculus #integration #area #limits
