import pygame, sys
from tiles import Tile, Flag
from player import Player
from settings import *

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.current_x = 0
        self.game_won = False
        
        # Calculate level height for vertical scrolling
        self.level_height = len(level_data) * TILE_SIZE
        
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.flag = pygame.sprite.GroupSingle()
        
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if cell == 'X':
                    tile = Tile((x, y), TILE_SIZE)
                    self.tiles.add(tile)
                elif cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif cell == 'F':
                    flag_sprite = Flag((x, y), TILE_SIZE)
                    self.flag.add(flag_sprite)
    
    def scroll_camera(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        player_y = player.rect.centery
        direction_x = player.direction.x
        
        # Horizontal scrolling
        if player_x < SCREEN_WIDTH / 4 and direction_x < 0:
            self.world_shift_x = 8
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH / 4) and direction_x > 0:
            self.world_shift_x = -8
        else:
            self.world_shift_x = 0
            
        # Vertical scrolling - follow player vertically
        if player_y < SCREEN_HEIGHT / 3:
            self.world_shift_y = 8  # Scroll down (objects move down)
        elif player_y > SCREEN_HEIGHT - (SCREEN_HEIGHT / 3):
            self.world_shift_y = -8  # Scroll up (objects move up)
        else:
            self.world_shift_y = 0
    
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
    
    def check_win(self, elapsed_time):
        player = self.player.sprite
        
        if pygame.sprite.spritecollide(player, self.flag, False) and not self.game_won:
            self.game_won = True
            
            # Format time as minutes:seconds.milliseconds
            minutes = int(elapsed_time / 60000)
            seconds = int((elapsed_time % 60000) / 1000)
            milliseconds = int(elapsed_time % 1000)
            time_str = f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
            
            # Create win message with time
            large_font = pygame.font.Font(None, 74)
            small_font = pygame.font.Font(None, 48)
            
            win_text = large_font.render('YOU WIN!', True, (255, 255, 255))
            time_text = small_font.render(f"Time: {time_str}", True, (255, 255, 255))
            
            win_rect = win_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 40))
            time_rect = time_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40))
            
            # Draw semi-transparent background
            bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            bg_surface.set_alpha(150)
            bg_surface.fill((0, 0, 0))
            self.display_surface.blit(bg_surface, (0, 0))
            
            # Draw text
            self.display_surface.blit(win_text, win_rect)
            self.display_surface.blit(time_text, time_rect)
            
            # For desktop version, quit after delay (but not for web version)
            if sys.platform != 'emscripten':
                pygame.display.update()
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()
    
    def run(self, elapsed_time):
        # Don't update game state if game is won (for web version)
        if self.game_won and sys.platform == 'emscripten':
            # Just redraw the win screen
            # Format time as minutes:seconds.milliseconds
            minutes = int(elapsed_time / 60000)
            seconds = int((elapsed_time % 60000) / 1000)
            milliseconds = int(elapsed_time % 1000)
            time_str = f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
            
            # Create win message with time
            large_font = pygame.font.Font(None, 74)
            small_font = pygame.font.Font(None, 48)
            
            win_text = large_font.render('YOU WIN!', True, (255, 255, 255))
            time_text = small_font.render(f"Time: {time_str}", True, (255, 255, 255))
            
            win_rect = win_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 40))
            time_rect = time_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40))
            
            # Draw semi-transparent background
            bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            bg_surface.set_alpha(150)
            bg_surface.fill((0, 0, 0))
            self.display_surface.blit(bg_surface, (0, 0))
            
            # Draw text
            self.display_surface.blit(win_text, win_rect)
            self.display_surface.blit(time_text, time_rect)
            return
        
        # Level tiles
        self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)
        
        # Flag
        self.flag.update(self.world_shift_x, self.world_shift_y)
        self.flag.draw(self.display_surface)
        
        # Player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        self.scroll_camera()
        
        # Check for win condition
        self.check_win(elapsed_time)
