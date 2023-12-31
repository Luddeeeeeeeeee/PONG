from typing import Any
import pygame


class PLayer(pygame.sprite.Sprite):
    def __init__(self,pos,one_or_two):
        super().__init__()
        self.image = pygame.image.load("PONG.png").convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.one_or_two = one_or_two

    def input(self):
        keys = pygame.key.get_pressed()

        if self.one_or_two == 0:

            if keys[pygame.K_UP]:
                self.rect.y -= 5

            if keys[pygame.K_DOWN]:
                self.rect.y += 5
        if self.one_or_two == 1:

            if keys[pygame.K_w]:
                self.rect.y -= 5

            if keys[pygame.K_s]:
                self.rect.y += 5

    def out_of_bounds(self):
        if self.rect.bottom >= 700:
            self.rect.bottom = 699

        if self.rect.top <= 0:
            self.rect.y = 1



    def update(self) -> None:
        self.input()
        self.out_of_bounds()