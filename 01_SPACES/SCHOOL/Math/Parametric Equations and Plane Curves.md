### Idea

A **parametric equation** represents a curve using a third variable (usually $t$), called a **parameter**.

Instead of writing $y$ as a function of $x$, we write:

$$
\begin{align}
x &= f(t) \\
y &= g(t)
\end{align}
$$

As $t$ changes, the point $(x, y)$ moves along a curve in the plane.

→ [[Trigonometric Identities]]  
→ [[Unit Circle]]

---

### Trigonometric Parametric Equations

We often use **trig functions** in parametric equations to describe **circular** and **elliptical** motion.
The difference between Parametric and rectangular equations, is that Parametric equations have a **direction***

#### Circle:
$$
x = r\cos(t), \quad y = r\sin(t)
$$

This traces a circle of radius $r$ centered at the origin.

#### Ellipse:
$$
x = a\cos(t), \quad y = b\sin(t)
$$

This traces an ellipse with:
- Width $2a$
- Height $2b$

→ [[Conic Sections]]

---

### Direction and Orientation

- As $t$ increases, the point $(x(t), y(t))$ moves along the curve.
- The **direction** of motion depends on how $t$ is used.

---

### Eliminating the Parameter (Back to Rectangular)

To eliminate the parameter:

1. Solve one parametric equation for $t$
2. Substitute into the other equation
3. Adjust the domain or range if needed

---

#### Example:

Given:

$$
x = 2\sin(t), \quad y = 3\cos(t)
$$

We want to eliminate $t$.

First, isolate the trig functions:

$$
\sin(t) = \frac{x}{2}, \quad \cos(t) = \frac{y}{3}
$$

Now use the identity:

$$
\sin^2(t) + \cos^2(t) = 1
$$

Substitute:

$$
\left(\frac{x}{2}\right)^2 + \left(\frac{y}{3}\right)^2 = 1
$$

Simplify:

$$
\frac{x^2}{4} + \frac{y^2}{9} = 1
$$

→ This is an **ellipse** centered at the origin.

---

#math #parametric #trigonometry #conic-sections

---

#### Tip:

When solving for $t$, try to isolate $t$ in the **simpler** equation (usually the one that doesn’t involve square roots or multiple terms).

→ [[Inverse Trig Functions]] can help when $t$ is inside a trig function.

---

### Summary

- Parametric equations let us describe curves using $t$
- Useful for modeling **motion** and **trig-based curves**
- Trig functions help define circular and elliptical motion

---

#math #trigonometry #parametric #unit-circle #graphing
