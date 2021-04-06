import numpy as np
import pandas as pd
import sys

class Sudoku():
    def __init__(self, problem):
        self.problem = problem
        self.board = pd.DataFrame(np.reshape([int(char) for char in problem],(9,9)))
        
#         self.lastSearch = None
#         self.prevCells = dict()
        
        self.count=0

    
#     def isComplete(self, remainDict):
#         for value in remainDict.values():
#             if sum(value) > 0:
#                 return False
#         return True
    
    def getSquare(self,num):
        if num in range(3): return range(3)
        elif num in range(3,6): return range(3,6)
        else: return range(6,9)

    def isinSquare(self,num,row,col):
        if (self.board.loc[self.getSquare(row),self.getSquare(col)] == num).any().any() == True:
            return True
        else: return False
        
    def isValid(self,num,row,col):
        if (self.board.loc[:,col]==num).any():
            return False
        elif (self.board.loc[row,:]==num).any():
            return False
        elif self.isinSquare(num,row,col):
            return False
        return True

    def nextPos(self,pos=None):
        if pos is None:
            row = col = 0
        elif pos[1] == self.board.shape[1]:
            row = pos[0]+1
            col = 0
        elif pos == (self.board.shape[0]+1, self.board.shape[1]+1):
            return None
        else:
            row = pos[0]
            col = pos[1]+1
    
        for r in range(row,self.board.shape[0]):
            for c in range(col, self.board.shape[1]):
                if self.board.loc[r,c] == 0:
                    return r,c
            col = 0
        return None

#     def prevPos(self):
#         pass
#         if self.lastSearch is None or self.lastSearch == (0,0):
#             print("is none")
#             return None
#         elif self.lastSearch[1] == 0:
#             print("is beginning")
#             row = self.lastSearch[0]-1
#             col = self.board.shape[1]
#         else:
#             row = self.lastSearch[0]
#             col = self.lastSearch[1]-1
#             print("normal {} {}".format(row,col))
        
        
#         for r in range(row,-1,-1):
#             for c in range(col,-1,-1):
#                 if self.board.loc[r,c] == 0:
#                     return (r,c)
#             col =self.board.shape[1]
#         return None

    def findValid(self,pos,startnum=1):
        if pos==None:
            return True
        row = pos[0]
        col = pos[1]
        for i in range(startnum,10):
            self.count+=1
            if self.isValid(i, row,col):
                self.board.loc[row,col] = i
#                 print("change {},{} to: {}".format(row,col,i))
                if self.findValid(self.nextPos(pos)):
                    return True
                self.board.loc[row,col] = 0
        return False
    
    def run(self):
        self.findValid(self.nextPos())
        
#        for row in range(9):
#             prevcol = 0
#             for col in range(9):
#                 if self.board.loc[col,row] == 0:
#                     for i in range(1,10):
#                         self.count+=1
#                         if self.isValid(i, row,col):
#                             self.board.loc[col,row] = i
#                             break
#                     if self.board.loc[col,row] == 0:
#                     prevcol = col
        
        
        
#         try:
#             if self.count == self.countmax:
#                 self.printBoard()
#                 sys.exit(0)
            
#             remain = self.getRemaining()
#             if(self.isComplete(remain)):
#                 self.printBoard()
#                 sys.exit(0)
#             else:
#                 self.updateBoard(self.getRemaining())
#                 self.count +=1;
#                 self.run()
                
#         except KeyboardInterrupt:
#             print("Program Interrupted!")
        
    
#     def getRemaining(self):
#         remain = dict()
#         for row in range(self.board.shape[0]):
#             for col in range(self.board.shape[1]):
#                 if self.board.loc[col,row] != 0: remain["{}{}".format(row,col)] = [0]
#                 else:
#                     remain["{}{}".format(row,col)] = [x for x in range(1,10) 
#                                                   if x not in (y for y in self.board.loc[:,row]) and 
#                                                   x not in(z for z in self.board.loc[col,:])]
#         return remain
    
#     def updateBoard(self, remain):
#         pass
#         for key in remain.keys():
#             if len(remain[key]) == 1 and remain[key][0] != 0:
#                 self.board.loc[int(key[1]),int(key[0])] = remain[key][0]
    
        
    def printSudoku(self):
        print("-"*25)
        count=0
        rowcount=0
        for nums in self.board.values:
            for num in nums:
                count+=1
                if num == 0:
                        num = " "
                if count < 9 and count%3 ==1:
                    print("| {} ".format(num),end="")
                elif count==9:
                    print("{} |".format(num))
                    count=0
                    rowcount+=1
                    if rowcount == 3:
                        print("-"*25)
                        rowcount=0
                else:
                    print("{} ".format(num),end="")
            
            

if __name__ == "__main__":
    with open("../res/problem1.txt",'r') as f:
        problems = f.read().splitlines()

    for problem in problems:
        game = Sudoku(problem)
        print("START")
        game.printSudoku()
        game.run()
        print("END")
        game.printSudoku()