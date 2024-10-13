import numpy as np

# Gram-Schmidt process to orthogonalize a matrix
def gram_schmidt(A):
    return np.linalg.qr(A)[0]

def svd(A):
    if A.shape[1] <= A.shape[0]:  # Tall or square matrix
        A1 = A @ A.T

        eigvals, eigvecs = np.linalg.eigh(A1)
        sorted_indices = np.argsort(eigvals)[::-1]  # Get indices that would sort the eigenvalues in descending order
        eigvals = eigvals[sorted_indices]
        eigvecs = eigvecs[:, sorted_indices]

        U = eigvecs
        
        eigvals = np.maximum(eigvals, 0)
        sing_vals = eigvals ** .5
        S = np.diag(sing_vals)
        nonzero_singulars = sing_vals >  1e-6
        S_inv = np.zeros_like(S.T)
        S_inv[nonzero_singulars, nonzero_singulars] = 1/S[nonzero_singulars,nonzero_singulars]

        V_T  = S_inv @ U.T @ A

        V = V_T.T

        if S.shape[1] < A.shape[1]:
            S = np.pad(S, ((0, 0), (0, A.shape[1] - S.shape[1])), 'constant')

    else: # wide matrix
        A2 = A.T @ A

        eigvals, eigvecs = np.linalg.eigh(A2)
        sorted_indices = np.argsort(eigvals)[::-1]  # Get indices that would sort the eigenvalues in descending order
        eigvals = eigvals[sorted_indices]
        eigvecs = eigvecs[:, sorted_indices]

        V = eigvecs
        
        eigvals = np.maximum(eigvals, 0)
        sing_vals = eigvals ** .5
        S = np.diag(sing_vals)
        nonzero_singulars = sing_vals >  1e-6
        S_inv = np.zeros_like(S.T)
        S_inv[nonzero_singulars, nonzero_singulars] = 1/S[nonzero_singulars,nonzero_singulars]

        U  = A @ V @ S_inv

        if S.shape[0] < A.shape[0]:
            S = np.pad(S, ((0, A.shape[0] - S.shape[0]), (0, 0)), 'constant')

    cond_num = np.max(sing_vals)/np.min([s for s in sing_vals if s>1e-6])

    if (sing_vals <  1e-6).any:
        A_inv = "A is not invertible"
    else:
        A_inv = V@S_inv@U.T
    return (U, S, V), cond_num, A_inv

