class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 1
        curr_list = [nums[l]]
        while r < len(nums):
            if r - l <= k:
                if nums[r] in curr_list:
                    return True
                curr_list.append(nums[r])
                r += 1
            
            else:
                curr_list.remove(nums[l])
                l += 1
        return False