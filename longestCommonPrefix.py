# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 12:18:36 2021
Find Longest Common Prefix amongst an array of strings.
@author: sherin
"""
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs)>200 or len(strs[0])==0):
            return ""
        if (len(strs)==1):
            return strs[0]
        
      
        AllStrPref=findPref2(strs[0],strs[1])
        if not AllStrPref:
            return ""
        for i in range(len(strs)-1):
            for j in range(i+1,len(strs)):
                pref=findPref2(strs[i],strs[j])
                AllStrPref=findPref2(pref,AllStrPref)
                if not AllStrPref:
                    return ""
        return AllStrPref
                
def findPref2(s1,s2):
    i=0
    while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
        i+=1
    return s1[:i]

print(longestCommonPrefix( ["dog"]))
