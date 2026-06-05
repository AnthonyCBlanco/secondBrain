### Idea

**Momentum** is a fundamental concept in mechanics that describes the motion of an object in terms of its **mass** and **velocity**.  
It represents the **quantity of motion** and is a **vector quantity** — meaning it has both magnitude and direction.

Momentum plays a central role in understanding how forces act over time, and it forms the basis of the **Law of Conservation of Momentum**, a key principle governing collisions and interactions between objects.

---

### Definition of Momentum

The **linear momentum** $\vec{p}$ of an object is defined as:

$$
\vec{p} = m\vec{v}
$$

where:  
- $m$ = mass of the object (kg)  
- $\vec{v}$ = velocity vector (m/s)

The **SI unit** of momentum is **kg·m/s**.

Because velocity is a vector, momentum points in the **same direction** as the object’s motion.

---

### Impulse and Momentum Change

When a force acts on an object for a period of time, it changes the object’s momentum.  
This relationship is known as the **Impulse–Momentum Theorem**:

$$
\vec{F}_{\text{net}} \, \Delta t = \Delta \vec{p}
$$

or equivalently,

$$
\vec{I} = \Delta \vec{p}
$$

where:  
- $\vec{I}$ = impulse (N·s)  
- $\Delta t$ = time interval during which the force acts  
- $\Delta \vec{p}$ = change in momentum  

**Impulse** represents the **area under a force–time graph** and measures the total effect of a force over time.

---

### Relationship Between Force and Momentum

From Newton’s Second Law:

$$
\vec{F}_{\text{net}} = \frac{d\vec{p}}{dt}
$$

If the mass is constant, this simplifies to the familiar form:

$$
\vec{F}_{\text{net}} = m \frac{d\vec{v}}{dt} = m\vec{a}
$$

Thus, Newton’s laws can be expressed equivalently in terms of momentum — particularly useful for systems with **variable mass** (e.g., rockets).

---

### Conservation of Momentum

The **Law of Conservation of Momentum** states:

> The total momentum of a system remains constant if no external net force acts on it.

Mathematically:

$$
\sum \vec{p}_{\text{initial}} = \sum \vec{p}_{\text{final}}
$$

or

$$
m_1 \vec{v}_{1i} + m_2 \vec{v}_{2i} = m_1 \vec{v}_{1f} + m_2 \vec{v}_{2f}
$$

This principle is vital in analyzing **collisions**, **explosions**, and **interacting systems**.

---

### Types of Collisions

| Type of Collision | Momentum Conserved? | Kinetic Energy Conserved? | Description |
|--------------------|--------------------|----------------------------|--------------|
| Elastic | ✅ Yes | ✅ Yes | Both momentum and kinetic energy are conserved (e.g., billiard balls) |
| Inelastic | ✅ Yes | ❌ No | Objects deform or stick together; some energy is lost as heat or sound |
| Perfectly Inelastic | ✅ Yes | ❌ No | Objects stick together and move as one mass after collision |

For a **perfectly inelastic collision**:

$$
m_1 \vec{v}_{1i} + m_2 \vec{v}_{2i} = (m_1 + m_2)\vec{v}_f
$$

---

### Center of Mass and Momentum

The **total momentum** of a system of particles can be written as:

$$
\vec{P}_{\text{total}} = M \vec{v}_{\text{cm}}
$$

where:  
- $M = \sum m_i$ = total mass  
- $\vec{v}_{\text{cm}}$ = velocity of the center of mass  

If no external forces act, the **center of mass moves with constant velocity**, reinforcing the conservation of momentum.

---

### Impulse and Force Graphs

For time-varying forces, impulse equals the **area under the force–time curve**:

$$
I = \int_{t_i}^{t_f} F(t) \, dt
$$

This allows experimental determination of momentum change even when forces vary over time (e.g., collisions measured with force sensors).

---

### Example Problems

**1. Impulse Calculation**  
A 2.0 kg ball experiences a net force of 10 N for 0.5 s.  
Find the change in momentum.

$$
\Delta p = F \Delta t = 10(0.5) = 5 \text{ kg·m/s}
$$

---

**2. Inelastic Collision**  
A 1.0 kg cart moving at $3.0 \, \text{m/s}$ collides and sticks to a 2.0 kg cart at rest.  
Find their common velocity after collision.

$$
(1.0)(3.0) + (2.0)(0) = (1.0 + 2.0)v_f \\
v_f = 1.0 \, \text{m/s}
$$

---

**3. Elastic Collision (1D)**  
A 0.5 kg ball moving at $4.0 \, \text{m/s}$ collides elastically with a stationary 0.5 kg ball.  
After collision, the first ball stops.  
Find the velocity of the second ball.

Since momentum is conserved:
$$
(0.5)(4.0) = (0.5)v_2 \Rightarrow v_2 = 4.0 \, \text{m/s}
$$

---

### Concept Summary

| Concept                  | Formula                                      | Description                       |
| ------------------------ | -------------------------------------------- | --------------------------------- |
| Momentum                 | $\vec{p} = m\vec{v}$                         | Quantity of motion (vector)       |
| Impulse                  | $\vec{I} = \vec{F}\Delta t = \Delta \vec{p}$ | Change in momentum                |
| Force–Momentum Relation  | $\vec{F}_{\text{net}} = \frac{d\vec{p}}{dt}$ | Newton’s 2nd Law in momentum form |
| Conservation of Momentum | $\sum \vec{p}_i = \sum \vec{p}_f$            | Holds when no external forces act |
| Elastic Collision        | $p$ and $K$ conserved                        | Energy-efficient collision        |
| Inelastic Collision      | $p$ conserved, $K$ lost                      | Objects deform or stick together  |

---

### Related Notes

- [[Laws Of Motion]]
- [[Work and Energy]]
- [[Conservation of Energy]]

---

#physics #mechanics #momentum
