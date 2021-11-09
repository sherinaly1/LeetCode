# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 08:44:10 2021

@author: sherin
"""

def findMedianSortedArrays( nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import heapq
        import numpy as np
        return np.median(np.array(list(heapq.merge(nums1, nums2))))
        
print(findMedianSortedArrays([1,3],[2]))