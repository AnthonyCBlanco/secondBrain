### Idea
We are very familiar with functions that work with *real values*, that is functions whose output is a real number. We can also look at functions that output a vector.

- **[[Multivariable Functions]]**: Multiple inputs ($x, y, \dots$), one scalar output ($z$).
- **Vector Valued Functions**: One input ($t$), one vector output ($\vec{r}$).


> [!tip] Vector Valued Functions
> **THE GENERAL FORM** 
$$ 
\begin{gather} 
\vec{r}(t)= \langle f(t),g(t) \rangle \\[]
\text{or} \\
\vec{r}(t)= \langle f(t), g(t), h(t \rangle) 
\end{gather}
$$

We can talk about range and domain for vector valued functions the same way we do with real values functions 
 - The ***domain*** of $\vec{r}$ is the set of all values of $t$ for which $\vec{r}(t)$ is defined.
 - The ***range*** of $\vec{r}$ is the set of all possible output [[Vectors|vectors]] $\vec{r}(t)$.

### Formally

#### Evaluating Vector-Valued Functions
Evaluating a vector-valued function at a specific value at a specific value of $t$ is straightforward. Simply evaluate each component function at that value of $t$. 

#### Algebra of Vector Valued Functions 
Using our general form, we can apply similar algebraic operations similar to how we compute [[Vectors|vector]] addition and scalar multiplication.

#### Displacement 
A vector-valued function $\vec{r}(t)$ is often used to describe the position of a moving object at some time $t$. We can find the difference of the locations and we call it ***displacement***.

We can use $\vec{d}$ as our displacement vector
$$
\vec{d} = \vec{r}(t_{1})-\vec{r}(t_{0})
$$

#math/calculus #math/[[Vectors|vectors]] #summer2026

