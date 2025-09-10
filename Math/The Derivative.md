# Derivatives

### Idea

One of the fundamentals of [[Basics Of Calculus|Calculus]] is the **tangent line problem**.  
The derivative allows us to find the slope of the tangent line at any point on a curve.  

This is done by calculating the slope of a **secant line** as the two points get infinitely close together.  

$$
\text{Slope } m = \lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x}
$$

The equation of the tangent line at a point $(x_1, y_1)$ is:  

$$
y - y_1 = m(x - x_1)
$$

---

### The Derivative (Definition)

The derivative of $f(x)$ at $x$ is:

$$
f'(x) = \lim_{\Delta x \to 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}
$$

Alternate notations:  

- $\frac{dy}{dx}$  
- $f'(x)$  
- $D[f(x)]$  

---

### Key Properties

1. If a function is **differentiable** at $x=c$, then it is **continuous** at $x=c$.  
   → Differentiability **implies continuity**  

2. A function can be **continuous** at $x=c$ but **not differentiable** there (e.g., sharp corners, cusps, or vertical tangents).  
   → [[Continuity and Limits]]  

---

### Basic Derivative Rules

#### 1. Constant Rule
The derivative of a constant is **zero**.  

$$
\frac{d}{dx}[C] = 0
$$

Example:  
$f(x) = 4 \quad \Rightarrow \quad f'(x) = 0$

---

#### 2. Power Rule
If $n$ is a rational number:  

$$
\frac{d}{dx}[x^n] = n x^{n-1}
$$

Example:  
$$
f(x) = x^2 \quad \Rightarrow \quad f'(x) = 2x
$$

---

#### 3. Constant Multiple Rule
If $c$ is a constant:  

$$
\frac{d}{dx}[c \cdot f(x)] = c \cdot f'(x)
$$

---

#### 4. Sum and Difference Rule
$$
\frac{d}{dx}[f(x) + g(x)] = f'(x) + g'(x)
$$

$$
\frac{d}{dx}[f(x) - g(x)] = f'(x) - g'(x)
$$

---

### Derivatives of Trigonometric Functions

- $\frac{d}{dx}[\sin x] = \cos x$  
- $\frac{d}{dx}[\cos x] = -\sin x$  


---

### Applications

- Finding tangent lines  
- Describing instantaneous rates of change  
- Analyzing motion in physics ($v(t) = s'(t)$, $a(t) = v'(t)$)  
- Optimization problems  

→ [[Difference Quotient]]  
→ [[Limits]]  
→ [[Continuity and Limits]]  

---

#math #calculus #derivatives #limits
