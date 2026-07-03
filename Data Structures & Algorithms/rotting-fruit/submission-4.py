from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        directions = [
            (0, 1),
            (1, 0),
            (-1, 0),
            (0, -1)
        ]
        max_count = 0
        while queue:
            i, j, k = queue.popleft()
            for di, dj in directions:
                ni = di + i
                nj = dj + j
                if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]) or grid[ni][nj] == 0 or grid[ni][nj] == 2:
                    continue
                else:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, k+1))
                max_count = max(max_count, k+1)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return max_count
