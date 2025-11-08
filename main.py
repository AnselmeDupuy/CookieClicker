import pygame
from src.Button import Button
from src.Menu import Menu
import sys

pygame.init()

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 900

GAME_STATE = "menu" # game state:  menu // playing // else?

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cookie Cliker (pour l'instant)")

stop = pygame.image.load("assets/exit_btn.png").convert_alpha()

button_list =  []

start_button = Button((WINDOW_WIDTH / 2), 250, "assets/start_btn.png", 0.8)
stop_button = Button((WINDOW_WIDTH / 2), 375 , "assets/exit_btn.png", 0.8)

menu = Menu()

button_list.append(start_button)
button_list.append(stop_button)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if start_button.handle_event(event) and GAME_STATE == "menu":
            print(f"Start button clicked")
            GAME_STATE = "playing"
        if stop_button.handle_event(event) and GAME_STATE == "playing":
            print(f"Exit button clicked")
            GAME_STATE = "menu"

    if GAME_STATE == "playing":
        screen.fill((50,50,50))
        stop_button.draw(screen)
    elif GAME_STATE == "menu":
        screen.fill((52,78,91))
        menu.display_menu(screen, button_list)

    pygame.display.flip()

    clock.tick(60)