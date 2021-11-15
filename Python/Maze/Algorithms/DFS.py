from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

def solve(maze, curr, end):
    row, col = curr
    print(row, col)
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
        return []
    
    if maze[row][col]:
        return []

    if curr == end:
        return [curr]

    maze[row][col] = 1
    res = float('inf')
    up = solve(maze, (row - 1, col), end)
    down = solve(maze, (row + 1, col), end)
    left = solve(maze, (row, col - 1), end)
    right = solve(maze, (row, col + 1), end)

    if (up, down, left, right) == ([]) * 4:
        return []
    else:
        return [curr] + min(up, down, left, right, key = lambda x: len(x) if len(x) > 0 else float('inf'))
