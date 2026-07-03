class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        flow_both_oceans = []
        # if pacific, no need to go up and left
        # if atlantic, no need to go right and down
        visited = set()
        pacific_visited = set()
        atlantic_visited = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(i, j, visited):
            visited.add((i, j))
            for di, dj in directions:
                ni = di + i
                nj = dj + j
                if ni < 0 or nj < 0 or ni >= len(heights) or nj >= len(heights[0]) or (ni, nj) in visited or heights[ni][nj] < heights[i][j]:
                    continue
                dfs(ni, nj, visited) 
                
        
        for i in range(len(heights)):
            dfs(i, 0, pacific_visited)
        for j in range(len(heights[0])):
            dfs(0, j, pacific_visited)

        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, atlantic_visited)
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, atlantic_visited)
        
        
        return list(pacific_visited & atlantic_visited)