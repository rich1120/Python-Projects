import pygame
import random
import pygame_gui

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
    [255, 0, 0],  # Red
    [0, 255, 0],  # Green
    [0, 0, 255],  # Blue
    [255, 255, 0],  # Yellow
    [255, 0, 255],  # Magenta
    [0, 255, 255],  # Cyan
    [255, 255, 255],  # White
]

color = color_index[random.randint(0, len(color_index) - 1)]

# Rotation angles (x, y, z)
angle_x, angle_y, angle_z = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("PyCube")

gui_manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')

button_rect = pygame.Rect((10, 10), (150, 50))
button_small_rect = pygame.Rect((10, 70), (120, 50))
spin_button = pygame_gui.elements.UIButton(
    relative_rect=button_rect,
    manager=gui_manager,
    object_id = '#spin_button',
    text='Spin Independently',
    visible=True
)
color_button = pygame_gui.elements.UIButton(
    relative_rect=button_small_rect,
    manager=gui_manager,
    object_id = '#color_button',
    text='Change Color',
    visible=True
)

spin_independently = False