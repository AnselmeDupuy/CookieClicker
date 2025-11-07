import pygame
from src.Button import Button
import sys

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 900

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cookie Cliker (pour l'instant)")

start = pygame.image.load("assets/start_btn.png").convert_alpha()
stop = pygame.image.load("assets/exit_btn.png").convert_alpha()

start_button = Button((WINDOW_WIDTH / 2) - (290 / 2), 450, start)
stop_button = Button((WINDOW_WIDTH / 2) - (250 / 2), 500 , stop)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((50,50,50))

    start_button.draw(screen)
    stop_button.draw(screen)


    pygame.display.flip()

    clock.tick(60)