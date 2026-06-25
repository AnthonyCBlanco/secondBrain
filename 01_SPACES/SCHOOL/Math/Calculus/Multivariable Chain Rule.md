### Idea
Using the chain rule with multivariable functions is similar but more complex. 
In calculus 1 we learn that [[The Chain Rule]] is defined by:
$$
\frac{d}{dx}[f \circ g]= \frac{d}{dx}[f(g(x))]=f'(g(x))\cdot g'(x) 
$$
When we are using partials to derive functions of multiple variables it can get confusing as we do not have simply $f'(g(x))=f'(g(x))\cdot g'(x)$ because we can get many partials from one function for example:

Given:
$$\begin{gather}
x=2t \,\,\,y=3t+s \,\,\, z=xy
\end{gather}
$$
We may encounter many different partial derivatives. Just as $g(x)$ is a function substituted into $f(x)$ in Calculus 1, here we have $x$ as a function of $t$, $y$ as a function of $s$ and $t$, and $z$ as a function of $x$ and $y$.

### Formally
If $z = f(x, y)$ is a differentiable function of $x$ and $y$, and $x = g(t)$ and $y = h(t)$ are differentiable functions of $t$, then $z$ is a differentiable function of $t$ and:
$$
\frac{dz}{dt} = \frac{\partial z}{\partial x} \frac{dx}{dt} + \frac{\partial z}{\partial y} \frac{dy}{dt}
$$

**General Case (Multiple Independent Variables):**
If $z = f(x, y)$ where $x = g(s, t)$ and $y = h(s, t)$ are differentiable functions of $s$ and $t$, then we use [[Partial Derivative|Partial Derivatives]] for everything:
$$
\frac{\partial z}{\partial s} = \frac{\partial z}{\partial x} \frac{\partial x}{\partial s} + \frac{\partial z}{\partial y} \frac{\partial y}{\partial s}
$$
$$
\frac{\partial z}{\partial t} = \frac{\partial z}{\partial x} \frac{\partial x}{\partial t} + \frac{\partial z}{\partial y} \frac{\partial y}{\partial t}
$$

### Tree Diagrams
To keep track of the variables and how to apply the chain rule without memorizing formulas, we can use a **Tree Diagram**.
1. Start with the **dependent variable** at the top.
2. Draw branches to the **intermediate variables**.
3. Draw branches from each intermediate variable to the **independent variables**.
4. To find the derivative with respect to an independent variable:
   - **Multiply** the derivatives along each path leading to that independent variable.
   - **Add** the products of all paths that lead to that independent variable.

#### Example (from above)
Given $z = xy$, where $x = 2t$ and $y = 3t + s$:
- The dependent variable is $z$.
- The intermediate variables are $x$ and $y$.
- The independent variables are $t$ and $s$.

Let's find $\frac{\partial z}{\partial t}$:
By tracing the paths to $t$ through both $x$ and $y$, we get:
$$
\frac{\partial z}{\partial t} = \frac{\partial z}{\partial x} \frac{dx}{dt} + \frac{\partial z}{\partial y} \frac{\partial y}{\partial t}
$$
Calculating each part:
- $\frac{\partial z}{\partial x} = y$
- $\frac{dx}{dt} = 2$
- $\frac{\partial z}{\partial y} = x$
- $\frac{\partial y}{\partial t} = 3$

Substituting these back into the formula:
$$
\frac{\partial z}{\partial t} = (y)(2) + (x)(3) = 2y + 3x
$$
Finally, we can express the answer completely in terms of independent variables ($s$ and $t$) by substituting $x$ and $y$:
$$
\frac{\partial z}{\partial t} = 2(3t + s) + 3(2t) = 6t + 2s + 6t = 12t + 2s
$$

### The Jacobian Matrix Method
The multivariable chain rule can also be expressed using **Jacobian Matrices**. This is particularly useful in Linear Algebra and when dealing with vector-valued functions. 

If we have a composition of functions, the derivative (Jacobian) of the composition is simply the product of their Jacobian matrices:
$$ D_{f \circ g} = D_{f} \cdot D_g $$

Using the general case where $z = f(x, y)$ and $(x, y)$ are functions of $(s, t)$:
1. The Jacobian of $z$ with respect to the intermediate variables $x, y$ is a $1 \times 2$ row vector:
   $$ D_z = \begin{bmatrix} \frac{\partial z}{\partial x} & \frac{\partial z}{\partial y} \end{bmatrix} $$

2. The Jacobian of the intermediate variables $x, y$ with respect to the independent variables $s, t$ is a $2 \times 2$ matrix:
   $$ D_{x,y} = \begin{bmatrix} \frac{\partial x}{\partial s} & \frac{\partial x}{\partial t} \\ \frac{\partial y}{\partial s} & \frac{\partial y}{\partial t} \end{bmatrix} $$

3. Multiplying them together gives the Jacobian of $z$ with respect to $s$ and $t$:
   $$ 
   D_{z(s,t)} = \begin{bmatrix} \frac{\partial z}{\partial x} & \frac{\partial z}{\partial y} \end{bmatrix} \begin{bmatrix} \frac{\partial x}{\partial s} & \frac{\partial x}{\partial t} \\ \frac{\partial y}{\partial s} & \frac{\partial y}{\partial t} \end{bmatrix} 
   $$
   $$
   D_{z(s,t)} = \begin{bmatrix} 
   \left( \frac{\partial z}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial s} \right) & 
   \left( \frac{\partial z}{\partial x}\frac{\partial x}{\partial t} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial t} \right)
   \end{bmatrix}
   $$
   
Notice that the resulting $1 \times 2$ matrix contains exactly the chain rule formulas for $\frac{\partial z}{\partial s}$ and $\frac{\partial z}{\partial t}$! Matrix multiplication automatically handles the "multiply paths and add them up" logic of the tree diagram.

#math/calculus #math/linearalgebra #summer2026
