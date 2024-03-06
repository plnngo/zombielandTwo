import pygame
import random
import math 
from engine import Creature

pygame.init()

# global variables
CELL_NUMBER = 10
SQ_SIZE = 50
FOV_HEIGHT = 3
FOV_WIDTH = 3
MAX_NUM_ROUNDS = 10
PENELTY_MISSING = 10
PENELTY_TOO_MANY = 5
PIXEL_OFFSET = 20

WIDTH, HEIGHT = SQ_SIZE * CELL_NUMBER, SQ_SIZE * CELL_NUMBER
WIN = pygame.display.set_mode((WIDTH + 300, HEIGHT))
pygame.display.set_caption("Zombieland - Multiplayer Version")

# cursor
targeting_cursor = pygame.cursors.Cursor(pygame.cursors.broken_x)
default_cursor = pygame.cursors.Cursor(pygame.cursors.arrow)

# colours
GREY = (40, 50, 60)
BLACK = (0, 0, 0)
GREEN = (50, 200, 150)
YELLOW = (250, 250, 0)
WHITE = (255, 255, 255)
MONITOR_GREEN = (175, 225, 175)

# draw grid
def draw_grid(left = 0, top = 0):
    for i in range(CELL_NUMBER*CELL_NUMBER):
        x = i % CELL_NUMBER * SQ_SIZE
        y = i // CELL_NUMBER * SQ_SIZE
        square = pygame.Rect(x, y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(WIN, BLACK, square, width=3)
    return

# draw zombie onto grids
def draw_zombies(zombie, display_result):
    x = zombie.col * SQ_SIZE + (PIXEL_OFFSET/2)
    y = zombie.row * SQ_SIZE + (PIXEL_OFFSET/2)
    rectangle = pygame.Rect(x, y, SQ_SIZE-PIXEL_OFFSET, SQ_SIZE-PIXEL_OFFSET)
    if display_result:
        pygame.draw.rect(WIN, GREEN, rectangle)
    else:
        pygame.draw.rect(WIN, GREY, rectangle)

# draw human onto grids
def draw_humans(human, display_result):
    x = human.col * SQ_SIZE + (PIXEL_OFFSET/2)
    y = human.row * SQ_SIZE + (PIXEL_OFFSET/2)
    rectangle = pygame.Rect(x, y, SQ_SIZE-PIXEL_OFFSET, SQ_SIZE-PIXEL_OFFSET)
    if display_result:
        pygame.draw.rect(WIN, YELLOW, rectangle)
    else:
        pygame.draw.rect(WIN, GREY, rectangle)