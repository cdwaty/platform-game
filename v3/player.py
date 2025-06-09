import pygame
from settings import *
from support import import_character_assets

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # Load player graphics
        self.load_graphics()
        
        # Animation setup
        self.frame_index = 0
        self.animation_speed = 8
        self.status = 'idle'
        self.facing_right = True
        
        # Set initial image and rect
        self.image = self.animations[f'{self.status}_right'][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=pos)
        
        # Player movement - SIMPLIFIED AND FIXED
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = PLAYER_SPEED
        self.gravity = GRAVITY
        self.jump_speed = JUMP_STRENGTH
        
        # Player status - SIMPLIFIED
        self.on_ground = False
    
    def load_graphics(self):
        """Load all player animation graphics"""
        self.animations = import_character_assets('graphics/player')
        
        # If no graphics found, create colored rectangles as fallback
        if not self.animations:
            self.create_fallback_graphics()
    
    def create_fallback_graphics(self):
        """Create simple colored rectangles if graphics can't be loaded"""
        self.animations = {}
        states = ['idle', 'run', 'jump', 'fall']
        directions = ['left', 'right']
        
        for state in states:
            for direction in directions:
                # Create simple colored surface
                surf = pygame.Surface((48, 64))
                surf.fill(PLAYER_COLOR)
                pygame.draw.rect(surf, (0, 0, 0), (0, 0, 48, 64), 2)
                self.animations[f'{state}_{direction}'] = [surf]
    
    def get_input(self):
        """FIXED input handling - no restrictions"""
        keys = pygame.key.get_pressed()
        
        # Reset horizontal movement
        self.direction.x = 0
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
            
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
    
    def get_status(self):
        """Determine player animation status based on movement"""
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
    
    def animate(self, dt):
        """Handle player animation"""
        direction = 'right' if self.facing_right else 'left'
        animation_key = f'{self.status}_{direction}'
        
        # Get current animation frames
        if animation_key in self.animations:
            current_animation = self.animations[animation_key]
        else:
            # Fallback to idle if animation doesn't exist
            current_animation = self.animations.get(f'idle_{direction}', [self.image])
        
        # Update frame index
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(current_animation):
            self.frame_index = 0
        
        # Set current image
        self.image = current_animation[int(self.frame_index)]
    
    def apply_gravity(self):
        """Apply gravity to player"""
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    
    def jump(self):
        """Make player jump"""
        self.direction.y = self.jump_speed
        self.on_ground = False
    
    def update(self, dt=1/60):
        """Update player - FIXED ORDER"""
        self.get_input()
        self.get_status()
        self.animate(dt)
