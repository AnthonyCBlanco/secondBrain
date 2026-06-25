# Derivatives of Inverse Functions

The derivative of an inverse function allows us to differentiate functions whose explicit derivative may be difficult to compute.  
This concept uses the fact that inverse functions “undo” each other and their slopes are reciprocals at corresponding points.

---

### Idea

If a function $f$ is **one-to-one**, differentiable, and has an inverse $f^{-1}$, then the slope of $f^{-1}$ at a point is the **reciprocal** of the slope of $f$ at the corresponding point.

The key identity:

$$
f(f^{-1}(x)) = x
$$

Differentiating both sides leads to the inverse derivative formula.

---

### Formally

## **1. Derivative of an Inverse Function**

If $y = f^{-1}(x)$, then:

$$
\frac{dy}{dx} = \frac{1}{f'(y)}
$$

Or equivalently, using $y = f^{-1}(x)$:

$$
\left(f^{-1}\right)'(x) = \frac{1}{f'(f^{-1}(x))}
$$

---

### **2. How It Works**

Start with:

$$
y = f^{-1}(x) \quad \Longleftrightarrow \quad x = f(y)
$$

Differentiate implicitly with respect to $x$:

$$
1 = f'(y)\frac{dy}{dx}
$$

Solve for $\frac{dy}{dx}$:

$$
\frac{dy}{dx} = \frac{1}{f'(y)}
$$

Since $y = f^{-1}(x)$:

$$
\left(f^{-1}\right)'(x) = \frac{1}{f'(f^{-1}(x))}
$$

---

### **3. Derivatives of Common Inverse Functions**

#### **Inverse Sine**

$$
\frac{d}{dx} \sin^{-1}(x) = \frac{1}{\sqrt{1 - x^2}}
$$

#### **Inverse Cosine**

$$
\frac{d}{dx} \cos^{-1}(x) = -\frac{1}{\sqrt{1 - x^2}}
$$

#### **Inverse Tangent**

$$
\frac{d}{dx} \tan^{-1}(x) = \frac{1}{1 + x^2}
$$

#### **Inverse Secant**

$$
\frac{d}{dx} \sec^{-1}(x) = \frac{1}{|x|\sqrt{x^2 - 1}}
$$

---

### Examples

#### **Example 1 — Using the Inverse Derivative Formula**

Suppose $f(x) = x^3 + 1$.  
Find $(f^{-1})'(2)$.

Step 1: Find the $x$ such that $f(x) = 2$.

$$
x^3 + 1 = 2 \quad \Rightarrow \quad x = 1
$$

Step 2: Apply inverse derivative rule:

$$
(f^{-1})'(2) = \frac{1}{f'(1)}
$$

Compute derivative:

$$
f'(x) = 3x^2 \qquad \Rightarrow \qquad f'(1) = 3
$$

Thus:

$$
(f^{-1})'(2) = \frac{1}{3}
$$

---

#### **Example 2 — Derivative of $\ln(x)$ Using Inverses**

Because $\ln(x)$ is the inverse of $e^x$:

$$
(\ln(x))' = \frac{1}{(e^x)'|_{x = \ln(x)}}
$$

Since $(e^x)' = e^x$:

$$
(\ln(x))' = \frac{1}{e^{\ln(x)}} = \frac{1}{x}
$$

---

### Concept Summary

| Concept | Formula | Meaning |
|--------|---------|---------|
| Inverse derivative rule | $(f^{-1})'(x) = \frac{1}{f'(f^{-1}(x))}$ | Key identity |
| Arcsin derivative | $\frac{1}{\sqrt{1-x^2}}$ | Applies for $|x|<1$ |
| Arccos derivative | $-\frac{1}{\sqrt{1-x^2}}$ | Opposite of arcsin |
| Arctan derivative | $\frac{1}{1+x^2}$ | For all real $x$ |
| Inverse relationship | $f(f^{-1}(x)) = x$ | Used for differentiation |

---

### Related Notes

- [[Chain Rule]]  
- [[Integration and Differentiation of Log Functions]]  
- [[Implicit Differentiation]]  

---

#math #calculus #derivatives
