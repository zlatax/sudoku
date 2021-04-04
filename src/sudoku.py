import numpy as np
import pandas as pd
import sys

class Sudoku():
    def __init__(self, problem):
        
        self.board = pd.DataFrame(np.reshape([int(char) for char in problem],(9,9)))
        
        self.count=0;
    
    def isComplete(self, remainDict):
        if sum((sum(x) for x in remainDict.values()))==0:
            return True
        return False
    
    def run(self):
        self.printBoard()
        remain = self.getRemaining()
        print(remain)
        if(self.isComplete(remain)):
            self.printBoard()
            sys.exit(0)
        else:
            self.updateBoard(self.getRemaining())
            self.run()
        
    
    def getRemaining(self):
        remain = dict()
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                if self.board.loc[row,col] != 0: remain["{}{}".format(row,col)] = 0
                else:
                    remain["{}{}".format(col,row)] = [x for x in range(1,10) 
                                                  if x not in (y for y in self.board.loc[:,row]) and 
                                                  x not in(z for z in self.board.loc[col,:])]
        return remain
    
    def updateBoard(self, remain):
        for key in remain.keys:
            if remain[key]!=0 and len(remain[key]) == 1:
                self.board.loc[key[0],key[1]] = remain[key][0]
    
    def printBoard(self):
        print(self.board.to_string(index=False))

if __name__ == "__main__":
    with open("../res/problem1.txt",'r') as f:
        problem = f.read()
        
    game = Sudoku(problem)
    game.run()