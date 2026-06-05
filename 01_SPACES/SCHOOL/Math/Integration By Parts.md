### Idea
We derive our formula for integrating by parts from the [[Product rule]]

$$
\begin{gather}  
(uv)'= uv'+vu'
\\
\int u dv=uv-\int vdu
\end{gather}

$$
Where $u$ and $v$ are functions of $x$. $du=u'$ and $dv=v'$

Steps for using Integration By Parts
- Pick u and dv so that $\int udv$ is the same as the original intergrand 
- Differentiate u to get du and integrate dv to get v
- Plug into formula
- Evaluate

We can use a similar formula for definite integrals integrating by parts
$$
\int_{a}^budv=uv]_{a}^b-\int_{a}^bvdx
$$


#### Example
If we used $u=e^x$ and $du=xdx$ then $du=e^xdx$ and $v=\frac{1}{2}x^2$ 
so we get
$$
\int xe^xdx=\frac{1}{2}x^2e^x
-\frac{1}{2}\int x^2e^xdx$$
Technically correct but very difficult to deal with

We are aloud to use $dv=dx$

#math  #integration