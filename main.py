

from flask import Flask, render_template,request,jsonify,redirect
from components import initialise_board,create_battleships,place_battleships
from game_engine import attack
from mp_game_engine import generate_attack
import json

players = {}
board_size = 0
playerships = create_battleships()
aiships = create_battleships()
diffuculty = 'Easy'


app = Flask(__name__) 


if board_size == 0:
    board_size = int(input('What size would you like the board to be? '))
    diffuculty = input('What Diffuculty Would You Like, Easy or Hard? ')

@app.route('/') 
def home(): 
    if(players == {}):
        
        return redirect('/placement')
    else:
        aiboard = place_battleships(initialise_board(board_size),aiships,diffuculty,algorithm='Random')
        players['AI'] = [aiships,aiboard]
        
   
    return render_template('home.html',player_board=(players['Player'])[1]) 



@app.route('/placement',methods = ['GET','POST']) 
def placement_interface(): 
   
   if request.method == 'POST':
    board_config = request.get_json()
    
       
       
    with open('placement.json', 'w') as json_file:
        json.dump(board_config, json_file, indent=4)  
        
    

    players['Player'] = [playerships,place_battleships(initialise_board(),playerships,algorithm='Custom')]
    
    return (jsonify({'message': 'Received'}), 200)
   
            
            
   if request.method == 'GET':
       
        return(render_template('placement.html',board_size =board_size,ships=playerships))
   


@app.route('/attack',methods=['GET'])
def player_attack():
    x =int(request.args.get('x'))
    y = int(request.args.get('y'))
    
    
    hit = attack((x, y), ((players['AI'])[1]), ((players['AI'])[0]))
    aiattack = generate_attack(board_size,diffuculty,playerships)
    
    aihit = attack(aiattack,((players['Player'])[1]), ((players['Player'])[0]),True)
    
    if(list(set((players['AI'])[0].values())) == [0]):

        return jsonify({'hit': hit,
            'AI_Turn': aiattack,
            'finished': "Game Over Player wins"})
    elif(list(set((players['Player'])[0].values())) == [0]):
        return jsonify({'hit': hit,
            'AI_Turn': aiattack,
            'finished': "Game Over AI wins"})
    else:
        return jsonify({'hit': hit,
            'AI_Turn': aiattack
            })



    
if __name__ == '__main__': 
    
    app.run()
    