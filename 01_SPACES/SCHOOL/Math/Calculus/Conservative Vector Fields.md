### Idea
In physics, a force is called "conservative" if the work it does moving an object between two points is independent of the path taken (like gravity). In mathematics, a [[Vector Fields|vector field]] $\vec{F}$ is **conservative** if it is the [[Gradient Vector|gradient]] of some scalar function $f$.
$$ \vec{F} = \nabla f $$
When this is true, the scalar function $f$ is called the **Potential Function** of $\vec{F}$.

### How to Test for a Conservative Field
You can quickly determine if a given vector field is conservative without having to find its potential function.

**In 2D ($\vec{F} = \langle P, Q \rangle$):**
Because mixed [[Partial Derivative|partial derivatives]] must be equal (Clairaut's Theorem, meaning $f_{xy} = f_{yx}$), a 2D vector field is conservative if and only if:
$$ \frac{\partial P}{\partial y} = \frac{\partial Q}{\partial x} $$

**In 3D ($\vec{F} = \langle P, Q, R \rangle$):**
A 3D vector field is conservative if and only if it is completely irrotational. This means its curl must be the zero vector:
$$ \text{curl } \vec{F} = \nabla \times \vec{F} = \vec{0} $$
(See [[Divergence and Curl]]).

### How to Find the Potential Function
If you know a 2D field $\vec{F} = \langle P, Q \rangle$ is conservative, you can reverse-engineer the gradient to find the original potential function $f(x, y)$.

1. **Set up your equations:** 
   Since $\vec{F} = \nabla f$, we know that $f_x = P$ and $f_y = Q$.
2. **Integrate with respect to $x$:**
   Take the first equation ($f_x = P$) and integrate it with respect to $x$. 
   $$ f(x, y) = \int P \, dx + g(y) $$
   *Note: Because you are partially integrating with respect to $x$, the "constant of integration" is not a number $C$, but an unknown function $g(y)$ that depends entirely on $y$.*
3. **Differentiate with respect to $y$:**
   Take your new $f(x, y)$ equation and take the partial derivative with respect to $y$. 
4. **Set equal to $Q$:**
   Set that derivative equal to your original $Q$ component. This will allow you to solve for $g'(y)$.
5. **Integrate $g'(y)$ to find $g(y)$:**
   Integrate your result with respect to $y$ to find the missing function $g(y)$ (this time using a standard $+ C$).
6. **Assemble the final function:**
   Plug $g(y)$ back into your equation from step 2 to get the complete potential function $f(x, y)$.

*(This exact same process applies to 3D fields, but you have an extra component $R$ and a $+ h(y, z)$ constant function to solve for).*

### The Fundamental Theorem of Line Integrals
The most powerful reason we care about conservative fields is because they make line integrals incredibly easy. If $\vec{F}$ is a conservative field with potential function $f$, then the line integral over any curve $C$ from point $A$ to point $B$ is completely **path independent**:
$$
\int_C \vec{F} \cdot d\vec{r} = \int_C \nabla f \cdot d\vec{r} = f(B) - f(A)
$$
You simply evaluate the potential function at the endpoints!

### Related
- [[Vector Fields]]
- [[Gradient Vector]]
- [[Divergence and Curl]]
- [[Partial Derivative]]

#math/calculus #summer2026
