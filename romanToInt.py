# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:55:26 2021

@author: sherin
"""
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1, 'V':5 , 'X': 10, 'L':50 ,'C':100 , 'D':500 , 'M':1000}
        roman=['']
        vald=[s[i] in dic for i in range(len(s))]
        if (len(s)>15 or not s or False in vald):
            return
        i,sum = 0,0
        
        while (i<(len(s)-1)):
               if ((s[i]=='I' and (s[i+1]=='V' or s[i+1]=='X')) or (s[i]=='X' and (s[i+1]=='L' or s[i+1]=='C'))
                    or (s[i]=='C' and (s[i+1]=='D' or s[i+1]=='M'))):
                   sum-=dic[s[i]]
                                    
               else:
                   sum+=dic[s[i]]               
               i+=1
        sum+=dic[s[i]] 
        return sum
print(romanToInt('MCMXCIV'))