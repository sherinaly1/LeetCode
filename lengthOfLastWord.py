# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:15:41 2021

Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

@author: sherin
"""
def lengthOfLastWord( s):
        """
        :type s: str
        :rtype: int
        """
        s_ = s.split()        
        return len(s_[-1])
res = lengthOfLastWord("Hello World")
print (res)