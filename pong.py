import pygame,sys
from pygame import *
from player1 import PLayer
from player2 import Player
from ball import Ball

pygame.init()

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
        self.speed = 1.1

        self.my_font = pygame.font.Font("freesansbold.ttf", 39)
    def collison_and_score(self):
        if pygame.sprite.spritecollide(self.player1.sprite,self.Ball,False) :
            self.Ball.sprite.ball_speed_x *= -1.1
        if pygame.sprite.spritecollide(self.player2.sprite,self.Ball,False) :
            self.Ball.sprite.ball_speed_x *= -1.1
            

        if self.Ball.sprite.rect.x <= 2:
            self.player1_score += 1
        if self.Ball.sprite.rect.x >= 698:
            self.player2_score += 1
        
    def run(self):
        self.collison_and_score()
        text_surface = self.my_font.render(str(self.player2_score), False, (255, 255, 255))
        text_surface2 = self.my_font.render(str(self.player1_score), False, (255, 255, 255))
        screen.blit(text_surface, (100,0))
        screen.blit(text_surface2, (600,0))
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
