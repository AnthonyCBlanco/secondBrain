### Idea
Chemical kinetics is the study of how fast chemical reactions occur (reaction rates) and the specific step-by-step molecular pathways (reaction mechanisms) through which reactants convert into products.

The **rate of a chemical reaction** measures the change in concentration of a reactant or product per unit of time (typically expressed in molarity per second, $\text{M/s}$ or $\text{mol}\cdot\text{L}^{-1}\cdot\text{s}^{-1}$). By convention, reaction rates are always defined as positive values.

### Formally
For a general chemical reaction with stoichiometric coefficients:
$$
aA + bB \rightarrow cC + dD
$$

The overall **rate of reaction** relates the rate of disappearance of reactants to the rate of appearance of products by dividing each concentration change by its stoichiometric coefficient:

$$
\text{Rate} = -\frac{1}{a}\frac{\Delta [A]}{\Delta t} = -\frac{1}{b}\frac{\Delta [B]}{\Delta t} = \frac{1}{c}\frac{\Delta [C]}{\Delta t} = \frac{1}{d}\frac{\Delta [D]}{\Delta t}
$$

In calculus terms (for instantaneous rate):
$$
\text{Rate} = -\frac{1}{a}\frac{d[A]}{dt} = -\frac{1}{b}\frac{d[B]}{dt} = \frac{1}{c}\frac{d[C]}{dt} = \frac{1}{d}\frac{d[D]}{dt}
$$

- **Negative sign on reactants:** Reactant concentrations decrease over time ($\Delta [\text{Reactant}] < 0$), so the negative sign ensures the overall rate is positive.
- **Positive sign on products:** Product concentrations increase over time ($\Delta [\text{Product}] > 0$).
- **Stoichiometric normalization:** Dividing by coefficients ($a, b, c, d$) ensures the reaction has a single, unambiguous rate regardless of which chemical species is monitored.

### Types of Reaction Rates
1. **Average Rate:**
   The average speed of the reaction measured across a discrete time interval ($\Delta t = t_2 - t_1$):
   $$
   \text{Average Rate} = -\frac{\Delta [A]}{\Delta t} = -\frac{[A]_2 - [A]_1}{t_2 - t_1}
   $$

2. **Instantaneous Rate:**
   The rate of reaction at a specific exact moment in time, given by the derivative of concentration with respect to time (the slope of the tangent line to the concentration-versus-time graph):
   $$
   \text{Instantaneous Rate} = \lim_{\Delta t \to 0} \left(-\frac{\Delta [A]}{\Delta t}\right) = -\frac{d[A]}{dt}
   $$

3. **Initial Rate:**
   The instantaneous rate measured at the very start of the reaction ($t = 0$). This is the standard rate used in the **Method of Initial Rates** to experimentally determine reaction orders and rate laws before reverse reactions or reactant depletion complicate measurements.

### Factors Influencing Reaction Rates
1. **Physical State and Surface Area:** Heterogeneous reactions occur at interfaces; increasing surface area (e.g., grinding a solid into a powder) increases collision frequency.
2. **Reactant Concentration:** Higher concentrations increase the number of particles per unit volume, increasing collision frequency.
3. **Temperature:** Increasing temperature raises the average kinetic energy of molecules, substantially increasing the fraction of collisions with energy $E \ge E_a$ (activation energy).
4. **Catalysts:** Substances that speed up reactions by offering an alternative pathway with lower activation energy without being consumed in the net process.

### Example
**Consider the combustion of methane:**
$$
\ce{CH4(g) + 2O2(g) -> CO2(g) + 2H2O(g)}
$$

**Suppose that at a given moment, molecular oxygen ($\ce{O2}$) is being consumed at a rate of $0.040 \text{ M/s}$ (meaning $-\frac{\Delta [\ce{O2}]}{\Delta t} = 0.040 \text{ M/s}$).**

1. Write the relative rate expression for all participants:
   $$
   \text{Rate} = -\frac{\Delta [\ce{CH4}]}{\Delta t} = -\frac{1}{2}\frac{\Delta [\ce{O2}]}{\Delta t} = \frac{\Delta [\ce{CO2}]}{\Delta t} = \frac{1}{2}\frac{\Delta [\ce{H2O}]}{\Delta t}
   $$

2. Determine the overall reaction rate:
   $$
   \text{Rate} = \frac{1}{2}\left(-\frac{\Delta [\ce{O2}]}{\Delta t}\right) = \frac{1}{2}(0.040 \text{ M/s}) = 0.020 \text{ M/s}
   $$

3. Calculate the rate of consumption of $\ce{CH4}$ and the rate of formation of $\ce{H2O}$:
   - Rate of $\ce{CH4}$ consumption:
     $$
     -\frac{\Delta [\ce{CH4}]}{\Delta t} = \text{Rate} = 0.020 \text{ M/s}
     $$
   - Rate of $\ce{H2O}$ formation:
     $$
     \frac{\Delta [\ce{H2O}]}{\Delta t} = 2 \times \text{Rate} = 2(0.020 \text{ M/s}) = 0.040 \text{ M/s}
     $$

### Related
- [[Chemistry MOC]]
- [[First-Order Kinetics]]
- [[Kinetics of Radioactive Decay]]
- [[The Derivative]]
- [[Differentials]]

#chemistry/kinetics #chemistry/general-chemistry-2 #fall2026
