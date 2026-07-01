class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        num_islands = 0
        def dfs(i, j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == "0" or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i-1, j)
            return
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    num_islands += 1
        return num_islands
        