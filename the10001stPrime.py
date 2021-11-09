# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 05:45:19 2021

@author: sherin
"""
import math
def the10001stPrime():
    cntr = 1
    n = 3
    lastPrime = 2
    while cntr < 10001:
       if  isPrime(n):
           cntr+=1
           lastPrime = n
       n+=1
    return lastPrime
def isPrime(n):
    
    if n <= 1:
        return False
    if n == 2:
    
        return True
    if n > 2 and n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n))+1,2):
        if n % i == 0:
            return False
    return True
print(the10001stPrime())
    
    