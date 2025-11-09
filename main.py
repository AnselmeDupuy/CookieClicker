import pygame
from src.Button import Button
from src.Bonus import Bonus
from src.Buildings import Buildings
from src.Cookie import Cookie
from src.Menu import Menu
from src.Save import Save
import sys

pygame.init()



clock = pygame.time.Clock()

# Game constants

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 900


# Initialize screen and window 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cookie Cliker (pour l'instant)")

# Initialize game objects

start_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) - 75 , "assets/start_btn.png", 0.8)

stop_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) + 75, "assets/exit_btn.png", 0.8)

bg = pygame.image.load("assets/bg.png").convert_alpha()
bg_rect = bg.get_rect()
cookie_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 3), "assets/cookie3.png")

cookie = Cookie()

saver = Save()

menu = Menu()


# Game variables

game_state = "menu"

buildings = []
bonuses = []
buttons =  []

buttons.append(start_button)
buttons.append(stop_button)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if start_button.handle_event(event) and game_state == "menu":
            print(f"Start button clicked")
            game_state = "playing"
        if stop_button.handle_event(event) and game_state == "playing":
            print(f"Exit button clicked")
            game_state = "menu"

    

    if game_state == "playing":
        screen.fill((50,50,50))
        screen.blit(bg, bg_rect)
        stop_button.draw(screen)
        cookie_button.draw(screen)
    elif game_state == "menu":
        screen.fill((52,78,91))
        menu.display_menu(screen, buttons)

    pygame.display.flip()

    clock.tick(60)