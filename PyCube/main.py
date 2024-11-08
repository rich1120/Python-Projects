from config import *
from rotate import *

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        gui_manager.process_events(event)
        gui_manager.update(1)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    spin_independently = not spin_independently
                    if spin_independently:
                        button.set_text("Follow Mouse")
                    else:
                        button.set_text("Spin Independently")

    
    if spin_independently:
        angle_x += 0.01
        angle_y += 0.01
    else:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle_x = -mouse_x / WIDTH * math.pi
        angle_y = -mouse_y / HEIGHT * math.pi

    screen.fill((0,0,0))
    rotate(angle_x, angle_y)

    # Update screen
    gui_manager.draw_ui(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()