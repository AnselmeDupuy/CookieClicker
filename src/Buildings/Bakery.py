import pygame
from src.Cookie import Cookie
from .Buildings import Buildings

class Bakery(Buildings):
    def __init__(self):
        self.name = "Bakery"
        self.multiplicator = 8
        self.bonus_per_click = 100
        self.price = 2500
        self.price_multiplicator = 9
        self.bonuses_multiplicator = 8
