import pygame
from modules.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from modules.player import Player
from modules.world import GameMap
from modules.npc import NPC
from modules.database import connect

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pixel Realms')

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
npc = NPC(SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)
game_map = GameMap()
connect()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move('left')
    if keys[pygame.K_d]:
        player.move('right')
    if keys[pygame.K_w]:
        player.move('up')
    if keys[pygame.K_s]:
        player.move('down')

    game_map.render(screen)
    player.render(screen)
    npc.render(screen)

    pygame.display.flip()

pygame.quit()






