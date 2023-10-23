import pygame
from modules.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.speed = 1
        self.direction = 'right'  # initialize direction to right

    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
            if self.direction == 'left':  # flip image if direction changed
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = 'right'
        elif direction == 'right':
            self.x += self.speed
            if self.direction == 'right':  # flip image if direction changed
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = 'left'
        elif direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed

        # Boundary checks
        if self.x < 0:
            self.x = 0
        elif self.x > SCREEN_WIDTH - self.image.get_width():
            self.x = SCREEN_WIDTH - self.image.get_width()
        if self.y < 0:
            self.y = 0
        elif self.y > SCREEN_HEIGHT - self.image.get_height():
            self.y = SCREEN_HEIGHT - self.image.get_height()

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
