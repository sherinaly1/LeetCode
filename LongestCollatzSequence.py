# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:24:43 2021

@author: sherin
"""
def LongestCollatzSequenceUnder1M():
    start = 1
    largest = 1
    for i in range(1,1000000):
        chL = LengthOfhain(i)
        if chL > largest:
            largest = chL
            start = i    
    return start

def LengthOfhain(n):
    seq = []
    while n!= 1:
        if n%2==0:
            n= n//2
        else:
            n = 3*n +1
        seq.append(n)
    seq.append(1)
    return len(seq)
print(LongestCollatzSequenceUnder1M())