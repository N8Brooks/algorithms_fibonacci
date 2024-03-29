# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:15:21 2019

@author: DSU
"""

# dynamic implementation
def FibLoop(x: int) -> int:
    assert x >= 0           # input validation
    # base case
    if x <= 1: return 1
    a, b, = 1, 1
    # keep adding until you reach your index
    for _ in range(x-1):
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
    # has been calculated (or base case)
    if x in dp:
        return dp[x]
    # has not been calculated, so calculate as fib
    else:
        fib = FibRecurDPWorker(x-2, dp) + FibRecurDPWorker(x-1, dp)
        dp[x] = fib
        return fib

# wrapper method for FibRecurDPWorker
def FibRecurDP(x: int) -> int:
    assert x >= 0
    # dp dict is only kept for 1 call of FibRecurDP
    # call with base cases already created
    return FibRecurDPWorker(x, {0:1, 1:1})

# helper method for power that multiplies matricies
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

# helper method for FibMatrix that computes powers of matrices
def MatrixPower(F: list, x: int) -> None: 
    if x <= 1: return
    
    # matrix to multiply by if odd
    M = [[1, 1],\
         [1, 0]]

    # multiply matrices
    MatrixPower(F, x // 2) 
    MatrixMultiply(F, F) 
    
    # multiply if odd
    if x % 2: 
        MatrixMultiply(F, M)

# matrix multiplication method
def FibMatrix(x: int) -> int:
    assert x >= 0
    # F is the matrix that is computed
    F = [[1, 1],\
         [1, 0]]
    # power
    MatrixPower(F, x) 
    
    return F[0][0]

# Returns n'th fuibonacci number using table f[] 
def FibCassini(x: int) -> int: 
    assert x >= 0
    # base cases 
    if x <= 1: return 1

    # applyting above formula [Note value n&1 is 1 
    # if n is odd, else 0. 
    if x % 2:
        k = x // 2
        return (2*FibCassini(k-1) + FibCassini(k))*FibCassini(k)
    else:
        k = (x + 1) // 2
        return FibCassini(k)*FibCassini(k) + FibCassini(k-1)*FibCassini(k-1)

# using golden ratio (only works to x==69 before precision becomes an issue)
def FibFormula(x: int) -> int:
    assert x >= 0
    phi = (1 + 5**0.5) / 2
    return round(phi ** (x+1) / 5**0.5)

# list of all algorithms
algorithms = [FibLoop, FibRecur, FibRecurDP, FibMatrix, FibCassini, FibFormula]
