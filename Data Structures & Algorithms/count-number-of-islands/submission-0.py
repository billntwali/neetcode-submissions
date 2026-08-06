class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    explore(grid, row, col, visited)
                    count += 1

        return count

def explore(grid, start_row, start_col, visited):
    rows = len(grid)
    cols = len(grid[0])

    stack = [(start_row, start_col)]

    while stack:
        row, col = stack.pop()

        if (row, col) in visited:
            continue

        if row < 0 or row >= rows:
            continue

        if col < 0 or col >= cols:
            continue

        if grid[row][col] == "0":
            continue

        visited.add((row, col))

        stack.append((row - 1, col))  # up
        stack.append((row + 1, col))  # down
        stack.append((row, col - 1))  # left
        stack.append((row, col + 1))  # right
        