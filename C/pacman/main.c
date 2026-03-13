#include "game.h"

int main(void) {
    // Initialize window
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "Pacman Clone");
    SetTargetFPS(60);
    
    // Initialize game
    Game game;
    game_init(&game);
    
    // Main game loop
    while (!WindowShouldClose()) {
        // Handle input
        game_handle_input(&game);
        
        // Update game state
        game_update(&game);
        
        // Allow exit after game ends
        if (game.state != GAME_PLAYING && IsKeyPressed(KEY_SPACE)) {
            break;
        }
        
        // Render
        BeginDrawing();
        ClearBackground(BLACK);
        game_render(&game);
        EndDrawing();
    }
    
    // Cleanup
    game_cleanup(&game);
    CloseWindow();
    
    return 0;
}
