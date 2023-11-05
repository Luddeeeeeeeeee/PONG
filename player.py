import pygame

class Shotter:
    def __init__(self) -> None:
        super.__init__()
        self.image = pygame.Surface([50,50])
        self.image.fill(0,255,255)
        self.rect = self.image.get_rect()
        self.rect.center = [250,250]