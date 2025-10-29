# Work and Energy

### Idea

**Work** and **energy** are closely related physical concepts.  
Work is the **transfer of energy** that occurs when a **force** acts over a **distance**.  

When work is done **on** an object, its **energy changes** — typically in the form of kinetic or potential energy.

---

### Definition of Work

Work ($W$) is defined as the **dot product** of force and displacement:

$$
W = \vec{F} \cdot \vec{\Delta r} = F \Delta r \cos\theta
$$

where:  
- $F$ = magnitude of the applied force  
- $\Delta r$ = displacement of the object  
- $\theta$ = angle between $\vec{F}$ and $\vec{\Delta r}$  

---

### Interpreting Work

- If $0° < \theta < 90°$: **Work is positive** → increases energy.  
- If $\theta = 90°$: **Work is zero** → no energy transfer.  
- If $90° < \theta < 180°$: **Work is negative** → energy is removed (slows motion).  

---

### Variable Force

If the force changes along the path, total work is found using the **integral**:

$$
W = \int_{x_i}^{x_f} \vec{F}(x) \cdot d\vec{r}
$$

Example: For a spring ($F = -kx$):

$$
W = \int_{0}^{x} (-kx) \, dx = -\frac{1}{2}kx^2
$$

---

### Units of Work

| Quantity | Symbol | SI Unit | Equivalent |
|-----------|---------|----------|-------------|
| Work | $W$ | Joule (J) | $1 \text{ J} = 1 \text{ N·m}$ |
| Force | $F$ | Newton (N) | $1 \text{ N} = 1 \text{ kg·m/s}^2$ |
| Displacement | $r$ | meter (m) | — |

---

### Work Done by Different Forces

| Force Type | Work Expression | Notes |
|-------------|----------------|-------|
| Constant Force | $W = F \Delta r \cos\theta$ | Simplest case |
| Spring Force | $W = -\frac{1}{2}kx^2$ | Negative sign indicates restoring force |
| Gravity | $W = -mg\Delta h$ | Work done by gravity is **negative** when lifting |
| Friction | $W_f = -f_k \Delta r$ | Always removes energy (non-conservative) |

---

### Kinetic Energy

The **kinetic energy** of an object is the energy due to motion:

$$
K = \frac{1}{2}mv^2
$$

---

### The Work–Energy Theorem

The **net work** done on an object is equal to its **change in kinetic energy**:

$$
W_{\text{net}} = \Delta K = K_f - K_i
$$

This connects **forces** to **energy changes** directly:

$$
\sum \vec{F} \cdot \vec{r} = \frac{1}{2}m v_f^2 - \frac{1}{2}m v_i^2
$$

> If net work is positive → the object speeds up.  
> If net work is negative → the object slows down.

---

### Potential Energy and Work

When forces are **conservative** (e.g., gravity, springs), the work done can be expressed as a change in **potential energy**:

$$
W = -\Delta U
$$

Examples:
- Gravitational potential energy: $U_g = mgh$
- Elastic potential energy: $U_s = \frac{1}{2}kx^2$

---

### Power

Power is the **rate** of doing work:

$$
P = \frac{dW}{dt}
$$

For constant force and velocity:

$$
P = \vec{F} \cdot \vec{v}
$$

Units of power: **Watt (W)**  
$1 \text{ W} = 1 \text{ J/s}$

---

### Example Problem

**A 5 kg box is pushed 3 m across a floor by a 10 N horizontal force. Find the work done.**

**Solution:**

Given:  
$F = 10 \text{ N}, \Delta r = 3 \text{ m}, \theta = 0°$

$$
W = F \Delta r \cos\theta = 10(3)(\cos 0°) = 30 \text{ J}
$$

---

### Concept Summary

| Concept             | Formula                     | Description                   |
| ------------------- | --------------------------- | ----------------------------- |
| Work                | $W = F \Delta r \cos\theta$ | Energy transferred by a force |
| Kinetic Energy      | $K = \frac{1}{2}mv^2$       | Energy of motion              |
| Work–Energy Theorem | $W_{\text{net}} = \Delta K$ | Relates work and motion       |
| Power               | $P = \frac{dW}{dt}$         | Rate of doing work            |
| Potential Energy    | $U = mgh, \frac{1}{2}kx^2$  | Stored energy due to position |

---

### Related Notes

- [[Conservation of Energy]]
- [[Laws of Motion]]
- [[Motion in One Dimension]]
- [[Friction]]

---

#physics #mechanics #energy #work #power
