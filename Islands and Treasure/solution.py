def islandsAndTreasure(self, grid) -> None:

    ROWS, COLS = len(grid), len(grid[0])    
    
    def bfs(r, c):
        queue = collections.deque()
        queue.append((r, c))
        distance = 1

        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < ROWS and 0 <= new_col < COLS:
                        if grid[new_row][new_col] > distance:
                            grid[new_row][new_col] = distance
                            queue.append((new_row, new_col))

            distance += 1

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                bfs(r, c)
