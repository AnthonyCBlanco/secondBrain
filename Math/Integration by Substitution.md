## Integration by Substitution

### Idea
**Integration by substitution** is a method used to evaluate integrals by reversing the **Chain Rule**.  
When a function is composed of an inner and an outer function, substitution simplifies the integral by introducing a new variable:

$$
u = g(x)
$$

This transforms the original integral into a simpler form in terms of $u$.  
It is one of the most important techniques for computing indefinite and definite integrals.

---

### Formally

#### Indefinite Integrals  
If $u = g(x)$ and $g$ is differentiable, then:

$$
\frac{du}{dx} = g'(x) \quad \Rightarrow \quad du = g'(x)\,dx
$$

A substitution converts:

$$
\int f(g(x)) g'(x)\,dx
$$

into

$$
\int f(u)\,du
$$

After integrating, substitute back using $u = g(x)$.

---

#### Definite Integrals  
When computing a definite integral using substitution:

1. Substitute $u = g(x)$  
2. Convert the integral limits:  
   If $x = a$, then $u = g(a)$;  
   If $x = b$, then $u = g(b)$  
3. Integrate in terms of $u$  
4. No need to substitute back to $x$

So:

$$
\int_a^b f(g(x))g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du
$$

---

### Why Substitution Works  
Integration by substitution “undoes” the **Chain Rule**:

$$
\frac{d}{dx}\left(F(g(x))\right) = F'(g(x)) \cdot g'(x)
$$

Thus,

$$
\int F'(g(x))g'(x)\,dx = F(g(x)) + C
$$

---

### Examples

#### Example 1: Indefinite Integral  
Evaluate:
$$
\int (6x)(x^2 + 5)^3 \, dx
$$

Let $u = x^2 + 5$  
Then $du = 2x\,dx$ → $6x\,dx = 3\,du$

Substitute:

$$
\int (x^2+5)^3 (6x \, dx) = \int 3u^3 \, du
$$

Integrate:

$$
3 \cdot \frac{u^4}{4} + C = \frac{3}{4}(x^2 + 5)^4 + C
$$

---

#### Example 2: Definite Integral  
Evaluate:
$$
\int_0^2 x\sqrt{x^2 + 1}\,dx
$$

Let $u = x^2 + 1$  
Then $du = 2x\,dx \Rightarrow x\,dx = \frac{1}{2}du$

Convert limits:  
- When $x = 0$: $u = 1$  
- When $x = 2$: $u = 5$

Substitute:

$$
\int_0^2 x\sqrt{x^2+1}\,dx = \int_1^5 \frac{1}{2}\sqrt{u}\,du
$$

Integrate:

$$
\frac{1}{2} \cdot \frac{2}{3} u^{3/2} \Big|_1^5 = \frac{1}{3}(5^{3/2} - 1)
$$

---

### Common Substitution Patterns

| Integrand Pattern | Suggested $u$ |
|-------------------|----------------|
| $(g(x))^n g'(x)$ | $u = g(x)$ |
| $\cos(x)\sin(x)$ | $u = \sin(x)$ or $\cos(x)$ |
| $\frac{g'(x)}{g(x)}$ | $u = g(x)$ |
| $e^{g(x)} g'(x)$ | $u = g(x)$ |
| $\sqrt{a^2 - x^2}$ | Trig substitution (advanced) |

---

### Tips  
- Choose $u$ to simplify the integrand.  
- Always compute **$du$ carefully**.  
- Rewrite *everything* in terms of $u$ before integrating.  
- For definite integrals, **change the limits** to avoid switching back to $x$.

---

### Concept Summary

| Concept | Formula | Meaning |
|---------|---------|---------|
| Substitution | $u = g(x)$ | Rewrites integral in simpler form |
| Differential | $du = g'(x)\,dx$ | Converts $dx$ terms |
| Definite integral rule | $\int_a^b f(g(x))g'(x)\,dx = \int_{g(a)}^{g(b)} f(u)\,du$ | Change bounds accordingly |
| Purpose | Simplification | Reverse the chain rule |

---

### Related Notes
- [[Indefinite Integration]]
- [[Definite Integrals]]
- [[Fundamental Theorem of Calculus]]
- [[The Chain Rule]]
- [[Riemann Sums]]

---

#math #calculus #integration #substitution
