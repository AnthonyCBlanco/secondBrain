---
date: 2026-11-05
chapter: 29
aliases:
  - Faraday-Lenz Law
  - Displacement Current
  - Ampère-Maxwell Law
  - Maxwell's Equations
tags:
  - physics/electromagnetism
  - physics/maxwell-equations
---

# Chapter 29: Faraday-Lenz Law, Eddy Currents, and Maxwell's Equations

> [!abstract] Lecture Overview
> Completes Chapter 29 by formalizing **electromotive force (EMF)** and **Faraday-Lenz law**, demonstrating **eddy currents**, resolving the charging-capacitor paradox in Ampère's law via **Maxwell's displacement current**, and assembling the full set of **Maxwell's equations**.

---

## 1. Electromotive Force (EMF) & Faraday-Lenz Law

### Physical Meaning of EMF ($\mathcal{E}$)
- **Definition:** Work done per unit positive charge ($q = 1\text{ C}$) around a **closed path**. Despite the historical name, EMF is **not a force**—it is energy per unit charge:
  $$W = q\mathcal{E} \implies [\mathcal{E}] = \text{V} = \frac{\text{J}}{\text{C}}$$
  - *Battery analogy:* Moving $1\text{ C}$ through a $1.5\text{ V}$ battery transfers $1.5\text{ J}$ of energy; moving $3\text{ C}$ requires $3\mathcal{E}$ of work.
- **Line Integral Form:** From $dW = \vec{F} \cdot d\vec{l} = F\,dl\cos\theta$ and $\vec{F} = q\vec{E}$ (with $q = 1\text{ C}$):
  $$\mathcal{E} = \oint_{\partial S} \vec{E} \cdot d\vec{l}$$
  where $\partial S$ is a topological symbol denoting the closed contour bounding open surface $S$ (not a partial derivative).

### Magnetic Flux & Faraday-Lenz Law
$$\Phi_B = \iint_S \vec{B} \cdot d\vec{A} = \iint_S B\,dA\cos\theta$$

$$\mathcal{E} = \oint_{\partial S} \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt} = -\frac{d}{dt} \iint_S \vec{B} \cdot d\vec{A}$$

- **Faraday's Contribution:** A time-varying magnetic flux induces an EMF (even in empty space where no physical conductor or current is present).
- **Lenz's Law (The Minus Sign):** Sets the direction of the induced EMF—any resulting induced current generates a secondary magnetic field opposing the *change* in magnetic flux.
- **Three Ways to Vary $\Phi_B(t)$:**
  1. **Time-varying field magnitude $B(t)$:** Field strength increases or decreases (e.g., Problem 34).
  2. **Time-varying area $A(t)$:** Boundary moves, such as a sliding conducting bar moving at velocity $v$ with constant $B$ and $\theta = 0^\circ$ (e.g., Problem 54).
  3. **Time-varying angle $\theta(t)$:** Loop rotates inside a magnetic field (e.g., AC power generators).

> [!important] Electrostatic vs. Induced Electric Fields
> - **Electrostatic $\vec{E}$:** Originates on positive charges and terminates on negative charges ($\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0}$, $\oint \vec{E} \cdot d\vec{l} = 0$).
> - **Induced $\vec{E}$:** Non-conservative field that **circulates in closed loops** (similar to $\vec{B}$). Because it is not sourced by charges, its divergence and closed-surface flux are zero:
>   $$\nabla \cdot \vec{E}_{\text{induced}} = 0 \qquad \text{and} \qquad \oint_{\partial V} \vec{E}_{\text{induced}} \cdot d\vec{A} = 0$$

---

## 2. Eddy Currents & Magnetic Braking

- **Mechanism:** Moving a magnet past a **non-ferromagnetic conductor** (such as copper, rather than iron which sticks ferromagnetically) changes $\Phi_B$ through the metal.
- Free conduction electrons experience the induced EMF and swirl in closed loops called **eddy currents**.
- **Opposition to $\Delta\Phi_B$:** Induced currents care *only* about the change in field lines, never the baseline value:
  - If $720$ field lines pass through and $2$ are added, the eddy current generates $2$ lines in the opposite direction.
  - If $3$ lines are removed, it generates $3$ lines in the original direction to compensate.
- **Magnetic Braking:** The opposing magnetic field exerts a retarding drag force on the moving magnet or conductor (as seen in **Problems 54 & 59**, where a moving bar decelerates to rest).

---

## 3. Breakdown of Ampère's Law & Displacement Current

