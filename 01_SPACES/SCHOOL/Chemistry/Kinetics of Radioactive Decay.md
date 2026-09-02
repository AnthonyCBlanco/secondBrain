### Idea
Radioactive decay is the spontaneous disintegration of an unstable atomic nucleus via the emission of ionizing particles and radiation. 

Regardless of the isotope, type of decay ($\alpha$, $\beta$, $\gamma$, positron emission, or electron capture), or environmental conditions, **all radioactive decay processes strictly follow [[First-Order Kinetics|first-order kinetics]]**. Because decay is a purely nuclear event, decay rates are completely unaffected by temperature, pressure, concentration, chemical bonding, or catalysts.

### Formally
Let $N$ represent the number of radioactive nuclei (nuclides) present at time $t$.

The **decay rate** (also called the **Activity**, $A$) is directly proportional to the number of radioactive nuclei:
$$
\text{Activity } (A) = -\frac{dN}{dt} = \lambda N
$$

- $\lambda$ is the **decay constant** (the first-order rate constant), specific to each radionuclide (units: $\text{s}^{-1}$, $\text{min}^{-1}$, $\text{hr}^{-1}$, or $\text{yr}^{-1}$).
- $N$ is the number of radioactive parent nuclei present.

### Units of Activity
- **Becquerel ($\text{Bq}$):** The SI unit of radioactivity.
  $$1 \text{ Bq} = 1 \text{ disintegration per second (dps)}$$
- **Curie ($\text{Ci}$):** Standard historical unit based on $1\text{ g}$ of Radium-226.
  $$1 \text{ Ci} = 3.7 \times 10^{10} \text{ Bq} = 3.7 \times 10^{10} \text{ dps}$$

### Integrated Rate Law for Radioactive Decay
Integrating the differential decay equation yields the relationship between the number of nuclei remaining ($N_t$) and time elapsed ($t$):

$$
\ln\left(\frac{N_t}{N_0}\right) = -\lambda t
$$

$$
\ln N_t = -\lambda t + \ln N_0
$$

$$
N_t = N_0 e^{-\lambda t}
$$

Because mass ($m$) and activity ($A$) are directly proportional to the number of nuclei ($N$), these equations apply identically to mass and activity:
$$
m_t = m_0 e^{-\lambda t} \quad \text{and} \quad A_t = A_0 e^{-\lambda t}
$$

### Half-Life ($t_{1/2}$)
The **half-life** is the time required for half ($50\%$) of the radioactive parent nuclei in a sample to decay:

$$
t_{1/2} = \frac{\ln(2)}{\lambda} \approx \frac{0.693}{\lambda}
$$

$$
\lambda = \frac{\ln(2)}{t_{1/2}} \approx \frac{0.693}{t_{1/2}}
$$

**Fraction Remaining:**
After $n$ half-lives (where $n = \frac{t}{t_{1/2}}$), the fraction of original radioactive nuclei remaining is:
$$
\text{Fraction Remaining} = \frac{N_t}{N_0} = \left(\frac{1}{2}\right)^n = \left(\frac{1}{2}\right)^{t / t_{1/2}}
$$

### Radiocarbon Dating (Carbon-14 Dating)
Carbon-14 is continuously produced in the upper atmosphere by cosmic neutrons colliding with nitrogen:
$$
\ce{^{14}_7N + ^1_0n -> ^{14}_6C + ^1_1H}
$$

- Living organisms maintain a constant $\ce{^{14}C}/\ce{^{12}C}$ ratio via continuous carbon exchange ($\text{CO}_2$ uptake / consumption).
- When the organism dies, carbon intake ceases and $\ce{^{14}C}$ decays via $\beta^-$ decay ($t_{1/2} = 5730\text{ years}$):
  $$
  \ce{^{14}_6C -> ^{14}_7N + ^0_{-1}e}
  $$
- Measuring the remaining activity ($A_t$) relative to living carbon activity ($A_0 \approx 15.3 \text{ dpm/g C}$) allows dating of artifacts up to $\sim 50,000\text{ years}$:
  $$
  t = -\frac{1}{\lambda} \ln\left(\frac{A_t}{A_0}\right) = -\frac{t_{1/2}}{0.693} \ln\left(\frac{A_t}{A_0}\right)
  $$

### Example
**A piece of ancient charcoal discovered at an archaeological excavation exhibits a $\ce{^{14}C}$ decay rate of $3.60 \text{ disintegrations per minute per gram of carbon (dpm/g)}$. Fresh living wood has an activity of $15.3 \text{ dpm/g}$. Given that the half-life of $\ce{^{14}C}$ is $5730\text{ years}$, calculate the age of the charcoal.**

1. Find the decay constant ($\lambda$):
   $$
   \lambda = \frac{0.6931}{t_{1/2}} = \frac{0.6931}{5730 \text{ yr}} = 1.2097 \times 10^{-4} \text{ yr}^{-1}
   $$

2. Use the integrated rate law to solve for age ($t$):
   $$
   \ln\left(\frac{A_t}{A_0}\right) = -\lambda t
   $$
   $$
   \ln\left(\frac{3.60}{15.3}\right) = -(1.2097 \times 10^{-4} \text{ yr}^{-1}) t
   $$
   $$
   \ln(0.2353) = -(1.2097 \times 10^{-4}) t
   $$
   $$
   -1.4469 = -(1.2097 \times 10^{-4}) t
   $$
   $$
   t = \frac{-1.4469}{-1.2097 \times 10^{-4} \text{ yr}^{-1}} \approx 11,960 \text{ years}
   $$

The charcoal is approximately **$1.20 \times 10^4 \text{ years old}$** (or $11,960\text{ years}$).

### Related
- [[Nuclear Reactions]]
- [[First-Order Kinetics]]
- [[Chemistry MOC]]
- [[Atomic Structure]]
- [[Isotopes]]

#chemistry/nuclear-chemistry #chemistry/kinetics #chemistry/general-chemistry-2 #fall2026
