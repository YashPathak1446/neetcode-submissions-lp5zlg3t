class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_nums = []
        sum_list = []

        def dfs(i):
            if sum(curr_nums) > target or i >= len(nums):
                return
            if sum(curr_nums) == target:
                sum_list.append(curr_nums[:])
                return
            
            curr_nums.append(nums[i])
            dfs(i)
            curr_nums.pop()
            dfs(i+1)
            

        dfs(0)
        return sum_list