# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 06:59:14 2021

@author: sherin
"""
def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (not needle and not haystack):
            return 0
        if not needle:
            return 0
        if not haystack:
            return -1
        return haystack.find(needle)