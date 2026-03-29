class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l

        if nums[-1] >= target:
            r = len(nums) - 1
        else:
            r = pivot - 1
            l = 0
        
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

                