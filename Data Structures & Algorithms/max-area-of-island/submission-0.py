class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == 0 or (i, j) in visited:
                return 0
            visited.add((i, j))
            return (1 + dfs(i, j+1)
            + dfs(i+1, j)
            + dfs(i, j-1)
            + dfs(i-1, j)
            )
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area, dfs(i, j))
        return max_area
        
