# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:59:03 2021

@author: sherin
"""
import math
def isPrime(N):
    if N<=1:
        return False
    elif N==2:
        return True
    elif N%2==0:
        return False
    for i in range(3, int(math.sqrt(N)) + 1, 2):
        if N % i == 0:
            return False     
    return True

def findPrimesLessThanOrEqualN(n):
    primes= []
    for i in range(n+1):
        if isPrime(i):            
            primes.append(i)
    return primes

# def getFactors(n):
#     p = findPrimesLessThanOrEqualN(n)
#     for i in range(len(p)):
        
    
    
def findMinDiv(n):
    keys = findPrimesLessThanOrEqualN(n)
    primesDic=dict.fromkeys(keys,0)
    
    for i in range(2,n+1):
        idx=0
        print (i,' ', keys[idx])
        while (idx<len(keys) and i>=keys[idx] ): 
            #print (i,' ', keys[idx])
            tmp = i
            cnt = 0
            while (tmp % keys[idx] == 0 and tmp!= 1):
                #print (i, ' ', tmp,' ', keys[idx])
                tmp = tmp // keys[idx]
                print (tmp)
                cnt+=1
            #print(cnt,' ', primesDic[keys[idx]])
            if cnt>primesDic[keys[idx]]:
                primesDic[keys[idx]]=cnt
            idx+=1
    print(primesDic)
    
    val = [k**primesDic[k] for k in keys]
    print (val)
    return math.prod(val)
            
print(findMinDiv(20)    )
#primesDic=dict.fromkeys(findPrimesLessThanOrEqualN(20),0)
#primesDic[2] =1
#print(primesDic)
#print(findMinDiv(20))
#print(findPrimesLessThanOrEqualN(20))