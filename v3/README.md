# 🏴‍☠️ Pirate Platform Adventure

A professional 2D platform adventure game built with Python and Pygame, featuring beautiful pirate-themed graphics, smooth animations, and engaging gameplay mechanics.

![Game Preview](https://img.shields.io/badge/Python-3.12-blue) ![Pygame](https://img.shields.io/badge/Pygame-2.6.1-green) ![Status](https://img.shields.io/badge/Status-Complete-success)

## 🎮 Game Overview

Navigate through challenging platforms as an animated pirate character, collect spinning gold coins, and reach the swaying palm tree goal to win! This game features professional-quality graphics from the PirateMaker asset collection and smooth gameplay mechanics.

### ✨ Key Features

- **🏴‍☠️ Animated Pirate Character**: 8-state sprite animation system (idle, run, jump, fall × left/right)
- **🪙 Collectible Gold Coins**: 6 spinning animated coins scattered across platforms
- **🌴 Animated Goal**: Swaying palm tree with realistic animation
- **☁️ Dynamic Background**: Moving clouds for atmospheric depth
- **⏱️ Professional Timer**: Precise stopwatch with millisecond accuracy
- **🎯 Smart Camera System**: Smooth camera following with boundary constraints
- **🎨 Beautiful Graphics**: High-quality pirate-themed sprite assets
- **🔄 Game State Management**: START/RETRY functionality with clean UI
- **🏆 Win Condition**: Collect all coins and reach the palm tree to victory

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Pygame 2.0 or higher
- Virtual environment (recommended)

### Installation

1. **Clone or navigate to the game directory:**
   ```bash
   cd /platform_game/v3
   ```

2. **Set up virtual environment:**
   ```bash
   python3 -m venv pygame-env
   source pygame-env/bin/activate  # On Windows: pygame-env\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install pygame
   ```

4. **Run the game:**
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Controls
- **Arrow Keys (← →)**: Move left and right
- **Space Bar**: Jump
- **Mouse**: Click START/RETRY buttons

### Objective
1. **🪙 Collect all 6 gold coins** scattered across different platforms
2. **🌴 Reach the animated palm tree** at the end of the level
3. **⏱️ Complete as quickly as possible** to achieve the best time
4. **🏆 Achieve victory** by collecting everything in one playthrough

### Game Mechanics
- **Gravity System**: Realistic falling and jumping physics
- **Platform Collision**: Precise collision detection with terrain
- **Coin Collection**: Automatic pickup when touching coins
- **Camera Following**: Smooth camera that follows the player
- **Animation States**: Character animations change based on movement
- **Timer System**: Tracks completion time with millisecond precision

## 🏗️ Technical Architecture

### File Structure
```
v3/
├── main.py              # Main game loop and UI management
├── player.py            # Player class with animation system
├── level.py             # Level management and sprite groups
├── tiles.py             # Terrain, coins, palm tree, and cloud classes
├── support.py           # Graphics loading utilities
├── settings.py          # Game configuration and constants
├── README.md            # This file
└── graphics/            # Game assets directory
    ├── player/          # Character animations (8 states)
    ├── terrain/         # Platform tiles and palm tree
    ├── items/           # Gold coin animations
    └── clouds/          # Background cloud graphics
```

### Core Systems

#### 🎨 Graphics Loading System
- **Automatic Asset Loading**: Dynamically loads sprites from organized folders
- **Animation Management**: Frame-based animation system with configurable speeds
- **Fallback Graphics**: Colored shapes if assets fail to load
- **Performance Optimized**: Graphics loaded once and reused

#### 🎮 Player Animation System
```python
# 8-state animation system
animations = {
    'idle_right': [frame1, frame2, frame3, frame4, frame5],
    'idle_left': [frame1, frame2, frame3, frame4, frame5],
    'run_right': [frame1, frame2, frame3, frame4],
    'run_left': [frame1, frame2, frame3, frame4],
    'jump_right': [frame1],
    'jump_left': [frame1],
    'fall_right': [frame1],
    'fall_left': [frame1]
}
```

#### 🏞️ Camera System
- **Smooth Following**: Camera smoothly tracks player movement
- **Boundary Constraints**: Prevents camera from showing empty areas
- **Layered Rendering**: Proper sprite layering (clouds → terrain → coins → player)

#### 🪙 Collectible System
- **Collision Detection**: Precise coin collection mechanics
- **Real-time Counter**: Live coin count display
- **Animation**: Spinning coin animations with floating effects

## ⚙️ Configuration

### Game Settings (`settings.py`)
```python
# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Player mechanics
PLAYER_SPEED = 8
JUMP_STRENGTH = -16
GRAVITY = 0.8

# Visual settings
TILE_SIZE = 64
FPS = 60
```

### Customization Options
- **Difficulty**: Adjust player speed and jump strength
- **Graphics**: Replace sprite assets in graphics/ folders
- **Level Design**: Modify level_map in settings.py
- **Colors**: Customize fallback colors for sprites
- **Animation Speed**: Adjust frame rates for different sprites

## 🎨 Graphics Assets

### Asset Organization
- **Player Sprites**: 37 individual animation frames across 8 states
- **Terrain Tiles**: Multiple platform tile variations
- **Gold Coins**: 4-frame spinning animation
- **Palm Tree**: 4-frame swaying animation
- **Clouds**: 3 different cloud types for variety

### Graphics Requirements
- **Format**: PNG with alpha transparency
- **Naming**: Sequential numbering (1.png, 2.png, etc.)
- **Organization**: Folder-based categorization
- **Fallback**: Game works without graphics (colored shapes)

## 🐛 Troubleshooting

### Common Issues

**Game won't start:**
```bash
# Check Python version
python --version  # Should be 3.8+

# Verify pygame installation
python -c "import pygame; print(pygame.version.ver)"

# Activate virtual environment
source pygame-env/bin/activate
```

**Graphics not loading:**
- Verify graphics/ folder exists in game directory
- Check file permissions on graphics files
- Game will use colored fallback shapes if graphics fail

**Performance issues:**
- Close other applications
- Check system requirements
- Reduce FPS in settings.py if needed

### Debug Mode
The game includes comprehensive error handling and will continue running even if individual assets fail to load.

## 🚀 Deployment Options

### Local Play
- Run directly with `python main.py`
- Requires pygame environment

### Web Deployment
- Convert to web version using pygbag
- Host on static web servers
- See deployment guides for AWS/cloud hosting

### Distribution
- Package with PyInstaller for standalone executables
- Include graphics folder in distribution
- Test on target platforms

## 🎯 Game Design Philosophy

### Player Experience
- **Immediate Fun**: Game is playable within seconds
- **Progressive Challenge**: Platforms increase in difficulty
- **Clear Objectives**: Visual feedback for all game elements
- **Smooth Controls**: Responsive and predictable movement

### Technical Excellence
- **Clean Code**: Well-organized, documented codebase
- **Performance**: 60 FPS gameplay on modest hardware
- **Reliability**: Comprehensive error handling
- **Extensibility**: Easy to modify and expand

## 🏆 Achievements & Stats

### Completion Metrics
- **Total Coins**: 6 collectible gold coins
- **Platform Count**: 5+ challenging platform sections
- **Animation Frames**: 50+ individual sprite frames
- **Code Quality**: 500+ lines of clean, documented Python

### Performance Targets
- **Target FPS**: 60 frames per second
- **Load Time**: < 2 seconds on modern hardware
- **Memory Usage**: < 100MB RAM
- **Compatibility**: Python 3.8+ on Windows/Mac/Linux

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create feature branch
3. Follow existing code style
4. Test thoroughly
5. Submit pull request

### Code Standards
- **PEP 8**: Follow Python style guidelines
- **Documentation**: Comment complex logic
- **Error Handling**: Include try/except blocks
- **Performance**: Optimize for 60 FPS gameplay

## 📜 License

This game is created for educational and entertainment purposes. Graphics assets are from  PixelFrog https://pixelfrog-assets.itch.io/treasure-hunters. Code is available under MIT license.

## 🎮 Credits

- **Game Engine**: Python + Pygame
- **Graphics**: PirateMaker Asset Collection - PixelFrog
- **Development**: Platform Game Development Project
- **Inspiration**: Classic 2D platform adventures

---

## 🚀 Ready to Play?

```bash
source pygame-env/bin/activate
python main.py
```

**Embark on your pirate platform adventure today!** 🏴‍☠️⚓🌴

