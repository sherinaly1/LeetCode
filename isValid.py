# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:51:00 2021

@author: sherin
"""
def isValid( s: str) -> bool:
        if (len(s)<2 or len(s)>10000):
            return False
        #validLetters='()[]{}'
        dic={'(':')','[':']','{':'}'}
        
        s2=[]
        
        for l in s:
            # print(l)
            if (l in dic):
                # print('pushing ',l)
                s2.append(l) # push
            else:
                if (len(s2)==0):
                    # print('false bec len s2 is 0')
                    return False
                tmp=s2.pop()
                # print ('popping ',tmp)
                if (not dic[tmp]==l):
                    # print('false tmp ==l')
                    return False
        
        if (len(s2)==0):
            return True
        else:
            return False
        

print(isValid("(([]"))