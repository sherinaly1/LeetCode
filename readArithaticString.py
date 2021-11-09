# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:33:27 2021

@author: sherin
"""

def readArithaticString(str):  
    operationQ = []
    numbersList= []
    number=''
    i =0
    for i in range(len(str)):  
        if i==0:
            if str[i]=='-' or not str[i] in ['+','*']:
                number+=str[i]
            else : 
                numbersList.append(int(number))  
                operationQ.append(str[i])
                number =''               
                          
        else:
            if (str[i] == '-' and str[i-1] in ['+','-','*']) or (not str[i] in ['+','-','*']):
                number+=str[i]                            
                
            elif str[i] in ['+','-','*']: 
                numbersList.append(int(number))  
                operationQ.append(str[i])
                number =''               
            
    
   
    numbersList.append(int(number))
    
    operationQ = list(reversed(operationQ)) 
    numbersList = list(reversed(numbersList))
    
    #print(operationQ )   
    #print(numbersList)
    allQ =[]
    
    allQ.append(numbersList.pop())
    while len(operationQ)>0:  
        
        op = operationQ.pop()
        #print(op)
        if op != '*':       
            allQ.append(op)
            allQ.append(numbersList.pop())
        
        if op == '*':
            left = int(allQ.pop())
            right = int(numbersList.pop())
            m = left*right
            allQ.append(m)
            
    
    #print(allQ)
    n = int(allQ[0])

    i = 1
    while i<len(allQ):
        op = allQ[i]
        i+=1
        if op=='+':
            n = n+ int(allQ[i])
           
        else:
            n = n - int(allQ[i])
        i+=1
    return(n)


str = "1--1"
print(readArithaticString(str))