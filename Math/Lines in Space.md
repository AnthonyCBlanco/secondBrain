### Idea
Just like a line in 2D space we need a point and slope. Slope Conveys direction information. As vertical lines have an undefined slope.

**To define a line, one needs a point on the line and the direction of the line.**
	This holds true for lines in space as well

Given some vector $\vec{p}$ who's tip ends on the line $P$, vector $\vec{d}$ which is parallel to $P$. Starting at $\vec{p}$ and traveling one length of $\vec{d}$ gives another vector that lands on the line $P$ 

We can now write this line a a function of a scalar $t$
$$\begin{gather}
\vec{l}(t)=\vec{p}+t\vec{d} \\
\text{or as a parametric equation} \\
\langle x_{0}+at, y_{0}+bt, z_{0}+ct\rangle \\
\end{gather}
$$

==Remember that typical equations of lines do not work in 3D space== 

##### Finding the intersection of two lines 
If two non-parallel lines intersect, then the intersection is a single point
	We need to find a point that is on both lines 
> To find intersection, we need a point on both lines, but the point does note need to be from same parameter value on each line, so use different parameters for each line




#math 