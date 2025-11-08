import pygame
#AhDesu
class Button():
    def __init__(self, x_pos, y_pos, image_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos,y_pos)
    
    # Dessine le bouton au coordonées à l'initialisation
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # Rend le bouton cliquable (clique gauche uniquement)
    def handle_event(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
    
    # animation
    # img
    # load image in class
    # 