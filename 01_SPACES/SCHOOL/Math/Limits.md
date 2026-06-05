# Limits

### Idea

In calculus, a **limit** describes the behavior of a function as the input approaches a certain value. Limits are foundational for defining **derivatives**, **integrals**, and **continuity**.

---

### Formal Definition (Intuitive)

The **limit** of a function $f(x)$ as $x$ approaches a value $a$ is written as:

$$
\lim_{x \to a} f(x) = L
$$

This represents what value $f(x)$ **approaches** as $x$ gets **close to** $a$ (but not necessarily equal to $a$).

---

### Formal Definition (ε–δ)

We say:

$$
\lim_{x \to a} f(x) = L
$$

**if and only if** for every $\epsilon > 0$ (no matter how small), there exists a $\delta > 0$ such that:

$$
0 < |x - a| < \delta \;\; \implies \;\; |f(x) - L| < \epsilon
$$

- $\epsilon$ (“epsilon”) represents how close $f(x)$ is to the limit value $L$.  
- $\delta$ (“delta”) represents how close $x$ must be to $a$ to guarantee that closeness.  

In words:  
> We can make $f(x)$ as close as we want to $L$ by choosing $x$ sufficiently close to $a$.

---

### Key Concepts

- A **limit exists** if the left-hand and right-hand limits are equal:

  $$
  \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)
  $$

- If the function "jumps" or behaves differently from each side, the limit **does not exist**.

→ [[One-Sided Limits]]  
→ [[Piecewise Functions]]

---

### Limit Notation Examples

- $\lim_{x \to 2} (3x + 1) = 7$  
- $\lim_{x \to 0} \frac{\sin x}{x} = 1$  
- $\lim_{x \to \infty} \frac{1}{x} = 0$  

→ [[Limits at Infinity]]  

---

### Properties of Limits

If $\lim_{x \to c} f(x) = L$ and $\lim_{x \to c} g(x) = K$, and $b$ is a constant:

1. **Constant Rule**  
   $$
   \lim_{x \to c} b = b
   $$

2. **Scalar Multiple**  
   $$
   \lim_{x \to c} \big(b \cdot f(x)\big) = b \cdot L
   $$

3. **Sum Rule**  
   $$
   \lim_{x \to c} \big(f(x) + g(x)\big) = L + K
   $$

4. **Difference Rule**  
   $$
   \lim_{x \to c} \big(f(x) - g(x)\big) = L - K
   $$

5. **Product Rule**  
   $$
   \lim_{x \to c} \big(f(x) \cdot g(x)\big) = L \cdot K
   $$

6. **Quotient Rule**  
   $$
   \lim_{x \to c} \frac{f(x)}{g(x)} = \frac{L}{K}, \quad \text{if } K \neq 0
   $$

7. **Power Rule**  
   $$
   \lim_{x \to c} \big(f(x)\big)^n = (L)^n
   $$

8. **Root Rule**  
   $$
   \lim_{x \to c} \sqrt[n]{f(x)} = \sqrt[n]{L}, \quad \text{if } L \geq 0 \text{ when } n \text{ is even}
   $$

---

### Trigonometric Limits

- $\lim_{x \to c} \sin(x) = \sin(c)$  
- $\lim_{x \to c} \cos(x) = \cos(c)$  
- In general, for any trig function, just substitute $c$ into $x$ (as long as the function is defined there).  

Special important limits:  

$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$

$$
\lim_{x \to 0} \frac{1 - \cos x}{x} = 0
$$

---

### Techniques for Finding Limits

1. **Direct Substitution**  
   If $f(a)$ is defined, just plug in $a$.

2. **Factoring and Simplifying**  
   Example:  
   $$
   \lim_{x \to 2} \frac{x^2 - 4}{x - 2} 
   = \lim_{x \to 2} \frac{(x - 2)(x + 2)}{x - 2} 
   = \lim_{x \to 2} (x + 2) = 4
   $$

3. **Rationalizing**  
   Use conjugates to simplify radicals.

4. **L'Hôpital's Rule**  
   If direct substitution gives an indeterminate form like $\tfrac{0}{0}$ or $\tfrac{\infty}{\infty}$:  

   $$
   \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} \quad \text{(if conditions apply)}
   $$

→ [[L'Hôpital’s Rule]]

---

### Indeterminate Forms

Common indeterminate forms include:

- $\tfrac{0}{0}$  
- $\tfrac{\infty}{\infty}$  
- $0 \cdot \infty$  
- $\infty - \infty$  
- $1^\infty$  
- $0^0$  
- $\infty^0$  

→ [[Indeterminate Forms]]

---

### Applications

- **Derivative definition**:  
  $$
  f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
  $$

- Understanding **asymptotes** and **behavior at infinity**  

→ [[Difference Quotient]]  
→ [[Asymptotic Behavior]]  
→ [[Continuity and Limits]]

---

#math #calculus #limits #derivatives #analysis
