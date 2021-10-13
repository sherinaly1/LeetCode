# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:27:35 2021

@author: sherin
"""
def removeDuplicates( nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for idx in range(1,len(nums)):
            if (nums[idx]==nums[k]):
                idx=+1
            else:
                nums[k+1]=nums[idx]
                k+=1
                idx+=1
        return k+1
nums=[0,0,1,1,1,2,2,3,3,4]
k=removeDuplicates(nums)
print (k,nums)