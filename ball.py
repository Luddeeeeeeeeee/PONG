
import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("balll.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = 350,350
        self.ball_speed_y,self.ball_speed_x = 3,3
    def update(self):
        self.rect.x += self.ball_speed_x
        self.rect.y += self.ball_speed_y

        if self.rect.bottom >= 700 or self.rect.top <= 0:
            self.ball_speed_y *= -1

        if self.rect.x >= 700 or self.rect.x <= 0:
            self.rect.x = 350
            self.rect.y = 350