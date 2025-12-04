## Definite Integral  

### Idea  
The **definite integral** represents the *net area* under a curve $y = f(x)$ between two points $x = a$ and $x = b$.  
It measures accumulation — the total change of a quantity over an interval — and is a cornerstone concept linking geometry, motion, and calculus.  

Unlike the **indefinite integral**, which gives a family of functions, the **definite integral** yields a single numerical value.  

### Formally  
For a continuous function $f(x)$ on the interval $[a, b]$, the **definite integral** is defined as the limit of a Riemann sum:  

$$
\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x
$$

where:  
- $[a, b]$ is divided into $n$ subintervals of equal width $\Delta x = \frac{b - a}{n}$  
- $x_i^*$ is a sample point in the $i$th subinterval $[x_{i-1}, x_i]$  
- $f(x_i^*)\Delta x$ approximates the area of a rectangle under the curve  

The definite integral represents the *exact* area as $n \to \infty$.  

### Properties  
| Property | Formula | Description |
|-----------|----------|-------------|
| **Additivity** | $\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$ | Integrals over adjacent intervals can be added |
| **Reversal of limits** | $\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$ | Reversing limits changes the sign |
| **Zero-width interval** | $\int_a^a f(x)\,dx = 0$ | No interval means zero area |
| **Constant multiple** | $\int_a^b kf(x)\,dx = k\int_a^b f(x)\,dx$ | Constants can be factored out |
| **Sum/Difference** | $\int_a^b [f(x) \pm g(x)]\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx$ | Integration distributes over addition/subtraction |

### Geometric Interpretation  
- If $f(x) \geq 0$ on $[a, b]$, then $\int_a^b f(x)\,dx$ is the **area under the curve**.  
- If $f(x)$ takes negative values, the integral measures **signed area** — areas below the $x$-axis are negative.  

### Example  
Find the area under $f(x) = x^2$ from $x = 0$ to $x = 2$:  

$$
\int_0^2 x^2\,dx = \left[\frac{x^3}{3}\right]_0^2 = \frac{8}{3}
$$

Thus, the area under the curve $y = x^2$ from 0 to 2 is $\frac{8}{3}$ square units.  

### Concept Summary  
- The definite integral is the *limit of Riemann sums*, representing accumulated change.  
- It measures **signed area** under a curve between two bounds.  
- It connects directly to the **Fundamental Theorem of Calculus**, linking differentiation and integration.  

### Related Notes  
- [[Area by Limit Definition]]
- [[Indefinite Integration]]  
- [[Fundamental Theorem of Calculus]]  

---

#math #calculus #integrals
