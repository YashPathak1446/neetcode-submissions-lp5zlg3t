class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        three_sum_list = []

        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]

            while l < r:
                if nums[l] + nums[r] == target:
                    if [nums[i], nums[l], nums[r]] not in three_sum_list:
                        three_sum_list.append([nums[i], nums[l], nums[r]])
                    l += 1
            
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1

        return three_sum_list