import pygame

class Cookie:
    def __init__(self):
        self.score = 0
        self.cookies_per_second = 0
        self.cookies_per_click = 1
        self.multiplicator = 1

    def buy(self, price):
        if self.score >= price:
            self.score -= price

    def add(self):
        self.score += self.cookies_per_click

    def update_multiplicator(self, multiplicator):
        self.multiplicator += multiplicator

    def update_cookies_per_click(self, cookies_per_click):
        self.cookies_per_click += cookies_per_click

    def get_score(self):
        return self.score
    
    def get_cookie_per_click(self):
        return self.cookies_per_click

    def add_1000_to_cookies(self):
        self.score += 1000