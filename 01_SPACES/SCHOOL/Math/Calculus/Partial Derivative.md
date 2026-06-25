### Idea
Previously we studied [[The Derivative|derivatives]] as the change of some $y$ with respect to $x$, ($\frac{dy}{dx}$). When we talk about [[Multivariable Functions]], it makes sense to want to know the change of $z$ with respect to $x$ and/or $y$. $z=f(x,y)$ 

We can think of partial derivatives as setting one variable as a constant.
$$\begin{gather}
\frac{\partial}{\partial x}(x^2y)=2xy \\
\text{or} \\
\frac{\partial}{\partial x}(y^3)=0 \, |\, \text{as if y was a constant!}
\end{gather}
$$

### Notation
For a function $f(x, y)$, the partial derivative with respect to $x$ can be written as:
- $f_x$ or $f_x(x, y)$
- $\frac{\partial f}{\partial x}$ or $\frac{\partial}{\partial x}f(x,y)$

### Geometric Interpretation
#### Tangent Plane idea
If we have a surface $z = f(x, y)$, the partial derivative $f_x(x_0, y_0)$ is the slope of the tangent line to the curve formed by the intersection of the surface and the plane $y = y_0$.

Similarly, $f_y(x_0, y_0)$ is the slope of the tangent line to the curve formed by the intersection of the surface and the plane $x = x_0$.

The **Tangent Plane** to the surface at $(x_0, y_0, z_0)$ is given by:
$$z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$

### Formally
The partial derivative of $f(x, y)$ with respect to $x$ at $(a, b)$ is defined as:
$$f_x(a, b) = \lim_{h \to 0} \frac{f(a+h, b) - f(a, b)}{h}$$

The partial derivative of $f(x, y)$ with respect to $y$ at $(a, b)$ is defined as:
$$f_y(a, b) = \lim_{h \to 0} \frac{f(a, b+h) - f(a, b)}{h}$$

### Higher-Order Partial Derivatives
We can take derivatives of derivatives:
- $f_{xx} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial^2 f}{\partial x^2}$
- $f_{yy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right) = \frac{\partial^2 f}{\partial y^2}$
- $f_{xy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) = \frac{\partial^2 f}{\partial y \partial x}$ (Mixed Partial)

#### Example
Let $f(x, y) = x^3 + x^2y^3 - 2y^2$.
1. $f_x = 3x^2 + 2xy^3$
2. $f_y = 3x^2y^2 - 4y$
3. $f_{xy} = \frac{\partial}{\partial y}(3x^2 + 2xy^3) = 6xy^2$
4. $f_{yx} = \frac{\partial}{\partial x}(3x^2y^2 - 4y) = 6xy^2$

#### Clairaut's Theorem
If $f_{xy}$ and $f_{yx}$ are continuous, then:
$$f_{xy} = f_{yx}$$
As seen in the example above, $f_{xy} = f_{yx} = 6xy^2$.

#math/calculus #summer2026