class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest_seq_len = 0
        curr_seq_len = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums) - 1):
            # skip
            if nums[i] == nums[i+1]:
                continue
            # actual cases
            if nums[i] == nums[i+1] - 1:
                curr_seq_len += 1
            else:
                longest_seq_len = max(longest_seq_len, curr_seq_len)
                curr_seq_len = 1

        return max(longest_seq_len, curr_seq_len)