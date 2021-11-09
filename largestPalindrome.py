# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:27:42 2021

@author: sherin
"""
def largestPalindrome():
    mx=0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            prod=i*j
            if prod>mx and isPalindrome(prod):
                mx=prod
    return mx
        
    pass
def isPalindrome(n):
    s=str(n)    
    #print(s[:len(s)//2], ' ' ,s[-1:-(len(s)//2)-1:-1])
    if s[:len(s)//2]==s[-1:-(len(s)//2)-1:-1]:
        return True
    else:
        return False
#print(isPalindrome(9009))
print(largestPalindrome())
    