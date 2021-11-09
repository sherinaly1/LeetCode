# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 11:27:35 2021
HighlyDivisibleTriangularNumber
@author: sherin
"""

import numpy as np
from math import sqrt
def HighlyDivisibleTriangularNumber(D):
    step = 1
    tIdx =step
    t = np.sum([x for x in range(1,tIdx+1)])    
    #print (t)
    d = getDivistors(t)
    #print (len(d))
    while len(d)<=D:
        tIdx += step
        t = sum([x for x in range(1,tIdx+1)])
        d = getDivistors(t)
       
    return t
    
def getDivistors(t):
    d=[]
    for i in range (1,int(sqrt(t))+1) :
        if  t%i==0:
            d.append(i)
            if t//i!=i:
                d.append(t//i)
    return 
print(HighlyDivisibleTriangularNumber(500))