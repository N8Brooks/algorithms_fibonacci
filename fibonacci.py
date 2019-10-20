# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:15:21 2019

@author: DSU
"""

# dynamic implementation
def FibLoop(x: int) -> int:
    assert x >= 0           # input validation
    if x <= 1: return 1     # base case
    a, b, = 1, 1
    for _ in range(x-1):    # sum until answer
        a, b = b, a+b
    return b

# brute force recursive
def FibRecur(x: int) -> int:
    assert x >= 0
    # base case
    if x <= 1:
        return 1
    # otherwise create
    else:
        return FibRecur(x-2) + FibRecur(x-1)

# recursive with memoization
def FibRecurDPWorker(x: int, dp: dict) -> int:
    # base case
    if x <= 1: return 1
    # create if not in dp
    return dp.setdefault(x, FibRecurDPWorker(x-2, dp) +\
                         FibRecurDPWorker(x-1, dp))

# wrapper method for FibRecurDPWorker
def FibRecurDP(x: int) -> int:
    assert x >= 0
    return FibRecurDPWorker(x, dict())  # delete dp after every run

# helper method for power
def MatrixMultiply(F: list, M: list) -> None:
    # calculate each
    x = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    y = (F[0][0] * M[0][1] + 
         F[0][1] * M[1][1]) 
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 

    # replace in-place
    F[0][0] = x 
    F[0][1] = y 
    F[1][0] = z 
    F[1][1] = w

# helper method for FibMatrix
def MatrixPower(F: list, x: int) -> None: 
    if x <= 1: return
    
    M = [[1, 1],\
         [1, 0]]

    MatrixPower(F, x // 2) 
    MatrixMultiply(F, F) 
    
    if x % 2 != 0: 
        MatrixMultiply(F, M)

# matrix multiplication method
def FibMatrix(x: int) -> int:
    assert x >= 0
    F = [[1, 1],\
         [1, 0]]
    MatrixPower(F, x) 
    
    return F[0][0] 

# using golden ratio
def FibFormula(x: int) -> int:
    phi = (1 + 5**0.5) / 2
    return round(phi ** (x+1) / 5**0.5)


















