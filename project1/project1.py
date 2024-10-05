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

def svd(A):
    m, n = A.shape
    if m >= n:
        # More rows or square matrix
        eigval, eigvect = np.linalg.eig(A.T @ A)
        eigval, V = sort_val_vect(eigval, eigvect)
        eigval = np.sqrt(np.maximum(eigval, 0))  # Take the non-negative eigenvalues
        E = np.diag(eigval)  # Diagonal matrix of singular values
        Einv = np.diag(1 / eigval[eigval > 1e-10])  # Inverse singular values

        # Calculate U from the formula U = A V Σ⁻¹
        U_partial = A @ V @ Einv
        U = complete_orthonormal_basis(U_partial)  # Ensure U is orthonormal and square

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
        V_partial = A.T @ U@ Einv.T#Einv @ U.T @ A
        # print(V_partial - A.T @ U@ Einv.T)
        V = complete_orthonormal_basis(V_partial)  # Ensure V is orthonormal and square
        print(V)
        if V.shape[1] != V.shape[0]:
            raise ValueError("V matrix should be square, but it's not.")
        print(U.shape)
        print(V.shape)
    return U, E, V

# Test case for rectangular matrix
A = np.array([[3, 2], [2, 3], [1, 4]])
u,e,v = svd(A)
A = np.array([[3, 2, 2],[2,3, -2]])
u,e,v = svd(A)
print(e)
e = np.hstack((e,np.array([[0],[0]])))
print(u@e@v.T)
# print(u@ e@ v.T)

