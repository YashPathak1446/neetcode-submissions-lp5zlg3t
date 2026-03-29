class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        if len(nums_set) == 1:
            return 1
        max_len = 0
        curr_len = 1
        for num in nums:
            while num + 1 in nums_set:
                curr_len += 1
                num = num + 1
            max_len = max(max_len, curr_len)
            curr_len = 1
        
        return max_len