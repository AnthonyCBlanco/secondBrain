### Idea

In calculus, a **limit** describes the behavior of a function as the input approaches a certain value. Limits are foundational for defining **derivatives**, **integrals**, and **continuity**.

---

### Formal Definition (Intuitive)

The **limit** of a function $$f(x)$$ as $$x$$ approaches a value $$a$$ is written as:

$$
\lim_{x \to a} f(x) = L
$$

This represents what value $$f(x)$$ **approaches** as $$x$$ gets **close to** $$a$$ (but not necessarily equal to $$a$$).

---

### Formal Definition (ε–δ)

We say:

$$
\lim_{x \to a} f(x) = L
$$

**if and only if** for every $$\epsilon > 0$$ (no matter how small), there exists a $$\delta > 0$$ such that:

$$
0 < |x - a| < \delta \;\; \implies \;\; |f(x) - L| < \epsilon
$$

 $$\epsilon$$ (“epsilon”) represents how close $$f(x)$$ is to the limit value $$L$$.   $$\delta$$ (“delta”) represents how close $$x$$ must be to $$a$$ to guarantee that closeness.  

In words:  
> We can make $$f(x)$$ as close as we want to $$L$$ by choosing $$x$$ sufficiently close to $$a$$

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

- $$\lim_{x \to 2} (3x + 1) = 7$$  
- $$\lim_{x \to 0} \frac{\sin x}{x} = 1$$  
- $$\lim_{x \to \infty} \frac{1}{x} = 0$$  

→ [[Limits at Infinity]]  
→ [[Trigonometric Limits]]

---

### Techniques for Finding Limits

#### 1. **Direct Substitution**

If $$f(a)$$ is defined, just plug in $$a$$.

#### 2. **Factoring and Simplifying**

Example:

$$
\lim_{x \to 2} \frac{x^2 - 4}{x - 2} 
= \lim_{x \to 2} \frac{(x - 2)(x + 2)}{x - 2} 
= \lim_{x \to 2} (x + 2) = 4
$$

#### 3. **Rationalizing**

Use conjugates to simplify radicals.

#### 4. **L'Hôpital's Rule**

If direct substitution gives an indeterminate form like $$\frac{0}{0}$$ or $$\frac{\infty}{\infty}$$:

$$
\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} \quad \text{(if conditions apply)}
$$

→ [[L'Hôpital’s Rule]]

---

### Indeterminate Forms

Common indeterminate forms include:

- $$\frac{0}{0}$$  
- $$\frac{\infty}{\infty}$$  
- $$0 \cdot \infty$$  
- $$\infty - \infty$$  
- $$1^\infty$$$$0^0$$$$\infty^0$$  

→ [[Indeterminate Forms]]

---

### Applications

- Define the **derivative** using:
  $$
  f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
  $$

- Understand **asymptotes** and **behavior at infinity**

→ [[Difference Quotient]]  
→ [[Asymptotic Behavior]]  
→ [[Continuity and Limits]]

---

#math #calculus #limits #derivatives #analysis