### The Charging Capacitor ("Soap Bubble") Paradox
Consider a wire carrying current $I$ charging a parallel-plate capacitor (plate area $A$, separation $d$, vacuum permittivity $\varepsilon_0$). At radial distance $r$ from the wire, a circular Amperian loop $\partial S$ yields:
$$\oint_{\partial S} \vec{B} \cdot d\vec{l} = B(2\pi r)$$

Because $\partial S$ bounds infinitely many open surfaces (like blowing on a soap film stretched across a ring), Ampère's original law $\oint_{\partial S} \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enc}}$ must give the same answer for every surface:
1. **Flat disk surface ($S_{\text{black}}$):** Pierced by the incoming wire $\implies I_{\text{enc}} = I \implies B(2\pi r) = \mu_0 I$.
2. **Surface stretched completely past the capacitor ($S_{\text{red}}$):** Pierced by the outgoing wire $\implies I_{\text{enc}} = I \implies B(2\pi r) = \mu_0 I$.
3. **Surface passing between the capacitor plates ($S_{\text{blue}}$):** No conduction charges cross the vacuum gap $\implies I_{\text{enc}} = 0 \implies B(2\pi r) = 0$ **(Contradiction!)**.

### Maxwell's Derivation of Displacement Current ($I_d$)
As charge $Q(t)$ accumulates on the plates with surface charge density $\sigma = \frac{Q}{A}$, the uniform electric field trapped between the plates builds up:
$$E = \frac{\sigma}{\varepsilon_0} \implies \sigma = \varepsilon_0 E \implies Q = \sigma A = \varepsilon_0 E A$$

Differentiating with respect to time equates the charging current $I = \frac{dQ}{dt}$ to the rate of change of electric flux $\Phi_E = \iint_S \vec{E} \cdot d\vec{A}$:
$$I_d = \frac{dQ}{dt} = \varepsilon_0 \frac{d}{dt}(EA) = \varepsilon_0 \frac{d}{dt} \iint_S \vec{E} \cdot d\vec{A} = \varepsilon_0 \frac{d\Phi_E}{dt}$$

- **In a Dielectric Medium:** Replace $\varepsilon_0$ with $\varepsilon = \varepsilon_r \varepsilon_0$:
  $$I_d = \varepsilon \frac{d\Phi_E}{dt}$$
- **Physical Takeaway:** Even in pure vacuum with **zero moving charges**, a time-varying electric flux produces a magnetic field identically to a real conduction current.

---

## 4. Complete Maxwell's Equations (Integral Form in Vacuum)

| Law | Equation | Surface / Path | Physical Meaning |
| :--- | :--- | :--- | :--- |
| **Gauss's Law ($\vec{E}$)** | $$\iint_{\partial V} \vec{E} \cdot d\vec{A} = \frac{Q_{\text{enc}}}{\varepsilon_0}$$ | Closed surface $\partial V$ enclosing volume $V$ | Electric flux is proportional to enclosed charge (electrostatic flow). |
| **Gauss's Law ($\vec{B}$)** | $$\iint_{\partial V} \vec{B} \cdot d\vec{A} = 0$$ | Closed surface $\partial V$ | **No magnetic monopoles.** $\vec{B}$ lines form continuous closed loops (N $\to$ S outside, S $\to$ N inside). |
| **Faraday-Lenz Law** | $$\oint_{\partial S} \vec{E} \cdot d\vec{l} = -\frac{d}{dt} \iint_S \vec{B} \cdot d\vec{A}$$ | Closed path $\partial S$ bounding open surface $S$ | Changing magnetic flux induces a circulating electric field. |
| **Ampère-Maxwell Law** | $$\oint_{\partial S} \vec{B} \cdot d\vec{l} = \mu_0 I_{\text{enc}} + \mu_0 \varepsilon_0 \frac{d}{dt} \iint_S \vec{E} \cdot d\vec{A}$$ | Closed path $\partial S$ bounding open surface $S$ | Conduction currents *and* changing electric flux induce a circulating magnetic field. |

**Lorentz Force Law** (couples fields to matter):
$$\vec{F} = q\vec{E} + q\vec{v} \times \vec{B}$$

---

## 5. Course Notes & Action Items

> [!info] Exam & Course Roadmap
> - **Chapter 29 is complete** and covered on **Exam 3** (expect displacement current problems).
> - **Upcoming:** Electromagnetic radiation ("season finale" application of Maxwell's equations), Exam 4, Final Exam, and Physics 204 (culminating in cosmology).

### Assigned Problems (Chapter 29)
- [ ] **Problem 31**
- [ ] **Problem 33**
- [ ] **Problem 34** *(time-varying $\vec{B}$ field — flagged as challenging)*
- [ ] Review related moving-bar problems: **Problem 54** and **Problem 59**