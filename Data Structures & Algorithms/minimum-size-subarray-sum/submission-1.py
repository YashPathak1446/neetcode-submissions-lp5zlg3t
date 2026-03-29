class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0

        l = 0
        r = 1
        curr_sum = nums[l]
        min_len = len(nums)
        while r < len(nums):
            if curr_sum >= target:
                min_len = min(min_len, r - l)
                curr_sum -= nums[l]
                l += 1
            else:
                curr_sum += nums[r]
                r += 1
        while curr_sum >= target:
            min_len = min(min_len, r - l)
            curr_sum -= nums[l]
            l += 1
        return min_len
