class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_count = dict()
        for i in range(len(nums)):
            if nums[i] not in num_count:
                num_count[nums[i]] = 1
            else:
                return nums[i]