# Platform Game

## Version 2 (v2)

An enhanced platform jumping game with a vertical level design, where the objective is to reach a flag at the top of the level.

### Features
- Player can move left/right and jump
- Vertical level design with platforms to climb
- Goal-oriented gameplay (reach the flag)
- Stopwatch to track completion time
- Start and Retry buttons
- Camera that follows the player both horizontally and vertically
- Web browser compatibility using Pygbag

### How to Play
- Use the **Left/Right arrow keys** to move
- Press **Spacebar** to jump
- Click the **START** button to begin the timer
- Navigate through platforms to reach the yellow flag at the top
- Click the **RETRY** button to restart the game

### Running the Game (Desktop)
```bash
cd platform_game/v2
python main.py
```

### Running the Game (Web Browser)
The game can be played in a web browser using WebAssembly technology.

#### Building for Web
```bash
cd platform_game/v2
pygbag --build .
```

This will create a `build/web` directory containing the necessary files for web deployment.

#### Running Locally in Browser
```bash
cd platform_game/v2
pygbag --port 8000 .
```

Then open a web browser and navigate to `http://localhost:8000`.

#### Deploying to AWS
To deploy the web version to AWS:

1. Upload all files from the `build/web` directory to an S3 bucket configured for static website hosting
2. Configure CloudFront for global distribution (optional)
3. Access the game through your S3 website endpoint or CloudFront URL

## Requirements

### Version 1
- Python 3.x
- Pygame

### Version 2
- Python 3.x
- Pygame
- Pygbag (for web browser deployment)

## Installation

```bash
# Install Pygame
pip install pygame

# For web browser deployment
pip install pygbag
```

## Code Structure (v2)

- `main.py`: Entry point and game loop
- `settings.py`: Game constants and level design
- `player.py`: Player class with movement and physics
- `level.py`: Level management and win condition
- `tiles.py`: Platform and flag objects

## Credits

This platform game was inspired by the PirateMaker project (https://github.com/clear-code-projects/PirateMaker) and adapted for educational purposes.
