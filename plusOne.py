# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:22:58 2021

You are given a large integer represented as an 
integer array digits, where each digits[i] 
is the ith digit of the integer. The digits are
 ordered from most significant to least significant in
 left-to-right order. The large integer does not contain 
 any leading 0's.
 

@author: sherin
"""
def plusOne( digits ):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Solution 1
        # idx=len(digits)-1
        # while idx>-1:
        #     if digits[idx]==9:
        #         digits[idx]=0
        #         idx-=1
        #     else:
        #         digits[idx]=digits[idx]+1
        #         print ("hi")
        #         return digits
        # #print (digits)
        # one=[1]
        # hi=one+digits
        # digits=hi
        # #print (digits)
        # return digits
        
        # Solution 2
        toString = ''
        for i in range(len(digits)):
            toString += str(digits[i])
        t = str(int(toString)+1)
        return[int(i) for i in t]

digits=[9,9,9]        
digits = plusOne(digits)
print(digits)
    
        
            
            