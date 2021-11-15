grids = []
currGrid = []

file = open('SudokuGrids.txt', 'r')
for line in file.readlines():
    line = line.strip()
    if line.split()[0] == 'Grid':
        if currGrid != []:
            grids.append(currGrid)
        
        currGrid = []
    else:
        row = list(map(int, line))
        currGrid.append(row)

grids.append(currGrid)
file.close()

gridNumber = int(input(f'Enter the grid number (1 - {len(grids)}): '))
grid = grids[gridNumber - 1]

def possible(x, y, n):
    for row in range(9):
        if grid[row][x] == n:
            return False
    
    for col in range(9):
        if grid[y][col] == n:
            return False
    
    for subgridX in range(x // 3 * 3, x // 3 * 3 + 3):
        for subgridY in range(y // 3 * 3, y // 3 * 3 + 3):
            if grid[subgridY][subgridX] == n:
                return False
    
    return True

def solve():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                continue

            for n in range(1, 10):
                if possible(x, y, n):
                    grid[y][x] = n
                    solve()
                    grid[y][x] = 0

            return
    
    print()
    for row in grid:
        print(*row, sep = ' ')
    exit()

print()
for row in grid:
    print(*row, sep = ' ')

solve()