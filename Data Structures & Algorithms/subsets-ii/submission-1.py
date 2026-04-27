class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset_lst = []
        curr_subset = []

        def dfs(i):
            if sorted(curr_subset) not in subset_lst:
                subset_lst.append(sorted(curr_subset[:]))
            if i >= len(nums):
                return
            curr_subset.append(nums[i])
            dfs(i+1)
            curr_subset.pop()
            dfs(i+1)

        dfs(0)
        return subset_lst