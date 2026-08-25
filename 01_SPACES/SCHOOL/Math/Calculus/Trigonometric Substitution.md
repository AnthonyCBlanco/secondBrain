## Trigonometric Substitution

### Idea
Trigonometric substitution is a specialized technique designed to evaluate integrals containing quadratic radical expressions of the forms $\sqrt{a^2 - x^2}$, $\sqrt{a^2 + x^2}$, or $\sqrt{x^2 - a^2}$ that cannot be resolved using standard algebraic substitutions.

By substituting the variable $x$ with an appropriate trigonometric function of a new variable $\theta$ ($a\sin\theta$, $a\tan\theta$, or $a\sec\theta$), the radical collapses into a single trigonometric expression via the fundamental Pythagorean identities. Once the trigonometric integral is evaluated in terms of $\theta$, a geometric right triangle (reference triangle) is used to translate the trigonometric functions back into algebraic expressions in $x$.

### Formally
#### Canonical Substitutions Table ($a > 0$)
| Radical Expression | Substitution | Restricted Angle Domain | Differential $dx$ | Identity Applied | Simplified Radical |
| :--- | :--- | :--- | :--- | :--- | :--- |
| $\sqrt{a^2 - x^2}$ | $x = a \sin \theta$ | $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2}$ | $dx = a \cos \theta \, d\theta$ | $1 - \sin^2 \theta = \cos^2 \theta$ | $a \cos \theta$ |
| $\sqrt{a^2 + x^2}$ | $x = a \tan \theta$ | $-\frac{\pi}{2} < \theta < \frac{\pi}{2}$ | $dx = a \sec^2 \theta \, d\theta$ | $1 + \tan^2 \theta = \sec^2 \theta$ | $a \sec \theta$ |
| $\sqrt{x^2 - a^2}$ | $x = a \sec \theta$ | $0 \le \theta < \frac{\pi}{2}$ or $\pi \le \theta < \frac{3\pi}{2}$ | $dx = a \sec \theta \tan \theta \, d\theta$ | $\sec^2 \theta - 1 = \tan^2 \theta$ | $a \tan \theta$ |

#### Reference Triangle Reconstruction
After evaluating the integral in $\theta$, construct a right triangle corresponding to the original substitution:
- For $x = a \sin \theta \implies \sin \theta = \frac{x}{a}$: $\text{opposite} = x$, $\text{hypotenuse} = a$, $\text{adjacent} = \sqrt{a^2 - x^2}$.
- For $x = a \tan \theta \implies \tan \theta = \frac{x}{a}$: $\text{opposite} = x$, $\text{adjacent} = a$, $\text{hypotenuse} = \sqrt{a^2 + x^2}$.
- For $x = a \sec \theta \implies \sec \theta = \frac{x}{a}$: $\text{hypotenuse} = x$, $\text{adjacent} = a$, $\text{opposite} = \sqrt{x^2 - a^2}$.

### Example
Evaluate the indefinite integral:
$$\int \frac{1}{x^2 \sqrt{4 - x^2}} \, dx$$

**Step 1: Identify the radical form and substitute**
The radical is of the form $\sqrt{a^2 - x^2}$ with $a = 2$.
- Let $x = 2 \sin \theta \implies dx = 2 \cos \theta \, d\theta$.
- Then $\sqrt{4 - x^2} = \sqrt{4 - 4\sin^2 \theta} = \sqrt{4\cos^2 \theta} = 2\cos \theta$ (since $-\frac{\pi}{2} \le \theta \le \frac{\pi}{2} \implies \cos \theta \ge 0$).

**Step 2: Substitute into the integral**
$$\int \frac{1}{x^2 \sqrt{4 - x^2}} \, dx = \int \frac{2 \cos \theta \, d\theta}{(2 \sin \theta)^2 (2 \cos \theta)} = \int \frac{2 \cos \theta \, d\theta}{4 \sin^2 \theta \cdot 2 \cos \theta} = \frac{1}{4} \int \frac{1}{\sin^2 \theta} \, d\theta$$

**Step 3: Integrate the trigonometric expression**
$$\frac{1}{4} \int \csc^2 \theta \, d\theta = -\frac{1}{4} \cot \theta + C$$

**Step 4: Return to the variable $x$ via the reference triangle**
Since $\sin \theta = \frac{x}{2} = \frac{\text{opposite}}{\text{hypotenuse}}$, the adjacent side is $\sqrt{4 - x^2}$.
Therefore:
$$\cot \theta = \frac{\text{adjacent}}{\text{opposite}} = \frac{\sqrt{4 - x^2}}{x}$$

**Step 5: Write the final algebraic antiderivative**
$$\int \frac{1}{x^2 \sqrt{4 - x^2}} \, dx = -\frac{\sqrt{4 - x^2}}{4x} + C$$

### Related
- [[Trigonometric Integrals]]
- [[Integration by Substitution]]
- [[Inverse Trig Functions Derivative & Integrals]]
- [[Indefinite Integration]]
- [[Definite Integrals]]

---
#math/calculus #spring2026
