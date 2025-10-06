# Motion in Two Dimensions

### Idea
- Motion in **2D** occurs along both **horizontal (x)** and **vertical (y)** directions simultaneously.  
- We analyze it by **separating** into components:  
  - Horizontal motion (usually constant velocity)  
  - Vertical motion (usually constant acceleration due to gravity)  
- Position, velocity, and acceleration are treated as **vectors**.  

---

## Vectors in 2D Motion
- A position vector:  
  $$
  \vec{r}(t) = x(t)\hat{i} + y(t)\hat{j}
  $$
- Velocity vector:  
  $$
  \vec{v}(t) = \frac{d\vec{r}}{dt} = v_x(t)\hat{i} + v_y(t)\hat{j}
  $$
- Acceleration vector:  
  $$
  \vec{a}(t) = \frac{d\vec{v}}{dt} = a_x(t)\hat{i} + a_y(t)\hat{j}
  $$

---

## Horizontal Motion
- If no horizontal acceleration:  
  $$
  a_x = 0 \quad \Rightarrow \quad v_x = \text{constant}
  $$
- Position:  
  $$
  x(t) = x_0 + v_x t
  $$

---

## Vertical Motion
- Usually subject to gravity:  
  $$
  a_y = -g
  $$
- Velocity:  
  $$
  v_y = v_{0y} - g t
  $$
- Position:  
  $$
  y(t) = y_0 + v_{0y}t - \tfrac{1}{2}gt^2
  $$

---

## Projectile Motion
- Combining horizontal and vertical:  

1. **Position equations**  
   $$
   x(t) = x_0 + v_{0x}t
   $$
   $$
   y(t) = y_0 + v_{0y}t - \tfrac{1}{2}gt^2
   $$

2. **Trajectory equation** (eliminating $t$):  
   $$
   y = y_0 + \Big(\frac{v_{0y}}{v_{0x}}\Big)(x - x_0) - \frac{g}{2v_{0x}^2}(x - x_0)^2
   $$  
   → This is a **parabola**.  

---

## Relative Velocity in 2D
- For two moving objects A and B:  
  $$
  \vec{v}_{A/B} = \vec{v}_A - \vec{v}_B
  $$
- Each velocity is treated as a vector and broken into components.  

---

## Magnitude and Direction
- Given components:  
  $$
  v = \sqrt{v_x^2 + v_y^2}
  $$
  $$
  \theta = \tan^{-1}\!\Big(\frac{v_y}{v_x}\Big)
  $$

- Same applies to **displacement** and **acceleration** vectors.  

---

## Key Notes
- **Horizontal and vertical motions are independent**, connected only by time.  
- Gravity affects **vertical motion only**.  
- The path of a projectile is a **parabola**.  

---

## Links
- [[Motion In One Dimension]]  
- [[Vectors]]
- [[Vectors In Physics]]
- [[The Derivative]]  

---

#physics #mechanics #2Dmotion #kinematics
