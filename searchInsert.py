# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:07:02 2021

@author: sherin
"""
def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx=0
        while(not idx==len(nums) and nums[idx]<target ):
            idx+=1
        # if idx==len(nums)-1:
        #     return idx-1
        return idx