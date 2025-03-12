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

### Quick Start
If you want to play, download dist.zip, unzip it, run `chess.exe`, and enjoy the game!
   - **Note**: If Windows shows a "Windows protected your PC" warning:
     - Click **"More info"** (Więcej informacji).
     - Click **"Run anyway"** (Uruchom mimo to) to launch the game.