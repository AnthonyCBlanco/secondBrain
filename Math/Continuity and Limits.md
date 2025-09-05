# Continuity

### Idea

A function is **continuous** if its graph has no breaks, jumps, or holes.  
- [[Piecewise Functions]] may not be continuous (depends on how they are defined).  
- [[Rational Functions]] are not continuous at values of $x$ where the denominator is zero.  

---

### Continuity at a Point

A function $f$ is **continuous at $x = c$** if all three of these conditions are satisfied:

1. $f(c)$ is defined  
2. $\lim_{x \to c} f(x)$ exists  
3. $\lim_{x \to c} f(x) = f(c)$  

→ [[Limits]]  
→ [[Continuity and Limits]]  

---

### Ways Continuity Can Fail

Continuity at $x = c$ can fail if:  
1. The function is not defined at $x = c$  
2. The limit $\lim_{x \to c} f(x)$ does not exist  
3. The limit exists, but $\lim_{x \to c} f(x) \neq f(c)$  

→ [[Indeterminate Forms]]  
→ [[One-Sided Limits]]  

---

### Types of Discontinuity

#### Removable Discontinuity
- Occurs when a "hole" appears in the graph.  
- Common in [[Rational Functions]] where a factor cancels.  
- Example:  
  $$
  f(x) = \frac{x^2 - 1}{x - 1} \quad \Rightarrow \quad f(x) = x + 1, \; x \neq 1
  $$  
  At $x=1$, there’s a removable discontinuity (a hole).

#### Nonremovable Discontinuity
- Cannot be "fixed" by redefining the function at one point.  
- Includes **jumps** and **vertical asymptotes**.  
- Example:  
  $$
  f(x) = \frac{1}{x}
  $$  
  At $x=0$, $f(x)$ is not continuous because it has a vertical asymptote.

---

### Formally

Example:

$$
f(x) = \frac{1}{x}
$$  

- $f(0)$ is **undefined**  
- $\lim_{x \to 0} f(x)$ does not exist (left- and right-hand limits go to $\pm \infty$)  

Therefore, $f$ is **not continuous** at $x = 0$.  

---

#math #precalc #calculus #limits 
