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
from src.Stylesheet import Stylesheet

pygame.init()

clock = pygame.time.Clock()

# Game constants

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 900
SPRITESHEET_PATH = "assets/sprite_windmill.png"
SPRITE_SHEET_WIDTH = 256
SPRITE_SHEET_HEIGHT = 256

# Initialize screen and window 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cookie Cliker (pour l'instant)")

# Initialize game objects

stylesheet = Stylesheet(pygame.image.load(SPRITESHEET_PATH))


start_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) - 175 , "assets/start_btn.png", 0.8)

save_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) - 60 , "assets/save_btn.png", 0.8)

load_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) + 60, "assets/load_btn.png", 0.8)

stop_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) + 175, "assets/exit_btn.png", 0.8)

cookie_button = Button((WINDOW_WIDTH / 2 - 256), (WINDOW_HEIGHT / 3), SPRITESHEET_PATH)

bakery = Bakery()
Bakery_button = Button((WINDOW_WIDTH - 448), (64), SPRITESHEET_PATH, 0.5)

farm = Farm()
farm_button = Button((WINDOW_WIDTH - 448), (192), SPRITESHEET_PATH, 0.5)

oven = Oven()
oven_button = Button((WINDOW_WIDTH - 448), (320), SPRITESHEET_PATH, 0.5)

flour_factory = FlourFactory()
flour_factory_button = Button((WINDOW_WIDTH - 448), (448), SPRITESHEET_PATH, 0.5)



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
buttons.append(save_button)
buttons.append(load_button)
buttons.append(stop_button)

buildings.append(flour_factory)
buildings.append(farm)
buildings.append(oven)
buildings.append(bakery)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "menu"

        if game_state == "menu":
            if start_button.handle_event(event) and game_state == "menu":
                print(f"Start button clicked")
                game_state = "playing"
            if stop_button.handle_event(event) and game_state == "menu":
                print(f"Exit button clicked in menu")
                pygame.quit()
                sys.exit()
            if save_button.handle_event(event) and game_state == "menu":
                save.save(cookie, buildings)

        if game_state == "playing":
            if Bakery_button.handle_event(event) and game_state == "playing":
                if cookie.get_score() >= bakery.get_price():
                    bakery.buy(cookie)
            if farm_button.handle_event(event) and game_state == "playing":
                if cookie.get_score() >= farm.get_price():
                    farm.buy(cookie)
            if oven_button.handle_event(event) and game_state == "playing":
                if cookie.get_score() >= oven.get_price():
                    oven.buy(cookie)
            if flour_factory_button.handle_event(event) and game_state == "playing":
                if cookie.get_score() >= flour_factory.get_price():
                    flour_factory.buy(cookie)
            if cookie_button.handle_event(event) and game_state == "playing":
                print(f"clicked cookie")
                cookie.add()


        

    if game_state == "playing":
        screen.fill((50,50,50))
        
        screen.blit(font.render(f"Score: {cookie.get_score()}", True, (255, 255, 255)),(10,10))
        screen.blit(font.render(f"Price for {bakery.get_name()}: {bakery.get_price()}", True, (255, 255, 255)),((WINDOW_WIDTH - 384), (64)))
        screen.blit(font.render(f"Price for {farm.get_name()}: {farm.get_price()}", True, (255, 255, 255)),((WINDOW_WIDTH - 384), (192)))
        screen.blit(font.render(f"Price for {oven.get_name()}: {oven.get_price()}", True, (255, 255, 255)),((WINDOW_WIDTH - 384), (320)))
        screen.blit(font.render(f"Price for {flour_factory.get_name()}: {flour_factory.get_price()}", True, (255, 255, 255)),((WINDOW_WIDTH - 384), (448)))

        cookie_button.draw(screen)
        Bakery_button.draw(screen)
        farm_button.draw(screen)
        oven_button.draw(screen)
        flour_factory_button.draw(screen)

    elif game_state == "menu":
        screen.fill((52,78,91))
        menu.display_menu(screen, buttons)


    pygame.display.flip()

    clock.tick(60)