Chess Game by Kosiv
This is a simple chess game built with Python, Pygame, and the Stockfish chess engine. It allows you to play against an AI opponent with basic chess rules implemented, including castling, pawn promotion, and check/checkmate detection.

Project Structure
The repository contains the following files and directories:

main.py: The entry point of the game, containing the main game loop and event handling.
config.py: Configuration file with constants like window size, colors, and piece image loading.
chess_logic.py: Core chess logic, including board creation, move validation, check detection, and legal move generation.
render.py: Rendering functions for drawing the board, pieces, and UI elements (e.g., promotion menu, game-over screen).
utils.py: Utility functions, such as converting the board state to FEN notation for Stockfish integration.
images/: Directory containing PNG images of chess pieces (e.g., chess_piece_2_white_rook.png, chess_piece_2_black_pawn.png, etc.).
stockfish-windows-x86-64.exe: The Stockfish chess engine executable (required for AI moves).
dist/: (Optional) Directory with a precompiled executable (chess.exe) for easy gameplay without Python setup.
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