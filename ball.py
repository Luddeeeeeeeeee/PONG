from typing import Any
import pygame
from pygame.sprite import _Group

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("balll.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = 350,350
    def update(self) -> None:
        self.rect.x += 1