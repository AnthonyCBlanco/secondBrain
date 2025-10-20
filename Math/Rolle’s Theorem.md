### Idea
Rolle’s Theorem is a special case of the **Mean Value Theorem (MVT)**.  
It guarantees that for a smooth curve connecting two points with the same $y$-value, there exists at least one point where the **tangent line is horizontal** (slope = 0).  

→ In other words, somewhere between two equal function values, the derivative must be **zero**.

---

### Formal Definition

If a function $f(x)$ satisfies all the following three conditions on a closed interval $[a, b]$:

1. $f(x)$ is **continuous** on $[a, b]$  
2. $f(x)$ is **differentiable** on $(a, b)$  
3. $f(a) = f(b)$  

Then, there exists at least one $c$ in $(a, b)$ such that:

$$
f'(c) = 0
$$

---

### Graphical Idea

If the endpoints of a smooth curve are at the same height ($f(a) = f(b)$),  
then there must be at least one point between them where the tangent is **flat (horizontal)**.

---

### Example 1

Let  
$$
f(x) = x^2 - 4x + 3
$$  
on $[1, 3]$.

**Step 1:** Check the conditions  
- $f(x)$ is a polynomial → continuous and differentiable everywhere ✅  
- $f(1) = 1^2 - 4(1) + 3 = 0$  
- $f(3) = 3^2 - 4(3) + 3 = 0$  
→ $f(1) = f(3)$ ✅  

**Step 2:** Apply Rolle’s Theorem  
There exists some $c$ in $(1, 3)$ where $f'(c) = 0$.

Find $f'(x)$:  
$$
f'(x) = 2x - 4
$$  

Set equal to zero:  
$$
2x - 4 = 0 \Rightarrow x = 2
$$  

✅ **Conclusion:** $f'(2) = 0$ — tangent is horizontal at $x = 2$.

---

### Example 2

Let  
$$
f(x) = \sin x
$$  
on $[0, \pi]$.

Check the conditions:
- $\sin x$ is continuous and differentiable everywhere ✅  
- $f(0) = 0$ and $f(\pi) = 0$ ✅  

Then there exists $c$ in $(0, \pi)$ where:  
$$
f'(c) = 0
$$  

$f'(x) = \cos x$  
Set equal to zero:  
$$
\cos c = 0 \Rightarrow c = \frac{\pi}{2}
$$  

✅ **Conclusion:** The tangent is horizontal at $x = \frac{\pi}{2}$.

---

### Notes

- Rolle’s Theorem is a **specific case** of the [[Mean Value Theorem]] where $f(a) = f(b)$.  
- Geometrically, it guarantees at least one point where the curve’s slope is zero.  
- It’s often used to **prove properties of derivatives** or **locate stationary points**.

---

### Summary Table

| Condition | Requirement |
|------------|-------------|
| Continuity | $f(x)$ continuous on $[a,b]$ |
| Differentiability | $f(x)$ differentiable on $(a,b)$ |
| Equal Endpoints | $f(a) = f(b)$ |
| Conclusion | $\exists c \in (a,b)$ s.t. $f'(c) = 0$ |

---

### Related Notes
- [[The Derivative]]  
- [[Continuity and Limits]]  

---

#math #calculus #derivatives 
