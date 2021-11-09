# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:25:38 2021

@author: sherin
"""
import math
def FactorialDigitSum(n):
    f = str(math.factorial(n))
    print(f)
    print(sum(list(map(int,list(f)))))
FactorialDigitSum(100)