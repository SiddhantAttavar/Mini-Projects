#include "game.h"
#include <string.h>
#include <stdlib.h>

// ============== HELPER FUNCTIONS ==============

// Classic Pacman-style maze (1 = wall, 0 = open space)
static const int MAZE[15][28] = {
    {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
    {1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1},
    {1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1},
    {1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1},
    {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1},
    {1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1,1},
    {1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1},
    {1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1},
    {1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1},
    {1,1,1,1,0,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,1,1,1,1},
    {1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1},
    {1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1},
    {1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1},
    {1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1},
    {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},
};

static bool is_wall(int x, int y) {
    if (x < 0 || x >= GRID_WIDTH || y < 0 || y >= GRID_HEIGHT) {
        return true;
    }
    return MAZE[y][x] == 1;
}

static bool can_move(int x, int y) {
    // Check bounds
    if (x < 0 || x >= GRID_WIDTH || y < 0 || y >= GRID_HEIGHT) {
        return false;
    }
    
    // Check if there's a wall
    return !is_wall(x, y);
}

static void move_entity(int *x, int *y, Direction dir, bool check_walls, Game *game) {
    (void)game;  // Suppress unused parameter warning
    
    int new_x = *x;
    int new_y = *y;
    
    switch (dir) {
        case DIR_UP:
            new_y--;
            break;
        case DIR_DOWN:
            new_y++;
            break;
        case DIR_LEFT:
            new_x--;
            break;
        case DIR_RIGHT:
            new_x++;
            break;
        case DIR_NONE:
            return;
    }
    
    // Wrap around edges
    if (new_x < 0) new_x = GRID_WIDTH - 1;
    if (new_x >= GRID_WIDTH) new_x = 0;
    if (new_y < 0) new_y = GRID_HEIGHT - 1;
    if (new_y >= GRID_HEIGHT) new_y = 0;
    
    // Check if movement is valid
    if (!check_walls || can_move(new_x, new_y)) {
        *x = new_x;
        *y = new_y;
    }
}

// ============== GAME FUNCTIONS ==============

void game_init(Game *game) {
    // Initialize Pacman
    game->pacman.x = 1;
    game->pacman.y = 1;
    game->pacman.dir = DIR_NONE;
    game->pacman.next_dir = DIR_NONE;
    game->pacman.speed = 6;  // Moves every 6 frames
    game->pacman.frame_counter = 0;
    
    // Initialize Ghosts at different corners
    Color ghost_colors[NUM_GHOSTS] = {RED, PINK, BLUE, ORANGE};
    int ghost_positions[NUM_GHOSTS][2] = {
        {13, 6},
        {12, 7},
        {14, 7},
        {13, 8}
    };
    
    for (int i = 0; i < NUM_GHOSTS; i++) {
        game->ghosts[i].x = ghost_positions[i][0];
        game->ghosts[i].y = ghost_positions[i][1];
        game->ghosts[i].dir = DIR_NONE;
        game->ghosts[i].speed = 7;  // Slightly slower than Pacman
        game->ghosts[i].frame_counter = 0;
        game->ghosts[i].color = ghost_colors[i];
    }
    
    // Initialize board with pellets
    memset(game->board, 0, sizeof(game->board));
    game->pellets_remaining = 0;
    
    for (int y = 0; y < GRID_HEIGHT; y++) {
        for (int x = 0; x < GRID_WIDTH; x++) {
            if (!is_wall(x, y)) {
                game->board[y][x] = true;
                game->pellets_remaining++;
            }
        }
    }
    
    // Initialize game state
    game->state = GAME_PLAYING;
    game->score = 0;
    game->lives = 3;
}

void game_handle_input(Game *game) {
    if (IsKeyPressed(KEY_UP)) {
        game->pacman.next_dir = DIR_UP;
    } else if (IsKeyPressed(KEY_DOWN)) {
        game->pacman.next_dir = DIR_DOWN;
    } else if (IsKeyPressed(KEY_LEFT)) {
        game->pacman.next_dir = DIR_LEFT;
    } else if (IsKeyPressed(KEY_RIGHT)) {
        game->pacman.next_dir = DIR_RIGHT;
    }
}

void game_update(Game *game) {
    if (game->state != GAME_PLAYING) {
        return;
    }
    
    // ========== UPDATE PACMAN ==========
    game->pacman.frame_counter++;
    
    if (game->pacman.frame_counter >= game->pacman.speed) {
        game->pacman.frame_counter = 0;
        
        // Try to move in the buffered direction
        int test_x = game->pacman.x;
        int test_y = game->pacman.y;
        move_entity(&test_x, &test_y, game->pacman.next_dir, true, game);
        
        if (test_x != game->pacman.x || test_y != game->pacman.y) {
            game->pacman.x = test_x;
            game->pacman.y = test_y;
            game->pacman.dir = game->pacman.next_dir;
        } else {
            // If buffered direction doesn't work, try current direction
            move_entity(&game->pacman.x, &game->pacman.y, game->pacman.dir, true, game);
        }
        
        // Check if Pacman collected a pellet
        if (game->board[game->pacman.y][game->pacman.x]) {
            game->board[game->pacman.y][game->pacman.x] = false;
            game->pellets_remaining--;
            game->score += 10;
        }
        
        // Check win condition
        if (game->pellets_remaining == 0) {
            game->state = GAME_WON;
        }
    }
    
    // ========== UPDATE GHOSTS ==========
    for (int i = 0; i < NUM_GHOSTS; i++) {
        game->ghosts[i].frame_counter++;
        
        if (game->ghosts[i].frame_counter >= game->ghosts[i].speed) {
            game->ghosts[i].frame_counter = 0;
            
            // Simple chase AI: calculate best direction towards Pacman
            int ghost_x = game->ghosts[i].x;
            int ghost_y = game->ghosts[i].y;
            int pacman_x = game->pacman.x;
            int pacman_y = game->pacman.y;
            
            // Calculate Manhattan distances in each direction
            int dist_up = (ghost_y > 0) ? abs(pacman_x - ghost_x) + abs(pacman_y - (ghost_y - 1)) : 999;
            int dist_down = (ghost_y < GRID_HEIGHT - 1) ? abs(pacman_x - ghost_x) + abs(pacman_y - (ghost_y + 1)) : 999;
            int dist_left = (ghost_x > 0) ? abs(pacman_x - (ghost_x - 1)) + abs(pacman_y - ghost_y) : 999;
            int dist_right = (ghost_x < GRID_WIDTH - 1) ? abs(pacman_x - (ghost_x + 1)) + abs(pacman_y - ghost_y) : 999;
            
            // Check which directions are valid (not walls)
            if (is_wall(ghost_x, ghost_y - 1)) dist_up = 999;
            if (is_wall(ghost_x, ghost_y + 1)) dist_down = 999;
            if (is_wall(ghost_x - 1, ghost_y)) dist_left = 999;
            if (is_wall(ghost_x + 1, ghost_y)) dist_right = 999;
            
            // Find best direction (smallest Manhattan distance)
            Direction best_dir = game->ghosts[i].dir;
            int best_dist = 999;
            
            if (dist_up < best_dist) {
                best_dist = dist_up;
                best_dir = DIR_UP;
            }
            if (dist_down < best_dist) {
                best_dist = dist_down;
                best_dir = DIR_DOWN;
            }
            if (dist_left < best_dist) {
                best_dist = dist_left;
                best_dir = DIR_LEFT;
            }
            if (dist_right < best_dist) {
                best_dist = dist_right;
                best_dir = DIR_RIGHT;
            }
            
            game->ghosts[i].dir = best_dir;
            move_entity(&game->ghosts[i].x, &game->ghosts[i].y, best_dir, true, game);
            
            // Check collision with Pacman
            if (game->ghosts[i].x == game->pacman.x && game->ghosts[i].y == game->pacman.y) {
                game->lives--;
                if (game->lives <= 0) {
                    game->state = GAME_LOST;
                } else {
                    // Reset Pacman position
                    game->pacman.x = 1;
                    game->pacman.y = 1;
                }
            }
        }
    }
}

void game_render(Game *game) {
    // Draw board (pellets and walls) - offset by info bar height
    for (int y = 0; y < GRID_HEIGHT; y++) {
        for (int x = 0; x < GRID_WIDTH; x++) {
            int px = x * TILE_SIZE;
            int py = y * TILE_SIZE + INFO_HEIGHT;
            
            if (is_wall(x, y)) {
                // Draw wall with border
                DrawRectangle(px, py, TILE_SIZE, TILE_SIZE, DARKBLUE);
                DrawRectangleLines(px, py, TILE_SIZE, TILE_SIZE, BLUE);
            } else if (game->board[y][x]) {
                // Draw pellet
                DrawCircle(px + TILE_SIZE/2, py + TILE_SIZE/2, 2, YELLOW);
            }
        }
    }
    
    // Draw Pacman (circle with animation) - offset by info bar height
    int pacman_x = game->pacman.x * TILE_SIZE + TILE_SIZE/2;
    int pacman_y = game->pacman.y * TILE_SIZE + TILE_SIZE/2 + INFO_HEIGHT;
    DrawCircle(pacman_x, pacman_y, 8, YELLOW);
    
    // Draw Pacman mouth (simple animation)
    int mouth_angle = (int)(GetTime() * 180) % 360;
    if (mouth_angle > 180) mouth_angle = 360 - mouth_angle;
    DrawRing((Vector2){pacman_x, pacman_y}, 6, 8, 45 - mouth_angle/2, 315 + mouth_angle/2, 20, YELLOW);
    
    // Draw Ghosts with eyes - offset by info bar height
    for (int i = 0; i < NUM_GHOSTS; i++) {
        int ghost_x = game->ghosts[i].x * TILE_SIZE;
        int ghost_y = game->ghosts[i].y * TILE_SIZE + INFO_HEIGHT;
        
        // Ghost body (rounded rectangle approximation)
        DrawRectangle(ghost_x, ghost_y + 4, TILE_SIZE, TILE_SIZE - 4, game->ghosts[i].color);
        DrawRectangle(ghost_x + 2, ghost_y, TILE_SIZE - 4, 6, game->ghosts[i].color);
        
        // Ghost eyes
        DrawCircle(ghost_x + 6, ghost_y + 6, 2, WHITE);
        DrawCircle(ghost_x + 14, ghost_y + 6, 2, WHITE);
        DrawCircle(ghost_x + 6, ghost_y + 6, 1, BLACK);
        DrawCircle(ghost_x + 14, ghost_y + 6, 1, BLACK);
    }
    
    // Draw UI background at top (doesn't cover play area)
    DrawRectangle(0, 0, SCREEN_WIDTH, INFO_HEIGHT, (Color){0, 0, 0, 200});
    DrawText(TextFormat("Score: %d", game->score), 10, 10, 16, YELLOW);
    DrawText(TextFormat("Lives: %d", game->lives), 200, 10, 16, RED);
    DrawText(TextFormat("Pellets: %d", game->pellets_remaining), 340, 10, 16, WHITE);
    DrawText("Arrow Keys", 10, 45, 12, WHITE);
    
    // Draw game state messages
    if (game->state == GAME_WON) {
        int text_width = MeasureText("YOU WON!", 40);
        DrawRectangle(0, 150, SCREEN_WIDTH, 120, (Color){0, 0, 0, 220});
        DrawText("YOU WON!", (SCREEN_WIDTH - text_width) / 2, 170, 40, GREEN);
        DrawText("Press SPACE to exit", 140, 230, 16, GREEN);
    } else if (game->state == GAME_LOST) {
        int text_width = MeasureText("GAME OVER!", 40);
        DrawRectangle(0, 150, SCREEN_WIDTH, 120, (Color){0, 0, 0, 220});
        DrawText("GAME OVER!", (SCREEN_WIDTH - text_width) / 2, 170, 40, RED);
        DrawText("Press SPACE to exit", 140, 230, 16, RED);
    }
}

void game_cleanup(Game *game) {
    // Nothing to clean up for now
    (void)game;
}
