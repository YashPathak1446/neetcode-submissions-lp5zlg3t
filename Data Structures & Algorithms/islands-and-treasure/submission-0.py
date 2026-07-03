from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        count = 0
        while queue:
            i, j = queue.popleft()
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if ni >= len(grid) or ni < 0 or nj >= len(grid[0]) or nj < 0 or grid[ni][nj] == -1:
                    continue
                elif grid[ni][nj] != 2147483647:
                    grid[ni][nj] = min(grid[i][j] + 1, grid[ni][nj])
                else:
                    grid[ni][nj] = grid[i][j] + 1
                    queue.append((ni, nj))

        return None
        