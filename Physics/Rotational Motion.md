## Rotational Motion  

### Idea  
**Rotational motion** occurs when an object spins or rotates about a fixed axis.  
Instead of moving linearly, every point on the object follows a **circular path** around the axis of rotation.  

Rotational motion mirrors **linear motion**, but with angular quantities such as **angular displacement**, **angular velocity**, and **angular acceleration**.  

Understanding this relationship allows us to translate between **linear kinematics** and **rotational kinematics**.

---

### Angular Quantities  

| Quantity | Symbol | Definition | Units |
|-----------|---------|-------------|--------|
| **Angular Displacement** | $\theta$ | Angle swept by a radius | radians (rad) |
| **Angular Velocity** | $\omega = \frac{d\theta}{dt}$ | Rate of change of angular displacement | rad/s |
| **Angular Acceleration** | $\alpha = \frac{d\omega}{dt}$ | Rate of change of angular velocity | rad/s² |

---

### Relationship Between Linear and Angular Variables  

| Linear Motion | Rotational Motion | Relation |
|----------------|------------------|-----------|
| Displacement $s$ | Angular displacement $\theta$ | $s = r\theta$ |
| Velocity $v$ | Angular velocity $\omega$ | $v = r\omega$ |
| Acceleration $a$ | Angular acceleration $\alpha$ | $a = r\alpha$ |

Here, $r$ is the **radius** from the axis of rotation to the point of interest.  

---

### Rotational Kinematic Equations  

Analogous to linear kinematics, when angular acceleration is constant:

1. $\omega = \omega_0 + \alpha t$  
2. $\theta = \omega_0 t + \frac{1}{2}\alpha t^2$  
3. $\omega^2 = \omega_0^2 + 2\alpha \theta$  

These equations describe how angular quantities evolve over time.

---

### Tangential and Centripetal Acceleration  

Each point on a rotating object has **two types of acceleration**:

- **Tangential acceleration:** changes the speed along the circular path  
  $$
  a_t = r\alpha
  $$
- **Centripetal acceleration:** changes the direction of motion (points toward the axis)  
  $$
  a_c = \frac{v^2}{r} = r\omega^2
  $$

Total acceleration is the vector sum:
$$
a = \sqrt{a_t^2 + a_c^2}
$$

---

### Rotational Inertia (Moment of Inertia)  

The **moment of inertia** ($I$) measures how mass is distributed about the axis of rotation and determines an object's resistance to angular acceleration:  

$$
I = \sum m_i r_i^2
$$

For continuous bodies:
$$
I = \int r^2\,dm
$$

| Object | Moment of Inertia ($I$) about Central Axis |
|---------|---------------------------------------------|
| Solid Cylinder | $\frac{1}{2}MR^2$ |
| Hollow Cylinder | $MR^2$ |
| Solid Sphere | $\frac{2}{5}MR^2$ |
| Thin Rod (about center) | $\frac{1}{12}ML^2$ |
| Thin Rod (about end) | $\frac{1}{3}ML^2$ |

---

### Rotational Dynamics  

Newton’s Second Law for rotation relates **net torque** to **angular acceleration**:  

$$
\sum \tau = I\alpha
$$

where  
- $\tau$ is **torque**, defined as $\tau = rF\sin\theta$,  
- $I$ is the moment of inertia, and  
- $\alpha$ is the angular acceleration.  

This is the rotational analog of $F = ma$ in linear motion.

---

### Rotational Kinetic Energy  

The energy associated with rotation is given by:  

$$
K_{\text{rot}} = \frac{1}{2}I\omega^2
$$

If an object both translates and rotates (e.g., rolling without slipping):  

$$
K_{\text{total}} = \frac{1}{2}mv^2 + \frac{1}{2}I\omega^2
$$

---

### Rolling Without Slipping  

When an object rolls smoothly on a surface (without sliding):  
$$
v = r\omega
$$

This connects rotational motion to linear motion.  

---

### Example  

**A solid cylinder (mass 2 kg, radius 0.5 m) rotates at 6 rad/s. Find its rotational kinetic energy.**  

Given:  
$I = \frac{1}{2}MR^2 = \frac{1}{2}(2)(0.5)^2 = 0.25$  
$$
K_{\text{rot}} = \frac{1}{2}I\omega^2 = \frac{1}{2}(0.25)(6)^2 = 4.5 \text{ J}
$$

---

### Concept Summary  

| Concept | Formula | Description |
|----------|----------|-------------|
| Angular velocity | $\omega = \frac{d\theta}{dt}$ | Rate of change of angle |
| Angular acceleration | $\alpha = \frac{d\omega}{dt}$ | Rate of change of angular velocity |
| Linear-angular relationship | $v = r\omega, \ a = r\alpha$ | Connects linear and rotational motion |
| Rotational kinetic energy | $K_{\text{rot}} = \frac{1}{2}I\omega^2$ | Energy due to rotation |
| Newton’s 2nd Law (rotational) | $\sum\tau = I\alpha$ | Torque causes angular acceleration |
| Moment of inertia | $I = \sum m_i r_i^2$ | Resistance to rotational acceleration |

---

### Related Notes  
- [[Torque]]  
- [[Work and Energy]]  
- [[Angular Momentum]]  
- [[Laws Of Motion]]  
- [[Kinetic Energy]]  

---

#physics #mechanics #rotation #energy #dynamics
