# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 19:45:41 2021

@author: sherin
"""
def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        # Solution 1 (Brute Force)
        # for i in range(x+1):            
        #     y=i*i            
        #     if y==x:
        #         return i
        #     if y>x:
        #         return i-1
        low=0
        high=x
        middle=(low+high)//2
        #print(low,middle,high)
        while (middle<high and middle>low):
            sqr=middle*middle
            if (sqr==x):
                return int(middle)
            if sqr>x:
                high=middle
            else:
                low=middle
            middle=(low+high)//2
            
        if x<high*high:
            return int(low)
        else:
            return int(high)
        
#print(5 // 3)   
print(mySqrt(4))