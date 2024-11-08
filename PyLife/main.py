import pygame
from config import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def draw_grid(positions):
    for position in positions:
        x, y = position
        pygame.draw.rect(screen, ORANGE, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, row * TILE_SIZE), (SCREEN_WIDTH, row * TILE_SIZE))

    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, BLACK, (col * TILE_SIZE, 0), (col * TILE_SIZE, SCREEN_HEIGHT))

def main():
    running = True
    positions = set()
    positions.add((10, 10))

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                positions.add((x // TILE_SIZE, y // TILE_SIZE))

        screen.fill(GRAY)
        draw_grid(positions)
        pygame.display.update()

    
    pygame.quit()

if __name__ == "__main__":
    main()