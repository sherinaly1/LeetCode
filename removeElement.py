# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:10:20 2021

@author: sherin
"""
def removeElement( nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=len(nums)-1
        if (len(nums)==1 and nums[0]==val):            
            return 0
        if (len(nums)==1 and not nums[0]==val):
            return 1
        idx=0
    
        swaped=False
        for idx in range(len(nums)):
            print (idx,k)
            if idx>k:
                return k+1
            if (nums[idx]==val and not idx==k):
                #print(k,nums[k])
                while(nums[k]==val and not k==idx):
                    k-=1
                #print (idx,k)
                if (k==idx):
                    print('jj')
                    return idx
                
                if k<idx and idx==0:
                    return 0
                
                nums[idx]=nums[k]                
                k-=1    
            else:  
                if (k==idx):
                    print('kk')
                    if (nums[idx]==val):
                        return k
                    else:
                        k+1
                        
                
                else:
                    print('swa')
                    swaped=True
                
        if swaped:
            return k+1
        else:
            return 0
#nums=[0,0,5,1,5,2,2,3,3,5]
#nums=[2,5,3,4,5]
nums=[2]
k=removeElement(nums,5)
print (k,nums)