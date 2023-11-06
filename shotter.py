import pygame
from pygame import *
from player import Shotter

class Game:
    def __init__(self):
        player_sprite = Shotter((250,250))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.draw(scren)

scren = pygame.display.set_mode((500,500))
Clock = pygame.time.Clock()
run = True
game = Game()

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    scren.fill((255,5,9))        
    game.run()
    pygame.display.flip()
    
    Clock.tick(60)
   



    