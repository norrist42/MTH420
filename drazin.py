

"""Volume 1: The Drazin Inverse.
<Timothy Norris>
<MTH 420>
"""

import numpy as np
from scipy import linalg as la


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.allclose(la.det(A),0):
        return 0
    
    n = len(A)
    k = 1
    Ak = A.copy()
    while k<=n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1
        
    return

a = np.matrix('1 3 0 0; 0 1 3 0; 0 0 1 3; 0 0 0 0')
ad = np.matrix('1 -3 9 81; 0 1 -3 -18; 0 0 1 3; 0 0 0 0') #FALSE
b = np.matrix('1 1 3; 5 2 6; -2 -1 -3')
bd = np.matrix('0 0 0; 0 0 0; 0 0 0')

print("a: ",a,"\n")
print("ad: ",ad,"\n")
print("b: ",b,"\n")
print("bd: ",bd,"\n")

print(index(a))
print(index(ad))
print(index(b))
print(index(bd))

# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    
    print("\nAAd=AdA")
    print(np.ma.allclose(np.dot(A,Ad),np.dot(Ad,A)))
    print("A**(k+1)Ad = A**k")
    print(np.ma.allclose(np.dot(A**(index(A)+1),Ad),A**(index(A))))
    print("AdAAd=Ad")
    print(np.ma.allclose(np.dot(np.dot(Ad,A),Ad),Ad))
    
is_drazin(a,ad,index(a))
is_drazin(b,bd,index(b))

# Problem 2
def drazin_inverse(A, tol = 1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    
    n = A.shape[1]
    f1 = lambda x:abs(x)>tol
    V,S,k1=la.schur(A,sort=f1)
    f2 = lambda x:abs(x)<=tol
    Z,T,k2 = la.schur(A,sort=f2)
    U=np.hstack((S[:,:(k1)],T[:,:(n-k1)]))
    Uinv=la.inv(U)
    V=np.dot(np.dot(Uinv,A),U)
    Minv=np.zeros_like(A)
    if k1 !=0:
        Minv[:(k1),:(k1)]=la.inv(V[:(k1),:(k1)])
    D=np.dot(np.dot(U,Minv),Uinv)
    return D
is_drazin(a,drazin_inverse(a),index(a))
is_drazin(b,drazin_inverse(b),index(b))

# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
from scipy.sparse import csgraph

g1 = np.matrix('0 1 0 0; 1 0 1 0; 0 1 0 1; 0 0 1 0')
g2 = np.matrix('0 1; 1 0')

l1 = csgraph.laplacian(g1, normed=False)
l2 = csgraph.laplacian(g2, normed=False)

d = []
for i in range(0,4):
    R = l1
    R[i]=np.eye(4)[i]
    d.append(np.diagonal(drazin_inverse(R)))
    i = i+1
    
print(np.vstack((d))[1,3],'\n', np.vstack((d)))

e = []
for i in range(0,2):
    R = l2
    R[i]=np.eye(2)[i]
    e.append(np.diagonal(drazin_inverse(R)))
    i=i+1

print(np.stack((e))[0,1],'\n', np.stack((e)))