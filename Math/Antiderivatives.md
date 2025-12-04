### Idea

An **antiderivative** is the reverse process of taking a derivative.  
While the derivative measures the **rate of change** of a function, the antiderivative finds the **original function** whose derivative is known.  

Antiderivatives form the foundation of **integration** and the **Fundamental Theorem of Calculus**.

---

### Definition

If $F'(x) = f(x)$ for all $x$ in an interval, then $F(x)$ is an **antiderivative** of $f(x)$.

$$
F'(x) = f(x)
$$

The **most general antiderivative** of $f(x)$ is:

$$
F(x) = \int f(x) \, dx = F(x) + C
$$

Where:
- $\int$ denotes the **integral symbol**  
- $f(x)$ is the **integrand**  
- $dx$ indicates the variable of integration  
- $C$ is the **constant of integration**, accounting for all possible vertical shifts

---

### Example

Find the antiderivative of $f(x) = 3x^2$.

$$
\int 3x^2 \, dx = x^3 + C
$$

Check by differentiation:

$$
\frac{d}{dx}[x^3 + C] = 3x^2
$$

✅ Therefore, $F(x) = x^3 + C$ is correct.

---

### Basic Antiderivative Rules

| Function $f(x)$ | Antiderivative $\displaystyle \int f(x)\,dx$ |
|:--|:--|
| $0$ | $C$ |
| $k$ | $kx + C$ |
| $x^n$ $(n \neq -1)$ | $\dfrac{x^{n+1}}{n+1} + C$ |
| $\dfrac{1}{x}$ | $\ln|x| + C$ |
| $e^x$ | $e^x + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |
| $\sec x \tan x$ | $\sec x + C$ |
| $\csc x \cot x$ | $-\csc x + C$ |

---

### Properties of Indefinite Integrals

1. **Constant Multiple Rule**  
   $$\int c \, f(x) \, dx = c \int f(x) \, dx$$

2. **Sum and Difference Rule**  
   $$\int [f(x) \pm g(x)] \, dx = \int f(x) \, dx \pm \int g(x) \, dx$$

3. **Derivative Check**  
   The derivative of an antiderivative returns the original function:  
   $$\frac{d}{dx}\left( \int f(x) \, dx \right) = f(x)$$

---

### Example 2 — Applying the Power Rule for Antiderivatives

Find:
$$
\int (2x^3 - 5x + 4) \, dx
$$

Apply the rule term by term:

$$
\frac{2x^4}{4} - \frac{5x^2}{2} + 4x + C
$$

Simplify:

$$
\frac{x^4}{2} - \frac{5x^2}{2} + 4x + C
$$

---

### Concept Summary

- The antiderivative is the **reverse** of differentiation.  
- There are **infinitely many** antiderivatives of a given function, differing only by a constant $C$.  
- The process is often called **indefinite integration**.  
- Antiderivatives are essential in computing **areas**, **displacement**, and **accumulated change** in physics and engineering.

---

### Related Notes

- [[The Derivative]]
- [[Definite Integrals]]
- [[Fundamental Theorem of Calculus]]
- [[Work and Energy]]
- [[Differentials]]
- [[Indefinite Integration]]

---

#math #calculus #integration #antiderivatives
