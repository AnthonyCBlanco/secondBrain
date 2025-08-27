### Idea

**Partial fraction decomposition** is a method used to break a **rational expression** (a fraction with polynomials in the numerator and denominator) into simpler fractions that are easier to integrate or work with.

We use this technique especially when integrating rational functions in calculus or simplifying expressions in algebra.

---

### When to Use

You can apply partial fractions when:
- The degree of the numerator is **less** than the degree of the denominator.
- The denominator **factors** into linear or irreducible quadratic terms.

→ [[Factoring Polynomials]]  
→ [[Integrating Rational Functions]]

---

### General Strategy

1. **Factor the denominator completely.**
2. **Set up the decomposition** using one term per factor.
3. **Multiply through by the common denominator** to eliminate fractions.
4. **Solve for the unknown constants** using substitution or comparing coefficients.

---

### Types of Decompositions

#### 1. **Distinct Linear Factors**

If the denominator is:  
$$
(x - a)(x - b)
$$  
Then decompose as:  
$$
\frac{A}{x - a} + \frac{B}{x - b}
$$

#### 2. **Repeated Linear Factors**

If the denominator is:  
$$
(x - a)^2
$$  
Then decompose as:  
$$
\frac{A}{x - a} + \frac{B}{(x - a)^2}
$$

#### 3. **Irreducible Quadratic Factors**

If the denominator includes:  
$$
x^2 + bx + c \quad \text{(can’t)}
$$