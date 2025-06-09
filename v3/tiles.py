import pygame
from settings import *
from support import import_folder_dict, import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(TILE_COLOR)
        self.rect = self.image.get_rect(topleft=pos)

class TerrainTile(pygame.sprite.Sprite):
    def __init__(self, pos, terrain_graphics=None):
        super().__init__()
        
        if terrain_graphics and 'X' in terrain_graphics:
            # Use loaded terrain graphics
            self.image = terrain_graphics['X']
        else:
            # Fallback to colored rectangle
            self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
            self.image.fill(TILE_COLOR)
            pygame.draw.rect(self.image, (0, 0, 0), (0, 0, TILE_SIZE, TILE_SIZE), 2)
        
        self.rect = self.image.get_rect(topleft=pos)

class PalmFlag(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # Load palm animation frames
        self.animation_frames = import_folder('graphics/terrain/palm/large_fg')
        
        if self.animation_frames:
            # Use palm graphics
            self.frame_index = 0
            self.animation_speed = 4  # Slower animation for palm
            self.image = self.animation_frames[0]
        else:
            # Fallback to simple flag if palm graphics don't load
            self.image = pygame.Surface((64, 128))
            self.image.fill(FLAG_COLOR)
            pygame.draw.rect(self.image, (139, 69, 19), (2, 0, 8, 128))  # Brown pole
            pygame.draw.rect(self.image, FLAG_COLOR, (10, 10, 48, 40))  # Flag
            self.animation_frames = [self.image]
            self.frame_index = 0
            self.animation_speed = 0
        
        # Position palm tree slightly above the platform to avoid root poking through
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.y -= 20  # Move palm tree 20 pixels up
    
    def animate(self, dt):
        """Animate the palm tree"""
        if len(self.animation_frames) > 1:
            self.frame_index += self.animation_speed * dt
            if self.frame_index >= len(self.animation_frames):
                self.frame_index = 0
            self.image = self.animation_frames[int(self.frame_index)]
    
    def update(self, dt=1/60):
        """Update the palm animation"""
        self.animate(dt)

class Coin(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        # Load coin animation frames
        self.animation_frames = import_folder('graphics/items/gold')
        
        if self.animation_frames:
            # Use gold coin graphics
            self.frame_index = 0
            self.animation_speed = 6  # Medium speed animation for coins
            self.image = self.animation_frames[0]
        else:
            # Fallback to simple yellow circle if coin graphics don't load
            self.image = pygame.Surface((32, 32))
            self.image.fill((0, 0, 0))  # Transparent background
            self.image.set_colorkey((0, 0, 0))
            pygame.draw.circle(self.image, (255, 215, 0), (16, 16), 14)  # Gold circle
            pygame.draw.circle(self.image, (255, 255, 0), (16, 16), 14, 2)  # Gold outline
            self.animation_frames = [self.image]
            self.frame_index = 0
            self.animation_speed = 0
        
        self.rect = self.image.get_rect(center=pos)
        
        # Add floating effect
        self.float_offset = 0
        self.float_speed = 3
    
    def animate(self, dt):
        """Animate the coin spinning"""
        if len(self.animation_frames) > 1:
            self.frame_index += self.animation_speed * dt
            if self.frame_index >= len(self.animation_frames):
                self.frame_index = 0
            self.image = self.animation_frames[int(self.frame_index)]
    
    def float_effect(self, dt):
        """Add subtle floating effect to coins"""
        self.float_offset += self.float_speed * dt
        float_y = 3 * pygame.math.Vector2(0, 1).rotate(self.float_offset * 50).y
        self.rect.centery = self.rect.centery + float_y * 0.1
    
    def update(self, dt=1/60):
        """Update coin animation and floating"""
        self.animate(dt)
        # Note: Floating effect disabled to avoid position drift
        # self.float_effect(dt)

class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos, cloud_type=1):
        super().__init__()
        
        # Load cloud graphics
        cloud_files = {
            1: 'graphics/clouds/Small Cloud 1.png',
            2: 'graphics/clouds/Small Cloud 2.png', 
            3: 'graphics/clouds/Small Cloud 3.png'
        }
        
        try:
            self.image = pygame.image.load(cloud_files[cloud_type]).convert_alpha()
        except:
            # Fallback to simple white cloud if graphics don't load
            self.image = pygame.Surface((80, 40))
            self.image.fill((255, 255, 255))
            self.image.set_alpha(180)  # Semi-transparent
            pygame.draw.ellipse(self.image, (240, 240, 240), (0, 0, 80, 40))
            pygame.draw.ellipse(self.image, (220, 220, 220), (10, 5, 60, 30))
        
        self.rect = self.image.get_rect(center=pos)
        
        # Cloud movement properties
        self.speed = 0.5 + (cloud_type * 0.2)  # Different speeds for variety
        self.original_x = pos[0]
        self.drift_range = 100  # How far clouds drift
        self.drift_direction = 1
    
    def update(self, dt=1/60):
        """Move clouds slowly for atmospheric effect"""
        # Slow horizontal drift
        self.rect.x += self.speed * self.drift_direction * dt * 60
        
        # Reverse direction when reaching drift limits
        if abs(self.rect.x - self.original_x) > self.drift_range:
            self.drift_direction *= -1

# Keep the old Flag class for backward compatibility
class Flag(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # Create a simple flag graphic
        self.image = pygame.Surface((32, 64))
        self.image.fill(FLAG_COLOR)
        # Add flag pole
        pygame.draw.rect(self.image, (139, 69, 19), (2, 0, 4, 64))  # Brown pole
        # Add flag
        pygame.draw.rect(self.image, FLAG_COLOR, (6, 5, 24, 20))
        self.rect = self.image.get_rect(topleft=pos)

def load_terrain_graphics():
    """Load terrain graphics from the graphics folder"""
    terrain_graphics = import_folder_dict('graphics/terrain/land')
    return terrain_graphics
