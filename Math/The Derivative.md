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

#### 5. Product Rule
For $f(x)$ and $g(x)$:  

$$
\frac{d}{dx}[f(x) \cdot g(x)] = f'(x)g(x) + f(x)g'(x)
$$

Example:  
$$
f(x) = x^2 \sin x \quad \Rightarrow \quad f'(x) = 2x \sin x + x^2 \cos x
$$

---

#### 6. Quotient Rule
For $\dfrac{f(x)}{g(x)}$ (with $g(x) \neq 0$):  

$$
\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}
$$

Example:  
$$
f(x) = \frac{x^2}{\sin x} \quad \Rightarrow \quad f'(x) = \frac{2x\sin x - x^2 \cos x}{\sin^2 x}
$$

---

#### 7. Chain Rule
If $y = f(g(x))$, then:  

$$
\frac{dy}{dx} = f'(g(x)) \cdot g'(x)
$$

Example:  
$$
f(x) = \sin(x^2) \quad \Rightarrow \quad f'(x) = \cos(x^2) \cdot 2x
$$

→ [[The Chain Rule]]

---

### Derivatives of Trigonometric Functions

- $\frac{d}{dx}[\sin x] = \cos x$  
- $\frac{d}{dx}[\cos x] = -\sin x$  
- $\frac{d}{dx}[\tan x] = \sec^2 x$  
- $\frac{d}{dx}[\cot x] = -\csc^2 x$  
- $\frac{d}{dx}[\sec x] = \sec x \tan x$  
- $\frac{d}{dx}[\csc x] = -\csc x \cot x$  

---

### Derivatives of Exponential and Logarithmic Functions

- $\frac{d}{dx}[e^x] = e^x$  
- $\frac{d}{dx}[a^x] = a^x \ln a$  

- $\frac{d}{dx}[\ln x] = \frac{1}{x}, \quad x>0$  
- $\frac{d}{dx}[\log_a x] = \frac{1}{x \ln a}$  

---

### Applications

- Finding tangent lines  
- Describing instantaneous rates of change  
- Analyzing motion in physics ($v(t) = s'(t)$, $a(t) = v'(t)$)  
- Optimization problems  
- Related rates  

→ [[Difference Quotient]]  
→ [[Limits]]  
→ [[Continuity and Limits]]  
→ [[The Chain Rule]]  

---

#math #calculus #derivatives #limits
