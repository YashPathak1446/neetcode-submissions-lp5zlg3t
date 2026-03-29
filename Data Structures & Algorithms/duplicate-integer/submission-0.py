class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for index in range(len(nums)):
            if nums[index] in nums[index + 1:]: return True
        return False