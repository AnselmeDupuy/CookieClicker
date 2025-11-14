import pygame
from src.Button import Button
#initialise le menu et lui donne l'état du jeu
class Menu:
    def __init__(self):
        pass

    # prend le screen pour l'affichage, et une liste de bouton et les affiches
    def display_menu(self, screen, button_list : list[Button]):
        for button in button_list:
            button.draw(screen)        


    # import save
    # Start / exit / newgame / load