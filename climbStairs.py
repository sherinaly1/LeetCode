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
        #Solution 1: Recursion
        if n ==1 or n==2:
            return n
        return climbStairs(n-1)+climbStairs(n-2)
# print(climbStairs(5))
# print(comb([2,2,1],3))
# print(perm([2,2,1],3))

import itertools
print(list(itertools.permutations([1, 2, 2])))