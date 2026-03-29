class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums)

        for num in nums:
            if num-1 not in nums_set:
                curr_length = 1                
                while (num+1) in nums_set:
                    curr_length += 1
                    num = num + 1
                max_length = max(curr_length, max_length)

        return max_length
