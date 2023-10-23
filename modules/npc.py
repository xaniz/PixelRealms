import pygame

class NPC:
    def __init__(self, x, y):
        self.x = 430
        self.y = 200 
        self.image = pygame.image.load('assets/npc.png')
        self.image = pygame.transform.scale(self.image, (64, 64))

    def interact(self):
        print("You're interacting with the NPC!")

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))
