### Idea

[[Number Systems]]

We can perform basic binary arithmetic just like we do in [[Number Systems|decimal]] arithmetic.

When doing **addition** or **multiplication** in binary (or any other base), we follow the same rules as in base 10:  
**carry over** whenever the result exceeds the highest digit allowed in that base.

For example, in binary:

- $1 + 1 = 10$ (carry the 1)
- $1 + 1 + 1 = 11$ (1 carried, 1 left behind)

→ [[Comp Sci/Binary Arithmetic]]  
→ [[Base Conversions]]  
→ [[Modular Arithmetic]]

---

### Formally

Rules for binary addition:

| A   | B   | A + B |
| --- | --- | ----- |
| 0   | 0   | 0     |
| 0   | 1   | 1     |
| 1   | 0   | 1     |
| 1   | 1   | 10    |

Rules for binary multiplication:

| A | B | A × B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   0    |
| 1 | 0 |   0    |
| 1 | 1 |   1    |

---

#math #compsci #numbersystems
