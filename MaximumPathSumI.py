# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:46:23 2021

@author: sherin
"""
import sys
def MaximumPathSumI():
    for i in reversed(range(len(triangle)-1)):
        for j in range(len(triangle[i])):
            #print(i,' ', j, ' ', (triangle[i+1][j],triangle[i+1][j+1]))        
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]
   
    # i =j = 0
    # n = triangle[i][j]
    # summ = n
    # newJ =j
    # for i in range(len(triangle)-1):
    #     if triangle[i+1][newJ]>=triangle[i+1][newJ+1]:
    #         print(triangle[i+1][newJ])
    #         summ += triangle[i+1][newJ]
            
    #     else:
    #         print(triangle[i+1][newJ+1])
    #         summ+=triangle[i+1][newJ+1]
    #         newJ=newJ+1
    # return summ

# def compute():
# 	for i in reversed(range(len(triangle)-1)):
#         for j in range(len(triangle[i])):            
#             triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1])
#     return str(triangle[0][0])


t =[[3],
[7, 4],
[2, 4 ,6],
[8, 5 ,9, 3  ]]     
    
triangle =[
[75],
[95, 64],
[17, 47 ,82],
[18, 35 ,87, 10],
[20, 4 ,82, 47, 65],
[19, 1 ,23, 75, 3, 34],
[88, 2 ,77, 73, 7, 63, 67],
[99, 65 ,4, 28, 6, 16, 70, 92],
[41, 41 ,26, 56, 83, 40, 80, 70 ,33],
[41, 48 ,72, 33, 47, 32, 37, 16 ,94, 29],
[53, 71 ,44, 65, 25, 43, 91, 52 ,97, 51, 14],
[70, 11 ,33, 28, 77, 73, 17, 78 ,39, 68, 17, 57],
[91, 71 ,52, 38, 17, 14, 91, 43 ,58, 50, 27, 29, 48],
[63, 66 ,4, 68, 89, 53, 67, 30 ,73, 16, 69, 87, 40, 31],
[4, 62 ,98, 27, 23, 9, 70, 98 ,73, 93, 38, 53, 60, 4, 23]]

# print(compute())

print(MaximumPathSumI())