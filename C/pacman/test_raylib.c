#include "raylib/src/raylib.h"

int main(void) {
    // Initialize window
    InitWindow(800, 600, "Raylib Test");
    SetTargetFPS(60);

    // Main game loop
    while (!WindowShouldClose()) {
        // Clear background
        BeginDrawing();
        ClearBackground(BLACK);
        
        // Draw test text
        DrawText("Raylib is working!", 300, 280, 20, WHITE);
        DrawRectangle(100, 100, 200, 200, RED);
        
        EndDrawing();
    }

    CloseWindow();
    return 0;
}
