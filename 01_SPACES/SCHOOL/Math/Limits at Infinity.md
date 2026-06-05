# Limits at Infinity

### Idea

A **limit at infinity** describes the behavior of a function as $x$ increases or decreases without bound ($x \to \infty$ or $x \to -\infty$).  
These limits help us understand the **end behavior** of functions and are closely related to **horizontal asymptotes**.  

→ [[Limits]]  
→ [[Continuity and Limits]]  

---

### Formal Definition

- $\lim_{x \to \infty} f(x) = L$ means the values of $f(x)$ get arbitrarily close to $L$ as $x$ becomes very large.  
- $\lim_{x \to -\infty} f(x) = L$ means the values of $f(x)$ get arbitrarily close to $L$ as $x$ becomes very negative.  

If such an $L$ exists, the line $y = L$ is a **horizontal asymptote** of $f(x)$.  

---

### Common Examples

#### 1. Reciprocal Function
$$
\lim_{x \to \infty} \frac{1}{x} = 0, 
\quad \lim_{x \to -\infty} \frac{1}{x} = 0
$$
→ [[Rational Functions]]

#### 2. Rational Functions (Degree Comparison)

For $\frac{p(x)}{q(x)}$ where $p(x)$ and $q(x)$ are polynomials:

- If $\deg(p) < \deg(q)$ → limit is $0$.  
- If $\deg(p) = \deg(q)$ → limit is ratio of leading coefficients.  
- If $\deg(p) > \deg(q)$ → limit is $\pm \infty$ (no horizontal asymptote).  

Example:  
$$
\lim_{x \to \infty} \frac{3x^2 + 1}{2x^2 + 5} = \frac{3}{2}
$$

#### 3. Exponential Functions
- $\lim_{x \to \infty} e^x = \infty$  
- $\lim_{x \to -\infty} e^x = 0$  

#### 4. Trigonometric Functions
Oscillating functions like $\sin x$ and $\cos x$ **do not have limits at infinity** because they do not settle to a single value.  

---

### Notation for Infinite Limits

Sometimes a function grows without bound:  

$$
\lim_{x \to \infty} f(x) = \infty
$$

This does **not** mean the limit exists in the traditional sense; instead, it describes **divergent behavior**.  

---

### Applications

- Determining **horizontal asymptotes**  
- Describing the **end behavior** of polynomial and rational functions  
- Analyzing **convergence of sequences and series**  

---

#math #calculus #limits #asymptotes
