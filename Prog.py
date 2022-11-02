import time 
import copy
# https://www.w3schools.com/python/ref_func_print.asp
# https://www.geeksforgeeks.org/python-string-split/
# https://www.programiz.com/python-programming/time
# https://docs.python.org/3/library/time.htm
# https://docs.python.org/3/tutorial/classes.html
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/

class Node:
    def __init__(self, depth, board):
        self.depth = depth
        self.board = board
        self.cost = 0
        self.childU = None
        self.childD = None
        self.childL = None
        self.childR = None#branching factor of 4

def main():
    prob = boardDecision()
    searchDecision(prob)

goalState = [[1,2,3], [4,5,6], [7,8,0]]
#board = [[], [], []]


def printBoard(board):
    for i in range(0,3):

        for j in range(0,3):
            
            print(board[i][j], end = ' ')

        print('\n')

#gets the different ways that the blank can move
def getChilds(Node1):
    for i in range(0,3):

        for j in range(0,3):
           # print(i)
           # print(j)
            #print(Node.board[i][j])
            if Node1.board[i][j] == "0":
                #print("hi5")
                #print(j)
                if i > 0:
                    childBoard = copy.deepcopy(Node1.board)
                    childBoard[i][j] = childBoard[i-1][j]
                    childBoard[i-1][j] = Node1.board[i][j]
                    Node1.childU =  Node(Node1.depth+1, childBoard)
            
                if i < 2:
                    childBoard = copy.deepcopy(Node1.board)
                    childBoard[i][j] = childBoard[i+1][j]
                    childBoard[i+1][j] = Node1.board[i][j]
                    Node1.childD =  Node(Node1.depth+1, childBoard)
                if j < 2:
                    childBoard = copy.deepcopy(Node1.board)
                    childBoard[i][j] = childBoard[i][j+1]
                    childBoard[i][j+1] = Node1.board[i][j]
                    Node1.childR =  Node(Node1.depth+1, childBoard)
                if j > 0:
                    childBoard = copy.deepcopy(Node1.board)
                    childBoard[i][j] = childBoard[i][j-1]
                    childBoard[i][j-1] = Node1.board[i][j]
                    Node1.childL =  Node(Node1.depth+1, childBoard)






def boardDecision():
    Pass = False
    while Pass == False:
        choice = input(" choose '0' to create your own board or choose one of the 8 other board u want to solve (1-8): ")
        if len(choice) == 1 and '0' <= choice <= '8':
            if choice == '0':
                Row1 = input("Enter row 1 with commas in between each number: ")

                Row2 = input("Enter row 2 with commas in between each number: ")

                Row3 = input("Enter row 3 with cpmmas in between each number: ")

                Row1 = (Row1.split(','))

                Row2 = (Row2.split(','))

                Row3 = (Row3.split(','))

                board = [Row1, Row2, Row3] 

            elif choice == '1':#depth 0
                board = [['1','2','3'],['4','5','6'],['7','8','0']] 

            elif choice == '2':#depth 2
                board = [['1','2','3'],['4','5','6'],['0','7','8']] 

            elif choice == '3':#depth 4
                board = [['1','2','3'],['5','0','6'],['4','7','8']] 

            elif choice == '4':#depth 8
                board = [['1','3','6'],['5','0','2'],['4','7','8']] 

            elif choice == '5':#depth 12
                board = [['1','3','6'],['5','0','7'],['4','8','2']] 

            elif choice == '6':#depth 16
                board = [['1','6','7'],['5','0','3'],['4','8','2']] 

            elif choice == '7':#depth 20
                board = [['7','1','2'],['4','8','5'],['6','3','0']] 

            elif choice == '8':#depth 24
                board = [['0','7','2'],['4','6','1'],['3','5','8']] 

            Pass = True

            
            
        else:        
            print("Error invalid input. Please try again")
    return board
