# Mean Value Theorem (MVT)

### Idea
The **Mean Value Theorem** connects the **average rate of change** of a function over an interval with its **instantaneous rate of change** (the derivative) at some point within that interval.

In simple terms, there is at least one point on a smooth curve where the **tangent line** is **parallel** to the **secant line** joining the endpoints.

---

### Formal Definition

If a function $f(x)$ satisfies all three of the following on the interval $[a, b]$:

1. $f(x)$ is **continuous** on $[a, b]$  
2. $f(x)$ is **differentiable** on $(a, b)$  

Then there exists at least one $c$ in $(a, b)$ such that:

$$
f'(c) = \frac{f(b) - f(a)}{b - a}
$$

---

### Geometric Interpretation

- The term $\frac{f(b) - f(a)}{b - a}$ is the **slope of the secant line** between $(a, f(a))$ and $(b, f(b))$.  
- Rolle’s Theorem is a **special case** where $f(a) = f(b)$, making that slope equal to **zero**.  

So MVT says:  
> There is at least one point where the **instantaneous slope (tangent)** equals the **average slope** over $[a,b]$.

---

### Example 1

Let  
$$
f(x) = x^2 + 2x + 1
$$  
on $[1, 3]$.

**Step 1:** Verify conditions  
- $f(x)$ is a polynomial → continuous and differentiable ✅  

**Step 2:** Apply the MVT formula  
$$
f'(c) = \frac{f(3) - f(1)}{3 - 1}
$$

Compute values:  
$$
f(3) = 3^2 + 2(3) + 1 = 16
$$  
$$
f(1) = 1^2 + 2(1) + 1 = 4
$$  

Then:  
$$
f'(c) = \frac{16 - 4}{2} = 6
$$  

**Step 3:** Find $c$  
$$
f'(x) = 2x + 2
$$  
Set equal to 6:  
$$
2x + 2 = 6 \Rightarrow x = 2
$$  

✅ **Conclusion:** $f'(2) = 6$ — tangent line is parallel to secant line at $x = 2$.

---

### Example 2

Let  
$$
f(x) = \sin x
$$  
on $[0, \pi]$.

Check conditions:  
- $\sin x$ is continuous and differentiable everywhere ✅  

Then:
$$
f'(c) = \frac{f(\pi) - f(0)}{\pi - 0} = \frac{0 - 0}{\pi} = 0
$$

So:
$$
f'(c) = 0 \implies \cos c = 0 \Rightarrow c = \frac{\pi}{2}
$$

✅ **Conclusion:** The tangent is horizontal at $x = \frac{\pi}{2}$.

---

### Physical Interpretation

If $s(t)$ represents **position**, then:  
$$
s'(t) = v(t)
$$  

By the MVT:  
> There exists a time $t = c$ where the **instantaneous velocity** equals the **average velocity** over $[t_1, t_2]$.

$$
v(c) = \frac{s(t_2) - s(t_1)}{t_2 - t_1}
$$

---

### Relationship to Rolle’s Theorem

Rolle’s Theorem is a **special case** of the Mean Value Theorem:  
If $f(a) = f(b)$, then the average rate of change is **zero**, and MVT reduces to:  

$$
f'(c) = 0
$$  

→ [[Rolle’s Theorem]]

---

### Summary Table

| Theorem | Conditions | Result |
|----------|-------------|--------|
| **Rolle’s Theorem** | Continuous on $[a,b]$, differentiable on $(a,b)$, and $f(a)=f(b)$ | $\exists c$ s.t. $f'(c)=0$ |
| **Mean Value Theorem** | Continuous on $[a,b]$, differentiable on $(a,b)$ | $\exists c$ s.t. $f'(c)=\frac{f(b)-f(a)}{b-a}$ |

---

### Related Notes
- [[Rolle’s Theorem]]  
- [[The Derivative]]  
- [[Continuity and Limits]]  

---

#math #calculus #derivatives