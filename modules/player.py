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
        self.health = 100  # add health attribute

    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
            if self.direction == 'right':  # flip image if direction changed
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = 'left'
        elif direction == 'right':
            self.x += self.speed
            if self.direction == 'left':  # flip image if direction changed
                self.image = pygame.transform.flip(self.image, True, False)
                self.direction = 'right'
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
        self.draw_health_bar(screen)  # call draw_health_bar method

    def draw_health_bar(self, screen):
        # Calculate width of health bar
        bar_width = self.health / 100 * self.image.get_width()

        # Draw background rectangle
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, self.image.get_width(), 5))

        # Draw health bar rectangle
        if self.health <= 75:
            pygame.draw.rect(screen, (255, 165, 0), (self.x, self.y - 10, bar_width, 5))
        elif self.health <= 50:
            pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y - 10, bar_width, 5))
        elif self.health <= 25:
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y - 10, bar_width, 5))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y - 10, bar_width, 5))

        
