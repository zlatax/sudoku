import numpy as np
import pandas as pd
import sys

class Sudoku():
    def __init__(self, problem, count):
        
        self.board = pd.DataFrame(np.reshape([int(char) for char in problem],(9,9)))
        
        self.count=0
        self.countmax = count
    
    def isComplete(self, remainDict):
        for value in remainDict.values():
            if sum(value) > 0:
                return False
        return True
    
    def run(self):
        try:
            if self.count == self.countmax:
                self.printBoard()
                sys.exit(0)
            
            remain = self.getRemaining()
            if(self.isComplete(remain)):
                self.printBoard()
                sys.exit(0)
            else:
                self.updateBoard(self.getRemaining())
                self.count +=1;
                self.run()
                
        except KeyboardInterrupt:
            print("Program Interrupted!")
        
    
    def getRemaining(self):
        remain = dict()
        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                if self.board.loc[col,row] != 0: remain["{}{}".format(row,col)] = [0]
                else:
                    remain["{}{}".format(row,col)] = [x for x in range(1,10) 
                                                  if x not in (y for y in self.board.loc[:,row]) and 
                                                  x not in(z for z in self.board.loc[col,:])]
        return remain
    
    def updateBoard(self, remain):
        for key in remain.keys():
            if len(remain[key]) == 1 and remain[key][0] != 0:
                self.board.loc[int(key[1]),int(key[0])] = remain[key][0]
    
    def printBoard(self):
        print(self.board.to_string(index=False))

if __name__ == "__main__":
    with open("../res/problem1.txt",'r') as f:
        problem = f.read()
        
    game = Sudoku(problem)
    game.run()