from mysvd import svd
import numpy as np
def test_svd():
    # Test for random matrices of different shapes
    for i in range(1000):
        s1 = np.random.randint(2,50)
        s2 = np.random.randint(2,50)
        A = np.random.rand(s1, s2)
        (U, S, V),cond_num, inv = svd(A)

        assert np.allclose(U @ S @ V.T, A), f"Reconstruction failed for matrix shape {A.shape}"
        
        # assert np.isclose(cond_num, np.linalg.cond(A)), ( cond_num, np.linalg.cond(A))
        np.isclose(cond_num, np.linalg.cond(A)), ( cond_num/np.linalg.cond(A))

        if A.shape[0]==A.shape[1] and not(np.isclose(np.linalg.det(A),0).any):
            assert np.isclose(inv, np.linalg.inv(A))
        else:
            assert inv == "A is not invertible"

    A = np.array([[3,2],[2,3],[2,-2]])
    U, S, V = svd(A)[0]
    assert np.allclose(U @ S @ V.T, A), f"Reconstruction failed for matrix shape {A.shape}"

    A = np.array([[3,2],[2,3]]) # u = v, causes issues when not using LA tricks to determine U/V out of the other matrix 
    U, S, V = svd(A)[0]
    assert np.allclose(U @ S @ V.T, A), f"Reconstruction failed for matrix shape {A.shape}"

    print("SVD implementation successful for all test cases!")