# Calculus — The Mathematics of Change

Calculus is the mathematics of **change**. It studies **velocities, accelerations, tangent lines, slopes, areas, volumes, arc length, centroids, curvatures,** and many other concepts that allow scientists, engineers, and economists to model real-world situations.  

- **Pre-Calculus** is *static*  
- **Calculus** is *dynamic*  

It is often called the **"limit machine"** because nearly all its ideas are built on the concept of a [[Limits|limit]].  

---

## Without Calculus vs With Calculus

| Without Calculus           | With Calculus                                                              |
| -------------------------- | -------------------------------------------------------------------------- |
| Value of $f$ at $x=c$      | $\lim_{x \to c} f(x)$                                                      |
| Slope of a line (constant) | Slope of a curve at a point (derivative) → [[The Derivative\|Derivatives]] |
| Area of simple shapes      | Area under a curve (integral) → [[Integrals]]                              |

---

## The Tangent Line Problem

A classic problem in calculus is finding the **equation of the [[The Derivative|tangent line also know as the derivative]]** to the graph of a function $f$ at a point $P(c, f(c))$.  

- A **secant line** passes through **two distinct points** on a curve  
- A **tangent line** "just touches" the curve at **one point**, sharing the same slope as the curve at that point  

$$
\Delta x=x_{2}-x_{2}
$$

### Secant Line Slope

The slope of the secant line is:

$$
m_{\sec} = \frac{f(c+\Delta x) - f(c)}{\Delta x}
$$

---

### Tangent Line Slope (Derivative)

The slope of the tangent line is found by taking the **limit** as $\Delta x \to 0$:

$$
m_{\tan} = \lim_{\Delta x \to c} \frac{f(c+\Delta x) - f(c)}{\Delta x}
$$

This defines the **derivative** of $f$ at $x=c$:  

$$
f'(c) = m_{\tan}
$$  

So, the **tangent line equation** at $P(c, f(c))$ is:  

$$
y - f(c) = f'(c)(x - c)
$$

---
![[Pasted image 20250825091321.png]]

---
## The Area Problem
Finding the area under a curve using increasing smaller rectangles 


## Key Links to Build On
- [[Limits]] — the foundation of calculus  
- [[The Derivative|Derivatives]] — the mathematics of slopes and rates of change  
- [[Integrals]] — the mathematics of accumulation and area  


#math #calculus #derivatives #integral