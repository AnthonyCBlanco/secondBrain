### Idea
A **first-order reaction** is a chemical reaction whose rate depends linearly on the concentration of a single reactant. If you double the concentration of that reactant, the reaction rate doubles.

This type of kinetics applies to many fundamental processes, including unimolecular decompositions, isomerization reactions, and all [[Nuclear Reactions|radioactive decay]].

### Formally
For a general unimolecular reaction:
$$
A \rightarrow \text{products}
$$

The **differential rate law** expresses the rate in terms of the rate constant $k$ and reactant concentration $[A]$:
$$
\text{Rate} = -\frac{d[A]}{dt} = k[A]
$$

- $k$ is the **rate constant** with SI units of $\text{s}^{-1}$ (or more generally $\text{time}^{-1}$).
- $[A]$ is the molar concentration of reactant $A$ at time $t$.

### Integrated Rate Law
Separating variables and integrating from $t = 0$ ($[A] = [A]_0$) to time $t$ ($[A] = [A]_t$):
$$
\int_{[A]_0}^{[A]_t} \frac{1}{[A]} \, d[A] = -k \int_0^t dt
$$

This gives the **integrated rate law** in several useful forms:

$$
\ln[A]_t = -kt + \ln[A]_0
$$

$$
\ln\left(\frac{[A]_t}{[A]_0}\right) = -kt
$$

$$
[A]_t = [A]_0 e^{-kt}
$$

### Graphical Determination ($y = mx + b$)
The equation $\ln[A]_t = -kt + \ln[A]_0$ matches the equation of a straight line $y = mx + b$:
- **y-axis:** $\ln[A]$
- **x-axis:** $t$ (time)
- **Slope ($m$):** $-k$
- **y-intercept ($b$):** $\ln[A]_0$

*Diagnostic Test:* If plotting $\ln[A]$ versus $t$ gives a straight line with a negative slope, the reaction is experimentally confirmed to be **first-order**.

### Half-Life ($t_{1/2}$)
The **half-life** is the time required for the reactant concentration to drop to half of its initial value ($[A]_t = \frac{1}{2}[A]_0$).

Substituting $[A]_t = \frac{1}{2}[A]_0$ into the integrated rate law:
$$
\ln\left(\frac{\frac{1}{2}[A]_0}{[A]_0}\right) = -k t_{1/2}
$$

$$
\ln\left(\frac{1}{2}\right) = -k t_{1/2} \implies -\ln(2) = -k t_{1/2}
$$

$$
t_{1/2} = \frac{\ln(2)}{k} \approx \frac{0.693}{k}
$$

**Key Property:** For first-order reactions, the half-life is **constant and completely independent of initial concentration $[A]_0$**. Every half-life interval that passes reduces the remaining reactant by exactly $50\%$.

### Example
**The decomposition of dinitrogen pentoxide ($\ce{2N2O5(g) -> 4NO2(g) + O2(g)}$) follows first-order kinetics with a rate constant $k = 5.0 \times 10^{-4} \text{ s}^{-1}$ at $45^\circ\text{C}$.**
1. **Find the half-life of the reaction.**
2. **If the initial concentration is $[\ce{N2O5}]_0 = 0.200 \text{ M}$, calculate the concentration after $10.0\text{ minutes}$.**

1. **Calculate $t_{1/2}$:**
   $$
   t_{1/2} = \frac{0.693}{k} = \frac{0.693}{5.0 \times 10^{-4} \text{ s}^{-1}} = 1386 \text{ s} \approx 23.1 \text{ min}
   $$

2. **Calculate $[\ce{N2O5}]_t$ at $t = 10.0 \text{ min} = 600 \text{ s}$:**
   $$
   \ln[\ce{N2O5}]_t = -kt + \ln[\ce{N2O5}]_0
   $$
   $$
   \ln[\ce{N2O5}]_t = -(5.0 \times 10^{-4} \text{ s}^{-1})(600 \text{ s}) + \ln(0.200)
   $$
   $$
   \ln[\ce{N2O5}]_t = -0.300 + (-1.609) = -1.909
   $$
   $$
   [\ce{N2O5}]_t = e^{-1.909} = 0.148 \text{ M}
   $$

After 10 minutes, the concentration of $\ce{N2O5}$ decreases from $0.200\text{ M}$ to **$0.148\text{ M}$**.

### Related
- [[Chemistry MOC]]
- [[Nuclear Reactions]]
- [[The Kinetics of Radioactive Decay]]
- [[Zero-Order Kinetics]]
- [[Second-Order Kinetics]]
- [[Reaction Rates and Rate Laws]]
- [[Integration and Differentiation of Logarithmic Functions]]

#chemistry/kinetics #chemistry/general-chemistry-2 #fall2026
