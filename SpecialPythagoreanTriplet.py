# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 06:59:25 2021

@author: sherin
"""
import math
def SpecialPythagoreanTriplet():
    a=b=1
    c = math.sqrt(a**2+b**2)
    while a+b+c<=3000:          
        if a==998:
            b+=1
            a=1
            c=math.sqrt(a**2+b**2)
        #print (a,' ',b,' ',c)
        p,c =isPythagorean(a,b)
        #print(c)
        if ((a+b)+c)==1000 and isPythagorean(a,b,c):                
            return (a*b)*c
        a+=1
    return 0
        
def isPythagorean(a,b,c = 1):
    c=math.sqrt(a**2+b**2)
    if c == int(c) :
        return True,int(c)
    else:
        
        return False,c
#print(isPythagorean(2,4))
print(SpecialPythagoreanTriplet())
    