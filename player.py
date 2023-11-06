import pygame

class Shotter(pygame.sprite.Sprite):
    def __init__(self,positon = (250,250)):
        super().__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill((0,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = positon