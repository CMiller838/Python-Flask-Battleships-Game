Description
This is a Python-based implementation of the classic Battleships game, featuring various algorithms for ship placement and difficulty levels. The game initializes a game board, reads ship data from a file, and places the ships on the board according to specified algorithms. It also includes an AI opponent that can attack based on the chosen difficulty.

Features
Board Initialization: Creates an empty game board of a specified size.

Ship Creation: Reads ship data from a text file and creates a dictionary of ships with their lengths.

Description

I have created a Battleships game that includes multiple difficulty levels. Players can place their ships on the board and trt to locate and sink the AI's fleet.

Features
Board Initialization: Creates an empty game board of a specified size.

Ship Creation: Reads ship data from a text file and creates a dictionary of ships with their lengths.

Ship Placement:

Simple Algorithm: Places ships row by row.

Random Algorithm: Places ships randomly, with constraints based on difficulty (Easy or Hard).

Custom Algorithm: Places ships using predefined positions from a JSON file.

Difficulty Levels: Supports Easy and Hard difficulty levels, affecting ship placement constraints and AI behavior.

AI Opponent: An AI opponent that can generate attacks based on the difficulty level.

Flask Web Interface: A web-based interface built using Flask for interacting with the game.

Self-Assessment
I had to overcome several difficulties to complete this project, which improved my programming and problem-solving skills. For this project, I created a web battleships game with a dynamic AI opponent. The dynamic AI adversary can position its own ships and carry out attacks of various difficulties. To place a ship, three methods are used. The random method, helpful for the AI's ships, places ships randomly depending on the difficulty, whereas the Simple method places ships row by row. The player's ships can be positioned using data obtained from placement.html using the Custom algorithm, which allows for specified ship placements. Incorporating an interactive user interface using HTML templates improved my battleships game by adding a visual dimension and making the game easier to operate. The hardest part was putting the difficult AI into the game, which required an algorithm that would track and completely sink the ship as soon as a strike was detected. Iterative testing and problem-solving were needed for this. However, it was worth it as it makes the game far more enjoyable. Overall, I think the project was a huge success and produced a fun and interesting game. My ability to use complex algorithms was demonstrated by this experience, which also improved my web development and AI integration skills.

Running the program
Everything to run the program is contained in the zip file including the 4 modules of code, the battleships text file used for creating battle ships and the templates used for displaying the webpages for the game. To run the game, run the main file and it will ask for the size of the board and the difficulty once those have been inputted the webpage will be created and you can access the game.  