from config import *
from tetromino import Tetromino
import pygame
import random

def create_grid(locked_positions={}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j,i)]
                grid[i][j] = c

    return grid

def draw_grid(surface):
    surface.fill(BLACK)
    grid = create_grid(locked_positions={})
    font = pygame.font.SysFont('comicsans', 20)
    label = font.render('TETRIS', 1, (255,255,255))

    surface.blit(label, (TOP_LEFT_X + PLAY_AREA_WIDTH / 2 - (label.get_width() / 2), 30))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (TOP_LEFT_X + j * 30, TOP_LEFT_Y + i * 30, 30, 30), 0)

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    global tetrominos, tetromino_colors
    return Tetromino(5, 0, random.choice(tetrominos))

def draw_text_middle(text, size, color, surface):
    pass


def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    pass

def main_menu():
    pass