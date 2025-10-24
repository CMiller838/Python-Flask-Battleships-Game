
from components import initialise_board,create_battleships,place_battleships 
from mp_game_engine import addHit

def attack(coordinates,board,battleships,ai = False):
    
    x,y = coordinates
    if board[y][x] == None:
        return False
    else:
        ship = board[y][x]
        length = battleships.get(ship)
        battleships[ship] = length-1
        board[y][x] = None
        if(ai):

            addHit(coordinates)
        return True


def cli_coordinates_input():
    x = int(input('Please Input X Co-Ordinate for an attack: '))
    y = int(input('Please Input Y Co-Ordinate for an attack: '))
    coordinates = (x,y)
    return coordinates

def simple_game_loop():
    print('Welcome to battleships!!!')
    board = initialise_board()
    ships = create_battleships()
    place_battleships(board,ships)
    while(not list(set(ships.values())) == [0]):
        coordinates = cli_coordinates_input()
        hit = attack(coordinates,board,ships)
        if(hit):
            print('HIT')
        else:
            print('MISS')
    print('Game Over All Ships Destroyed')




    




