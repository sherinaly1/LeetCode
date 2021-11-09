# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:28:52 2021

@author: sherin
"""
import math
def largestPrimeFactor(N):
    primes=[]
    while N%2==0:
        primes.append(2)
        N=N/2
    for i in range(3,int(math.sqrt(N))+1,2):
        while N%i==0:
            primes.append(i)
            N=N/i
    if N>2:
        primes.append(N)
    return max(primes)

        
        
        
    # mx=0
    # if N<41:
    #     for n in range(N):
    #         l=6*n-1
    #         h=6*n+1
    #         if l<=N and l%2>0 and l%3>0 and l%5>0 and l%7>0 and l%11>0:
    #             mx=l
    #             print (mx)
            
    #         l=6*n+1
    #         if l<=N and l%2>0 and l%3>0 and l%5>0 and l%7>0 and l%11>0:
    #             mx=l
    #             print (mx)
    # else:
    #     for n in range(39):
            
    #         if 2*n  + n + 41 <=N:
    #             mx=3*n  + 41
    #             print(mx,' ',N)
    # return mx
            
print (largestPrimeFactor(600851475143))  
#print (largestPrimeFactor(600851475143))
