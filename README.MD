Chess Game by Kosiv
This is a simple chess game built with Python, Pygame, and the Stockfish chess engine. It allows you to play against an AI opponent with basic chess rules implemented, including castling, pawn promotion, and check/checkmate detection.

Project Structure
The repository contains the following files and directories:

## Project Structure
- **`main.py`**: Main game loop and event handling.
- **`config.py`**: Game configuration (colors, piece images).
- **`chess_logic.py`**: Chess rules and move validation.
- **`render.py`**: Drawing the board and UI.
- **`utils.py`**: Helper functions (e.g., FEN conversion).
- **`images/`**: Chess piece PNGs.
- **`dist/`**: Contains the compiled `chess.exe`.

## Notes
- The AI uses Stockfish with a skill level of 10.
- Requires Windows to run the precompiled `.exe`.

Enjoy the game!

How to Play
Option 1: Run from Source
Clone this repository:
text

Collapse

Wrap

Copy
git clone https://github.com/yourusername/your-repo-name.git
Install dependencies:
text

Collapse

Wrap

Copy
pip install pygame python-chess
Ensure stockfish-windows-x86-64.exe is in the root directory.
Run the game:
text

Collapse

Wrap

Copy
python main.py
Option 2: Play the Executable
If you just want to play the game without setting up Python:

Download the dist folder from this repository.
Open the dist folder and double-click chess.exe to launch the game.
Gameplay
Play as White against the Stockfish AI (Black).
Click a piece to select it, then click a destination square to move.
Supports pawn promotion (choose a piece when a pawn reaches the end), castling, and check/checkmate detection.
When the game ends, click "Play Again" to restart.
Requirements
Python 3.12+ (for source code execution)
Pygame and python-chess libraries
Stockfish executable (included or downloadable from Stockfish website)
Notes
Ensure all chess piece images are in the images/ directory with the exact names specified in config.py.
The AI skill level is set to 10 in Stockfish (configurable in main.py).
Enjoy the game! Contributions and feedback are welcome.