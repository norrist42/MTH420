"""Python Essentials: The Standard Library.
<Timothy Norris>
<MTH420>
"""

import numpy as np
def prob1():
    """Define the matrices A and B as arrays. Return the matrix product AB."""

    A = np.array([[1,2,4],[1,3,7]])
    B = np.array([[1,1,1],[3,4,5],[4,5,8]])
    print(np.dot(A,B))
    print("\n")
prob1();

def prob2():
    """Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A."""
    A1 = np.array([[5,0,3],[9,8,4],[-1,8,5]])
    A2 = -1*np.dot(np.dot(A1,A1),A1)
    A3 = 9*np.dot(A1,A1)
    A4 = 15*A1
    print(A2+A3-A4)
    print("\n")
    
prob2()

def prob3():
    """Define the matrices A and B as arrays. Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    
    A5 = np.triu(np.ones((7,7)))
    B5 = -1*np.tril(np.ones((7,7)))+5*np.triu(np.ones((7,7))) -5*np.diag(np.diag(A5))
    print(np.dot(np.dot(A5,B5),A5))
    R = np.dot(np.dot(A5,B5),A5)
    R = R.astype(np.int64)
    print(R)
    print("\n")
    
prob3()

def prob4(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    mask = A<0
    A[mask] = 0
    print(A)
    print("\n")
    
    
y = np.arange(-11,13,17)
prob4(y)
mask = y <0
y[mask] = 0
print(y)

A6 = np.array([[-4,2,0],[0,4,4],[1,5,4]])
prob4(A6)
print(prob4(A6))
print("\n")

def prob5():
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    
    A7 = np.array([[6,2,4],[8,3,1]])
    B7 = 4 * np.tril(np.ones((3,3)))
    C7 = np.diag([-2,-2,-2])
    print(np.bmat([[np.zeros((3,4)),A7.T,np.eye(3)],[A7,np.zeros((2,3)),np.zeros((2,3))],[B7,np.zeros((3,3)),C7]]))
    
def prob6(A):
    """Divide each row of 'A' by the row sum and return the resulting array.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    print(A/A.sum(axis=1)[:,None])

A6 = np.array(([1,1,0],[0,1,0],[1,1,1]))
print(prob6(A6))
print("\n")

def prob7():
    """Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid.
    """
    
    grid = np.load("grid.npy")
    print(grid)
   
    horizontal_max = max(grid[i][j]*grid[i][j+1]*grid[i][j+2][i][j+3]for i in range(21) for j in range(18))
   
    vertical_max = max(grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j] for i in range (18) for j in range(21))
   
    diag1_max = max(grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3] for i in range(17) for j in range(17))
   
    diag2_max = max(grid[i][j]*grid[i-1][j-1]*grid[i-2][j-2]*grid[i-3][j-3] for i in range(3,20) for j in range(17))
   
    max_max = max(horizontal_max, vertical_max, diag1_max, diag2_max)
   
    print(max_max)
   
    i_step=1
    j_step=1
    i_min=1
    i_limit=19
    j_limit=19
    max(grid[i][j]
    * grid[i+i_step][j+j_step]
    * grid[i+2*i_step][j+2*j_step]
    * grid[i+3*i_step][j+3*j_step]
    for i in range(i_min, i_limit)
    for j in range(j_limit))
    print(max(max(grid[i][j]
              * grid[i+i_step][j+j_step]
              * grid[i+2*i_step][j+2*j_step]
              * grid[i+3*i_step][j+3*j_step]
              for i in range(i_min, i_limit)
              for j in range(j_limit)))
          for i_step, j_step, i_min, i_limit, j_limit
          in [( 0, 1, 0, 20, 17),  # horizontal
              ( 1, 0, 0, 17, 20),  # vertical
              ( 1, 1, 0, 17, 17),  # leading diagonal
              (-1, 1, 3, 20, 17)]) # trailing diagonal

print(prob7())

from functools import reduce
from operator import mul

def product(iterable):
    """Return the product of the numbers in the iterable."""
    return reduce(mul, iterable, 1)
	
print(max(max(product(grid[i+k*i_step][j+k*j_step] for k in range(4))
              for i in range(i_min, i_limit)
              for j in range(j_limit)))
          for i_step, j_step, i_min, i_limit, j_limit
          in [( 0, 1, 0, 20, 17),  # horizontal
              ( 1, 0, 0, 17, 20),  # vertical
              ( 1, 1, 0, 17, 17),  # leading diagonal
              (-1, 1, 3, 20, 17)]) # trailing diagonal
              
