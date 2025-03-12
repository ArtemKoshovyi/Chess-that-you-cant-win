import pygame
from config import SQUARE_SIZE, LIGHT, DARK, piece_images, BLACK, WHITE, RED

def draw_board(screen, board):
    for row in range(8):
        for col in range(8):
            color = LIGHT if (row + col) % 2 == 0 else DARK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece:
                img = piece_images[piece]
                img = pygame.transform.scale(img, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(img, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def draw_promotion_menu(screen, font):
    pygame.draw.rect(screen, LIGHT, (150, 100, 100, 200))
    options = ["Queen", "Rook", "Bishop", "Knight"]
    for i, option in enumerate(options):
        text = font.render(option, True, BLACK)
        screen.blit(text, (160, 110 + i * 50))

def draw_game_over(screen, font, winner, play_again_rect):
    mate_shadow = font.render(f"Checkmate! {winner} wins!", True, BLACK)
    mate_text = font.render(f"Checkmate! {winner} wins!", True, WHITE)
    screen.blit(mate_shadow, (screen.get_width()//2 - 110 + 2, screen.get_height()//2 - 22))
    screen.blit(mate_text, (screen.get_width()//2 - 110, screen.get_height()//2 - 20))
    pygame.draw.rect(screen, LIGHT, play_again_rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, play_again_rect, 2, border_radius=10)
    play_again_shadow = font.render("Play Again", True, DARK)
    play_again_text = font.render("Play Again", True, BLACK)
    screen.blit(play_again_shadow, (screen.get_width()//2 - 50 + 2, screen.get_height()//2 + 42))
    screen.blit(play_again_text, (screen.get_width()//2 - 50, screen.get_height()//2 + 40))

def draw_check(screen, font, turn):
    check_shadow = font.render("Check!", True, BLACK)
    check_text = font.render("Check!", True, RED)
    screen.blit(check_shadow, (screen.get_width()//2 - 50 + 2, 12))
    screen.blit(check_text, (screen.get_width()//2 - 50, 10))