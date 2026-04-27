class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset_lst = []
        curr_subset = []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                subset_lst.append(curr_subset[:])
                return
                
            curr_subset.append(nums[i])
            dfs(i + 1)
            curr_subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return subset_lst
        