from src import sudoku
import sys

def main():
    with open("res/problem1.txt",'r') as f:
        problem = f.read()
        
    game = sudoku.Sudoku(problem, int(sys.argv[1]))
    game.run()

if __name__ == "__main__":
    main()
    