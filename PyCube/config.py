import pygame
import random
import pygame_gui
import numpy as np
import math
import time

# Window dimensions
WIDTH, HEIGHT = 640, 480

# Cube vertices (x, y, z)
vertices = [
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1],
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1]
]

normals = [
    [0, 0, -1], [0, 0, -1], [0, 0, -1], [0, 0, -1],
    [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],
    [-1, 0, 0], [-1, 0, 0], [-1, 0, 0], [-1, 0, 0],
    [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0],
    [0, -1, 0], [0, -1, 0], [0, -1, 0], [0, -1, 0],
    [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]
]

# Cube edges (connects vertices)
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

color_index = [
    [255, 255, 255],
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [255, 0, 255],
    [0, 255, 255],
    [128, 0, 0],
    [0, 128, 0],
    [0, 0, 128],
    [128, 128, 0],
    [128, 0, 128],
    [0, 128, 128],
    [192, 0, 0],
    [0, 192, 0],
    [0, 0, 192],
    [192, 192, 0],
    [192, 0, 192],
    [0, 192, 192],
    [64, 0, 0],
    [0, 64, 0],
    [0, 0, 64],
    [64, 64, 0],
    [64, 0, 64],
    [0, 64, 64]

]

color = color_index[0]

# Rotation angles (x, y, z)
angle_x, angle_y, angle_z = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("PyCube")

gui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))

button_rect = pygame.Rect((10, 10), (150, 50))
button_small_rect = pygame.Rect((10, 70), (120, 50))
button_tiny_rect = pygame.Rect((10, 130), (80, 50))

spin_button = pygame_gui.elements.UIButton(
    relative_rect=button_rect,
    manager=gui_manager,
    object_id = '#spin_button',
    text='Follow Mouse',
    visible=True
)
color_button = pygame_gui.elements.UIButton(
    relative_rect=button_small_rect,
    manager=gui_manager,
    object_id = '#color_button',
    text='Change Color',
    visible=True
)
fast_button = pygame_gui.elements.UIButton(
    relative_rect=button_tiny_rect,
    manager=gui_manager,
    object_id = '#fast_button',
    text='Speed',
    visible=True
)

spin_independently = True
fast = False