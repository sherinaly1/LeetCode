# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 05:51:44 2021

@author: sherin
"""
def maxProduct(nums):
    res = max(nums)
    currMax= 1
    currMin=1
    
    for n in nums:
        if n==0:
            currMax=1
            currMin=1
            continue
        tmp = currMax
        currMax= max(n*currMax, n*currMin,n)  
        currMin = min(tmp*n, n, currMin*n)
        res=max(res,currMax)
       
        print(currMax,currMin)
    return res


print(maxProduct([-1,-2,-3,0,7]))
            
            
