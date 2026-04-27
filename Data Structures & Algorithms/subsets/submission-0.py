class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        k = len(nums)
        subset_nums = []
        curr_subset = []
        
        def recurse(i):
            if i >= len(nums):
                subset_nums.append(curr_subset[:])
                return
            curr_subset.append(nums[i])
            recurse(i+1)
            curr_subset.pop()
            recurse(i+1)

        recurse(0)
        return subset_nums