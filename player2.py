from typing import Any
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PONG.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = 100,350

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= 5

        if keys[pygame.K_s]:
            self.rect.y += 5

    def update(self) -> None:
        self.input()