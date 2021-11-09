# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 09:48:18 2021

@author: sherin
"""
def cellCompete(states, days):
    # WRITE YOUR CODE HERE
    newSt = [0]+states+[0]
    for d in range(days):
        
        tmp = [newSt[i-1]^newSt[i+1] for i in range(1,len(newSt)-1)]
        newSt = [0]+tmp+[0]

    return newSt[1:-1]
print (cellCompete([1, 1, 1, 0, 1, 1, 1, 1],2))
        
        