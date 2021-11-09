# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:57:07 2021

@author: sherin
"""
def multiplyOfThreeFive(n):       
    return sum([x for x in range (n) if x%3==0 or x%5==0])
print(multiplyOfThreeFive(1000))