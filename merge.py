# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 07:05:07 2021

Merge Sorted Array

@author: sherin
"""
def merge( nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums2 and n==0:
            return nums1
        if m==0 and n>0:
            nums1 = nums2
            return nums1
        # tmp=[]        
        # i,j=0,0
        # while i<m and j<n:
        #     if nums1[i]<nums2[j]:
        #         tmp.append(nums1[i])
        #         i+=1
                
        #     else:
        #         tmp.append (nums2[j])
        #         j+=1
                
        # if i==m and j<n:
        #     tmp += nums2[j:]
        # elif j==n and i<m:
        #      tmp += nums1[i:]
        # nums1=tmp
        # return nums1
        
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[n+m-1]=nums1[m-1]
                m-=1
            else:
                nums1[n+m-1]=nums2[n-1]
                n-=1
        if n>0:
            nums1[:n]=nums2[:n]
            
        return nums1
    
    
    
print(merge([2,3,4,0,0,0],3,[0,1,6],3))