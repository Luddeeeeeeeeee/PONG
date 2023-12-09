import pygame
from pygame import *
from player1 import PLayer
from player2 import Player
from ball import Ball

class Game:
    def __init__(self):
        player_sprite = PLayer()
        player_sprite2 = Player()
        ball_sprite =  Ball()
        self.player1 = pygame.sprite.GroupSingle(player_sprite)
        self.player2 = pygame.sprite.GroupSingle(player_sprite2)
        self.Ball = pygame.sprite.GroupSingle(ball_sprite)
        self.player1_score = 0
        self.player2_score = 0
        self.recently_hit = 0
    def collison_and_score(self):
        if pygame.sprite.spritecollide(self.player1.sprite,self.Ball,False) :
            self.Ball.sprite.ball_speed_x *= -1
            self.recently_hit = 1
        if pygame.sprite.spritecollide(self.player2.sprite,self.Ball,False) :
            self.Ball.sprite.ball_speed_x *= -1
            self.recently_hit = 0

        if self.recently_hit == 1 and self.Ball.sprite.rect.x <= 2:
            self.player1_score += 1
        
        print(self.player1_score)
    def run(self):
        self.collison_and_score()
        self.player2.update()
        self.player1.update()
        self.Ball.update()
        self.Ball.draw(screen)
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
