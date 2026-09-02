## Limits

### Idea
In calculus, a **limit** describes the behavior of a function as the input approaches a certain value, rather than what the function is *exactly* at that value. 

Imagine walking along a path (the function) toward a specific destination (the x-value); the limit is the location you seem to be heading toward (the y-value). Limits are the foundation for the rest of Calculus 1, including derivatives and continuity, because they allow us to analyze behavior at points where a function might otherwise be broken, "jumping", or undefined.

### Formally
The **limit** of a function $f(x)$ as $x$ approaches a value $a$ is written as:

$$
\lim_{x \to a} f(x) = L
$$

This means that as $x$ gets **infinitely close to** $a$ (without actually reaching $a$), the value of $f(x)$ gets infinitely close to $L$.

For a limit to **exist**, the function must approach the same value from both the left side and the right side:
$$
\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L
$$
If the function "jumps" or behaves differently depending on which side you approach from, the overall limit **does not exist**.

*(Note for rigorous proofs: The formal $\epsilon-\delta$ definition states that for every $\epsilon > 0$, there exists a $\delta > 0$ such that $0 < |x - a| < \delta \implies |f(x) - L| < \epsilon$. This just formally means we can make the output as close as we want to $L$ by keeping the input close enough to $a$.)*

### Properties of Limits
If you know the limits of two functions, $\lim_{x \to c} f(x) = L$ and $\lim_{x \to c} g(x) = K$, you can combine them using these intuitive rules (where $b$ is a constant):

- **Constant Rule**: $\lim_{x \to c} b = b$
- **Scalar Multiple**: $\lim_{x \to c} \big(b \cdot f(x)\big) = b \cdot L$
- **Sum/Difference Rule**: $\lim_{x \to c} \big(f(x) \pm g(x)\big) = L \pm K$
- **Product Rule**: $\lim_{x \to c} \big(f(x) \cdot g(x)\big) = L \cdot K$
- **Quotient Rule**: $\lim_{x \to c} \frac{f(x)}{g(x)} = \frac{L}{K}$ (as long as $K \neq 0$)
- **Power/Root Rule**: $\lim_{x \to c} \big(f(x)\big)^n = (L)^n$

### Techniques for Finding Limits
When you are asked to evaluate a limit, try these steps in order:

1. **Direct Substitution**: Always try this first! If $f(x)$ is a standard, continuous function, just plug in $a$.
   $$ \lim_{x \to 2} (3x + 1) = 3(2) + 1 = 7 $$
2. **Factoring and Simplifying**: If substitution gives you $\frac{0}{0}$ (an indeterminate form), the limit might still exist. Try factoring the numerator and denominator to cancel out the "problem" term.
3. **Rationalizing**: Use conjugate expressions if you see square roots that result in $\frac{0}{0}$.
4. **Trigonometric Rules**: For trig functions, direct substitution works where the function is defined. Also, remember this special limit:
   $$ \lim_{x \to 0} \frac{\sin x}{x} = 1 $$
*(Note: Later in Calculus 2, you will learn **L'Hôpital's Rule**, which provides another powerful way to solve limits that result in $\frac{0}{0}$ or $\frac{\infty}{\infty}$ by using derivatives!)*

### Example
Evaluate the following limit:
$$
\lim_{x \to 2} \frac{x^2 - 4}{x - 2} 
$$

**Step 1: Try Direct Substitution**
Plugging in $x = 2$ gives $\frac{2^2 - 4}{2 - 2} = \frac{0}{0}$, which is undefined. We need to do more work.

**Step 2: Factor and Simplify**
Notice that the numerator is a difference of squares:
$$
\frac{x^2 - 4}{x - 2} = \frac{(x - 2)(x + 2)}{x - 2}
$$
Because a limit only cares about what happens as we *approach* $x = 2$ (so $x \neq 2$), we can cancel the $(x-2)$ terms.

**Step 3: Evaluate the new limit**
$$
\lim_{x \to 2} (x + 2) = 2 + 2 = 4
$$

**Conclusion:**
The limit is 4. Even though there is a "hole" in the graph exactly at $x = 2$, as the x-value gets really close to 2, the y-value gets really close to 4.

### Related
- [[One-Sided Limits]]
- [[Continuity and Limits]]
- [[Limits at Infinity]]
- [[Indeterminate Forms]]
- [[Difference Quotient]]

---
#math/analysis #math/calculus #math/derivatives #math/limits
