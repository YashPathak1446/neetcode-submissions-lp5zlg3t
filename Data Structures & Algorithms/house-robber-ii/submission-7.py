class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = dict()

        if len(nums) == 1:
            return nums[0]

        def dfs(i, zero):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                if zero:
                    return 0
            if (i, zero) in memo:
                return memo[(i, zero)]
            if i == 0:
                memo[(i, zero)] = max(nums[i] + dfs(i+2, True), dfs(i+1, False))
            else:
                memo[(i, zero)] = max(nums[i] + dfs(i+2, zero), dfs(i+1, zero))
            return memo[(i, zero)]
        
        return dfs(0, True)