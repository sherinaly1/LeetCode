# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:16:05 2021

@author: sherin
"""
def mergeTwoLists( l1, l2) :
        newList=[]
        if (len(l1)==0 and len(l2)):
            return newList
        if len(l1)==0 :
            return l2
        if len(l2)==0 :
            return l1
        i,j=0,0
        while (i<len(l1) and j<len(l2)):
            if (l1[i]<l2[j]):
                newList.append(l1[i])
                i+=1
            else:
                newList.append(l2[j])
                j+=1    
        while (j<len(l2)):
            newList.append(l2[j])
            j+=1
        while (i<len(l1)):
            newList.append(l1[i])
            i+=1
        return newList

l1=[1,2,3]
l2= [1,3,5]
l3 = mergeTwoLists( l1, l2)
print (l3)