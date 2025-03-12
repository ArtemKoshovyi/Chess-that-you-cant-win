import pygame

# Initialization of Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 400, 400
SQUARE_SIZE = WIDTH // 8

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT = (245, 222, 179)
DARK = (139, 69, 19)
RED = (255, 0, 0)

# Loading piece images with error handling
piece_images = {}
try:
    piece_images["wR"] = pygame.image.load("images/Chess_rlt60.png") 
    piece_images["bR"] = pygame.image.load("images/Chess_rdt60.png") 
    piece_images["wP"] = pygame.image.load("images/Chess_plt60.png") 
    piece_images["bP"] = pygame.image.load("images/Chess_pdt60.png") 
    piece_images["wN"] = pygame.image.load("images/Chess_nlt60.png") 
    piece_images["bN"] = pygame.image.load("images/Chess_ndt60.png") 
    piece_images["wB"] = pygame.image.load("images/Chess_blt60.png") 
    piece_images["bB"] = pygame.image.load("images/Chess_bdt60.png") 
    piece_images["wQ"] = pygame.image.load("images/Chess_qlt60.png") 
    piece_images["bQ"] = pygame.image.load("images/Chess_qdt60.png") 
    piece_images["wK"] = pygame.image.load("images/Chess_klt60.png") 
    piece_images["bK"] = pygame.image.load("images/Chess_kdt60.png")
except FileNotFoundError as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    exit(1)
except Exception as e:
    print(f"Unexpected error: {e}")
    pygame.quit()
    exit(1)