# Sigma Notation

### Idea

**Sigma notation** (∑) provides a concise way to represent the **sum of a sequence of terms**.  
It’s commonly used in calculus and algebra to express repeated addition without writing each term individually.  

For example, instead of writing:
$$
2x^0 + 2x^1 + 2x^2 + 2x^3 + 2x^4 + 2x^5
$$
we can use sigma notation:
$$
\sum_{n=0}^{5} 2x^n
$$

---

### Definition

The general form of sigma notation is:

$$
\sum_{n=a}^{b} f(n)
$$

where:  
- $\sum$ = the summation symbol (the Greek letter Sigma)  
- $n$ = the **index of summation**  
- $a$ = **lower limit** (starting value of $n$)  
- $b$ = **upper limit** (ending value of $n$)  
- $f(n)$ = **expression** to be summed  

This represents:
$$
f(a) + f(a+1) + f(a+2) + \dots + f(b)
$$

---

### Common Properties of Summations

| Property | Formula | Description |
|-----------|----------|-------------|
| Constant Factor | $\displaystyle \sum_{i=1}^{n} c \, a_i = c \sum_{i=1}^{n} a_i$ | Constants can be factored out |
| Sum Rule | $\displaystyle \sum_{i=1}^{n} (a_i + b_i) = \sum_{i=1}^{n} a_i + \sum_{i=1}^{n} b_i$ | Summation distributes over addition |
| Difference Rule | $\displaystyle \sum_{i=1}^{n} (a_i - b_i) = \sum_{i=1}^{n} a_i - \sum_{i=1}^{n} b_i$ | Same for subtraction |
| Index Shift | $\displaystyle \sum_{i=k}^{n+k} a_{i-k} = \sum_{i=0}^{n} a_i$ | You can shift the index |
| Splitting Range | $\displaystyle \sum_{i=1}^{n} a_i = \sum_{i=1}^{m} a_i + \sum_{i=m+1}^{n} a_i$ | Can divide one sum into parts |

---

### Useful Summation Formulas

| Formula | Description |
|----------|-------------|
| $\displaystyle \sum_{i=1}^{n} 1 = n$ | Sum of constants |
| $\displaystyle \sum_{i=1}^{n} i = \frac{n(n+1)}{2}$ | Sum of first $n$ integers |
| $\displaystyle \sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$ | Sum of squares |
| $\displaystyle \sum_{i=1}^{n} i^3 = \left[\frac{n(n+1)}{2}\right]^2$ | Sum of cubes |

---

### Example 1 — Basic Evaluation

Evaluate:
$$
\sum_{n=1}^{4} (2n + 1)
$$

**Solution:**

Expand each term:
$$
(2(1) + 1) + (2(2) + 1) + (2(3) + 1) + (2(4) + 1) = 3 + 5 + 7 + 9 = 24
$$

---

### Example 2 — Applying Formulas

Find the value of:
$$
\sum_{n=1}^{100} n
$$

Using the formula:
$$
\sum_{n=1}^{n} n = \frac{n(n+1)}{2}
$$

Substitute $n=100$:
$$
\frac{100(101)}{2} = 5050
$$

---

### Example 3 — Variable Index

Simplify:
$$
\sum_{k=2}^{5} (k^2 - 1)
$$

Compute each term:
$$
(2^2 - 1) + (3^2 - 1) + (4^2 - 1) + (5^2 - 1) = 3 + 8 + 15 + 24 = 50
$$

---

### Concept Summary

| Concept | Formula / Description |
|----------|-----------------------|
| Definition | $\displaystyle \sum_{n=a}^{b} f(n)$ represents $f(a) + f(a+1) + \dots + f(b)$ |
| Constant Multiple | $\displaystyle c \sum f(n) = \sum c f(n)$ |
| Sum Formula | $\displaystyle \sum_{n=1}^{N} n = \frac{N(N+1)}{2}$ |
| Square Formula | $\displaystyle \sum_{n=1}^{N} n^2 = \frac{N(N+1)(2N+1)}{6}$ |
| Cube Formula | $\displaystyle \sum_{n=1}^{N} n^3 = \left[\frac{N(N+1)}{2}\right]^2$ |

---

### Related Notes

- [[Sequences and Series]]
- [[Arithmetic Series]]
- [[Geometric Series]]
- [[Limits]]
- [[The Derivative]]

---

#math #calculus #summation #notation #series
