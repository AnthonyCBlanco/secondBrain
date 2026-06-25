### Idea 
We can apply calculus concepts to Vector-Valued Functions the same way we apply them to real valued functions. These functions are often used to represent [[Parametric Equations and Plane Curves|curves]] in space.
#### Limits of Vector-Valued Functions
The initial definition of the limit of the vector-valued may seem difficult but its not different from limits of real-valued functions


> [!important] Definition
> Let **I*** be an open interval containing **c**. The **limit of $\vec{r}(t)$, as $t$ approaches $c$ i $\vec{L}$**, expressed as :
$$
\lim_{ t \to c }\vec{r}(t)=\vec{L} 
$$

Let $\vec{r}(t)=\langle\lim_{ t \to c }f(t), \lim_{ t \to c }g(t)\rangle$ be some vector-valued function in $\mathbb{R}^2$ defined on an open interval $I$ containing $c$, except possibly at $c$. Then
$$
\lim_{ t \to c } \vec{r}(r)=\langle \lim_{ t \to c } f(t), \lim_{ t \to c } g(t)\rangle  
$$

We can expand this expression to $\mathbb{R}^3$ using the same idea.

#### Continuity of Vector-Valued Functions
Just like continuity of real-valued functions we apply the same rules
- [[Continuity and Limits]]


### Derivatives of Vector-Valued Functions 
> [!tip] Application 
> In physics, if $\vec{r}(t)$ represents position, then the derivative $\vec{r}'(t)$ represents velocity. See: [[The Calculus of Motion]].

By the limit definition:
$$\begin{gather}
\vec{r}\,'(c)= \lim_{ h \to 0 } \frac{\vec{r}(c+h)-\vec{r}(c)}{h}   \\
\text{Or by Prime Notation} \\
\vec{r}\,' (t)= \langle f'(t), g'(t) \rangle
\end{gather}

$$

### Integration of Vector-Valued Functions
We can define antiderivatives and the indefinite integral of vector-valued functions the same manner we defined [[Indefinite Integration]] before. We can also evaluate [[Definite Integrals]] component-wise using the [[Fundamental Theorem of Calculus]]. 
$$
\int \vec{r}(t)dt= \langle \int f(t)dt, \int g(t)dt \rangle
$$

#math/calculus #summer2026 #math/vectors