import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platform Star Collector")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Game variables
clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.75
SCROLL_THRESH = 200
scroll = 0
bg_scroll = 0
score = 0
font = pygame.font.SysFont('Arial', 30)

# Player class
class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 50)
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
        self.flip = False
        self.speed = 5
    
    def move(self, platforms):
        # Reset variables
        dx = 0
        dy = 0
        
        # Process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx = -self.speed
            self.flip = True
        if key[pygame.K_RIGHT]:
            dx = self.speed
            self.flip = False
        if key[pygame.K_SPACE] and not self.jumped and not self.in_air:
            self.vel_y = -15
            self.jumped = True
        
        # Add gravity
        self.vel_y += GRAVITY
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y
        
        # Check for collision with platforms
        self.in_air = True
        for platform in platforms:
            # Check for collision in x direction
            if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                dx = 0
            
            # Check for collision in y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                # Check if below platform (jumping)
                if self.vel_y < 0:
                    dy = platform.rect.bottom - self.rect.top
                    self.vel_y = 0
                # Check if above platform (falling)
                elif self.vel_y >= 0:
                    dy = platform.rect.top - self.rect.bottom
                    self.vel_y = 0
                    self.in_air = False
                    self.jumped = False
        
        # Update player position
        self.rect.x += dx
        self.rect.y += dy
        
        # Ensure player doesn't go off the left side of the screen
        if self.rect.left < 0:
            self.rect.left = 0
        
        return scroll
    
    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.rect.x - scroll, self.rect.y, self.rect.width, self.rect.height))

# Platform class
class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
    
    def draw(self):
        pygame.draw.rect(screen, BROWN, (self.rect.x - scroll, self.rect.y, self.rect.width, self.rect.height))

# Star class
class Star:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.collected = False
    
    def draw(self):
        if not self.collected:
            pygame.draw.polygon(screen, YELLOW, [
                (self.rect.centerx - scroll, self.rect.y),
                (self.rect.centerx - 5 - scroll, self.rect.centery - 5),
                (self.rect.x - scroll, self.rect.centery),
                (self.rect.centerx - 5 - scroll, self.rect.centery + 5),
                (self.rect.centerx - scroll, self.rect.bottom),
                (self.rect.centerx + 5 - scroll, self.rect.centery + 5),
                (self.rect.right - scroll, self.rect.centery),
                (self.rect.centerx + 5 - scroll, self.rect.centery - 5)
            ])

# Function to generate platforms
def generate_platforms():
    platforms = []
    
    # Ground platform
    platforms.append(Platform(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH * 3, 50))
    
    # Generate random floating platforms
    for i in range(20):
        x = random.randint(100, SCREEN_WIDTH * 3 - 200)
        y = random.randint(SCREEN_HEIGHT - 350, SCREEN_HEIGHT - 100)
        width = random.randint(80, 150)
        platforms.append(Platform(x, y, width, 20))
    
    return platforms

# Function to generate stars
def generate_stars(platforms):
    stars = []
    
    # Add stars on the ground
    for i in range(15):
        x = random.randint(50, SCREEN_WIDTH * 3 - 50)
        stars.append(Star(x, SCREEN_HEIGHT - 70))
    
    # Add stars on platforms
    for platform in platforms[1:]:  # Skip the ground platform
        if random.random() > 0.5:  # 50% chance to have a star on a platform
            x = random.randint(platform.rect.x, platform.rect.x + platform.rect.width - 20)
            stars.append(Star(x, platform.rect.y - 30))
    
    return stars

# Function to draw the background
def draw_background(scroll):
    screen.fill((135, 206, 235))  # Sky blue
    
    # Draw clouds
    for i in range(10):
        x = (i * 200 - (bg_scroll * 0.5)) % (SCREEN_WIDTH * 3)
        pygame.draw.ellipse(screen, WHITE, (x - scroll, 100, 100, 50))
    
    # Draw hills
    for i in range(5):
        x = (i * 400 - (bg_scroll * 0.6)) % (SCREEN_WIDTH * 3)
        pygame.draw.polygon(screen, GREEN, [(x - 100 - scroll, SCREEN_HEIGHT - 50), 
                                          (x + 100 - scroll, SCREEN_HEIGHT - 50), 
                                          (x - scroll, SCREEN_HEIGHT - 150)])

# Function to draw text
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

# Main function
def main():
    global scroll, bg_scroll, score
    
    # Create player
    player = Player(100, SCREEN_HEIGHT - 150)
    
    # Generate platforms and stars
    platforms = generate_platforms()
    stars = generate_stars(platforms)
    
    # Game loop
    run = True
    while run:
        clock.tick(FPS)
        
        # Draw background
        draw_background(scroll)
        
        # Draw platforms
        for platform in platforms:
            platform.draw()
        
        # Draw stars
        for star in stars:
            star.draw()
        
        # Draw player
        player.draw()
        
        # Draw score
        draw_text(f'Score: {score}', font, BLACK, 20, 20)
        
        # Check for star collection
        for star in stars:
            if not star.collected and player.rect.colliderect(star.rect):
                star.collected = True
                score += 1
        
        # Update player and scroll
        scroll_change = player.move(platforms)
        scroll += scroll_change
        bg_scroll += scroll_change
        
        # Handle scrolling
        if player.rect.right > SCREEN_WIDTH - SCROLL_THRESH and player.direction > 0:
            scroll += player.speed
        
        # Check for game end (player falls off screen)
        if player.rect.top > SCREEN_HEIGHT:
            run = False
        
        # Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
