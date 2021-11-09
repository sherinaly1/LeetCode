# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:06:41 2021

@author: sherin
"""
def sumFibEven(maxVal):
    fib=[1,2]
    i=1
    
    while fib[i]+fib[i-1]<=maxVal:
        fib.append(fib[i]+fib[i-1])
        i+=1
    return sum(fib[1::3])
    
print(sumFibEven(4000000))
List = [-999, 'G4G', 1706256, '^_^', 3.1496]
 
# Show original list
print("\nOriginal List:\n", List)
 
print("\nSliced Lists: ")
 
# Display sliced list
print(List[10::2])
 
# Display sliced list
print(List[1:1:1])
 
# Display sliced list
print(List[-1:-1:-1])
 
# Display sliced list
print(List[:0:])
    