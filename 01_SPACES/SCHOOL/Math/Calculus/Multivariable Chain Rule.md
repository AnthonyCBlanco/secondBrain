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
If $z = f(x, y)$ where $x = g(s, t)$ and $y = h(s, t)$ are differentiable functions of $s$ and $t$, then we use partial derivatives for everything:
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

#math/calculus #math/linearalgebra #summer2026
