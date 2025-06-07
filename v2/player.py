import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Make player larger and more visible with bright red color
        self.image = pygame.Surface((48, 64))
        self.image.fill(PLAYER_COLOR)
        # Add black border to player
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, 48, 64), 2)
        self.rect = self.image.get_rect(topleft = pos)
        
        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.gravity = GRAVITY
        self.jump_speed = JUMP_STRENGTH
        
        # Player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        self.direction.y = self.jump_speed
        self.on_ground = False
    
    def update(self):
        self.get_input()
