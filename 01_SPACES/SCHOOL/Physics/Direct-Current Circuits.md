### Idea
A **Direct-Current (DC) Circuit** is one where the current always flows in **one direction** (like from a battery), as opposed to Alternating Current (AC) from a wall outlet, which flips back and forth.

Real circuits are rarely just one battery and one resistor. They're networks of resistors, batteries, and [[Capacitors]] wired together in complicated ways. This chapter gives you the toolkit to break any network down and find the current through, and voltage across, every single piece.

The two big ideas behind everything here are just conservation laws in disguise:
- **Charge is conserved.** Current can't appear or vanish at a junction.
- **Energy is conserved.** Go all the way around a loop and you end up back at the same potential.

*(For the basics of current, resistance, Ohm's Law, and EMF, see [[Current, Resistance, and Electromotive Force]].)*

### Formally: Resistors in Series and Parallel
Resistors combine the **opposite** way [[Capacitors]] do!

**Series (end-to-end):**
- Every resistor carries the **same current** ($I$).
- The voltages add up: $V_{total} = V_1 + V_2 + \dots$
$$ R_{eq} = R_1 + R_2 + R_3 + \dots $$
*(Series = one longer wire, so resistance goes **up**.)*

**Parallel (side-by-side):**
- Every resistor gets the **same voltage** ($V$).
- The currents add up: $I_{total} = I_1 + I_2 + \dots$
$$ \frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \dots $$
*(Parallel = more lanes for current to flow through, so resistance goes **down**. $R_{eq}$ is always smaller than the smallest resistor.)*

**Shortcut for two in parallel:**
$$ R_{eq} = \frac{R_1 R_2}{R_1 + R_2} $$

| | Resistors | Capacitors |
|---|---|---|
| **Series** | $R_{eq} = R_1 + R_2$ | $\frac{1}{C_{eq}} = \frac{1}{C_1} + \frac{1}{C_2}$ |
| **Parallel** | $\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2}$ | $C_{eq} = C_1 + C_2$ |

### Kirchhoff's Rules
When a circuit can't be simplified into simple series/parallel pieces (e.g., multiple batteries in different branches), use Kirchhoff's Rules.

**1. Junction Rule (Conservation of Charge):**
The total current flowing **into** any junction equals the total current flowing **out**:
$$ \sum I_{in} = \sum I_{out} $$

**2. Loop Rule (Conservation of Energy):**
The sum of all potential changes around **any** closed loop is zero:
$$ \sum \Delta V = 0 $$

**Sign Conventions for the Loop Rule:**
Pick a direction to walk around the loop, then:
- **Resistor**, walking *with* the current: $-IR$ (going downhill)
- **Resistor**, walking *against* the current: $+IR$
- **Battery**, walking from $-$ to $+$: $+\mathcal{E}$ (going uphill)
- **Battery**, walking from $+$ to $-$: $-\mathcal{E}$

**Step-by-Step Strategy:**
1. Label a current (with a guessed direction) in every branch.
2. Write junction equations for the junctions.
3. Write loop equations until you have as many equations as unknown currents.
4. Solve the system of equations.
5. If a current comes out **negative**, your guess was just backwards. The magnitude is still correct!

### Electrical Measuring Instruments
- **Ammeter**: measures **current**. It must be connected in **series** with the element and should have **very low** resistance (ideally $0$) so it doesn't block the current.
- **Voltmeter**: measures **voltage**. It must be connected in **parallel** across the element and should have **very high** resistance (ideally $\infty$) so it doesn't steal current.

### R-C Circuits (Charging and Discharging)
When a [[Capacitors|capacitor]] is in a circuit with a resistor, it doesn't charge or discharge instantly. Current is large at first, then dies off **exponentially** as the capacitor fills up (or empties).

**Time Constant ($\tau$):**
$$ \tau = RC $$
- **Units**: seconds.
- After one time constant, the capacitor has reached about **63%** of its final charge (or dropped to about **37%** when discharging).
- After about $5\tau$, it's considered fully charged or discharged.

**Charging** (battery $\mathcal{E}$ connected, starting empty):
$$ q(t) = C\mathcal{E}\left(1 - e^{-t/RC}\right) $$
$$ i(t) = \frac{\mathcal{E}}{R} e^{-t/RC} $$

**Discharging** (battery removed, starting with charge $Q_0$):
$$ q(t) = Q_0 \, e^{-t/RC} $$
$$ i(t) = -\frac{Q_0}{RC} e^{-t/RC} $$

**Quick Intuition:**
- At $t = 0$, an **uncharged** capacitor acts like a **plain wire** (current flows freely).
- At $t \to \infty$, a **fully charged** capacitor acts like a **broken wire** (no current flows through its branch).

**Connection to Calculus:**
These come from applying the loop rule, which gives a separable differential equation. For charging:
$$ \mathcal{E} - iR - \frac{q}{C} = 0 \quad \Rightarrow \quad \frac{dq}{dt} = \frac{\mathcal{E}}{R} - \frac{q}{RC} $$

### Power Distribution Systems
Household wiring is a real-world parallel circuit:
- Appliances are wired in **parallel**, so each gets the full outlet voltage and can be switched on/off independently.
- Every appliance you add draws more current, increasing the total current through the main line.
- **Fuses** and **circuit breakers** are placed in **series** with the line and cut the circuit if the current gets dangerously high, which prevents the wires from overheating.

### Related
- [[Current, Resistance, and Electromotive Force]]
- [[Capacitors]]
- [[Capacitance and Dielectrics]]
- [[Electric Potential]]
- [[Conservation of Energy]]

#physics #electromagnetism #circuits
