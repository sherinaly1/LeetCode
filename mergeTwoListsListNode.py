# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:16:30 2021

@author: sherin
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr=ListNode()
        newList=ptr
        if (not l1 and not l2):
            return newList
        if not l1 :
            return l2
        if not l2 :
            return l1
        # if (l1.val<l2.val):                
        #     newList.val=l1.val
        #     l1=l1.next      
        # else:
        #     newList.val=l2.val
        #     l2=l2.next  
        
        while (l1 and l2):            
            if (l1.val<l2.val): 
                tmp=ListNode(l1.val)                
                l1=l1.next
                newList.next=tmp
                newList=newList.next
                
            else:
                tmp=ListNode(l2.val)                
                l2=l2.next
                newList.next=tmp
                newList.next
        
        while (l2):
            newList.val=l2.val
            l2=l2.next
            newList.next=ListNode()
            newList=newList.next
            
        while (l1):
            newList.val=l1.val
            l1=l1.next
            newList.next=ListNode()
            newList=newList.next
        return ptr