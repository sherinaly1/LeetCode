# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 09:21:44 2021

@author: sherin
"""
from scipy.special import comb,perm
def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """
        #Solution 1 : Recursion
        # if n==0: 
        #     return 1
        # if n ==1 or n==2:
        #     return n
        # return climbStairs(n-1)+climbStairs(n-2)
        # Solution 2: Sliding Window
        # temp = 0
        # res = [1]
     
        # Solution 2 : Sliding window
        # for i in range(1, n + 1):
        #     s = i - 3
        #     e = i - 1
        #     if (s >= 0):
        #         temp -= res[s]
        #     temp += res[e]
        #     res.append(temp)
        # print(res)
        # return res[n] 
        
        # Solution 3 : Dictionaries and sliding wndows The fastest
        mem={0:1,1:1}
        
        for i in range(2,n+1):
            mem[i]=mem[i-1]+mem[i-2]
        return mem[n]
        
print(climbStairs(5))
