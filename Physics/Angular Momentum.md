# Angular Momentum

### Idea
**Angular momentum** describes the rotational equivalent of linear momentum.  
It measures how much rotational motion an object has, depending on its **mass distribution**, **velocity**, and **distance from the axis of rotation**.

Angular momentum is deeply connected to **torque**, **moment of inertia**, and **rotational kinematics**, and it obeys a powerful conservation law when the net external torque is zero.

---

### Rotational Kinematics (Reference)

These describe how angular quantities change with time under constant angular acceleration:

$$
\alpha = \frac{d\omega}{dt}
$$

$$
\omega = \omega_i + \alpha t
$$

$$
\Delta \theta = \omega_i t + \frac{1}{2}\alpha t^2
$$

where:  
- $\omega$ = angular velocity (rad/s)  
- $\alpha$ = angular acceleration (rad/s²)  
- $\theta$ = angular displacement (rad)

---

### Moment of Inertia

Moment of inertia describes how mass is distributed relative to the axis of rotation.

**General definition:**
$$
I = \int r^2\,dm
$$

**Point mass:**
$$
I = mr^2
$$

**Parallel axis theorem:**
$$
I = I_{cm} + MD^2
$$

where:  
- $I_{cm}$ = moment of inertia about center of mass  
- $D$ = distance between axes  
- $M$ = total mass  

---

### Rotational Kinetic Energy

The rotational analog of linear kinetic energy:

$$
K_r = \frac{1}{2}I\omega^2
$$

---

### Torque

Torque is the rotational analog of force.

**Vector definition:**
$$
\vec{T} = \vec{r} \times \vec{F}
$$

**Relation to angular acceleration:**
$$
\vec{T} = I\vec{\alpha}
$$

**Net torque:**
$$
\vec{T}_{net} = \sum_i \vec{T}_i
$$

If $\vec{T}_{net} = 0$, angular momentum is conserved.

---

### Linear Momentum (for comparison)
$$
\vec{p} = m\vec{v}
$$

---

### Angular Momentum

#### Particle definition:
$$
\vec{L} = \vec{r} \times \vec{p}
$$

#### Rigid body rotating about a fixed axis:
$$
\vec{L} = I\vec{\omega}
$$

---

### Conservation of Angular Momentum

If no net external torque acts on a system:

$$
\vec{T}_{net} = 0 \quad \Rightarrow \quad \frac{d\vec{L}}{dt} = 0
$$

Thus,

$$
\vec{L}_{initial} = \vec{L}_{final}
$$

This explains phenomena such as ice skaters pulling their arms in to spin faster.

---

### Mass per Unit Length (useful for rods)
For non-uniform or uniform rods:

$$
\lambda = \frac{M}{L} = \frac{dm}{dr}
$$

---

### Related Notes
- [[Rotational Motion]]
- [[Torque]]
- [[Linear Momentum]]
- [[Work and Energy]]

---

#physics #mechanics #rotation #angularmomentum
