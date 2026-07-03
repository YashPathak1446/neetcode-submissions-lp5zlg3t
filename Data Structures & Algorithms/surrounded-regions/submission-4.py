class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j, visited):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "X" or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i, j+1, visited)
            dfs(i+1, j, visited)
            dfs(i, j-1, visited)
            dfs(i-1, j, visited)
            return
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O":
                    visited = set()
                    dfs(i, j, visited)
                    contains_edge = False
                    print(visited)
                    for x, y in visited:
                        if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1:
                            contains_edge = True
                            break
                    if not contains_edge:
                        for x, y in visited:
                            board[x][y] = "X"
        return 
