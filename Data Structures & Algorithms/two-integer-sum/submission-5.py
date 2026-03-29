class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, 1
        while (nums[l] + nums[r]) != target:
            r += 1
            if r == len(nums):
                l += 1
                r = l + 1
        return [l, r]