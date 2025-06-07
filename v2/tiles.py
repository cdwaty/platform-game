import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(TILE_COLOR)
        # Add a black border to make tiles more visible
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, size, size), 2)
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift

class Flag(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size // 2, size))
        self.image.fill(FLAG_COLOR)
        # Add a black border to make flag more visible
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, size // 2, size), 2)
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift
