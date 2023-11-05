import pygame
from pygame import *
from player import Shotter

class Game:
    def __init__(self) -> None:
        player_sprite = Shotter
        self.player = pygame.sprite.Group(Shotter)

    def run(self):
        self.player.draw(scren)

scren = pygame.display.set_mode((500,500))
Clock = pygame.time.Clock()
run = True
game = Game

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
    game.run()
    scren.fill((255,5,9))
    Clock.tick(60)
   



    