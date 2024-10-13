import numpy as np
from mysvd import svd  # Import your SVD algorithm
np.seterr(divide='ignore', invalid='ignore')
## Area vector for internal stresses

def create_shifted_matrix(rows, cols):
    # Initialize an empty matrix with zeros
    matrix = np.zeros((rows, cols))
    
    # Create the main diagonal with -1
    np.fill_diagonal(matrix[:, :-1], -1)
    
    # Create the first upper diagonal with 1
    np.fill_diagonal(matrix[:, 1:], 1)
    
    return matrix

def solve_spring_mass_system(num_springs, spring_constants, masses, boundary_condition):
    # Step 1: Set up the stiffness matrix K and force vector f
    num_masses = len(masses)
    C = np.zeros((num_springs, num_springs))
    f = np.zeros(num_masses)
    
    # Populate stiffness matrix based on spring consta nts
    for i in range(num_springs):
        C[i, i] += spring_constants[i]

    # Add masses to the force vector
    for i in range(num_masses):
        f[i] = masses[i] * 9.81  # gravitational force
    

    # Apply boundary conditions
    if boundary_condition == "fixed-free":
        assert num_masses == num_springs, "incorrect number of springs or masses for boundary condition"
        A = create_shifted_matrix(num_springs-1, num_masses)
        one = np.zeros((1,num_masses))
        one[0,0] = 1
        A = np.vstack((one, A))

    elif boundary_condition == "fixed-fixed":
        # Fix both ends
        assert num_masses == num_springs - 1, "incorrect number of springs or masses for boundary condition"
        A = create_shifted_matrix(num_springs-2, num_masses)
        one = np.zeros((1,num_masses))
        one[0,0] = 1
        last = np.zeros((1,num_masses))
        last[-1,-1] = -1
        A = np.vstack((one, A,  last))

    elif boundary_condition == "free-free":
        raise ValueError("Cannot evaluate two-free end problem; no solutions available")
   

    K = A.T @ C@ A
    (U, S, V), cond_num, Kinv = svd(K) 
    if isinstance(Kinv, np.ndarray):
        pass
    else: # note we calculate the pseudo-inverse, here, in case the true inverse of K does not exist (0 value for one or more singular values)
        Sinv = np.where(np.abs(S) >= 10**(-5), 1.0 / S, 0)

        Kinv = V@ Sinv @ U.T

    # Solve for displacements u
    u = Kinv @ f

    # Step 3: Compute elongations and internal stresses
    elongations = np.zeros(num_springs)
    stresses = np.zeros(num_springs)

    if boundary_condition == "fixed-fixed":
        elongations = np.hstack((u[0],np.diff(u),-u[-1]))
    else: # must be "fixed-free"
       elongations =  np.hstack((u[0],np.diff(u)))

    # assuming constant spring cross-sectional areas =1
    areas = np.ones((num_springs))
    stresses = elongations * spring_constants/areas

    # Return displacements, elongations, stresses, and condition number of K
    return u, elongations, stresses, cond_num






