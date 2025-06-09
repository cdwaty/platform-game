import pygame
from settings import *
from tiles import TerrainTile, PalmFlag, Coin, Cloud, load_terrain_graphics
from player import Player
import random

class Level:
    def __init__(self, level_data, surface):
        # Level setup
        self.display_surface = surface
        self.world_shift = 0
        
        # Load graphics
        self.terrain_graphics = load_terrain_graphics()
        
        # Sprite groups
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.coin_sprites = pygame.sprite.Group()
        self.cloud_sprites = pygame.sprite.Group()  # Background clouds
        
        # Game state
        self.game_won = False
        self.coins_collected = 0
        self.total_coins = 0
        
        # Setup level
        self.setup_level(level_data)
        self.setup_clouds()  # Add background clouds
    
    def setup_level(self, layout):
        """Create the level from the layout data"""
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if cell == 'X':
                    # Create terrain tile
                    tile = TerrainTile((x, y), self.terrain_graphics)
                    self.visible_sprites.add(tile)
                    self.collision_sprites.add(tile)
                
                elif cell == 'P':
                    # Create player
                    self.player = pygame.sprite.GroupSingle()
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                    self.visible_sprites.add(player_sprite)
                    self.active_sprites.add(player_sprite)
                
                elif cell == 'F':
                    # Create palm flag (goal)
                    palm_flag = PalmFlag((x, y))
                    self.visible_sprites.add(palm_flag)
                    self.active_sprites.add(palm_flag)  # Add to active sprites for animation
                    self.goal_sprites = pygame.sprite.GroupSingle(palm_flag)
                
                elif cell == 'C':
                    # Create coin
                    coin = Coin((x + TILE_SIZE//2, y + TILE_SIZE//2))  # Center coin in tile
                    self.visible_sprites.add(coin)
                    self.active_sprites.add(coin)  # Add to active sprites for animation
                    self.coin_sprites.add(coin)
                    self.total_coins += 1
    
    def setup_clouds(self):
        """Create background clouds for atmosphere"""
        # Calculate level dimensions
        level_width = len(level_map[0]) * TILE_SIZE
        level_height = len(level_map) * TILE_SIZE
        
        # Create clouds at various positions
        cloud_positions = [
            (200, 100), (500, 80), (800, 120), (1100, 90),
            (300, 200), (700, 180), (1000, 160), (1300, 140),
            (150, 300), (450, 280), (750, 320), (1050, 290),
            (400, 50), (900, 60), (1200, 100)
        ]
        
        for i, pos in enumerate(cloud_positions):
            # Use different cloud types for variety
            cloud_type = (i % 3) + 1
            cloud = Cloud(pos, cloud_type)
            self.visible_sprites.add(cloud)
            self.active_sprites.add(cloud)  # Add to active for movement
            self.cloud_sprites.add(cloud)
    
    def horizontal_movement_collision(self):
        """Handle horizontal collision detection - FIXED VERSION"""
        player = self.player.sprite
        
        # Move player horizontally
        player.rect.x += player.direction.x * player.speed
        
        # Check for collisions
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:  # Moving left
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:  # Moving right
                    player.rect.right = sprite.rect.left
    
    def vertical_movement_collision(self):
        """Handle vertical collision detection - FIXED VERSION"""
        player = self.player.sprite
        player.apply_gravity()
        
        # Reset ground status
        player.on_ground = False
        
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:  # Falling
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:  # Jumping
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    
    def check_coin_collision(self):
        """Check if player collected any coins"""
        collected_coins = pygame.sprite.spritecollide(self.player.sprite, self.coin_sprites, True)
        if collected_coins:
            self.coins_collected += len(collected_coins)
            # You could add a coin collection sound effect here
    
    def check_goal_collision(self):
        """Check if player reached the goal"""
        if hasattr(self, 'goal_sprites'):
            if pygame.sprite.spritecollide(self.player.sprite, self.goal_sprites, False):
                self.game_won = True
    
    def run(self, elapsed_time, dt=1/60):
        """Main level update method"""
        # Update active sprites
        self.active_sprites.update(dt)
        
        # Handle collisions - FIXED ORDER
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        
        # Check coin collection
        self.check_coin_collision()
        
        # Check goal
        self.check_goal_collision()
        
        # Draw everything
        self.visible_sprites.custom_draw(self.player.sprite)
        
        # Display win message
        if self.game_won:
            font = pygame.font.Font(None, 72)
            win_text = font.render('YOU WIN!', True, (255, 255, 0))
            win_rect = win_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
            self.display_surface.blit(win_text, win_rect)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        
        # Camera box setup
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2
        
        # Camera borders
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l, t, w, h)
    
    def center_target_camera(self, target):
        """Center camera on target"""
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def box_target_camera(self, target):
        """Box camera following"""
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom
        
        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']
    
    def custom_draw(self, player):
        """Custom draw method with camera and layered rendering"""
        # Update camera
        self.box_target_camera(player)
        
        # Draw clouds first (background layer)
        for sprite in self.sprites():
            if hasattr(sprite, '__class__') and sprite.__class__.__name__ == 'Cloud':
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
        
        # Draw all other sprites (foreground layer)
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            if not (hasattr(sprite, '__class__') and sprite.__class__.__name__ == 'Cloud'):
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
