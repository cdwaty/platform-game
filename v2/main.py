import pygame, sys
import asyncio
from settings import *
from level import Level

async def main():
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Platform Jumper')
    clock = pygame.time.Clock()
    
    # Create level after pygame is initialized
    level = Level(level_map, screen)
    
    # Button font
    button_font = pygame.font.Font(None, 36)
    
    # Retry button
    retry_text = button_font.render('RETRY', True, (255, 255, 255))
    retry_rect = retry_text.get_rect(topleft=(20, 50))
    retry_button_bg = pygame.Rect(15, 45, retry_rect.width + 10, retry_rect.height + 10)
    
    # Start button
    start_text = button_font.render('START', True, (255, 255, 255))
    start_rect = start_text.get_rect(topleft=(20, 110))
    start_button_bg = pygame.Rect(15, 105, start_rect.width + 10, start_rect.height + 10)
    
    # Stopwatch variables
    start_time = None
    elapsed_time = 0
    game_started = False
    
    running = True
    while running:
        # Update elapsed time only if game has started and not won
        if game_started and not level.game_won:
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Check for button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Retry button
                if retry_button_bg.collidepoint(event.pos):
                    # Restart the game by creating a new level and resetting timer
                    level = Level(level_map, screen)
                    if game_started:
                        start_time = pygame.time.get_ticks()
                    else:
                        elapsed_time = 0
                
                # Start button
                if start_button_bg.collidepoint(event.pos) and not game_started:
                    game_started = True
                    start_time = pygame.time.get_ticks()
        
        # STEP 1: Clear screen with sky blue background - MUST BE FIRST
        screen.fill('skyblue')
        
        # STEP 2: Run game logic and draw elements
        level.run(elapsed_time)
        
        # STEP 3: Draw player highlight if game is not won
        player = level.player.sprite
        if not level.game_won:
            # Draw a white highlight around the player to make it more visible
            pygame.draw.rect(screen, (255, 255, 255), 
                            (player.rect.x - 3, player.rect.y - 3, 
                             player.rect.width + 6, player.rect.height + 6), 3)
        
        # Draw retry button
        pygame.draw.rect(screen, (50, 50, 200), retry_button_bg, border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), retry_button_bg, 2, border_radius=5)
        screen.blit(retry_text, retry_rect)
        
        # Draw start button (green if not started, gray if already started)
        button_color = (100, 100, 100) if game_started else (50, 200, 50)
        pygame.draw.rect(screen, button_color, start_button_bg, border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), start_button_bg, 2, border_radius=5)
        screen.blit(start_text, start_rect)
        
        # Draw stopwatch
        if game_started:
            minutes = int(elapsed_time / 60000)
            seconds = int((elapsed_time % 60000) / 1000)
            milliseconds = int((elapsed_time % 1000) / 10)
            time_str = f"Time: {minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        else:
            time_str = "Time: 00:00.00"
        
        time_surf = button_font.render(time_str, True, (0, 0, 0))
        screen.blit(time_surf, (SCREEN_WIDTH - 200, 10))
        
        # STEP 4: Update display
        pygame.display.flip()
        
        # Maintain 60 FPS and yield to browser
        clock.tick(60)
        await asyncio.sleep(0)
    
    pygame.quit()

# Pygbag entry point
if __name__ == "__main__":
    if sys.platform == 'emscripten':
        asyncio.run(main())
    else:
        # For desktop, use this
        asyncio.run(main())
