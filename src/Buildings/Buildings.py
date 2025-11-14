import pygame
from src.Cookie import Cookie

class Buildings:
    def __init__(self, name : str, multiplicator : float, bonus_per_click : int, price : int, price_multiplicator : float, bonuses_multiplicator : float, cookies_per_second : float, cookies_per_second_multiplicator: float):
        self.name = name
        self.multiplicator = multiplicator
        self.bonus_per_click = bonus_per_click
        self.price = price
        self.price_multiplicator = price_multiplicator
        self.bonuses_multiplicator = bonuses_multiplicator
        self.cookies_per_second = cookies_per_second
        self.cookies_per_second_multiplicator = cookies_per_second_multiplicator

    def buy(self, cookie: Cookie):
        if cookie.score >= self.price:
            cookie.cookies_per_click += self.bonus_per_click
            cookie.multiplicator *= self.multiplicator
            cookie.score -= self.price
            self.price *= self.price_multiplicator
            self.multiplicator *= self.bonuses_multiplicator
            self.bonus_per_click *= self.bonuses_multiplicator
            self.cookies_per_second *= self.cookies_per_second_multiplicator
            return True
        return False
    
    def get_price(self):
        return self.price
    
    def get_name(self):
        return self.name