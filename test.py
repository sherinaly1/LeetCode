# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 05:11:17 2021

@author: sherin
"""
# st= 'hello'
# st[0]
# print(len(st))
# print (st[2])
# print(st[:2])
# print(st[-2:])
# st2='world'
# print(st+st2)
# print(','.join([st,st2]))

se=['A','C','T','G']
# print(','.join(se))

import random
random.seed(0)
print(random.choice(se))
print(random.choice('AGTC'))

seq=''
for i in range(10):
    seq+=random.choice(se)
    
print(seq)


seq2=''.join(random.choice(se) for _ in range(10))
print(seq2)


def longComPref(s1,s2):
    i=0
    while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
        i+=1
    print(s1[:i])

longComPref('ACCAT', 'ACCATB')

def match(s1,s2):
    if not len(s1) == len(s2):
        return False
    for i in range (len(s1)):
        if not s1[i] ==s2[i]:
            return False
    return True
print(match('AB','Ab'))
print('AB'=='ABm')


def reverseComplement(s):
    complement = {'A':'T', 'C':'G','G':'C','T':'A'}
    t=''
    for i in s:
        t=complement[i]+t
    print(t)
reverseComplement('ACG')