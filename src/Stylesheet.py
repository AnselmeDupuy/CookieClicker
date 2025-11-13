import pygame

class Stylesheet:
    def __init__(self, image):
        self.sheet = image
    def get_image(self, frame, width, height, line=0):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), (line * height), width, height))
        image.set_colorkey((0,0,0))
        return image