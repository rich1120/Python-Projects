import pygame
from config import *
import random

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


def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)

        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)

    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) == 3:
            new_positions.add(position)

    return new_positions

def get_neighbors(position):
    x, y = position
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x + dx >= GRID_WIDTH:
            continue
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy >= GRID_HEIGHT:
                continue
            if dx == dy == 0:
                continue
            neighbors.append((x + dx, y + dy))

    return neighbors


def gen(num):
    return set([(random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)) for _ in range(num)])

def main():
    running = True
    playing = True
    step = 0
    step_freq = 120
    positions = set()
    # positions.add((10, 10))

    while running:
        clock.tick(FPS)

        if playing:
            step += 1
        
        if step >= step_freq:
            step = 0
            positions = adjust_grid(positions)

        pygame.display.set_caption(f"PyLife - {len(positions)} cells")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                pos = (x // TILE_SIZE, y // TILE_SIZE)
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing
                if event.key == pygame.K_c:
                    positions.clear()
                    playing = False

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(2, 5) * GRID_WIDTH)

        screen.fill(GRAY)
        draw_grid(positions)
        pygame.display.update()

    
    pygame.quit()

if __name__ == "__main__":
    main()