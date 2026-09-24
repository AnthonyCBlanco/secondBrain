### Idea
**Chemical equilibrium** is the state in a reversible chemical reaction where the rate of the forward reaction equals the rate of the reverse reaction ($\text{Rate}_{\text{forward}} = \text{Rate}_{\text{reverse}}$). 

Equilibrium is **dynamic**: reactions continue to occur in both directions simultaneously at equal speeds, causing the macroscopic concentrations of reactants and products to remain constant over time.

### Formally
For a general reversible reaction:
$$
aA + bB \rightleftharpoons cC + dD
$$

Applying the rate laws for elementary forward and reverse processes:
$$
\text{Rate}_f = k_f [A]^a [B]^b \quad \text{and} \quad \text{Rate}_r = k_r [C]^c [D]^d
$$

At equilibrium ($\text{Rate}_f = \text{Rate}_r$):
$$
k_f [A]^a [B]^b = k_r [C]^c [D]^d \implies \frac{k_f}{k_r} = \frac{[C]^c [D]^d}{[A]^a [B]^b}
$$

The ratio of the rate constants defines the **Equilibrium Constant ($K$)**.

### The Equilibrium Constant ($K_c$ and $K_p$)
The Law of Mass Action states that at a given temperature, the ratio of product concentrations to reactant concentrations (each raised to their stoichiometric powers) is constant.

**Concentration Basis ($K_c$):**
$$
K_c = \frac{[C]^c [D]^d}{[A]^a [B]^b}
$$
*(Concentrations are expressed in molarity, $\text{M}$).*

**Partial Pressure Basis ($K_p$, for gas-phase reactions):**
$$
K_p = \frac{(P_C)^c (P_D)^d}{(P_A)^a (P_B)^b}
$$
*(Partial pressures are typically expressed in atmospheres, $\text{atm}$).*

**Magnitude of $K$:**
- **$K \gg 1$ ($K > 10^3$):** Products are heavily favored; equilibrium lies far to the right.
- **$K \ll 1$ ($K < 10^{-3}$):** Reactants are heavily favored; equilibrium lies far to the left.
- **$K \approx 1$ ($10^{-3} \le K \le 10^3$):** Appreciable amounts of both reactants and products exist at equilibrium.

### Relationship Between $K_p$ and $K_c$
Using the Ideal Gas Law ($P = \frac{n}{V}RT = CRT$):
$$
K_p = K_c (RT)^{\Delta n}
$$

- $R = 0.08206 \text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$
- $T$ = absolute temperature in Kelvin ($\text{K}$)
- $\Delta n = (\text{moles of gaseous products}) - (\text{moles of gaseous reactants}) = (c + d) - (a + b)$
- If $\Delta n = 0$, then **$K_p = K_c$**.

### Reaction Quotient ($Q$) vs. Equilibrium Constant ($K$)
The **reaction quotient ($Q$)** has the exact same mathematical form as $K$, but is evaluated using **instantaneous non-equilibrium concentrations or pressures**:
$$
Q_c = \frac{[C]^c [D]^d}{[A]^a [B]^b}
$$

Comparing $Q$ to $K$ predicts the direction of net reaction:
- **$Q < K$:** Not enough products; the reaction proceeds **forward (to the right)** ($\rightarrow$).
- **$Q = K$:** System is at **equilibrium**; no net change occurs.
- **$Q > K$:** Too many products; the reaction proceeds in **reverse (to the left)** ($\leftarrow$).

### Rules for Manipulating $K$
1. **Reversing a Reaction:**
   $$K_{\text{rev}} = \frac{1}{K_{\text{fwd}}}$$
2. **Multiplying Coefficients by a Factor $n$:**
   $$K_{\text{new}} = (K_{\text{orig}})^n$$
3. **Adding Consecutive Reactions (Multi-step):**
   $$K_{\text{overall}} = K_1 \times K_2 \times K_3 \times \dots$$

### Heterogeneous Equilibria
In reactions involving multiple phases:
- **Pure solids ($\text{s}$)** and **pure liquids ($\text{l}$)** have constant concentrations/activities ($= 1$) and are **omitted** from $K_c$ and $K_p$ expressions.
- Only **gases ($\text{g}$)** and **aqueous species ($\text{aq}$)** are included.

*Example:*
$$
\ce{CaCO3(s) <=> CaO(s) + CO2(g)} \implies K_c = [\ce{CO2}] \quad \text{and} \quad K_p = P_{\ce{CO2}}
$$

### Le Châtelier's Principle
If an external stress is applied to a system at equilibrium, the system shifts its equilibrium position in a direction that counteracts the stress.

- **Concentration:**
  - Adding a reactant/product $\rightarrow$ shifts **away** from the added substance.
  - Removing a reactant/product $\rightarrow$ shifts **toward** the removed substance.
- **Volume & Pressure (Gases):**
  - Decreasing volume (increasing pressure) $\rightarrow$ shifts toward the side with **fewer moles of gas**.
  - Increasing volume (decreasing pressure) $\rightarrow$ shifts toward the side with **more moles of gas**.
  - Adding an inert gas at constant volume has **no effect** on equilibrium.
- **Temperature ($K$ changes value):**
  - **Endothermic ($\Delta H > 0$):** Heat acts like a reactant. Increasing $T$ shifts **right** ($\rightarrow$) and **$K$ increases**.
  - **Exothermic ($\Delta H < 0$):** Heat acts like a product. Increasing $T$ shifts **left** ($\leftarrow$) and **$K$ decreases**.
- **Catalyst:**
  - Lowers $E_a$ equally in both directions. Reaches equilibrium faster, but **does not alter the equilibrium composition or value of $K$**.

### Example
**For the Haber-Bosch synthesis of ammonia at $500\text{ K}$:**
$$
\ce{N2(g) + 3H2(g) <=> 2NH3(g)} \quad K_c = 0.060
$$

**A reaction vessel contains $[\ce{N2}] = 0.50 \text{ M}$, $[\ce{H2}] = 0.20 \text{ M}$, and $[\ce{NH3}] = 0.020 \text{ M}$.**
1. **Calculate the reaction quotient $Q_c$ and determine which way the reaction will shift.**
2. **Calculate $K_p$ at $500\text{ K}$.**

1. Calculate $Q_c$:
   $$
   Q_c = \frac{[\ce{NH3}]^2}{[\ce{N2}][\ce{H2}]^3} = \frac{(0.020)^2}{(0.50)(0.20)^3} = \frac{0.00040}{(0.50)(0.0080)} = \frac{0.00040}{0.0040} = 0.10
   $$

   Since **$Q_c (0.10) > K_c (0.060)$**, the system contains excess products. The reaction must **shift to the left ($\leftarrow$, in reverse)** to reach equilibrium.

2. Calculate $K_p$:
   - $\Delta n = 2 - (1 + 3) = -2$
   - $T = 500\text{ K}$, $R = 0.08206 \text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$

   $$
   K_p = K_c (RT)^{\Delta n} = 0.060 \times (0.08206 \times 500)^{-2} = 0.060 \times (41.03)^{-2} = \frac{0.060}{1683.46} \approx 3.6 \times 10^{-5}
   $$

### Related
- [[Chemistry MOC]]
- [[Rate of Chemical Reactions]]
- [[First-Order Kinetics]]
- [[Acid-Base Equilibria]]
- [[Solubility Equilibria]]

#chemistry/equilibrium #chemistry/general-chemistry-2 #fall2026
