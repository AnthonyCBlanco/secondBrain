## Integration by Parts

### Idea
Integration by parts is the integral calculus analogue of the product rule for differentiation. When an integrand consists of a product of two distinct functions—such as algebraic, exponential, logarithmic, or trigonometric terms—where standard $u$-substitution is inapplicable, integration by parts transforms the original integral into a simpler, more tractable integral.

The core strategy involves partitioning the integrand into two components: a part $u$ to be differentiated, and a differential part $dv$ to be integrated. The choice of $u$ is guided by the **LIATE** mnemonic rule of priority:
1. **L** - Logarithmic functions ($\ln x$, $\log_b x$)
2. **I** - Inverse trigonometric functions ($\arctan x$, $\arcsin x$)
3. **A** - Algebraic / Polynomial functions ($x^n$, $3x^2 + 1$)
4. **T** - Trigonometric functions ($\sin x$, $\cos x$, $\sec x$)
5. **E** - Exponential functions ($e^x$, $2^x$)

### Formally
The integration by parts formula is derived directly from the product rule for differentiation:
$$\frac{d}{dx}[u(x)v(x)] = u'(x)v(x) + u(x)v'(x)$$

Integrating both sides with respect to $x$:
$$u(x)v(x) = \int u(x)v'(x)\,dx + \int v(x)u'(x)\,dx$$

Rearranging terms yields the standard indefinite integration by parts formula:
$$\int u \, dv = uv - \int v \, du$$

For definite integrals evaluated over the interval $[a, b]$, the Fundamental Theorem of Calculus gives:
$$\int_a^b u \, dv = \left[ u(x)v(x) \right]_a^b - \int_a^b v \, du = u(b)v(b) - u(a)v(a) - \int_a^b v \, du$$

#### Tabular Integration
When integrating polynomials multiplied by functions that can be repeatedly integrated (such as $e^{kx}$, $\sin(kx)$, or $\cos(kx)$), repeated integration by parts can be systematized using the tabular method:
1. Differentiate the polynomial column repeatedly until reaching zero.
2. Integrate the second column repeatedly.
3. Form diagonal products with alternating signs $(+, -, +, -, \dots)$.

#### Cyclic Integration
For integrands involving products of exponentials and sines or cosines (e.g., $\int e^{ax}\cos(bx)\,dx$), applying integration by parts twice yields a constant multiple of the original integral on the right-hand side, allowing the integral to be solved algebraically.

### Example
Evaluate the indefinite integral:
$$\int x e^{2x} \, dx$$

**Step 1: Assign $u$ and $dv$ using LIATE**
- Let $u = x \implies du = dx$
- Let $dv = e^{2x}dx \implies v = \int e^{2x}dx = \frac{1}{2}e^{2x}$

**Step 2: Apply the integration by parts formula**
$$\int u \, dv = uv - \int v \, du$$
$$\int x e^{2x} \, dx = x\left(\frac{1}{2}e^{2x}\right) - \int \frac{1}{2}e^{2x} \, dx$$

**Step 3: Evaluate the remaining integral**
$$\int x e^{2x} \, dx = \frac{1}{2}x e^{2x} - \frac{1}{2}\left(\frac{1}{2}e^{2x}\right) + C = \frac{1}{2}x e^{2x} - \frac{1}{4}e^{2x} + C$$

**Step 4: Factor to simplify**
$$\int x e^{2x} \, dx = \frac{1}{4}e^{2x}(2x - 1) + C$$

### Related
- [[The Chain Rule]]
- [[The Derivative]]
- [[Indefinite Integration]]
- [[Definite Integrals]]
- [[Fundamental Theorem of Calculus]]
- [[Integration by Substitution]]
- [[Trigonometric Integrals]]
- [[Volume by Cylindrical Shells]]

---
#math/calculus #spring2026
