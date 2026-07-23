### Idea
A **Vector Field** is a function that assigns a vector to every single point in a space. 
Imagine looking at a weather map showing wind currents: at every coordinate $(x, y)$ on the map, there is an arrow pointing in the direction the wind is blowing, with a length proportional to the wind speed. That entire collection of arrows is a vector field.

Vector fields are incredibly important in physics and engineering to model fluid flow (velocity fields), gravity, and electromagnetism (force fields).

### Formally
In 2D space ($\mathbb{R}^2$), a vector field $\vec{F}$ is defined by two scalar component functions, $P(x, y)$ and $Q(x, y)$:
$$
\vec{F}(x, y) = \langle P(x, y), Q(x, y) \rangle = P(x, y)\hat{i} + Q(x, y)\hat{j}
$$

In 3D space ($\mathbb{R}^3$), it requires three component functions:
$$
\vec{F}(x, y, z) = \langle P(x, y, z), Q(x, y, z), R(x, y, z) \rangle = P\hat{i} + Q\hat{j} + R\hat{k}
$$

*(Note: Don't confuse this with [[Vector Valued Functions]], which map a single parameter $t$ to a vector to trace out a curve. A vector field maps spatial coordinates to a vector to fill a space).*

### [[Gradient Vector]] Fields
One of the most important types of vector fields comes from scalar functions. If you take a standard scalar function $f(x, y)$ (like a topographical map of a mountain) and calculate its [[Gradient Vector]] at every point, the resulting collection of gradient [[Vectors|vectors]] forms a **[[Gradient Vector]] Field**:
$$
\vec{F}(x, y) = \nabla f(x, y)
$$

If a vector field $\vec{F}$ happens to equal the gradient of some scalar function $f$, then:
1. $\vec{F}$ is called a **Conservative Vector Field**.
2. The scalar function $f$ is called the **Potential Function** for $\vec{F}$.

In physics, gravitational and electrostatic fields are conservative, meaning they have a potential function (gravitational potential energy or electric potential).

### Visualization
To visualize a vector field $\vec{F}(x, y) = \langle -y, x \rangle$:
- At point $(1, 0)$, the vector is $\langle 0, 1 \rangle$ (points straight up).
- At point $(0, 1)$, the vector is $\langle -1, 0 \rangle$ (points left).
- At point $(-1, 0)$, the vector is $\langle 0, -1 \rangle$ (points down).
- At point $(0, -1)$, the vector is $\langle 1, 0 \rangle$ (points right).

If you plot these arrows on a graph, you will see a counter-clockwise rotational pattern (a vortex).

### Related
- [[Gradient Vector]]
- [[Vector Valued Functions]]

#math/calculus #summer2026
