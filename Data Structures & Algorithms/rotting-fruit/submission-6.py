from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
        
        directions = [
            [0, 1],
            [1, 0], 
            [-1, 0],
            [0,-1]
        ]
        max_time = 0

        while queue:
            i, j, k = queue.popleft()
            for dx, dy in directions:
                nx = i + dx
                ny = j + dy
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == 0 or grid[nx][ny] == 2:
                    continue
                grid[nx][ny] = 2
                queue.append((nx, ny, k+1))
            max_time = max(k, max_time)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return max_time


