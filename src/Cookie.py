import pygame

class Cookie:
    def __init__(self):
        self.score = 0
        self.cookies_per_second = 0
        self.cookies_per_click = 0
        self.multiplicator = 1

    def buy(self, price):
        if self.score >= price:
            self.score -= price

    def add(self, price):
        self.score += price

    def update_multiplicator(self, multiplicator):
        self.multiplicator += multiplicator

    def update_cookies_per_click(self, cookies_per_click):
        self.cookies_per_click += cookies_per_click