import pygame
from src.Cookie import Cookie
from .Buildings import Buildings

class Farm(Buildings):
    def __init__(self):
        self.name = "Farm"
        self.multiplicator = 2
        self.bonus_per_click = 10
        self.price = 2500
        self.price_multiplicator = 8
        self.bonuses_multiplicator = 5
