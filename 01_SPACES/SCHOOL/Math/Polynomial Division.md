### Idea

To find the **zeros** of a polynomial, we can use **polynomial division** (or **synthetic division**) to factor the polynomial and solve for where it equals zero.

---

### Step-by-Step Strategy

1. **Guess a potential zero** using the [[Rational Root Theorem]].
2. **Divide** the polynomial by $(x - r)$ where $r$ is a potential zero.
   - Use **synthetic division** or **long division**.
3. If the remainder is **0**, then $r$ is a zero, and $(x - r)$ is a factor.
4. **Repeat** the process with the quotient polynomial.
5. When you're left with a quadratic, solve it using factoring or the quadratic formula.

---

### Synthetic Division Example

Let’s say we’re given:

$$
f(x) = x^3 - 4x^2 - 7x + 10
$$

Try $x = 1$:

| 1 |  1 | –4 | –7 | 10 |
|---|----|-----|-----|-----|
|   |   | 1 | –3 | –10 |
|   | 1 | –3 | –10 | **0** |

So $x = 1$ is a zero and:

$$
f(x) = (x - 1)(x^2 - 3x - 10)
$$

Now factor or solve:

$$
x^2 - 3x - 10 = (x - 5)(x + 2)
$$

**Final factored form:**

$$
f(x) = (x - 1)(x - 5)(x + 2)
$$

**Zeros:** $x = 1$, $5$, $-2$

---

### When to Use Division

- When factoring is hard or impossible at first glance.
- When checking possible rational zeros.
- When simplifying higher-degree polynomials.

---

→ [[Rational Root Theorem]]  
→ [[Factoring Polynomials]]  
→ [[Synthetic Division Guide]]  
→ [[Quadratic Formula]]

---

#math #polynomials #algebra #division #zeros
