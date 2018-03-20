#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:29:26 2018

@author: buddynorris13
"""

def Add(a,b):
    return a+b

def AddList(a):
    s = 0
    for i in a:
            s = s + i
    return s

def Subtract(a,b):
    return a-b

def Multiply(a,b):
    return a*b

def Divide(a,b):
    if b == 0:
            print("Error: Divide by zero")
    else:
            return a/b

def Power(a,b):
    return a**b

def OddOrEven(a):
    if (a % 2)== 0:
            print("It is Even")
    else:
            print("It is Odd")

c = 13
d = 1

print("Add(c,d): ",Add(c,d),'\n')
print("Subtract(c,d): ",Subtract(c,d),'\n')
print("Multiply(c,d): ", Multiply(c,d), '\n')
print("Divide(c,d): ",Divide(c,d),'\n')
print("Power(c,d): ",Power(c,d),'\n')
print("OddOrEven(c): ",OddOrEven(c),'\n')