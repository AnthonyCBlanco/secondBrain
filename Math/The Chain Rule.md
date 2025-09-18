# The Chain Rule

### Idea

The **Chain Rule** is used to differentiate a **composition of functions**.  
If $y = f(g(x))$, then the derivative is:

$$
\frac{dy}{dx} = f'(g(x)) \cdot g'(x)
$$

In words:  
> Differentiate the **outer function**, keep the inner function unchanged, then multiply by the derivative of the **inner function**.

---

### Formal Statement

If $y = f(u)$ and $u = g(x)$, then:

$$
\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}
$$

---

### Step-by-Step Process
1. Identify the **outer function** and the **inner function**.  
2. Differentiate the outer function (leave the inner part intact).  
3. Multiply by the derivative of the inner function.  

---

### Examples

#### Example 1: Power Function
$$
y = (3x^2 + 1)^5
$$

Outer function: $f(u) = u^5$  
Inner function: $u = 3x^2 + 1$  

$$
\frac{dy}{dx} = 5(3x^2 + 1)^4 \cdot (6x) = 30x(3x^2 + 1)^4
$$

---

#### Example 2: Trigonometric Function
$$
y = \sin(2x)
$$

Outer function: $f(u) = \sin u$  
Inner function: $u = 2x$  

$$
\frac{dy}{dx} = \cos(2x) \cdot (2) = 2\cos(2x)
$$

---

#### Example 3: Exponential Function
$$
y = e^{x^2}
$$

Outer function: $f(u) = e^u$  
Inner function: $u = x^2$  

$$
\frac{dy}{dx} = e^{x^2} \cdot (2x) = 2x e^{x^2}
$$

---

### Extended Chain Rule

If we have multiple nested functions:  
$$
y = f(g(h(x)))
$$  

Then:  

$$
\frac{dy}{dx} = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)
$$  

---

### Graphical / Conceptual View
- The **chain rule** expresses how a small change in $x$ affects $u$, and how a change in $u$ affects $y$.  
- Multiplying the rates gives the total rate of change.  

---

### Related Notes
- [[The Derivative]]

---

#math #calculus #derivatives
