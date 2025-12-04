# Indefinite Integrals

### Idea

An **indefinite integral** represents the **family of all antiderivatives** of a given function.  
It is the reverse process of differentiation and is used to find a function whose derivative equals a given expression.

The indefinite integral does **not** compute a specific numerical value (unlike a [[Definite Integrals|definite integral]]); instead, it gives a **general formula** that includes an arbitrary constant $C$.

---

### Definition

If $F'(x) = f(x)$, then the **indefinite integral** of $f(x)$ is defined as:

$$
\int f(x) \, dx = F(x) + C
$$

Where:  
- $\int$ is the **integral sign**, representing summation of infinitesimals  
- $f(x)$ is the **integrand**  
- $dx$ indicates the **variable of integration**  
- $C$ is the **constant of integration**, accounting for all vertical shifts of the antiderivative  

---

### Interpretation

The process of integration “undoes” differentiation:

$$
\frac{d}{dx}\left(\int f(x)\,dx\right) = f(x)
$$

This means every indefinite integral produces a **family of curves** that differ only by a constant $C$.

---

### Basic Rules of Indefinite Integration

1. **Constant Rule**
   $$
   \int k \, dx = kx + C
   $$

2. **Power Rule**
   $$
   \int x^n \, dx = \frac{x^{n+1}}{n+1} + C \quad (n \neq -1)
   $$

3. **Constant Multiple Rule**
   $$
   \int c \, f(x) \, dx = c \int f(x) \, dx
   $$

4. **Sum and Difference Rule**
   $$
   \int [f(x) \pm g(x)] \, dx = \int f(x)\,dx \pm \int g(x)\,dx
   $$

---

### Common Indefinite Integrals

| Function $f(x)$ | Indefinite Integral $\displaystyle \int f(x)\,dx$ |
|:--|:--|
| $0$ | $C$ |
| $1$ | $x + C$ |
| $x^n$ $(n \neq -1)$ | $\dfrac{x^{n+1}}{n+1} + C$ |
| $\dfrac{1}{x}$ | $\ln|x| + C$ |
| $e^x$ | $e^x + C$ |
| $a^x$ | $\dfrac{a^x}{\ln a} + C$ |
| $\sin x$ | $-\cos x + C$ |
| $\cos x$ | $\sin x + C$ |
| $\sec^2 x$ | $\tan x + C$ |
| $\csc^2 x$ | $-\cot x + C$ |
| $\sec x \tan x$ | $\sec x + C$ |
| $\csc x \cot x$ | $-\csc x + C$ |

---

### Example 1

Find the indefinite integral:

$$
\int (4x^3 - 5x + 7)\, dx
$$

Apply the power rule to each term:

$$
\int 4x^3\,dx - \int 5x\,dx + \int 7\,dx
$$

$$
= x^4 - \frac{5x^2}{2} + 7x + C
$$

✅ Therefore:

$$
\int (4x^3 - 5x + 7)\,dx = x^4 - \frac{5x^2}{2} + 7x + C
$$

---

### Example 2 — Using Trigonometric Functions

$$
\int (\sin x + \cos x)\, dx = -\cos x + \sin x + C
$$

---

### Concept Summary

- The **indefinite integral** gives a **family of antiderivatives**.  
- Always include the **constant of integration** $C$.  
- The derivative of the result gives back the **original function**.  
- Used in physics and engineering for **position**, **velocity**, **work**, and **energy** calculations.  

---

### Related Notes

- [[Antiderivatives]]
- [[Definite Integrals]]
- [[Fundamental Theorem of Calculus]]
- [[Work and Energy]]
- [[Differentials]]

---

#math #calculus #integration #indefiniteintegrals
