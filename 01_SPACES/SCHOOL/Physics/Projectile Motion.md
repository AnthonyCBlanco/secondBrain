# Projectile Motion

### Idea
- A type of **two-dimensional motion** where an object is launched into the air and moves under the influence of **gravity** (ignoring air resistance).  
- The motion is a combination of:  
  - **Horizontal motion** with constant velocity.  
  - **Vertical motion** with constant acceleration ($a_y = -g$).  
- The path (trajectory) is a **parabola**.  

---

## Assumptions
1. Acceleration due to gravity is constant ($g \approx 9.8 \, \text{m/s}^2$).  
2. Air resistance is negligible.  
3. The horizontal and vertical components are independent, connected only by **time**.  

---

## Equations of Motion

### Horizontal Motion
- Constant velocity:  
  $$
  v_x = v_{0x}
  $$
- Position:  
  $$
  x(t) = x_0 + v_{0x}t
  $$

---

### Vertical Motion
- Velocity:  
  $$
  v_y = v_{0y} - g t
  $$
- Position:  
  $$
  y(t) = y_0 + v_{0y}t - \tfrac{1}{2}gt^2
  $$

---

## Trajectory Equation
Eliminating time ($t = \frac{x-x_0}{v_{0x}}$):  

$$
y = y_0 + \Big(\frac{v_{0y}}{v_{0x}}\Big)(x - x_0) - \frac{g}{2v_{0x}^2}(x - x_0)^2
$$  

This is a **parabola**.  

---

## Key Results (Launched from Ground, $y_0=0$)

1. **Time of Flight**  
   $$
   T = \frac{2v_{0y}}{g}
   $$

2. **Maximum Height**  
   $$
   H = \frac{v_{0y}^2}{2g}
   $$

3. **Horizontal Range**  
   $$
   R = \frac{v_0^2 \sin(2\theta)}{g}
   $$

Where:  
- $v_0$ = initial launch speed  
- $\theta$ = launch angle  
- $v_{0x} = v_0 \cos\theta$  
- $v_{0y} = v_0 \sin\theta$  

---

## Vector Components
- Displacement:  
  $$
  \vec{r}(t) = (x_0 + v_{0x}t)\hat{i} + \big(y_0 + v_{0y}t - \tfrac{1}{2}gt^2\big)\hat{j}
  $$

- Velocity:  
  $$
  \vec{v}(t) = v_{0x}\hat{i} + (v_{0y} - gt)\hat{j}
  $$

- Acceleration:  
  $$
  \vec{a} = -g \hat{j}
  $$

---

## Key Notes
- Horizontal motion is **uniform (constant velocity)**.  
- Vertical motion is **accelerated** (constant acceleration).  
- Maximum height occurs when $v_y = 0$.  
- Range is maximized at $\theta = 45^\circ$.  

---

## Links
- [[Motion in Two Dimensions]]  
- [[Motion In One Dimension]]  
- [[Vectors]]  

---

#physics #mechanics #projectilemotion #2Dmotion
