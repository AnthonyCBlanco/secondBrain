# Static Equilibrium

Static equilibrium occurs when an object is **at rest** and remains at rest.  
For an object to be in equilibrium, the **net force** and **net torque** on the object must both be zero.

This concept is essential for analyzing structures, supports, objects on inclined planes, and any situation involving forces that balance exactly.

---

### Idea

An object is in **static equilibrium** when:

- It has **no linear acceleration** → forces balance.
- It has **no angular acceleration** → torques balance.

The conditions ensure the object stays perfectly still.

---

### Formally

### **1. Conditions for Static Equilibrium**

#### **Translational equilibrium (no linear acceleration)**

$$
\sum \vec{F} = 0
$$

In component form:

$$
\sum F_x = 0
\qquad
\sum F_y = 0
\qquad
\sum F_z = 0
$$

---

#### **Rotational equilibrium (no angular acceleration)**

$$
\sum \vec{\tau} = 0
$$

Where torque is:

$$
\vec{\tau} = \vec{r} \times \vec{F}
$$

Magnitude:

$$
\tau = rF\sin(\theta)
$$

---

### **2. Choosing a Pivot Point**

In equilibrium problems, you may choose **any point** as the pivot.  
A good pivot eliminates unknown forces.

Example strategy:
- Choose a pivot where multiple unknown forces act → they produce **zero torque** because $r = 0$.

---

### **3. Common Forces in Equilibrium Problems**

- Weight: $mg$  
- Normal force: $N$  
- Tension: $T$  
- Applied forces: $F$  
- Friction:  
  - Static friction (up to its maximum):  
    $$
    f_s \le \mu_s N
    $$
  - Kinetic friction (if slipping occurs):  
    $$
    f_k = \mu_k N
    $$

---

### Examples

#### **Example 1 — Uniform beam supported at two points**

A 4 m long uniform beam of weight $W$ rests on two supports.  
Find the forces at each support.

Take torque about the left support:

$$
\sum \tau = 0
$$

$$
W \left(\frac{4}{2}\right) - F_R(4) = 0
$$

$$
F_R = \frac{W}{2}
$$

Then:

$$
F_L + F_R = W
\Rightarrow F_L = \frac{W}{2}
$$

---

#### **Example 2 — Ladder against a wall**

A ladder of length $L$ leans against a frictionless wall.  
Choosing the bottom of the ladder as the pivot eliminates unknown normal forces at that point.

Torque balance:

$$
\tau_{\text{weight}} = \tau_{\text{wall normal}}
$$

Resulting in:

$$
mg\left(\frac{L}{2}\right)\sin\theta = N_{\text{wall}}L\cos\theta
$$

---

### Concept Summary

| Concept | Formula | Meaning |
|--------|---------|---------|
| Translational Equilibrium | $\sum \vec{F} = 0$ | All linear forces cancel |
| Rotational Equilibrium | $\sum \vec{\tau} = 0$ | All torques cancel |
| Torque | $\tau = rF\sin\theta$ | Rotational effect of a force |
| Static Friction | $f_s \le \mu_s N$ | Prevents motion until max value |

---

### Related Notes

- [[Torque]]  
- [[Rotational Motion]]  
- [[Laws Of Motion]]  
- [[Friction]]  

---

#physics #mechanics #equilibrium
