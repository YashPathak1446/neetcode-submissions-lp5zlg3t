class Solution:
    def tribonacci(self, n: int) -> int:
        memo = dict()

        def dfs(curr_num):
            if curr_num in memo:
                return memo[curr_num]
            if curr_num == 0:
                return 0
            if curr_num == 1:
                return 1
            if curr_num == 2:
                return 1
            memo[curr_num] = dfs(curr_num - 1) + dfs(curr_num - 2) + dfs(curr_num - 3)
            return memo[curr_num]
        
        return dfs(n)