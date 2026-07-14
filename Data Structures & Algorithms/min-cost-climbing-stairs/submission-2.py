class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = dict()
        # track as min cost to reach top of the staircase

        def dfs(curr_step):
            if curr_step in memo:
                return memo[curr_step]
            if curr_step >= len(cost):
                return 0
            memo[curr_step] = cost[curr_step] + min(dfs(curr_step + 1), dfs(curr_step + 2))
            return memo[curr_step]
        
        return min(dfs(0), dfs(1))
