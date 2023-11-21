import pygame
from pygame import *
from players import PLayer


class Game:
    def __init__(self):
        player_sprite = PLayer()
        self.player = pygame.sprite.GroupSingle(player_sprite)
    def run(self):

        self.player.update()
        self.player.draw(screen)
        

run = True
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((700,700))

game = Game()

while run:
    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    game.run()

    pygame.display.flip()
    Clock.tick(60)
