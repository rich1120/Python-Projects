import pygame
import math
from config import *
from rotate import *

running = True
last_mouse_x, last_mouse_y = pygame.mouse.get_pos()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((0, 0, 0))

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate rotation angles based on mouse movement
    angle_x += (mouse_x - last_mouse_x) / WIDTH * math.pi
    angle_y += (mouse_y - last_mouse_y) / HEIGHT * math.pi

    last_mouse_x, last_mouse_y = mouse_x, mouse_y

    rotate(angle_x, angle_y)

    # Update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()