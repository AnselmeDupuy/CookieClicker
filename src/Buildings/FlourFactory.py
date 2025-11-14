import pygame
from src.Cookie import Cookie
from .Buildings import Buildings

class FlourFactory(Buildings):
    def __init__(self):
        self.name = "FlourFactory"
        self.multiplicator = 1.5
        self.bonus_per_click = 4
        self.price = 50
        self.price_multiplicator = 4
        self.bonuses_multiplicator = 3
