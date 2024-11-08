import pygame
import math
import random
from cell import *
from render import *
from config import *
import asyncio

pygame.init()

height = m*scale
width = n*scale
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Garden")

def render_screen(changes):
    tp = get_colors(changes)
    for t in tp:
        i, j = t
        pygame.draw.rect(screen, get_render(i,j), (j*scale, i*scale, scale, scale))
    pygame.display.update()

def get_mouse_cell(mouse_x, mouse_y):
    return int(mouse_y/scale), int(mouse_x/scale)


def process_mouse(state):
    spread = get_spread()-1
    mouse_x, mouse_y = pygame.mouse.get_pos()
    i, j = get_mouse_cell(mouse_x, mouse_y)
    if state:
        generate(state, i, j)


init()
screen.fill(colors[BLANK][0])
pygame.display.update()



c = pygame.time.Clock()
running = True
READOUT = False
PAUSED = False
state = None

def print_readout():
    print("----")
    fps = int(c.get_fps())
    print("performance:\t"+str(int(100*fps/max_frame_rate))+"%")
    print("step:\t"+str(get_step()))
    print("active cells:\t"+str(len(active_locations)))
    debug = {}
    for i in range(m):
        for j in range(n):
            name = names[matrix[i][j].logic]
            if not name in debug:
                debug[name] = 1
            else:
                debug[name] = debug[name] + 1
    print("cell types:\t\t"+str(debug))
    active_debug = {}
    for t in active_locations:
        log = names[get_cell(t).logic]
        if not log in active_debug:
            active_debug[log] = 1
        else:
            active_debug[log] = active_debug[log]+1
    print("active cell types:\t\t"+str(active_debug))

async def main():

    global running
    global READOUT
    global PAUSED
    global state
    global c
    global CONTROLS

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    state = None
                elif event.key == pygame.K_g:
                    invert_gravity()
                elif event.key == pygame.K_SLASH:
                    print_readout()
                elif event.key == pygame.K_p:
                    PAUSED = not PAUSED
                    if PAUSED:
                        print("paused")
                    else:
                        print("resumed")
                elif event.unicode.isdigit():
                    set_spread(int(event.unicode))
                else:
                    inp = pygame.key.name(event.key)
                    if inp in CONTROLS:
                        state = CONTROLS[inp]
                    else:
                        print("unrecognized input - "+inp)

            elif pygame.mouse.get_pressed()[0]:
                x, y = event.pos
                i, j = get_mouse_cell(x, y)
                if state:
                    generate(state, i, j)
        
        c.tick(max_frame_rate)            
        changes = evolve(PAUSED)
        render_screen(changes)
        asyncio.sleep(1/max_frame_rate)  
        
        

asyncio.run(main())