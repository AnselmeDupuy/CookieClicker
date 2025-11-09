import pygame
from src.Cookie import Cookie

class Buildings:
    def __init__(self):
        self.multiplicator = None
        self.bonus_per_click = None
        self.price = None
        self.price_multiplicator = None
        self.bonuses_multiplicator = None

    def buy(self, cookie: Cookie):
        if cookie.score >= self.price:
            cookie.cookies_per_click += self.bonus_per_click
            cookie.multiplicator *= self.multiplicator
            cookie.score -= self.price
            self.price *= self.price_multiplicator
            self.multiplicator *= self.bonuses_multiplicator
            self.bonus_per_click *= self.bonuses_multiplicator
            return True
        return False