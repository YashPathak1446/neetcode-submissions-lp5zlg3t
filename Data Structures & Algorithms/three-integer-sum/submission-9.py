class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zero_sum_list = []
        nums.sort()

        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l != r:
                if nums[l] + nums[r] == target:
                    if [nums[i], nums[l], nums[r]] not in zero_sum_list:
                        zero_sum_list.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return zero_sum_list