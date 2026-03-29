class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        four_sum_list = []

        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                l = j + 1
                r = len(nums) - 1
                while l != r:
                    if nums[i] + nums[j] + nums[l] + nums[r] == target:
                        sorted_list = sorted([nums[i], nums[j], nums[l], nums[r]])
                        if sorted_list not in four_sum_list:
                            four_sum_list.append(sorted_list)
                        l += 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return four_sum_list
                    