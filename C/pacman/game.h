#ifndef GAME_H
#define GAME_H

#include "raylib/src/raylib.h"

// ============== CONSTANTS ==============
#define SCREEN_WIDTH 560
#define SCREEN_HEIGHT 600
#define INFO_HEIGHT 80
#define PLAY_HEIGHT (SCREEN_HEIGHT - INFO_HEIGHT)
#define TILE_SIZE 20
#define GRID_WIDTH (SCREEN_WIDTH / TILE_SIZE)
#define GRID_HEIGHT (PLAY_HEIGHT / TILE_SIZE)
#define NUM_GHOSTS 4

// Game states
typedef enum {
    GAME_PLAYING,
    GAME_WON,
    GAME_LOST,
    GAME_OVER
} GameState;

// Direction enum
typedef enum {
    DIR_UP,
    DIR_DOWN,
    DIR_LEFT,
    DIR_RIGHT,
    DIR_NONE
} Direction;

// ============== STRUCTURES ==============

// Pacman structure
typedef struct {
    int x, y;           // Grid position
    Direction dir;      // Current direction
    Direction next_dir; // Buffered next direction
    int speed;          // Movement speed (frames per move)
    int frame_counter;  // Counter for movement timing
} Pacman;

// Ghost structure
typedef struct {
    int x, y;           // Grid position
    Direction dir;      // Current direction
    int speed;          // Movement speed
    int frame_counter;  // Counter for movement timing
    Color color;        // Ghost color
} Ghost;

// Game state structure
typedef struct {
    Pacman pacman;
    Ghost ghosts[NUM_GHOSTS];
    
    // Board state
    bool board[GRID_HEIGHT][GRID_WIDTH];  // true = pellet, false = empty
    int pellets_remaining;
    
    // Game status
    GameState state;
    int score;
    int lives;
    
} Game;

// ============== FUNCTIONS ==============

// Game initialization and management
void game_init(Game *game);
void game_update(Game *game);
void game_render(Game *game);
void game_handle_input(Game *game);
void game_cleanup(Game *game);

#endif
