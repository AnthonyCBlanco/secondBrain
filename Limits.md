# Limits

In calculus, a **limit** describes the behavior of a function as the input approaches a certain value. Limits are foundational for defining **derivatives**, **integrals**, and **continuity**.  

Limits are what number the graph approaches 

---

## Formal Definition

The **limit** of a function $f(x)$ as $x$ approaches a value $a$ is written as:

$$
\lim_{x \to a} f(x)
$$

This represents the value $f(x)$ **approaches** as $x$ gets **close to** $a$ (but not necessarily equal to $a$).  

---

## Key Concepts

- A **limit exists** if the left-hand and right-hand limits are equal:

  $$
  \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)
  $$

- If the function "jumps" or behaves differently from each side, the limit **does not exist**.  

---

## Limit Notation Examples

- $\lim_{x \to 2} (3x + 1) = 7$  
- $\lim_{x \to 0} \frac{\sin x}{x} = 1$  
- $\lim_{x \to \infty} \frac{1}{x} = 0$  

→ [[Limits at Infinity]]  
→ [[Trigonometric Limits]]  

---

## Techniques for Finding Limits

### 1. Direct Substitution  
If $f(a)$ is defined, just plug in $a$.  

---

### 2. Factoring and Simplifying  
Use algebra to cancel terms before substituting.  

Example:  

$$
\lim_{x \to 2} \frac{x^2 - 4}{x - 2}
= \lim_{x \to 2} \frac{(x - 2)(x + 2)}{x - 2}
= \lim_{x \to 2} (x + 2) = 4
$$  

---

### 3. Rationalizing  
Use conjugates to simplify expressions with radicals.  

---

### 4. L'Hôpital's Rule  
If substitution gives an indeterminate form like $\tfrac{0}{0}$ or $\tfrac{\infty}{\infty}$, differentiate the top and bottom:  

$$
\lim_{x \to a} \frac{f(x)}{g(x)}
= \lim_{x \to a} \frac{f'(x)}{g'(x)} \quad \text{(if conditions apply)}
$$  

→ [[L'Hôpital’s Rule]]  

---

## Indeterminate Forms

Common indeterminate forms include:  

- $\tfrac{0}{0}$  
- $\tfrac{\infty}{\infty}$  
- $0 \cdot \infty$  
- $\infty - \infty$  
- $1^\infty$, $0^0$, $\infty^0$  

→ [[Indeterminate Forms]]  

---

## Applications of Limits

- Define the **derivative**:  

  $$
  f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{_
