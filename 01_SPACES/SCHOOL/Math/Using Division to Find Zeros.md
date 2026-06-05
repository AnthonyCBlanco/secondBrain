### Idea

To find **zeros** (or roots) of a polynomial, we can use **division** to simplify the polynomial step-by-step, especially after identifying a root.

---

### Why Use Division?

Once you know a **zero** (say, $x = c$), you can divide the polynomial by $(x - c)$ to reduce its degree.

→ This helps you factor the polynomial completely or solve it more easily.

---

### Steps

1. **Use the Rational Root Theorem** to list possible rational roots.  
   → [[Rational Root Theorem]]

2. **Test a root** by substitution or synthetic division.

3. **If it works** (remainder is 0), then:
   - $(x - r)$ is a factor
   - Use **polynomial division** (long or synthetic) to divide the polynomial

4. **Repeat** the process with the quotient polynomial.

---

### Example

Given:

$$
f(x) = x^3 - 6x^2 + 11x - 6
$$

Step 1: Try $x = 1$

$$
f(1) = 1 - 6 + 11 - 6 = 0 \Rightarrow x = 1 \text{ is a root}
$$

Step 2: Divide by $(x - 1)$ using synthetic division:


So,

$$
f(x) = (x - 1)(x^2 - 5x + 6)
$$

Step 3: Factor the quadratic:

$$
x^2 - 5x + 6 = (x - 2)(x - 3)
$$

Final factorization:

$$
f(x) = (x - 1)(x - 2)(x - 3)
$$

→ Zeros: $x = 1,\ 2,\ 3$

---

### Summary

- Use division to **reduce polynomial degree** after finding one zero
- Continue until you reach a **quadratic** or **linear** polynomial
- Always verify your roots by substitution or graphing

→ [[Polynomial Division]]  
→ [[Factoring Polynomials]]  
→ [[Synthetic Division]]  
→ [[Finding Roots of Quadratics]]

---

#math #algebra #polynomials #zeros #division
