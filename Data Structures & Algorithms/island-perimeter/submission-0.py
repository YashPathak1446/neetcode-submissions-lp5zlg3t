class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        # check the nearest neighbors for each cell on +-1 vertically and horizontally
        i = 0
        j = 0
        total_perimeter = 0

        def find_start_island(grid):
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] == 1:
                        return x, y
        
        # Set start index of island
        i, j = find_start_island(grid)
        visited = set()
        def dfs(i, j):
            # if out of bounds, or water, return 1
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[i]) or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            curr_perimeter = 0
            curr_perimeter += dfs(i, j+1)
            curr_perimeter += dfs(i+1, j)
            curr_perimeter += dfs(i-1, j)
            curr_perimeter += dfs(i, j-1)
                    
            return curr_perimeter

        
        total_perimeter = dfs(i, j)
        return total_perimeter