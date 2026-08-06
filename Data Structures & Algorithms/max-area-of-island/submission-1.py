class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        maximum = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maximum = max(maximum, explore(grid, row, col, visited))

        return maximum

def explore(grid, f_row, f_col, visited):
    rows = len(grid)
    cols = len(grid[0])
    individual = 0
    stack = [(f_row, f_col)]

    while stack:
        row, col = stack.pop()

        if (row, col) in visited:
            continue
        if row < 0 or row >= rows:
            continue
        if col < 0 or col >= cols:
            continue
        if grid[row][col] == 0:
            continue
        if grid[row][col] == 1:
            individual += 1
        visited.add((row, col))
    
        stack.append((row-1, col))
        stack.append((row+1, col))
        stack.append((row, col+1))
        stack.append((row, col-1))
    return individual        