import pygame
from src.Cookie import Cookie

class Bonus:
    def __init__(self):
        self.multiplicator = None
        self.bonus_per_click = None
        self.price = None

    def buy(self, cookie : Cookie):
        if cookie.score >= self.price:
            cookie.cookies_per_click += self.bonus_per_click
            cookie.multiplicator *= self.multiplicator
            cookie.score -= self.price
            return True
        return False