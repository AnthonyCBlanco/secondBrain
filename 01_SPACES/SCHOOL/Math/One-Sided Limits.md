# One-Sided Limits

### Idea

A **one-sided limit** focuses on the behavior of a function as $x$ approaches a point $c$ **from one direction only**.  

- **Right-hand limit**: as $x \to c^+$ (approaches from values greater than $c$)  
- **Left-hand limit**: as $x \to c^-$ (approaches from values less than $c$)  

→ [[Limits]]  
→ [[Piecewise Functions]]  
→ [[Continuity]]  

---

### Formal Definition

- **Right-hand limit**:  
  $$
  \lim_{x \to c^+} f(x) = L
  $$
  means $f(x)$ approaches $L$ as $x$ approaches $c$ **from the right**.

- **Left-hand limit**:  
  $$
  \lim_{x \to c^-} f(x) = L
  $$
  means $f(x)$ approaches $L$ as $x$ approaches $c$ **from the left**.

---

### When Does the Limit Exist?

A two-sided limit exists if and only if:

$$
\lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L
$$

If the left-hand and right-hand limits are not equal, the limit **does not exist**.

---

### Example 1: Piecewise Function

$$
f(x) = 
\begin{cases} 
  1, & x < 0 \\
  2, & x \geq 0
\end{cases}
$$

- $\lim_{x \to 0^-} f(x) = 1$  
- $\lim_{x \to 0^+} f(x) = 2$  
- Since the left and right limits are different, $\lim_{x \to 0} f(x)$ **does not exist**.  

→ [[Discontinuities]]  

---

### Example 2: Rational Function

$$
f(x) = \frac{1}{x}
$$

- $\lim_{x \to 0^+} \frac{1}{x} = +\infty$  
- $\lim_{x \to 0^-} \frac{1}{x} = -\infty$  
- Since the left- and right-hand limits go to different infinities, $\lim_{x \to 0} \frac{1}{x}$ does **not exist**.  

→ [[Asymptotic Behavior]]  

---

#math #calculus #limits 
