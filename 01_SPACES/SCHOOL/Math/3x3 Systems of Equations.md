### Idea

A **3×3 system of equations** consists of **three equations** with **three variables**, typically $x$, $y$, and $z$.

We aim to find a common solution $(x, y, z)$ that satisfies all three equations.

---

### General Form

$$

\begin{aligned}
a_1x + b_1y + c_1z &= d_1 \\
a_2x + b_2y + c_2z &= d_2 \\
a_3x + b_3y + c_3z &= d_3
\end{aligned}


$$
Where each $a$, $b$, $c$, and $d$ is a constant.

---

### Solving Methods

#### 1. **Substitution**
- Solve one equation for one variable.
- Substitute into the other two to reduce to a 2×2 system.
- Repeat until all variables are found.

→ [[Solving 2x2 Systems]]

#### 2. **Elimination**
- Add or subtract equations to eliminate one variable.
- Reduce the system to 2×2, then solve.

#### 3. **Matrix Method (Gaussian Elimination)**
- Convert the system to an **augmented matrix**.
- Use **row operations** to reach row-echelon form.
- Back-substitute to find the solution.

→ [[Matrices and Row Operations]]  
→ [[Gaussian Elimination]]

---

### Example

Solve:

$$

\begin{aligned}
x + 2y + z &= 9 \\
2x - y + 3z &= 8 \\
-x + 3y + 2z &= 3
\end{aligned}
$$

Step 1: Eliminate $x$ from Equations 2 and 3 using Equation 1.

Step 2: Solve the resulting 2×2 system for $y$ and $z$.

Step 3: Back-substitute to find $x$.

---

### Types of Solutions

- **One solution** → lines intersect at one point  
- **No solution** → system is inconsistent (parallel planes)  
- **Infinitely many solutions** → system is dependent (same plane)

---

### Tip

Check your solution by plugging all values into the original equations!

→ [[Systems of Equations]]  

---

#math #algebra #systems #3x3 #linear
