import pygame
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

# Rotation angles (x, y, z)
angle_x, angle_y, angle_z = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("PyCube")

gui_manager = pygame_gui.UIManager((WIDTH, HEIGHT), 'theme.json')

button_rect = pygame.Rect((10, 10), (200, 50))
button = pygame_gui.elements.UIButton(
    relative_rect=button_rect,
    manager=gui_manager,
    object_id = '#spin_button',
    text='Spin Independently',
    visible=True
)

spin_independently = False