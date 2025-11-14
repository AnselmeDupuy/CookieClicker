import pygame
from src.Cookie import Cookie
from .Buildings import Buildings

class Oven(Buildings):
    def __init__(self):
        self.name = "Oven"
        self.multiplicator = 4
        self.bonus_per_click = 50
        self.price = 7800
        self.price_multiplicator = 8
        self.bonuses_multiplicator = 6
        self.cookies_per_second = 5
        self.cookies_per_second_multiplicator = 1.8
        