# Pacman Clone - C with Raylib

A simple Pacman game clone written in C using the raylib graphics library.

## Features

- **Pacman Movement**: Use arrow keys to navigate the maze
- **Ghost AI**: 4 ghosts with simple random movement AI
- **Pellet Collection**: Eat all pellets to win the game
- **Score System**: Gain 10 points per pellet collected
- **Lives System**: Start with 3 lives, lose one when hit by a ghost
- **Win/Lose Conditions**: Win by eating all pellets, lose when out of lives
- **Animated Graphics**: Pacman mouth animation, ghost eyes, and smooth rendering

## Building

```bash
cd /home/sidat/programming/Mini-Projects/C/pacman
make
```

## Running

```bash
./pacman
```

Or use the Makefile shortcut:
```bash
make run
```

## Controls

- **Arrow Keys**: Move Pacman up, down, left, or right
- **Space**: Exit after game ends (win/lose)

## Game Rules

1. Move Pacman to eat all yellow pellets on the board
2. Avoid the 4 colored ghosts (Red, Pink, Blue, Orange)
3. When a ghost catches you, you lose a life
4. Collect all pellets before losing all 3 lives to win
5. Score points (10 per pellet) to see your final score

## File Structure

```
pacman/
├── main.c              Main game loop and entry point
├── game.h              Game structures and function declarations
├── game.c              Core game logic, rendering, and physics
├── Makefile            Build configuration
└── raylib/             Raylib library (built locally)
```

## Game Architecture

### Game State (`Game` struct)
- Pacman position and direction
- 4 Ghost positions and directions
- Board with pellet locations
- Score, lives, and game state

### Game Loop
1. **Input**: Read arrow key presses and buffer direction
2. **Update**: Move Pacman and ghosts, check collisions, update score
3. **Render**: Draw maze, pellets, Pacman, ghosts, and UI
4. **Frame Control**: 60 FPS via raylib

### Movement System
- Pacman and ghosts move on a grid (20x20 pixels per tile)
- Movement is frame-based (happens every N frames)
- Direction buffering allows smooth turn-ahead input

### Collision Detection
- Wall collisions prevent movement
- Pellet collection on same tile
- Ghost collision ends game or resets Pacman

### Ghost AI
- Simple random direction changes
- Wraps around screen edges
- No chase algorithm (only random wandering)

## Future Enhancements

Possible improvements to make:
- Advanced ghost AI (chase vs. scatter modes)
- Power-ups (temporary ghost invulnerability)
- Multiple levels with increasing difficulty
- Sound effects
- High score tracking
- Animated sprites
- Power-up pellets for aggressive gameplay

## Compilation Details

- **Compiler**: GCC with C99 standard
- **Graphics**: Raylib 5.0 (latest stable)
- **Linking**: OpenGL 3.3, system libraries
- **Executable Size**: ~1.1 MB

## License

Educational project for learning C and game development.
