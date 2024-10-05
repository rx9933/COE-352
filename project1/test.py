import numpy as np
from scipy.linalg import qr

def sort_val_vect(eigval, eigvect):
    # Sort eigenvalues and corresponding eigenvectors in descending order
    sorted_indices = np.argsort(eigval)[::-1]
    eigval_sorted = eigval[sorted_indices]
    eigvect_sorted = eigvect[:, sorted_indices]
    return eigval_sorted, eigvect_sorted

def complete_orthonormal_basis(matrix):
    """Given a matrix with linearly independent columns, this function completes the orthonormal basis
    for the column space."""
    # QR decomposition gives us orthonormal vectors
    Q, R = qr(matrix, mode='full')
    return Q

def adjust_sign(U, V):
    # Adjust the sign of U and V such that the first component of each singular vector is positive
    for i in range(U.shape[1]):
        if U[0, i] < 0:
            U[:, i] *= -1
            V[:, i] *= -1
    return U, V

def e_full(e, u_s, v_s):
    if u_s > v_s:
        e_full =  np.vstack((e, np.zeros((u_s-v_s, v_s))))
    else:
        print("es", e.shape)
        print("v_s", v_s)
        print(np.zeros((v_s-u_s, v_s)).shape)
        e_full =  np.hstack((e, np.zeros((v_s-u_s, u_s))))
    return e_full

def svd(A):
    m, n = A.shape
    if m >= n:
        # More rows or square matrix
        eigval, eigvect = np.linalg.eig(A.T @ A)
        eigval, Vt = sort_val_vect(eigval, eigvect)
        eigval = np.sqrt(np.maximum(eigval, 0))  # Take the non-negative eigenvalues
        E = np.diag(eigval)  # Diagonal matrix of singular values
        Einv = np.diag(1 / eigval[eigval > 1e-10])  # Inverse singular values

        # Calculate U from the formula U = A V Σ⁻¹
        U_partial = A @ Vt @ Einv
        U = complete_orthonormal_basis(U_partial)  # Ensure U is orthonormal and square

        U, Vt = adjust_sign(U, V)  # Adjust sign for consistency

    if U.shape[0] != m:
            raise ValueError("U matrix should be of shape (m, m), but it's not.")
    
    else:
        # More columns than rows
        eigval, U = np.linalg.eig(A @ A.T)
        eigval, U = sort_val_vect(eigval, U)
        eigval = np.sqrt(np.maximum(eigval, 0))
        E = np.diag(eigval)
        Einv = np.diag(1 / eigval[eigval > 1e-10])

        # Calculate V from the formula V = Σ⁻¹ Uᵀ A
        V_partial = A.T @ U @ Einv.T # CHECK, need a Transpose?
        V = complete_orthonormal_basis(V_partial)  # Ensure V is orthonormal and square

        U, V = adjust_sign(U, V)  # Adjust sign for consistency

        if V.shape[1] != V.shape[0]:
            raise ValueError("V matrix should be square, but it's not.")
    
    return U, E, V

# Test case for rectangular matrix
A = np.array([[3, 2], [2, 3], [1, 4]])
u, e, v = svd(A)
print("U:\n", u)
print("E:\n", e)
print("V:\n", v)

# Verify reconstruction
e_f = e_full(e, u.shape[0], v.shape[0])
# e_full = np.hstack((e, np.zeros((e.shape[0], u.shape[0] - e.shape[1]))))  # Fill missing entries in e
reconstructed_A = u @ e_f @ v.T
print(np.linalg.svd(A))
print("Reconstructed A:\n", reconstructed_A)
"""
# Another test case
A = np.array([[3, 2, 2], [2, 3, -2]])
u, e, v = svd(A)
print("U:\n", u)
print("E:\n", e)
print("V:\n", v)

# e_full = np.hstack((e, np.zeros((e.shape[0], u.shape[0] - e.shape[1]))))  # Fill missing entries in e
e_f = e_full(e, u.shape[0], v.shape[0])
reconstructed_A = u @ e_f @ v.T
print("Reconstructed A:\n", reconstructed_A)
"""