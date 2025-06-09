import pygame

# Screen settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
TILE_SIZE = 64

# Player settings - IMPROVED for better jumping
PLAYER_SPEED = 8
GRAVITY = 0.8
JUMP_STRENGTH = -18  # Increased jump power

# Colors
BG_COLOR = (107, 140, 255)
PLAYER_COLOR = (255, 0, 0)  # Bright Red
TILE_COLOR = (111, 196, 169)  # Green
FLAG_COLOR = (255, 255, 0)  # Yellow

# FIXED Level map - Better platform spacing for jumping with coins
# X = Platform, P = Player start, F = Palm tree goal, C = Coin
level_map = [
    '                                ',
    '                   F            ',
    '                   XXX          ',
    '                        XXXXX   ',
    '    C                           ',
    '    XXX            C            ',
    '       XX   XXX    XXX          ',
    '                                ',
    '          C                     ',
    '              XXX               ',
    '                        XXX     ',
    '                                ',
    '         XXX         C          ',
    '                    XXX         ',
    '    C                           ',
    '    XXX                     C   ',
    '                       XX       ',
    'P                        XXX    ',
    'XXXX                            ',
    'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
]
