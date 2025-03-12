import pygame
import chess
import chess.engine
import os
from config import WIDTH, HEIGHT, BLACK, piece_images
from chess_logic import create_board, is_valid_move, is_king_in_check, has_legal_moves
from render import draw_board, draw_promotion_menu, draw_game_over, draw_check
from utils import board_to_fen

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess by Kosiv")
    board = create_board()
    turn = "w"
    player_color = "w"
    bot_color = "b"
    selected = None
    game_over = False
    winner = None
    promotion = False
    promotion_start = None
    promotion_end = None

    font = pygame.font.SysFont("Arial", 20, bold=True)
    play_again_rect = pygame.Rect(WIDTH//2 - 90, HEIGHT//2 + 30, 180, 50)

    stockfish_path = "stockfish-windows-x86-64.exe"
    if not os.path.exists(stockfish_path):
        print(f"Error: File {stockfish_path} not found in the project folder!")
        pygame.quit()
        exit(1)
    try:
        engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        engine.configure({"Skill Level": 10})
    except Exception as e:
        print(f"Failed to start Stockfish: {e}")
        pygame.quit()
        exit(1)

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_over:
                    x, y = event.pos
                    if play_again_rect.collidepoint(x, y):
                        board = create_board()
                        turn = "w"
                        game_over = False
                        winner = None
                        promotion = False
                elif promotion:
                    x, y = event.pos
                    if 150 <= x <= 250:
                        if 100 <= y <= 150:
                            board[promotion_end[0]][promotion_end[1]] = turn + "Q"
                        elif 150 <= y <= 200:
                            board[promotion_end[0]][promotion_end[1]] = turn + "R"
                        elif 200 <= y <= 250:
                            board[promotion_end[0]][promotion_end[1]] = turn + "B"
                        elif 250 <= y <= 300:
                            board[promotion_end[0]][promotion_end[1]] = turn + "N"
                        promotion = False
                        turn = bot_color
                elif turn == player_color and not game_over:
                    x, y = event.pos
                    col, row = x // (WIDTH // 8), y // (HEIGHT // 8)
                    if selected is None and board[row][col] and board[row][col][0] == "w":
                        selected = (row, col)
                        print(f"Selected: {selected}")
                    elif selected:
                        start = selected
                        end = (row, col)
                        print(f"Attempted move: {start} -> {end}")
                        if is_valid_move(board, start, end, turn):
                            piece = board[start[0]][start[1]]
                            temp_target = board[end[0]][end[1]]
                            board[end[0]][end[1]] = piece
                            board[start[0]][start[1]] = None
                            if is_king_in_check(board, turn):
                                print("Move canceled: king is in check")
                                board[start[0]][start[1]] = piece
                                board[end[0]][end[1]] = temp_target
                            else:
                                if piece == "wP" and end[0] == 0:
                                    promotion = True
                                    promotion_start = start
                                    promotion_end = end
                                    print("Pawn reached the end, selecting a new piece")
                                elif piece == "wK" and start == (7, 4):
                                    if end == (7, 6):
                                        board[7][5] = "wR"
                                        board[7][7] = None
                                        print("Short castling for white performed")
                                    elif end == (7, 2):
                                        board[7][3] = "wR"
                                        board[7][0] = None
                                        print("Long castling for white performed")
                                if not promotion:
                                    if is_king_in_check(board, bot_color) and not has_legal_moves(board, bot_color):
                                        game_over = True
                                        winner = "White"
                                        print(f"Checkmate! {winner} wins")
                                    else:
                                        turn = bot_color
                                        print("Move completed, bot's turn")
                        else:
                            print("Move not allowed by the rules")
                        selected = None

        if not game_over and turn == bot_color:
            fen = board_to_fen(board, turn)
            chess_board = chess.Board(fen)
            result = engine.play(chess_board, chess.engine.Limit(time=0.1))
            move = result.move
            start = (7 - move.from_square // 8, move.from_square % 8)
            end = (7 - move.to_square // 8, move.to_square % 8)
            piece = board[start[0]][start[1]]
            board[end[0]][end[1]] = piece
            board[start[0]][start[1]] = None
            if piece == "bK" and start == (0, 4):
                if end == (0, 6):
                    board[0][5] = "bR"
                    board[0][7] = None
                    print("Bot performed short castling")
                elif end == (0, 2):
                    board[0][3] = "bR"
                    board[0][0] = None
                    print("Bot performed long castling")
            if piece == "bP" and end[0] == 7:
                board[end[0]][end[1]] = "bQ"
                print("Bot promoted pawn to queen")
            if is_king_in_check(board, player_color) and not has_legal_moves(board, player_color):
                game_over = True
                winner = "Black"
                print(f"Checkmate! {winner} wins")
            else:
                turn = player_color

        screen.fill(BLACK)
        draw_board(screen, board)

        if promotion:
            draw_promotion_menu(screen, font)
        if not game_over:
            if is_king_in_check(board, turn):
                draw_check(screen, font, turn)
        elif game_over:
            draw_game_over(screen, font, winner, play_again_rect)

        pygame.display.flip()
        clock.tick(60)

    engine.quit()
    pygame.quit()

if __name__ == "__main__":
    main()