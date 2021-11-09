# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 05:16:10 2021

Given an array of integers nums and an integer target,
 return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
 and you may not use the same element twice.

You can return the answer in any order.
This solution Runtime: 572 ms, faster than 48.14% of 
Python online submissions for Two Sum.
@author: sherin
"""
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            nw=target-nums[i]
            if nw in nums[i+1:]:
                return [i,i+nums[i+1:].index(nw)+1]
            
            # if target>=nums[i] and target>=0 and nums[i]>=0:
            #     if target-nums[i] in nums[i+1:]:
            #         return [i,nums[i+1:].index(target-nums[i])+i+1]
            # elif target<nums[i]  and target>=0 and nums[i]>=0:
            #     if nums[i]-target in nums[i+1:]:
            #         return [i,nums[i+1:].index(nums[i]-target)+i+1]
            # elif target<nums[i] and target<0 and nums[i]<0:
            #     return [i,nums[i+1:].index(target-nums[i])+i+1]
            # else:
            #     return [i,nums[i+1:].index(nums[i]-target)+i+1]
#print(twoSum([-3,4,3,90],0))
print([1,0]^[1,1])
