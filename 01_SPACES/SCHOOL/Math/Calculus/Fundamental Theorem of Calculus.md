## Fundamental Theorem of Calculus  

### Idea  
The **Fundamental Theorem of Calculus (FTC)** forms the bridge between **differentiation** and **integration** — the two central operations in calculus.  
It shows that **integration** (finding the area under a curve) and **differentiation** (finding the rate of change) are *inverse processes*.  

This theorem has two parts:  
1. The **First Fundamental Theorem of Calculus** relates the derivative of an integral to the original function.  
2. The **Second Fundamental Theorem of Calculus** provides a method to evaluate definite integrals using antiderivatives.  

---

### Formally  

#### Part 1 — The First Fundamental Theorem of Calculus  

If $f$ is continuous on $[a, b]$ and  
$$
F(x) = \int_a^x f(t)\,dt
$$  
then $F'(x) = f(x)$.  

**Interpretation:**  
Differentiating an integral “undoes” the integration process. The derivative of the accumulated area function $F(x)$ is simply the original function $f(x)$.  

---

#### Part 2 — The Second Fundamental Theorem of Calculus  

If $f$ is continuous on $[a, b]$ and $F$ is *any* antiderivative of $f$, then  

$$
\int_a^b f(x)\,dx = F(b) - F(a)
$$  

**Interpretation:**  
To compute a definite integral, find any antiderivative of the function and subtract its values at the limits of integration.  

---

### Conceptual Connection  

| Operation | Meaning | Example |
|------------|----------|----------|
| Differentiation | Finds rate of change | $\frac{d}{dx}[x^3] = 3x^2$ |
| Integration | Finds accumulated change | $\int 3x^2\,dx = x^3 + C$ |
| Fundamental Link | These are inverse operations | $\frac{d}{dx}\left(\int_a^x f(t)\,dt\right) = f(x)$ |

---

### Example  

**Problem:** Evaluate $\int_0^3 (2x)\,dx$ using the Fundamental Theorem of Calculus.  

**Solution:**  
1. Find an antiderivative of $2x$:  
   $F(x) = x^2$  
2. Apply the FTC:  
   $$
   \int_0^3 2x\,dx = F(3) - F(0) = 3^2 - 0^2 = 9
   $$  

Thus, the area under $y = 2x$ from $x=0$ to $x=3$ is **9**.  

---

### Notes  

- The **First FTC** allows us to interpret accumulation functions as differentiable.  
- The **Second FTC** turns the problem of finding area (a limit) into finding an antiderivative — much simpler computationally.  
- The FTC only applies to **continuous** functions on closed intervals $[a, b]$.  

---

### Concept Summary  

| Part | Statement | Meaning |
|------|------------|----------|
| **FTC I** | $\frac{d}{dx}\left(\int_a^x f(t)\,dt\right) = f(x)$ | Derivative of an integral equals the original function |
| **FTC II** | $\int_a^b f(x)\,dx = F(b) - F(a)$ | Area under a curve equals the change in antiderivative |

---

### Related Notes  
- [[Definite Integrals]]  
- [[Indefinite Integration]]  
- [[Area by Limit Definition]]
- [[Antiderivatives]]  

---

#math #calculus #integrals #fundamentals
