# Integration and Differentiation of Logarithmic Functions

Logarithmic functions appear frequently in calculus, especially in problems involving growth, decay, and inverse functions.  
This note summarizes how to **differentiate** and **integrate** logarithmic expressions, focusing on natural logarithms $ \ln(x) $, their properties, and related forms.

---

### Idea

Logarithmic functions provide a convenient way to represent inverse exponential behavior.  
Their derivatives and integrals follow predictable patterns based on the chain rule and substitution method.

The natural logarithm $\ln(x)$ is the most commonly used because it simplifies many expressions involving derivatives and integrals.

---

### Formally

## **1. Differentiation of Logarithmic Functions**

### **Basic Derivative**

$$
\frac{d}{dx} \ln(x) = \frac{1}{x}
$$

---

### **Log of a Function (Chain Rule)**

If $u = u(x)$:

$$
\frac{d}{dx} \ln(u) = \frac{1}{u} \frac{du}{dx}
$$

Example:
$$
\frac{d}{dx}\ln(3x^2 + 1) = \frac{6x}{3x^2 + 1}
$$

---

### **Derivative of Logarithm with a Different Base**

$$
\frac{d}{dx} \log_a(x) = \frac{1}{x\ln(a)}
$$

---

### **Logarithmic Differentiation**

Used when functions involve products, quotients, or exponents:

1. Take $\ln$ of both sides  
2. Simplify using log rules  
3. Differentiate  

Example:  
$$
y = x^x
$$

Take logs:

$$
\ln(y) = x\ln(x)
$$

Differentiate:

$$
\frac{1}{y} \frac{dy}{dx} = \ln(x) + 1
$$

Thus:

$$
\frac{dy}{dx} = x^x (\ln(x)+1)
$$

---

## **2. Integration of Logarithmic Functions**

### **Basic Integral**

$$
\int \frac{1}{x}\, dx = \ln|x| + C
$$

---

### **Integral of $\ln(x)$**

Use integration by parts:

$$
\int \ln(x)\, dx = x\ln(x) - x + C
$$

---

### **Integral of Log of a Function**

If $u = u(x)$:

$$
\int \frac{1}{u} \frac{du}{dx}\, dx = \ln|u| + C
$$

Example:

$$
\int \frac{3x^2}{x^3 + 1} \, dx = \ln|x^3 + 1| + C
$$

---

### **Integrals Involving Logarithmic Forms**

Common patterns:

1.  
$$
\int x\ln(x)\, dx
$$

Use integration by parts:

$$
\int x\ln(x)\, dx = \frac{x^2}{2}\ln(x) - \frac{x^2}{4} + C
$$

2.  
$$
\int \frac{\ln(x)}{x}\, dx = \frac{1}{2}(\ln(x))^2 + C
$$

Reason:

Let $u = \ln(x)$.

---

### Useful Logarithm Properties

- $\ln(ab) = \ln(a) + \ln(b)$  
- $\ln\left(\frac{a}{b}\right) = \ln(a) - \ln(b)$  
- $\ln(a^n) = n\ln(a)$  
- $e^{\ln(x)} = x$  

---

### Examples

#### **Example 1 — Differentiation**
$$
\frac{d}{dx} \ln(5x^4) = \frac{20x^3}{5x^4} = \frac{4}{x}
$$

#### **Example 2 — Integration**
$$
\int \ln(2x)\, dx
$$

Use integration by parts:

$$
x\ln(2x) - x + C
$$

---

### Concept Summary

| Concept                | Formula                                     | Meaning                  |       |                      |
| ---------------------- | ------------------------------------------- | ------------------------ | ----- | -------------------- |
| Derivative of $\ln(x)$ | $\frac{1}{x}$                               | Basic log derivative     |       |                      |
| Chain Rule             | $\frac{d}{dx}\ln(u) = \frac{u'}{u}$         | Log of a function        |       |                      |
| Change of Base         | $\frac{d}{dx}\log_a(x) = \frac{1}{x\ln(a)}$ | Non-natural logs         |       |                      |
| Integral of $\ln(x)$   | $x\ln(x)-x+C$                               | Via integration by parts |       |                      |
| Integral of $1/x$      | $\ln$                                       | $x$                      | $+ C$ | Basic antiderivative |

---

### Related Notes

- [[Integration by Substitution]]    
- [[The Chain Rule]]  
- [[Exponential Functions]]  

---

#math #calculus #derivatives #integrals
