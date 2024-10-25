## **Project 1**: A linear spring-mass system solver using an explicitly coded SVD decomposition (for computing matrix inverses).

Notes about project:
1. The program has outputs for "internal force vectors" which are the same as the "internal stress vectors". Note that we do not have a spring cross-sectional area to consider, so the two terms are interchangeable.
2. Only 2 spring-mass systems are considered: fixed-fixed (both ends of the spring system are fixed) and fixed-free (same as free-fixed, one end of the spring system is fixed, one end is free).
We discuss the **free-free system** (neither of the ends of the spring system are fixed) below.
The free-free system has no external constraints or boundary conditions on the system; so, there is no constraint that holds the springs/masses in place. Consider the following issues that arise:
* Rigid Body Motion: The system is underdetermined (it can experience rigid body motion), so the mass displacements do not have a unique solution; the system could shift in any direction (or continue with indefinate motion, never settling in a unique configuration), and yet, equilibrium would hold.
  Rigid body motion would not change the relative positions of the masses or the spring elongations, so the system would have multiple possible solutions for the displacements (no unique solutions).
* Unique Solution/Singular Matrix: The stiffness matrix ($`$K`$) is singular and non-invertible; there is a rank deficiency ($`rank(K) < d`$) ($`d \in R`$, the degrees of freedom for the system). Mathematically, there are eigenvalues of value 0 in the stiffness matrix, causing infinite or undefined displacements as solutions to the system of equations $`Ku = f`$ (where $`u`$ is the nodal displacement, $`f`$ is the net force).
Thus we cannot provide a unique solution for a free-free spring-mass system; there are infinite solutions, and to determine a single valid solution, we require at least one more boundary condition (i.e. by fixing one (or both) of the spring-mass system's ends), fixing an arbitrary set of points within the system, etc.).

Proof of singular $`K`$ matrix:
$`K = A^{T} C A`$ where $`A ~`$ transformation of system configuration and $`C ~`$ positive semi-definite matrix of spring constants (material properites). Then, we seek to solve $`Ku = f`$ for $`u`$, the displacements, given $`f`$  as the applied forces (generally by mass(es) weight). 
We notice $`A`$ to be non-square for a free-free system; $`A \in R^{d \times d-1}`$ where $`u \in R^{d}`$ and $`C \in R^{d \times d}`$. Thus, we notice $`K`$ to be rank deficient ($`K \in R^{d-1 \times d-1}`$). 
