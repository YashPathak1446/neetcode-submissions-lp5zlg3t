class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0

        for num in nums_set:
            curr_len = 1
            while num + 1 in nums_set:
                curr_len += 1
                num = num + 1
            max_len = max(max_len, curr_len)

        return max_len               
