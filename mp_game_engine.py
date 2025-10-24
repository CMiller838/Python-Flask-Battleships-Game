import random
from components import initialise_board,create_battleships,place_battleships 




players = {}
attacks = [(-1,-1)]
attackshit = []
potentialattack = []
attacksize = 0
maxsize = 5

def generate_attack(size = 10,diffuculty='Easy',ships={}):
    global maxsize
    global attacks
    global attackshit
    global potentialattack
    if diffuculty == 'Easy':
        return random_attack(size)
        
    elif diffuculty == 'Hard':
        
        try:
            if attackshit == [] and potentialattack == []:
                
                maxsize = max(ships.values())
            
                return random_attack(size)
            elif(len(attackshit) > 1):
                if (len(attackshit) > maxsize):

                    attackshit.clear()
                    
                    maxsize = max(ships.values())
                    return random_attack(size)
                last = len(attackshit) -1
                x,y = attackshit[last]
                lx,ly = attackshit[last -1]
                

                addx = x - lx
                addy = y - ly
                newx = x + addx
                newy = y + addy
                
                if(newx < size and newx > -1 and newy < size and newy > -1 and (not ((newx,newy) in attacks))):
                    attacks.append((newx,newy))
                    return (newx,newy)
                else:
                    attackshit.clear()
                    
                    maxsize = max(ships.values())
                    return random_attack(size)
            elif(potentialattack == []):
                x,y = attackshit[0]

                if(x+1 < size ):
                    potentialattack.append((x+1,y))
                if(x-1 > -1 ):
                    potentialattack.append((x-1,y))
                if(y+1 < size ):
                    potentialattack.append((x,y+1))
                if(y-1 > -1 ):
                    potentialattack.append((x,y-1))
                choice = random.choice(potentialattack)
                while (choice in attacks):
                    potentialattack.remove(choice)
                    choice = random.choice(potentialattack)
                if(potentialattack == []):
                    maxsize = max(ships.values())
                    return random_attack(size)
                potentialattack.remove(choice)
                attacks.append(choice)
                return choice
            elif   (not potentialattack == []):
                choice = random.choice(potentialattack)
                while (choice in attacks and not potentialattack == []):
                    choice = random.choice(potentialattack)
                    potentialattack.remove(choice)
                    
                if(potentialattack == []):
                    maxsize = max(ships.values())
                    return random_attack(size)
                potentialattack.remove(choice)
                attacks.append(choice)
                return choice
        except:
            return random_attack(size)
            
        

            
def addHit(xy):
    attackshit.append(xy)


def attack(coordinates,board,battleships):
    x,y = coordinates
    if board[y][x] == None:
        return False
    else:
        ship = board[y][x]
        length = battleships.get(ship)
        battleships[ship] = length-1
        board[y][x] = None
        addHit(coordinates)
        return True

def random_attack(size):
    
    x = -1
    y = -1
    
    while (((x,y) in attacks)):
            
        
        x = random.randint(0,size -1)
        y = random.randint(0,size -1)
    attacks.append((x,y))
    
    return ((x,y))

def cli_coordinates_input():
    x = int(input('Please Input X Co-Ordinate for an attack: '))
    y = int(input('Please Input Y Co-Ordinate for an attack: '))
    coordinates = (x,y)
    return coordinates



def ai_opponent_game_loop():
    print('Hello and welcome to battleships')
    aibattleship = create_battleships()
    playerbattleship = create_battleships()

    aiboard = place_battleships(initialise_board(),aibattleship,algorithm='Random')
    playerboard = place_battleships(initialise_board(),playerbattleship,algorithm='Custom')

    players['AI'] = [aiboard,aibattleship]
    players['User'] = [playerboard,playerbattleship]

    while(not list(set(aibattleship)) == [0] or not list(set(playerbattleship))):
        coordinates = cli_coordinates_input()
        hit = attack(coordinates,aiboard,aibattleship)
        if (hit):
            print('HIT')
        else:
            print('MISS')

        aicoordinates = generate_attack(len(playerboard))
        print('AI attacks :',aicoordinates)
        aihit = attack(aicoordinates,playerboard,playerbattleship)
        if(aihit):
            print('AI has attacked one of your ships!')
        else:
            print('AI has missed your ships')
        board_str = "" 
        for row in playerboard: 
            row_str = " | ".join(['O' if cell not in (None, 'O') else ' ' for cell in row]) 
            board_str += row_str + "\n" 
        print(board_str)
    if (list(set(aibattleship)) == [0]):
        print('You have won!')
    elif(list(set(playerbattleship)) == [0]):
        print('You have lost')
            
