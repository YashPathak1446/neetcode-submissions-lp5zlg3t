class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        l = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                k -= 1
            else:
                nums[l] = nums[i]
                l += 1
            i += 1

        return k