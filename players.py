import pygame


class PLayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("PONG.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = 350,350