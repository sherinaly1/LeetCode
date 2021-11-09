# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 10:27:02 2021

@author: sherin
"""
def SumSquareDifference(n):
    sumSquare= SquareSum = 0
    for i in range(1,n+1):
        sumSquare += i**2
        SquareSum += i
    SquareSum = SquareSum**2
    return abs(SquareSum - sumSquare)
print(SumSquareDifference(100))