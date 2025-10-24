import random
import json
def initialise_board(size=10):

    return [[None for _ in range(size)] for _ in range(size)]


def  create_battleships(filename = 'battleships.txt'):
    ships = {}
    with open(filename, 'r') as file:
        for line in file:
            split = line.split(':')
            ships[split[0].strip()] = int(split[1].strip())
    return ships


def place_battleships(board, ships,diffuculty = 'Easy', algorithm='Simple'):
    if algorithm == 'Simple':
        row = 0
        size = len(board)
        for ship,length in ships.items():
            if(row < size):
                for i in range(int(length)):
                    board[row][i] = ship
            row += 1
    

    if algorithm == 'Random':
        size = len(board)

        for ship,length in ships.items():
            placed = False

            while(not placed):
                placed = True
                orientation = random.randint(0,1)
                if(orientation == 0):
                    x = random.randint(0, size -(1 + int(length)))
                    y = random.randint(0,size - 1)
                else:
                    y = random.randint(0,size - (1+int(length)))
                    x = random.randint(0,size - 1)
                tempx = x
                tempy = y
                for i in range(int(length)):
                    if (diffuculty=='Hard'):
                        
                        try:
                            if(not (board[tempy +1][tempx] == None)):
                                placed = False
                        except IndexError:
                            pass
                        try:
                            if(not (board[tempy -1][tempx] == None)):
                                placed = False
                        except IndexError:
                            pass
                        try:
                            if( not (board[tempy][tempx +1] == None)):
                                placed = False
                        except IndexError:
                            pass
                        try:
                            if(not (board[tempy][tempx -1] == None)):
                                placed = False
                        except IndexError:
                            pass    
                    




                    if(not board[tempy][tempx] == None):
                        placed = False
                    if orientation == 0:
                        tempx += 1
                    else:
                        tempy += 1
            tempx = x
            tempy = y
            for i in range(int(length)):                               
                                  
                    board[tempy][tempx] = ship
                    if orientation == 0:
                        tempx += 1
                    else:
                        tempy += 1
        
        
    if algorithm == 'Custom':
        with open('placement.json', 'r') as file:
               
            data = json.load(file)
            for ship in data.keys():
                position = data.get(ship)
                x = int(position[0])
                y=int(position[1])
                orientation = position[2]
                length = ships.get(ship)
                for i in range(int(length)):
                    
                    board[y][x] = ship
                    if(orientation == 'v'):
                        y += 1
                    elif(orientation == 'h'):
                        x += 1


    return board





