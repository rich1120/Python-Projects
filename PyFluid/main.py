import pygame
from config import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        pygame.display.set_caption(f"PyFluid - {pygame.mouse.get_pos()}")
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
