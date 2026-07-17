from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        directions = [
            [0, 1],
            [1, 0],
            [-1, 0],
            [0, -1]
        ]

        while queue:
            i, j, k = queue.popleft()
            for x, y in directions:
                nx = i + x
                ny = y + j
                if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] == -1 or grid[nx][ny] != 2147483647:
                    continue
                grid[nx][ny] = min(grid[nx][ny], k+1)
                queue.append((nx, ny, k+1))
        return