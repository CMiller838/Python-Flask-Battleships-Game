# Python & Flask Battleships (with AI Opponent)

This is a full-stack, web-based Battleships game built for the ECM1400 Programming module at the University of Exeter (2024-25). The application is built with **Python** and **Flask**, featuring a full game loop, an interactive web UI for ship placement, and a rule-based AI opponent with multiple difficulty settings.

---

## Key Features

* **Full-Stack Web Application:** A complete web app powered by a **Flask** backend (`main.py`) that serves an HTML/CSS/JavaScript front-end.
* **Rule-Based AI Opponent:** A dynamic AI opponent (`mp_game_engine.py`) with 'Easy' and 'Hard' difficulty modes.
    * **Easy Mode:** The AI selects attack coordinates randomly.
    * **Hard Mode:** The AI uses a heuristic-based algorithm. After scoring a hit, it actively "hunts" for the rest of the ship by attacking adjacent squares.
* **Multiple Ship Placement Algorithms:** The game supports three distinct methods for placing ships on the board (`components.py`):
    * **Simple:** Places ships row by row.
    * **Random:** Places ships randomly (used by the AI).
    * **Custom:** Allows the player to place their ships interactively via the web UI, saving the layout to `placement.json`.
* **Interactive Web UI:** A `placement.html` page for drag-and-drop ship setup and a main `home.html` game board.

---

## Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript (via Flask templates)
* **Data:** JSON (for custom ship placement)

---
# How to Run

1.  Clone this repository.
2.  (Optional but recommended) Create and activate a Python virtual environment.
3.  Install the required dependency:
    ```bash
    pip install Flask
    ```
4.  Run the main application:
    ```bash
    python main.py
    ```
5.  [cite_start]The console will prompt you for the **board size** and **difficulty**[cite: 112, 293].
6.  After entering these, open your web browser and go to `http://127.0.0.1:5000/` to play. You will be directed to the placement page first.
