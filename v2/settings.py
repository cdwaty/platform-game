import pygame

# Screen settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
TILE_SIZE = 64

# Player settings - adjusted for better gameplay
PLAYER_SPEED = 8
GRAVITY = 0.8
JUMP_STRENGTH = -20  # Strong jump for vertical platforming

# Colors
BG_COLOR = (107, 140, 255)
PLAYER_COLOR = (255, 0, 0)  # Bright Red
TILE_COLOR = (111, 196, 169)  # Green
FLAG_COLOR = (255, 255, 0)  # Yellow

# Level map - X represents platforms, P is player start position, F is flag
# Vertical platforming level with player starting at bottom left
level_map = [
    '                            ',
    '                F           ',
    '               XXX          ',
    '                            ',
    '          XXX               ',
    '                            ',
    '                 XXX        ',
    '                            ',
    '        XXX                 ',
    '                            ',
    '               XXX          ',
    '                            ',
    '      XXX                   ',
    '                            ',
    '                XXX         ',
    '                            ',
    'P                           ',
    'XXX                         ',
    'XXXXXXXXXXXXXXXXXXXXXXXX    '
]
