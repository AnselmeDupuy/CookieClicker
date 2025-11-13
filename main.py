import importlib
import subprocess
import sys

package_name = "pygame"

try:
    importlib.import_module(package_name)
except ImportError:
    print(f"pygame not found, do you wish to install it now? (y/n)")
    choice = input().lower()
    if choice != 'y':
        print("Cannot proceed without installing pygame. Exiting.")
        sys.exit(1)
    print(f"Installing {package_name}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    print("Installation complete! \nGame starting...")

import pygame
from src.Button import Button
from src.Bonus import Bonus
from src.Buildings import Bakery, Farm, FlourFactory, Oven
from src.Cookie import Cookie
from src.Menu import Menu
from src.Save import Save

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

building_1 = Bakery()
building_1_button = Button((WINDOW_WIDTH - 250), ( 125), "assets/golden_cookie.png")


cookie = Cookie()

save = Save()

menu = Menu()

buildings_menu = Menu()


# Game variables
font = pygame.font.Font(None, 36) 


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
            print(f"Exit button clicked in game")
            game_state = "menu"
        elif stop_button.handle_event(event) and game_state == "menu":
            print(f"Exit button clicked in menu")
            pygame.quit()
            sys.exit()
        if building_1_button.handle_event(event) and game_state == "playing":
            if cookie.get_score() >= building_1.get_price():
                building_1.buy(cookie)
                print(f"building bought")
            print(f"clicked building")
        if cookie_button.handle_event(event) and game_state == "playing":
            print(f"clicked cookie")
            cookie.add()


        

    if game_state == "playing":
        screen.fill((50,50,50))
        if game_state == "playing" and cookie.get_score() >= 100:
            screen.blit(bg, bg_rect)
        
        screen.blit(font.render(f"Score: {cookie.get_score()}", True, (255, 255, 255)),(10,10))
        screen.blit(font.render(f"Price: {building_1.get_price()}", True, (255, 255, 255)),((30),(30)))
        stop_button.draw(screen)
        cookie_button.draw(screen)
        building_1_button.draw(screen)
    elif game_state == "menu":
        screen.fill((52,78,91))
        menu.display_menu(screen, buttons)


    pygame.display.flip()

    clock.tick(60)