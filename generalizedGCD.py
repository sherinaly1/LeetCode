# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 10:13:01 2021

@author: sherin
"""
def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    minn = min(arr)
    #print (minn)
    if minn ==0 or minn ==1:
        return minn
    for i in range(minn,0,-1):
        tmp = [(arr[j]%i)>0 for j in range(num)]
       # print (tmp)
        if not True in tmp:
            return i
    
print(generalizedGCD(5,[2,8,5,72,10]))