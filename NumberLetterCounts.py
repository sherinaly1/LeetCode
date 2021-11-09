# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 15:59:02 2021

@author: sherin
"""
def getLength(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    twos =["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n<20:
        s= ones[n]
    elif n<=99:
        s = twos[n//10] + (ones[n%10] if n%10!= 0 else "")
    elif n<=999:        
        s= ones[n//100] + ("hundred" if ((n%100)//10 == 0 and n%10 ==0) else "hundredand"+ getLength(n%100))
    else:
        s= "onethousand"
    return s

print(sum([len(getLength(i)) for i in range(1,1001)]))
