## Partial Fractions

### Idea
Partial fraction decomposition is an algebraic technique used to integrate rational functions $\frac{P(x)}{Q(x)}$, where $P(x)$ and $Q(x)$ are polynomials. 

By decomposing a complex rational expression into a sum of simpler algebraic fractions whose denominators are the linear or irreducible quadratic factors of $Q(x)$, each constituent term can be integrated straightforwardly using logarithmic rules ($\int \frac{1}{u}\,du = \ln|u| + C$), inverse trigonometric rules ($\int \frac{1}{u^2 + a^2}\,du = \frac{1}{a}\arctan\left(\frac{u}{a}\right) + C$), or standard power rules.

### Formally
#### Prerequisite: Proper Rational Function
The degree of the numerator must be strictly less than the degree of the denominator ($\deg(P) < \deg(Q)$). If $\deg(P) \ge \deg(Q)$, polynomial long division must first be executed:
$$\frac{P(x)}{Q(x)} = S(x) + \frac{R(x)}{Q(x)} \quad \text{where } \deg(R) < \deg(Q)$$

#### Decomposition Cases for $Q(x)$ over $\mathbb{R}$
1. **Distinct Linear Factors:** If $Q(x) = (x - r_1)(x - r_2)\dots(x - r_k)$, the decomposition has the form:
   $$\frac{P(x)}{Q(x)} = \frac{A_1}{x - r_1} + \frac{A_2}{x - r_2} + \dots + \frac{A_k}{x - r_k}$$
2. **Repeated Linear Factors:** If $Q(x)$ contains a repeated linear factor $(x - r)^k$:
   $$\frac{A_1}{x - r} + \frac{A_2}{(x - r)^2} + \dots + \frac{A_k}{(x - r)^k}$$
3. **Distinct Irreducible Quadratic Factors:** For non-repeated factors of the form $ax^2 + bx + c$ with discriminant $b^2 - 4ac < 0$:
   $$\frac{Ax + B}{ax^2 + bx + c}$$
4. **Repeated Irreducible Quadratic Factors:** For factors of the form $(ax^2 + bx + c)^k$:
   $$\frac{A_1 x + B_1}{ax^2 + bx + c} + \frac{A_2 x + B_2}{(ax^2 + bx + c)^2} + \dots + \frac{A_k x + B_k}{(ax^2 + bx + c)^k}$$

#### Solving for Unknown Coefficients
- **Method of Equating Coefficients:** Clear denominators, expand both sides, group terms by powers of $x$, and solve the resulting system of linear equations.
- **Heaviside Cover-Up Method:** For distinct linear factors, evaluate the cleared equation at the roots $x = r_i$ to isolate each constant $A_i$ directly.

### Example
Evaluate the indefinite integral:
$$\int \frac{5x - 3}{x^2 - 2x - 3} \, dx$$

**Step 1: Verify degrees and factor the denominator**
The fraction is proper since $\deg(P) = 1 < \deg(Q) = 2$. Factor the denominator:
$$x^2 - 2x - 3 = (x - 3)(x + 1)$$

**Step 2: Set up the partial fraction decomposition**
$$\frac{5x - 3}{(x - 3)(x + 1)} = \frac{A}{x - 3} + \frac{B}{x + 1}$$

**Step 3: Clear denominators**
$$5x - 3 = A(x + 1) + B(x - 3)$$

**Step 4: Solve for coefficients $A$ and $B$**
- Substitute $x = 3$:
  $$5(3) - 3 = A(3 + 1) + B(0) \implies 12 = 4A \implies A = 3$$
- Substitute $x = -1$:
  $$5(-1) - 3 = A(0) + B(-1 - 3) \implies -8 = -4B \implies B = 2$$

**Step 5: Integrate the decomposed components**
$$\int \left( \frac{3}{x - 3} + \frac{2}{x + 1} \right) dx = 3\int \frac{1}{x - 3}\,dx + 2\int \frac{1}{x + 1}\,dx$$
$$= 3\ln|x - 3| + 2\ln|x + 1| + C = \ln\left( |x - 3|^3 (x + 1)^2 \right) + C$$

### Related
- [[Integration and Differentiation of Logarithmic Functions]]
- [[Inverse Trig Functions Derivative & Integrals]]
- [[Indefinite Integration]]
- [[Integration by Substitution]]
- [[Fundamental Theorem of Calculus]]
- [[Trigonometric Substitution]]
- [[Improper Integrals]]

---
#math/calculus #spring2026
