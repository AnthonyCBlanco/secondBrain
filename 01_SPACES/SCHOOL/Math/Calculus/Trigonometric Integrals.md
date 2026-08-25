## Trigonometric Integrals

### Idea
Trigonometric integrals involve integrands composed of products and powers of trigonometric functions, predominantly of the forms $\int \sin^m x \cos^n x \, dx$ and $\int \tan^m x \sec^n x \, dx$. 

The overarching strategy relies on exploiting fundamental trigonometric identities (Pythagorean and half-angle / power-reducing identities) to isolate a single derivative factor (such as $\sin x \, dx$, $\cos x \, dx$, $\sec^2 x \, dx$, or $\sec x \tan x \, dx$) and rewrite the remaining integrand purely in terms of the corresponding base trigonometric function, enabling standard $u$-substitution.

### Formally
#### Core Trigonometric Identities
1. **Pythagorean Identities:**
   $$\sin^2 x + \cos^2 x = 1, \quad \tan^2 x + 1 = \sec^2 x, \quad 1 + \cot^2 x = \csc^2 x$$
2. **Half-Angle / Power-Reducing Identities:**
   $$\sin^2 x = \frac{1 - \cos(2x)}{2}, \quad \cos^2 x = \frac{1 + \cos(2x)}{2}, \quad \sin x \cos x = \frac{1}{2}\sin(2x)$$

#### Strategy for $\int \sin^m x \cos^n x \, dx$
- **Case 1 (Power of sine $m$ is odd):**
  Split off one factor of $\sin x \, dx$, convert the remaining even power $\sin^{m-1} x$ into cosines using $\sin^2 x = 1 - \cos^2 x$, and substitute $u = \cos x$, $du = -\sin x \, dx$:
  $$\int \sin^{2k+1} x \cos^n x \, dx = \int (1 - \cos^2 x)^k \cos^n x (\sin x \, dx) = -\int (1 - u^2)^k u^n \, du$$
- **Case 2 (Power of cosine $n$ is odd):**
  Split off one factor of $\cos x \, dx$, convert the remaining even power $\cos^{n-1} x$ into sines using $\cos^2 x = 1 - \sin^2 x$, and substitute $u = \sin x$, $du = \cos x \, dx$:
  $$\int \sin^m x \cos^{2k+1} x \, dx = \int \sin^m x (1 - \sin^2 x)^k (\cos x \, dx) = \int u^m (1 - u^2)^k \, du$$
- **Case 3 (Both powers $m$ and $n$ are even and non-negative):**
  Repeatedly apply the half-angle formulas to lower the exponents until reducible to standard cosine integrals.

#### Strategy for $\int \tan^m x \sec^n x \, dx$
- **Case 1 (Power of secant $n$ is even):**
  Split off $\sec^2 x \, dx$, convert the remaining $\sec^{n-2} x$ into tangents using $\sec^2 x = 1 + \tan^2 x$, and substitute $u = \tan x$, $du = \sec^2 x \, dx$.
- **Case 2 (Power of tangent $m$ is odd):**
  Split off $\sec x \tan x \, dx$, convert the remaining $\tan^{m-1} x$ into secants using $\tan^2 x = \sec^2 x - 1$, and substitute $u = \sec x$, $du = \sec x \tan x \, dx$.

#### Essential Antiderivatives
$$\int \tan x \, dx = \ln|\sec x| + C, \quad \int \sec x \, dx = \ln|\sec x + \tan x| + C$$
$$\int \cot x \, dx = \ln|\sin x| + C, \quad \int \csc x \, dx = -\ln|\csc x + \cot x| + C$$

### Example
Evaluate the indefinite integral:
$$\int \sin^3 x \cos^2 x \, dx$$

**Step 1: Separate one factor of sine (since the power of sine is odd, $m = 3$)**
$$\int \sin^3 x \cos^2 x \, dx = \int \sin^2 x \cos^2 x (\sin x \, dx)$$

**Step 2: Express $\sin^2 x$ in terms of $\cos x$ using $\sin^2 x = 1 - \cos^2 x$**
$$\int \sin^2 x \cos^2 x (\sin x \, dx) = \int (1 - \cos^2 x) \cos^2 x (\sin x \, dx)$$

**Step 3: Perform $u$-substitution**
Let $u = \cos x \implies du = -\sin x \, dx \implies \sin x \, dx = -du$.
$$\int (1 - u^2) u^2 (-du) = -\int (u^2 - u^4) \, du = \int (u^4 - u^2) \, du$$

**Step 4: Integrate using the power rule**
$$\int (u^4 - u^2) \, du = \frac{u^5}{5} - \frac{u^3}{3} + C$$

**Step 5: Substitute back $u = \cos x$**
$$\int \sin^3 x \cos^2 x \, dx = \frac{1}{5}\cos^5 x - \frac{1}{3}\cos^3 x + C$$

### Related
- [[Integration by Substitution]]
- [[Integration by Parts]]
- [[Trigonometric Substitution]]
- [[Indefinite Integration]]
- [[Definite Integrals]]

---
#math/calculus #spring2026
