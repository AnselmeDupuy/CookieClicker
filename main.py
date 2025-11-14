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
import math

pygame.init()

clock = pygame.time.Clock()

# Game constants

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 900
SPRITE_SHEET_WIDTH = 256
SPRITE_SHEET_HEIGHT = 256

# Initialize screen and window 
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cookie Cliker (pour l'instant)")

# Initialize game objects



start_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) - 175 , "assets/start_btn.png", 0.8)

save_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) - 60 , "assets/save_btn.png", 0.8)

load_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) + 60, "assets/load_btn.png", 0.8)

stop_button = Button((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2 ) + 175, "assets/exit_btn.png", 0.8)

cookie_button = Button((WINDOW_WIDTH / 2 - 256), (WINDOW_HEIGHT / 3), "assets/sprite_cookie.png", 0.9)

credits_button = Button((WINDOW_WIDTH - 50), (WINDOW_HEIGHT - 30), "assets/credits_btn.png", 0.2)

option_button = Button((WINDOW_WIDTH - 30), (30), "assets/option_btn.png", 0.2)


bakery = Bakery()
Bakery_button = Button((WINDOW_WIDTH - 448), (64), "assets/sprite_bakery.png", 0.3)

farm = Farm()
farm_button = Button((WINDOW_WIDTH - 448), (192), "assets/sprite_farm.png", 0.3)

oven = Oven()
oven_button = Button((WINDOW_WIDTH - 448), (320), "assets/sprite_oven.png", 0.3)

flour_factory = FlourFactory()
flour_factory_button = Button((WINDOW_WIDTH - 448), (448), "assets/sprite_windmill.png", 0.3)



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
buttons.append(credits_button)

buildings.append(flour_factory)
buildings.append(farm)
buildings.append(oven)
buildings.append(bakery)

last_update = pygame.time.get_ticks()
cooldown = 1000

while True:
    for event in pygame.event.get():
        # base event:
        if event.type == pygame.QUIT:
            save.save(cookie, buildings)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = "menu"
                
        # cheat to add 1000 cookie with "y" key, testing purpose
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                cookie.add_1000_to_cookies()
                print("added 1000 cookie")

        # while in menu:
        if game_state == "menu":
            screen.fill((52,78,91))
            menu.display_menu(screen, buttons)

            if load_button.handle_event(event):
                save.load(cookie, buildings)
                screen.blit(font.render(f"GAME LOADED!", True, (255, 255, 255)),(((WINDOW_WIDTH / 2) - 100), (10)))

            if start_button.handle_event(event):
                game_state = "playing"

            if stop_button.handle_event(event):
                save.save(cookie, buildings)
                pygame.quit()
                sys.exit()

            if save_button.handle_event(event):
                save.save(cookie, buildings)
                screen.blit(font.render(f"GAME SAVED!", True, (255, 255, 255)),(((WINDOW_WIDTH / 2) - 100), (10)))

            if credits_button.handle_event(event):
                game_state = "credits"

        # All if while playing the game
        if game_state == "playing":
            screen.fill((52,78,91))
            
            screen.blit(font.render(f"Score: {cookie.get_score()}", True, (255, 255, 255)),(10,10))
            screen.blit(font.render(f"Cookie per seconds: {cookie.get_cookies_per_second()}",True, (255,255,255)), (10,40))
            screen.blit(font.render(f"Price for {bakery.get_name()}: {bakery.get_price()}", True, (255, 255, 255)),((WINDOW_WIDTH - 384), (64)))
            screen.blit(font.render(f"Price for {farm.get_name()}: {farm.get_price()}", True, (255, 255, 255)),((WINDOW_WIDTH - 384), (192)))
            screen.blit(font.render(f"Price for {oven.get_name()}: {oven.get_price()}", True, (255, 255, 255)),((WINDOW_WIDTH - 384), (320)))
            screen.blit(font.render(f"Price for {flour_factory.get_name()}: {flour_factory.get_price()}", True, (255, 255, 255)),((WINDOW_WIDTH - 384), (448)))

            cookie_button.draw(screen)
            Bakery_button.draw(screen)
            farm_button.draw(screen)
            oven_button.draw(screen)
            flour_factory_button.draw(screen)
            option_button.draw(screen)

            current_time = pygame.time.get_ticks()
            if current_time - last_update >= cooldown:
                cookie.add_cookie_per_seconds()
                last_update = current_time

            if option_button.handle_event(event):
                game_state = "menu"

            if Bakery_button.handle_event(event):
                if cookie.get_score() >= bakery.get_price():
                    bakery.buy(cookie)
                    cookie.update_cookies_per_seconds(bakery.cookies_per_second)

            if farm_button.handle_event(event):
                if cookie.get_score() >= farm.get_price():
                    farm.buy(cookie)
                    cookie.update_cookies_per_seconds(farm.cookies_per_second)

            if oven_button.handle_event(event):
                if cookie.get_score() >= oven.get_price():
                    oven.buy(cookie)
                    cookie.update_cookies_per_seconds(oven.cookies_per_second)

            if flour_factory_button.handle_event(event):
                if cookie.get_score() >= flour_factory.get_price():
                    flour_factory.buy(cookie)
                    cookie.update_cookies_per_seconds(flour_factory.cookies_per_second)

            if cookie_button.handle_event(event):
                cookie.add()

        if game_state == "credits":
            screen.fill((52,78,91))
            credits_title_font = pygame.font.Font(None, 74)
            credits_text = credits_title_font.render("Credits", True, (255, 255, 255))
            text_rect = credits_text.get_rect(center=(WINDOW_WIDTH/2, 150))
            screen.blit(credits_text, text_rect)

            credits_font = pygame.font.Font(None, 50)
            
            creator1_text = credits_font.render("Léo Chappart", True, (255, 255, 255))
            text_rect = creator1_text.get_rect(center=(WINDOW_WIDTH/2, 250))
            screen.blit(creator1_text, text_rect)

            creator2_text = credits_font.render("Anselme Dupuy", True, (255, 255, 255))
            text_rect = creator2_text.get_rect(center=(WINDOW_WIDTH/2, 300))
            screen.blit(creator2_text, text_rect)

            back_text = font.render("Press ESC to return to menu", True, (255, 255, 255))
            text_rect = back_text.get_rect(center=(WINDOW_WIDTH/2, 500))
            screen.blit(back_text, text_rect)
            



    pygame.display.flip()

    clock.tick(60)