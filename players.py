from typing import Any
import pygame


class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PONG.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = 350,350

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y += 5

        if keys[pygame.K_DOWN]:
            self.rect.y -= 5

    def update(self) -> None:
        self.input()