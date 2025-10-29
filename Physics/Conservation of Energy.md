# Conservation of Energy

### Idea

The **Work–Energy Theorem** connects the concepts of **force**, **work**, and **kinetic energy**.  
It states that the **net work** done on an object is equal to its **change in kinetic energy**:

$$
W_{\text{net}} = \Delta K = K_f - K_i
$$

This relationship serves as the foundation for the **Principle of Conservation of Energy**, which says that **energy cannot be created or destroyed — only transformed** between forms (kinetic, potential, thermal, etc.).

---

### Work and Energy

Work is the transfer of energy by a **force** acting over a **displacement**.

$$
W = \vec{F} \cdot \vec{\Delta r} = F \Delta r \cos \theta
$$

If the force varies over distance, work is found using integration:

$$
W = \int \vec{F} \cdot d\vec{r}
$$

---

### Kinetic Energy

The **kinetic energy** of an object of mass $m$ moving with velocity $v$ is:

$$
K = \frac{1}{2}mv^2
$$

From the Work–Energy Theorem:

$$
W_{\text{net}} = \Delta K
$$

> Work done *on* an object increases its kinetic energy.  
> Work done *against* an object (by friction, for instance) decreases its kinetic energy.

---

### Potential Energy

Potential energy ($U$) is **stored energy** associated with the position of an object in a force field.

#### Gravitational Potential Energy
$$
U_g = mgh
$$
where  
- $m$ = mass  
- $g$ = acceleration due to gravity  
- $h$ = height above a reference level  

#### Elastic (Spring) Potential Energy
For a spring that obeys Hooke’s Law ($F = -kx$):

$$
U_s = \frac{1}{2}kx^2
$$

---

### Conservation of Mechanical Energy

If only **conservative forces** (like gravity or spring force) act on a system, the **total mechanical energy** remains constant.

$$
E = K + U = \text{constant}
$$

or

$$
K_i + U_i = K_f + U_f
$$

> When no non-conservative forces (like friction or air resistance) act on a system, **mechanical energy is conserved**.

---

### Non-Conservative Forces

When forces like **friction**, **air resistance**, or **applied forces** do work, they cause mechanical energy to **change** (usually converting to thermal energy):

$$
W_{\text{nc}} = \Delta E_{\text{mechanical}} = (K_f + U_f) - (K_i + U_i)
$$

---

### Power

**Power** is the rate at which work is done or energy is transferred:

$$
P = \frac{dW}{dt}
$$

For constant force and velocity:

$$
P = \vec{F} \cdot \vec{v}
$$

---

### Energy Diagrams and Conservation

An energy diagram shows the relationship between potential energy $U(x)$ and total mechanical energy $E$.  
Points where $E = U$ represent **turning points** — where kinetic energy momentarily becomes zero.

---

### Summary

| Type of Energy | Symbol | Expression | Description |
|-----------------|---------|-------------|--------------|
| Kinetic | $K$ | $\frac{1}{2}mv^2$ | Motion energy |
| Gravitational Potential | $U_g$ | $mgh$ | Height-based energy |
| Elastic Potential | $U_s$ | $\frac{1}{2}kx^2$ | Stored spring energy |
| Work | $W$ | $F\Delta r \cos\theta$ | Energy transfer via force |
| Power | $P$ | $\frac{dW}{dt} = Fv$ | Rate of energy transfer |

---

### Formally

The **Law of Conservation of Energy**:

$$
E_{\text{total, initial}} = E_{\text{total, final}}
$$

$$
K_i + U_i + W_{\text{nc}} = K_f + U_f
$$

> Energy can change **forms**, but the **total energy** of an isolated system remains **constant**.

---

### Related Notes

- [[Laws Of Motion]]
- [[Motion In One Dimension]]
- [[Friction]]
- [[Work and Energy]]

---

#physics #mechanics #energy #work #conservationofenergy
