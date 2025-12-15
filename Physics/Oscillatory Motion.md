# Oscillatory Motion

### Idea
Oscillatory motion refers to any motion in which an object moves back and forth around an equilibrium position in a repetitive manner. Many physical systems—springs, pendulums, and circuits—exhibit oscillations when displaced from equilibrium and acted on by a restoring force.

---

### Formally

#### **Simple Harmonic Motion (SHM)**
Simple Harmonic Motion occurs when the restoring force is directly proportional to displacement and directed toward equilibrium.

$$F = -kx$$

This leads to the differential equation:

$$\frac{d^2x}{dt^2} = -\frac{k}{m}x$$

Solution for position:

$$x(t) = A\cos(\omega t + \phi)$$

Where:
- $A$ = amplitude  
- $\omega = \sqrt{\frac{k}{m}}$ = angular frequency  
- $\phi$ = phase constant  

Velocity:

$$v(t) = -A\omega \sin(\omega t + \phi)$$

Acceleration:

$$a(t) = -A\omega^2 \cos(\omega t + \phi) = -\omega^2 x$$

---

### Energy in SHM

Total mechanical energy is conserved:

$$E = K + U$$

Kinetic energy:

$$K = \frac{1}{2}mv^2 = \frac{1}{2}m\omega^2 (A^2 - x^2)$$

Potential energy of the spring:

$$U = \frac{1}{2}kx^2 = \frac{1}{2}m\omega^2 x^2$$

Total energy:

$$E = \frac{1}{2}kA^2$$

---

### Period and Frequency

Period:

$$T = 2\pi \sqrt{\frac{m}{k}}$$

Frequency:

$$f = \frac{1}{T} = \frac{1}{2\pi} \sqrt{\frac{k}{m}}$$

Angular frequency:

$$\omega = 2\pi f$$

---

### Pendulum Motion (Small-Angle Approximation)

For a simple pendulum of length $L$:

Restoring torque leads to:

$$T = 2\pi \sqrt{\frac{L}{g}}$$

Angular frequency:

$$\omega = \sqrt{\frac{g}{L}}$$

Valid only for small angles: $\theta \lesssim 15^\circ$.

---

### Damped Oscillations

Damping introduces a resistive force:

$$F_d = -b v$$

Underdamped motion solution:

$$x(t) = A e^{-\frac{b}{2m}t} \cos(\omega_d t + \phi)$$

Damped angular frequency:

$$\omega_d = \sqrt{\omega^2 - \left(\frac{b}{2m}\right)^2}$$

---

### Driven Oscillations & Resonance

Driving force:

$$F(t) = F_0 \cos(\omega_d t)$$


Resonance occurs when the driving frequency matches the natural frequency:

$$\omega_d = \omega$$

Amplitude becomes maximized.

---

### Examples

#### Example 1: Mass–Spring SHM
A 0.5 kg mass attached to a spring with stiffness $k = 8\ \text{N/m}$:

$$\omega = \sqrt{\frac{8}{0.5}} = 4\ \text{rad/s}$$
$$T = \frac{2\pi}{4} = \frac{\pi}{2}\ \text{s}$$

#### Example 2: Pendulum Period
For a pendulum with $L = 1.0\ \text{m}$:

$$T = 2\pi \sqrt{\frac{1}{9.8}} \approx 2.01\ \text{s}$$

---

### Concept Summary
- Oscillatory motion repeats around equilibrium.  
- SHM occurs when force is proportional to displacement ($F = -kx$).  
- Energy oscillates between kinetic and potential, but total energy remains constant.  
- Pendulum motion approximates SHM for small angles.  
- Damping reduces amplitude; driving forces can induce resonance.  

---

### Related Notes
- [[Rotational Motion]]
- [[Torque]]
- [[Work and Energy]]
- [[Universal Gravitation]]

---

**Tags:** #physics #mechanics #oscillations 
