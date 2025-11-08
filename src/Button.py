import pygame

class Button():
    # initialise la position et le chemin de l'image pour le bouton (scale permet de changer la taille du bouton)
    def __init__(self, x_pos : float, y_pos : float, image_path : str, scale = 1):
        self.image = pygame.image.load(image_path).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, ((width * scale), (height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos,y_pos)
    
    # Dessine le bouton aux coordonées à l'initialisation
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # Rend le bouton cliquable (clique gauche uniquement)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
