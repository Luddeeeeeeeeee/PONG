import pygame
from pygame import *
from player1 import PLayer
from player2 import Player
from ball import Ball

class Game:
    def __init__(self):
        player_sprite = PLayer()
        player_sprite2 = Player()
        ball =  Ball()
        self.player1 = pygame.sprite.GroupSingle(player_sprite)
        self.player2 = pygame.sprite.GroupSingle(player_sprite2)
        self.Bell = pygame.sprite.GroupSingle(ball)
    def run(self):
        self.player2.update()
        self.player1.update()
        self.Bell.update()
        self.Bell.draw()
        self.player2.draw(screen)
        self.player1.draw(screen)

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
