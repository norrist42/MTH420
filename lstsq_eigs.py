#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:10:12 2018

@author: buddynorris13
"""

"""Volume 1: Least Squares and Computing Eigenvalues.
<Name>
<Class>
<Date>
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy import linalg as spla

# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    m,n=A.shape
    Q,R=np.linalg.qr(A,mode="complete")
    p = np.dot(Q.T,b)
    return spla.solve_triangular(R[:n], Q.T[:n].dot(b), lower=False)

a = np.array([[4,2], [4,6]])
b = np.array([5,8])
x = np.linalg.solve(a, b)
print(x)

print(least_squares(a,b))

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    data = np.load("housing.npy")
    b=np.array([row[1] for row in data])
    a1=np.array([row[0] for row in data])
    a=np.stack((a1,np.ones(33)),axis=-1)
	
    x=[row[0] for row in data]
    y=[row[1] for row in data]
	
    slope,intercept=least_squares(a,b)
    abline_values = [slope * i + intercept for i in x]
    
    plt.plot(x, abline_values, 'r')
    plt.plot(x,y,'bo')
    plt.ylabel('housing prices')
    plt.xlabel('year')
    plt.show()


print(least_squares(a,b))
line_fit()

# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    data = np.load("housing.npy")
    b=np.array([row[1] for row in data])
    a1=np.array([row[0] for row in data])
    a3=np.stack((a1**3,a1**2,a1,np.ones(33)),axis=-1)
    a6=np.stack((a1**6,a1**5,a1**4,a1**3,a1**2,a1,np.ones(33)),axis=-1)
    a9=np.stack((a1**9,a1**8,a1**7,a1**6,a1**5,a1**4,a1**3,a1**2,a1,np.ones(33)),axis=-1)
    a12=np.stack((a1**(12),a1**(11),a1**(10),a1**9,a1**8,a1**7,a1**6,a1**5,a1**4,a1**3,a1**2,a1,np.ones(33)),axis=-1)
    
	
    x=[row[0] for row in data]
    y=[row[1] for row in data]
	
    z = spla.lstsq(a3, b)[0]
    p = np.poly1d(z)
	
    z2 = spla.lstsq(a6, b)[0]
    p2 = np.poly1d(z2)
	
    z3 = spla.lstsq(a9, b)[0]
    p3 = np.poly1d(z3)
	
    z4 = spla.lstsq(a12, b)[0]
    p4 = np.poly1d(z4)
	
    plt.plot(x, p(x), 'r')
    plt.plot(x, p2(x), 'r')
    plt.plot(x, p3(x), 'r')
    plt.plot(x, p4(x), 'r')
    plt.plot(x,y,'bo')
    plt.ylabel('housing prices')
    plt.xlabel('year')
    plt.show()

polynomial_fit()

