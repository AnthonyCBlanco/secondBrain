### Idea

A **rational function** is any function that can be written as a ratio of two polynomials:

$$
f(x) = \frac{p(x)}{q(x)}
$$

where $p(x)$ and $q(x)$ are polynomials and $q(x) \neq 0$.  

→ [[Polynomial Functions]]  
→ [[Limits]]  
→ [[Continuity and Limits]]  
→ [[Limits at Infinity]]  

---

### Domain

- The domain of a rational function is **all real numbers** except where the denominator $q(x) = 0$.  
- Points where $q(x) = 0$ may correspond to:
  - **Holes (removable discontinuities)** if the factor cancels with the numerator  
  - **Vertical asymptotes** if the factor does not cancel  

---

### Graph Features

#### 1. Vertical Asymptotes
- Occur where $q(x) = 0$ and does not cancel with $p(x)$.  
- Example: $f(x) = \frac{1}{x}$ has a vertical asymptote at $x=0$.  

#### 2. Horizontal Asymptotes
Determined by comparing the **degree** of numerator ($n$) and denominator ($m$):  

- If $n < m$: $y = 0$  
- If $n = m$: $y = \frac{\text{leading coefficient of } p}{\text{leading coefficient of } q}$  
- If $n > m$: **no horizontal asymptote** (may have an **oblique/slant asymptote**)  

→ [[Limits at Infinity]]  

#### 3. Holes (Removable Discontinuities)
- If $(x - a)$ is a common factor in numerator and denominator, then there is a **hole** at $x = a$.  

---

### Continuity

- Rational functions are **continuous** everywhere on their domain.  
- They are **discontinuous** where the denominator is zero.  

→ [[Continuity and Limits]]  

---

### Examples

1. $f(x) = \frac{x^2 - 4}{x - 2}$  
   - Factor: $\frac{(x - 2)(x + 2)}{x - 2}$  
   - Simplifies to $f(x) = x + 2$ (for $x \neq 2$)  
   - Hole at $x = 2$  

2. $f(x) = \frac{3x^2 + 1}{2x^2 + 5}$  
   - $\lim_{x \to \infty} f(x) = \frac{3}{2}$  
   - Horizontal asymptote: $y = \tfrac{3}{2}$  

3. $f(x) = \frac{x^3}{x^2 + 1}$  
   - Degree of numerator > denominator  
   - No horizontal asymptote → has an oblique asymptote  

---

### Applications

- Useful in **modeling ratios** and rates of change  
- Key in studying **limits**, **asymptotes**, and **continuity**  
- Appear in **partial fractions** and **integration techniques** (advanced topics)  

---

#math #precalc #calculus #limits 
