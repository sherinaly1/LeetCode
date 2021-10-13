# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:58:57 2021

@author: sherin
"""
#!wget http://d28rh4a8wq0iu5.cloudfront.net/ads1/data/lambda_virus.fa


# def readFile(fn):
#     gn=''
#     with open(fn,'r') as f:
#         for line in f:
#             if not line[0]=='>':
#                 gn+=line.rstrip()
#         return gn
# gn=readFile('lambda_virus.fa')
# print(gn[:10])


# count={'A':0,'T':0,'C':0,'G':0}
# for i in gn:
#     count[i]+=1
# print (count)

# lowercase = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'

# answer =[a+b+c+d for a in lowercase for b in lowercase for c in digits for d in digits ]
# #answer = [lowercase[i:i+2]+digits[j:j+2] for i in range(len(lowercase)-1) for j in range(len(digits)-1)]
# print (answer)


# def findWords(board, words):
#     """
#     :type board: List[List[str]]
#     :type words: List[str]
#     :rtype: List[str]
#     """
#     for w in words:
#         print(w)
#         flag=True
#         for letter in w:
#             if not letter in board:
#                 flag=False
#                 break
#         print(w,flag)
# board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
# words = ["oath","pea","eat","rain"]
# print(len(board[]))
# print (board)
# findWords(board, words)


# class Solution(object):
#     def findWords(self, board, words):
#         """
#         :type board: List[List[str]]
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         List=[]
#         for w in words:
#             if wordExist(w,board):
#                 List.append(w)
#         return List
        
#     def wordExist(w,board):
#         # for each letter search adjacent neighbors for following letter, if exist advance to next letter until end of word and return true otherwise retuen false        
       
#         # for idx in range (len(w)):
#         #     if (adjacent(w(idx),w(idx+1)) and )
#         locList = searchForLetter(w[0],board)
        
#         if (len(locList)==0):            
#             return False # not found
#         else if (len(w)==1):
#             return True # found and exit
        
#         wordFound=False
#         while (len(locList)>0 and wordFound==False):
#             l=locList.pop()
#             letterAdjLoc = getLetterAdjLocFromStartPoint(l[1:])
       
        
#     def getLetterAdjLocFromStartPoint(startPoint,letter,board,visitedLocations):
#         list=[]
#         loc=startPoint
#         i,j=loc[0],loc[1]
#         if (board[i+1][j]==letter and not [i+1,j] in visitedLocations):
#             list.append( [i+1,j])                 
#         if board(loc[i+1][j+1]==letter  and not [i+1,j+1] in visitedLocations):
#             list.append( [i+1,j+1])
#         if board(loc[i][j+1]==letter and not [i,j+1] in visitedLocations):
#              list.append( [i,j+1])
#         if (board(loc[i-1][j+1])==letter and not [i-1,j+1] in visitedLocations):
#             list.append(  [i-1,j+1])
#         if (board(loc[i-1][j])==letter and not [i-1,j] in visitedLocations):
#             list.append(  [i-1,j])
#         if (board(loc[i-1][j-1])==letter and not [i-1,j-1] in visitedLocations):
#             list.append( [i-1,j-1])
#         if (board(loc[i][j-1])==letter and not [i,j-1] in visitedLocations):
#             list.append( [i,j-1])
#         if (board(loc[i+1][j-1])==letter and not [i+1,j-1] in visitedLocations):
#             list.append( [i+1,j-1])            
#         return list
    
    
#     def searchForLetter(letter,board):
#         loc=[]
#         for row in range(len(board)):
#             cols =  [i for i, x in enumerate(a[row]) if x == letter]    

#             if (len(cols)>0):
#                 for c in cols:
#                     loc.append([letter, row,c])
#         # print (loc)
#         return loc
        
#         # index_row = [board.index(row) for row in board if letter in row]
#         # index_column = [row.index(letter) for row in board if letter in row]
  

    
    
#  #Testing
        
#     board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#     words = ["oath","pea","eat","rain"]
    



    
    
    
    
    
    
    