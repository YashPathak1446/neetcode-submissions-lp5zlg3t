class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_nums = []
        sum_list = []

        def dfs(i):
            if sum(curr_nums) > target or i >= len(nums):
                return
            elif sum(curr_nums) == target:
                sum_list.append(curr_nums[:])
                return
            else:
                curr_nums.append(nums[i])
                dfs(i)
            if curr_nums:
                curr_nums.pop()
                dfs(i+1)
            

        dfs(0)
        return sum_list