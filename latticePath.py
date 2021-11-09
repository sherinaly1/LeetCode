# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:24:49 2021

@author: sherin
"""
import math
def BinomialCoefficient(n,k):
    if n>k and k>=0:
        return math.factorial(n)//(math.factorial(k) * math.factorial(n-k))
    else:
        return 0
def latticePath(a,b):
    return BinomialCoefficient(a+b,a)
print(latticePath(20,20))
