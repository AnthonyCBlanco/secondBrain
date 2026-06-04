### Idea
When we talk about Planes in space we are talking about a flat "sheet" with some location in space. Previously we talked about [[Lines in Space]], how we can define a line in space if we know a point on the line and the direction of which to line is going. For planes in space we can make a similar statement,
	**We can define a plane in space given a point on the plane and the direction it faces**

### Finding Direction
The direction information will be supplied by a vector, called a *normal* vector, that is orthogonal(parallel) to the plane. 
	What does "orthogonal to the plane" mean?
	- We chose any to points that are in the plane, $P$ and $Q$ 
	- We think about the direction vector $\vec{PQ}$, which is just a line within our plane between two points
	- We can find if some arbitrary vector $\vec{n}$ is orthogonal to the plane by solve the equations $\vec{n} \cdot \vec{PQ} =0$  
> [!note] When the dot product is equal to zero our vector are orthogonal 


### Equation of a Plane
> General form and Standard form

The plane passing through the point $P=(x_{0}, y_{0}, z_{0})$ with a normal vector $\vec{n}=\langle a,b,c \rangle$ can be described by the equation with **standard form**
$$\begin{gather}
a(x-x_{0})+ b(y-y_{0})+c(z-z_{0})=0  \\
\text{or in general form} \\
ax+by+ca=d
\end{gather}
$$

> [!quote] Remember
> A key to remember thoughout is to find the eqaution of a plane, we need a point and a normal vector. 


##### Testing if two planes are orthogonal
Given two planes, we can test if they are orthogonal by take to [[Cross Product]].

> [!quote] Remember
> Two planes are orthogonal to each other if the cross product produces the zero vector

We can find the normal vector of each plane and take the cross product

##### Finding the intersection of two planes 



#math