import pygame

class GameMap:
    def render(self, screen):
        background = pygame.image.load('assets/map.png')
        screen.blit(background, (0, 0))