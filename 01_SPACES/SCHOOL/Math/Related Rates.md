# Related Rates

### Idea
Related rates problems involve finding how two or more **quantities that change with time** are related through derivatives.  

They often require:  
- Differentiating equations **implicitly with respect to time ($t$)**.  
- Applying the **Chain Rule**.  
- Plugging in known values to solve for the desired rate.  

See also → [[The Derivative]], [[Implicit Differentiation]], [[The Chain Rule]]  

---

### General Steps for Solving Related Rates Problems

1. **Read the problem carefully** and identify what is **given** and what you need to **find**.  
2. **Assign variables** to represent the changing quantities.  
3. **Write an equation** relating the variables.  
4. **Differentiate implicitly** with respect to time ($t$).  
5. **Substitute** known values (numbers and rates).  
6. **Solve for the desired rate**.  

---

### Example 1: Ladder Sliding Problem

**Problem:**  
A 10 ft ladder is leaning against a vertical wall. The bottom slides away from the wall at 2 ft/s. How fast is the top sliding down when the bottom is 6 ft from the wall?

**Step 1: Variables**  
- $x =$ distance of bottom from wall (ft)  
- $y =$ height of top on wall (ft)  
- $\frac{dx}{dt} = 2 \, \text{ft/s}$  
- Ladder length: $10 \, \text{ft}$  

**Step 2: Equation**  
$$
x^2 + y^2 = 10^2
$$

**Step 3: Differentiate**  
$$
2x \frac{dx}{dt} + 2y \frac{dy}{dt} = 0
$$

**Step 4: Simplify**  
$$
x \frac{dx}{dt} + y \frac{dy}{dt} = 0
$$

**Step 5: Plug in values**  
When $x = 6$, solve for $y$:  
$$
6^2 + y^2 = 100 \quad \Rightarrow \quad y = 8
$$

Now substitute:  
$$
6(2) + 8 \frac{dy}{dt} = 0
$$

**Step 6: Solve**  
$$
12 + 8 \frac{dy}{dt} = 0 \quad \Rightarrow \quad \frac{dy}{dt} = -\frac{12}{8} = -1.5 \, \text{ft/s}
$$

**Answer:** The top slides down at **1.5 ft/s**.  

---

### Example 2: Inflating Balloon

**Problem:**  
A spherical balloon is inflated so that its radius increases at $3 \, \text{cm/s}$. How fast is the volume increasing when the radius is $5 \, \text{cm}$?

**Step 1: Variables**  
- $r =$ radius (cm)  
- $V =$ volume (cm³)  
- $\frac{dr}{dt} = 3 \, \text{cm/s}$  

**Step 2: Equation**  
$$
V = \frac{4}{3}\pi r^3
$$

**Step 3: Differentiate**  
$$
\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt}
$$

**Step 4: Plug in values**  
$$
\frac{dV}{dt} = 4\pi (5^2)(3)
$$

**Step 5: Solve**  
$$
\frac{dV}{dt} = 300\pi \, \text{cm}^3/\text{s}
$$

**Answer:** The volume is increasing at **$300\pi \, \text{cm}^3/\text{s}$**.  

---

### Example 3: Cone Filling with Water

**Problem:**  
Water is being poured into a cone at $2 \, \text{cm}^3/s$. The cone has height $12 \, \text{cm}$ and base radius $6 \, \text{cm}$. How fast is the water level rising when the water is 4 cm deep?

**Step 1: Variables**  
- $V =$ volume of water (cm³)  
- $h =$ height of water (cm)  
- $\frac{dV}{dt} = 2 \, \text{cm}^3/\text{s}$  

**Step 2: Equation**  
Volume of cone:  
$$
V = \frac{1}{3}\pi r^2 h
$$

Relationship between $r$ and $h$ (similar triangles):  
$$
\frac{r}{h} = \frac{6}{12} = \frac{1}{2} \quad \Rightarrow \quad r = \frac{h}{2}
$$

So:  
$$
V = \frac{1}{3}\pi \left(\frac{h}{2}\right)^2 h = \frac{1}{12}\pi h^3
$$

**Step 3: Differentiate**  
$$
\frac{dV}{dt} = \frac{1}{4}\pi h^2 \frac{dh}{dt}
$$

**Step 4: Plug in values**  
When $h=4$:  
$$
2 = \frac{1}{4}\pi (4^2)\frac{dh}{dt}
$$

**Step 5: Solve**  
$$
2 = 4\pi \frac{dh}{dt} \quad \Rightarrow \quad \frac{dh}{dt} = \frac{1}{2\pi} \, \text{cm/s}
$$

**Answer:** The water level rises at **$\frac{1}{2\pi} \, \text{cm/s}$**.  

---

### Key Notes
- Always **relate variables before differentiating** (using geometry/algebra if needed).  
- Use the **chain rule** when differentiating with respect to time.  
- Watch for **signs**: positive means increasing, negative means decreasing.  

---

#math #calculus #derivatives 
