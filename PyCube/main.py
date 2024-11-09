from config import *
from rotate import *
from draw import *



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        gui_manager.process_events(event)
        gui_manager.update(120)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == spin_button:
                    spin_independently = not spin_independently
                    if spin_independently:
                        spin_button.set_text("Follow Mouse")
                    else:
                        spin_button.set_text("Spin Independently")

                elif event.ui_element == color_button:
                    change_color(color_index)

                elif event.ui_element == fast_button:
                    fast = not fast
                    if fast:
                        fast_button.set_text("Slower")
                    else:
                        fast_button.set_text("Faster")
                    
                            

    
    if spin_independently:
        if fast == False:
            angle_x += 0.01
            angle_y += 0.01
        else:
            angle_x += 0.03
            angle_y += 0.03
    else:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle_x = -mouse_x / WIDTH * math.pi
        angle_y = -mouse_y / HEIGHT * math.pi

    screen.fill((32, 32, 32))
    rotate(angle_x, angle_y)

    # Update screen
    gui_manager.draw_ui(screen)
    pygame.display.update()
    clock.tick(120)

pygame.quit()
