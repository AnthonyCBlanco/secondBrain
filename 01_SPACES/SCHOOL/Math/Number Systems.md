### Idea

**Number Bases** (also called **radix systems**) define how we represent numbers using different sets of digits and positional values.

In base-$b$, each digit in a number represents a power of $b$, starting from the right:

$$
(d_n d_{n-1} \dots d_1 d_0)_b = d_n \cdot b^n + d_{n-1} \cdot b^{n-1} + \dots + d_1 \cdot b^1 + d_0 \cdot b^0
$$

→ [[Binary (Base-2)]]  
→ [[Octal (Base-8)]]  
→ [[Decimal (Base-10)]]  
→ [[Hexadecimal (Base-16)]]

---

### Common Bases

| Base | Name         | Digits Used           | Notes                           |
|------|--------------|------------------------|---------------------------------|
| 2    | Binary       | 0, 1                   | Used in computers and logic     |
| 8    | Octal        | 0–7                    | Shorthand for binary            |
| 10   | Decimal      | 0–9                    | Standard human number system    |
| 16   | Hexadecimal  | 0–9, A–F               | Used in memory addresses, color codes |

---

### Conversions

#### Decimal to Base-$b$

1. Divide the number by $b$
2. Record the remainder
3. Repeat with the quotient until 0
4. Read remainders **in reverse**

Example (Decimal 13 to Binary):

$$
13 ÷ 2 = 6 \text{ R } 1 \\
6 ÷ 2 = 3 \text{ R } 0 \\
3 ÷ 2 = 1 \text{ R } 1 \\
1 ÷ 2 = 0 \text{ R } 1 \Rightarrow (1101)_2
$$

#### Base-$b$ to Decimal

Multiply each digit by its place value (power of $b$) and sum:

$$(1101)_2 = 1\cdot2^3 + 1\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 = 8 + 4 + 0 + 1 = 13$$

→ [[Base Conversion Examples]]

---

### Applications

- Binary (Base-2) → digital circuits, logic
- Hexadecimal → color codes, memory addresses
- Octal → compact binary representation

---

#math #compsci #numbersystems #discrete-structures
