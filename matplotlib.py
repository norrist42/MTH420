#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:28:47 2018

@author: buddynorris13
"""

# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name> Timothy Norris Jr.
<Class> MTH 420
<Date> 2018-02-23
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    A = np.random.normal(size=(n,n))
    B = np.mean(A, axis= 1)
    return np.var(B, axis = 0)
	
def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    plt.figure(1)
    plt.plot([var_of_means(n) for n in range(100,1000,100)])
    plt.show()
prob1()

# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    
    plt.figure(2)
    plt.subplot(211)
    plt.plot(x, np.cos(2*np.pi*x), 'r')
    plt.subplot(211)
    plt.plot(x, np.sin(2*np.pi*x), 'b')
    plt.subplot(211) 
    plt.plot(x, np.arctan(2*np.pi*x), 'g')
    plt.show()
prob2()

# Problem 3
def f(x):
    return 1/(x**2-1)

def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x = np.linspace(-2,.9,100)
    y = np.linspace(1.1,6,100)
    plt.figure(3)
    plt.plot(x, f(x), 'm--', linewidth=4)
    plt.plot(y, f(y), 'm--', linewidth=4)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    plt.show()
prob3()

# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0, 2*np.pi, 100)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
    fig.suptitle("Graphs of sin(x)")
    ax1.plot(x, np.sin(x),'g')
    ax1.set_title("sin(x)")
    ax1.set_xlim(0, 2*np.pi)
    ax1.set_ylim(-2,2)
    ax2.plot(x, np.sin(2*x),'r--')
    ax2.set_title("sin(2x)")
    ax2.set_xlim(0, 2*np.pi)
    ax2.set_ylim(-2,2)
    ax3.plot(x,2*np.sin(x),'b--')
    ax3.set_title("2sin(x)")
    ax4.plot(x,2*np.sin(2*x),'m:')
    ax4.set_title("2sin(2x)")
prob4()

# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    header = ("Time", "Longitude", "Latitude")
    data = np.load("FARS.npy")

    ax4 = plt.subplot(121)
    ax4.plot(data[:,1],data[:,2], 'k', markersize=5, alpha=.5)
    plt.axis("equal")
    ax5 = plt.subplot(122)
    ax5.hist(data[:,0], bins=np.arange(0, 24)) # Or, equivalently,
    plt.show()
prob5()

# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """


    # Create a 2-D domain with np.meshgrid().
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = x.copy()
    X, Y = np.meshgrid(x, y)
    g = np.sin(X) * np.sin(Y)/(X*Y)
    # Plot the heat map of g over the 2-D domain.
    plt.subplot(131)
    plt.pcolormesh(X, Y, g, cmap="magma")
    plt.colorbar()
    plt.xlim(-np.pi, np.pi)
    plt.ylim(-np.pi, np.pi)
    # Plot a contour map of f with 10 level curves.
    plt.subplot(132)
    plt.contour(X, Y, g, 10, cmap="coolwarm")
    plt.colorbar()
    
    plt.show()

prob6()
