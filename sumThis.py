# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:35:43 2021

@author: sherin
"""
def sumThis(x,p):
    return sum([int(c) for c in str(x**p)])
    #return sum(list(map(int,list(str(x**p)))))


print(sumThis(2,1000))