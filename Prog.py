import time 
import copy
# https://www.w3schools.com/python/ref_func_print.asp
# https://www.geeksforgeeks.org/python-string-split/
# https://www.programiz.com/python-programming/time
# https://docs.python.org/3/library/time.htm
# https://docs.python.org/3/tutorial/classes.html
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
#https://www.geeksforgeeks.org/priority-queue-in-python/


class Node:
    def __init__(self, depth, board):
        self.depth = depth
        self.board = board
        self.cost = 0
        self.heuristic = 0
        self.childU = None
        self.childD = None
        self.childL = None
        self.childR = None#branching factor of 4

def main():
    prob = boardDecision()
    searchDecision(prob)

goalState = [['1','2','3'], ['4','5','6'], ['7','8','0']]
#board = [[], [], []]

#print board function
def printBoard(board):
    for i in range(len(board)):

        for j in range(len(board)):
            
            print(board[i][j], end = ' ')

        print('\n')

#gets the different ways that the blank can move
def getChilds(Node1):
    for i in range(len(Node1.board)):

        for j in range(len(Node1.board)):
           # print(i)
           # print(j)
            #print(Node.board[i][j])
            if Node1.board[i][j] == "0":
                #print("hi5")
                #print(j)
                if i > 0:#checks if a child in able to be create in each direction and if so it creates a copy of the current node and uses it to make a child
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






def boardDecision():#decision to choose what type of board you create
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






def searchDecision(board):#chooses what type of search function you want to run on your board
    choice2 = input('Which search would you like to implement? Options: Uniform Cost Search, Misplaced Tile Search, Manhatten Distance Search (1,2,3) ')
    
    
    while len(choice2) != 1 or '1' > choice2 > '3':#error checing
        print('Try again')
        choice2 = input('Which search would you like to implement? Options: Uniform Cost Search, Misplaced Tile Search, Manhatten Distance Search (1,2,3) ')
    

    if choice2 == '1':
        print('Uniform Cost Search chosen')
        UniformCostSearch(board, goalState, choice2)
        
    elif choice2 == '2':
        print('Misplaced Tile Search chosen')
        
        UniformCostSearch(board, goalState, choice2)
        

    elif choice2 == '3':
        print('Manhatten Distance Search chosen')
        UniformCostSearch(board, goalState, choice2)
        
       
    


def UniformCostSearch(board,goalState, choice2):
#Breadth First Search - A* g(n) + h(n) where h(n) = 0
    #lowest = 100
    startTime = time.time()

   
    maxQSize = 0
    NumNodesExpanded = 0
    queue = []
    start = Node(0, board)
    #print("hi3")
    queue.append(start)
    if choice2 == "2":
        start.heuristic = MisTileSearch(start.board, goalState)
        start.cost = start.depth + start.heuristic
        
    elif choice2 == "3":
        start.heuristic = ManhattenDistSearch(start.board,goalState)
        start.cost = start.depth + start.heuristic
    
    done = []
    
    #for k in range(0,35):
    while len(queue) > 0 :
        MisChild1= 100
        MisChild2= 100
        MisChild3= 100
        MisChild4= 100
        lowestChild = 0
        lowest = 100
        
        minCostChild = 0
        for e in range (len(queue)):#prioity queue where the lowest cost nodes get popped first
            if queue[e].cost < queue[minCostChild].cost:
                minCostChild = e
        i = queue.pop(minCostChild)
        print("The best state to expand with a g(n) =" + str(i.depth) + "and h(n) =" + str(i.heuristic))
        NumNodesExpanded+=1
        

        #print("hi2")
        printBoard(i.board)
        if i.board == goalState:#output once goal state is achieved
            
            print("\n")
            printBoard(i.board)
            print("Time elapsed : " + str(f'{(time.time()- startTime):.2f}'))#gets the time elapsed
            print ("goal State!")
            print ("solution depth was: " + str(i.depth))
            print ("Number of Nodes expanded: " + str(NumNodesExpanded) )
            print ("Max queue size was: " + str(maxQSize))
            return
       
        getChilds(i)
        

        if done == []:#runs if it is the first node and there is no chance of a duplicate node
            if i.childU != None:
                if choice2 =="1":
                    #print("hi4")
                    i.childU.cost = i.childU.depth 
                    queue.append(i.childU)
                    #NumNodesExpanded+=1
                elif choice2 == "2":
                    #print("mis3")
                    i.childU.heuristic  = MisTileSearch(i.childU.board, goalState)
                    i.childU.cost = i.childU.depth + i.childU.heuristic
                    queue.append(i.childU)
                elif choice2 == "3":
                    i.childU.heuristic  = ManhattenDistSearch(i.childU.board, goalState)
                    i.childU.cost = i.childU.depth + i.childU.heuristic
                    queue.append(i.childU)
            if i.childD != None:
                if choice2 =="1":
                    i.childD.cost = i.childD.depth 
                    queue.append(i.childD)
                    #NumNodesExpanded+=1
                elif choice2 == "2":
                    i.childD.heuristic = MisTileSearch(i.childD.board, goalState)
                    i.childD.cost = i.childD.depth + i.childD.heuristic
                    queue.append(i.childD)
                elif choice2 == "3":
                    i.childD.heuristic  = ManhattenDistSearch(i.childD.board, goalState)
                    i.childD.cost = i.childD.depth + i.childD.heuristic
                    queue.append(i.childD)
            if i.childR != None:
                #print("mis4")
                if choice2 =="1":
                    i.childR.cost = i.childR.depth 
                    queue.append(i.childR)
                    #NumNodesExpanded+=1
                elif choice2 == "2":
                    i.childR.heuristic  = MisTileSearch(i.childR.board, goalState)
                    i.childR.cost = i.childR.depth + i.childR.heuristic
                    queue.append(i.childR)
                elif choice2 == "3":
                    i.childR.heuristic  = ManhattenDistSearch(i.childR.board, goalState)
                    i.childR.cost = i.childR.depth + i.childR.heuristic
                    queue.append(i.childR)
            if i.childL != None:
                if choice2 =="1":
                    i.childL.cost = i.childL.depth 
                    queue.append(i.childL)
                    #NumNodesExpanded+=1
                elif choice2 == "2":
                    i.childL.heuristic =  MisTileSearch(i.childL.board, goalState)
                    i.childL.cost = i.childL.depth + i.childL.heuristic
                    queue.append(i.childL)
                elif choice2 == "3":
                    i.childL.heuristic  = ManhattenDistSearch(i.childL.board, goalState)
                    i.childL.cost = i.childL.depth + i.childL.heuristic
                    queue.append(i.childL)

        else:
            #print(done)
            #checks for duplicate nodes in the done array
            dupU = False
            dupD = False
            dupR = False
            dupL = False
            for j in done :
                if i.childU != None and j.board == i.childU.board:
                    dupU = True
                if i.childD != None and j.board == i.childD.board:
                    dupD = True
                if i.childR != None and j.board == i.childR.board:
                    dupR = True
                if i.childL != None and j.board == i.childL.board:
                    dupL = True
            if i.childU != None and dupU == False :#if up child was created it runs it through the search chosen above
                #print("hi6")
                if choice2 =="1":
                    #print("hi7")
                    i.childU.cost = i.childU.depth
                    queue.append(i.childU)
                    #NumNodesExpanded+=1
                elif choice2 == "2":#misplaced
                    i.childU.heuristic  = MisTileSearch(i.childU.board, goalState)
                    i.childU.cost = i.childU.depth + i.childU.heuristic
                    queue.append(i.childU)
                elif choice2 == "3":#Manhatan distance 
                    i.childU.heuristic  = ManhattenDistSearch(i.childU.board, goalState)
                    i.childU.cost = i.childU.depth + i.childU.heuristic
                    queue.append(i.childU)
                
            if i.childD != None and dupD == False:#if down child was created it runs it through the search chosen above
                if choice2 =="1":
                    i.childD.cost = i.childD.depth
                    queue.append(i.childD)
                    #NumNodesExpanded+=1
                elif choice2 == "2":
                    i.childD.heuristic = MisTileSearch(i.childD.board, goalState)
                    i.childD.cost = i.childD.depth + i.childD.heuristic
                    queue.append(i.childD)
                elif choice2 == "3":
                    i.childD.heuristic  = ManhattenDistSearch(i.childD.board, goalState)
                    i.childD.cost = i.childD.depth + i.childD.heuristic
                    queue.append(i.childD)

            if i.childR != None and dupR == False:#if Right child was created it runs it through the search chosen above
                if choice2 =="1":
                    i.childR.cost = i.childR.depth
                    queue.append(i.childR)
                    #NumNodesExpanded+=1
                elif choice2 == "2":
                    i.childR.heuristic= MisTileSearch(i.childR.board, goalState)
                    i.childR.cost = i.childR.depth + i.childR.heuristic
                    queue.append(i.childR)
                elif choice2 == "3":
                    i.childR.heuristic  = ManhattenDistSearch(i.childR.board, goalState)
                    i.childR.cost = i.childR.depth + i.childR.heuristic
                    queue.append(i.childR)
                
            if i.childL != None and dupL == False:#if Left child was created it runs it through the search chosen above
                if choice2 =="1":
                    i.childL.cost = i.childL.depth
                    queue.append(i.childL)
                   # NumNodesExpanded+=1
                elif choice2 == "2":
                    i.childL.heuristic =  MisTileSearch(i.childL.board, goalState)
                    i.childL.cost = i.childL.depth + i.childL.heuristic
                    queue.append(i.childL)
                elif choice2 == "3":
                    i.childL.heuristic  = ManhattenDistSearch(i.childL.board, goalState)
                    i.childL.cost = i.childL.depth + i.childL.heuristic
                    queue.append(i.childL)

      
                
                


                

        
        done.append (i)#adds finished nodes into the done array
        #print (len(queue))
        if maxQSize < len(queue):#updates the current max size the queue reaches
            maxQSize = len(queue)

    #if board == goal:
    #  return board
        
        #queue.append()





def ManhattenDistSearch(board, goalState):
    
    MDsum=0
    for i in range (len(board)):#check whole board
        for j in range (len(board)):
            num = int(board [i][j])
            
            if num != '0':#ignores 0 tile
                goalX = (num-1) / (len(board))
                goalY = (num-1) % (len(board))
                xDist = i-goalX
                yDist = j-goalY
                MDsum += abs(xDist) + abs(yDist)

    ManHatDist = MDsum
    return ManHatDist

    

def MisTileSearch(board, goalState):
    #print('hi Mis')
    
    MisTile =0
    for i in range (len(board)):#checks whole board
        for j in range (len(board)):
            if board [i][j] != '0' and board[i][j] != goalState[i][j] :#comapres each tile between the goals state and the current state
            
                MisTile+=1
    #if board[2][2] != '0':
       # MisTile -=1

    #print(MisTile)
    return MisTile
                


    
if __name__ == "__main__":
    main()
