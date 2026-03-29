class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        three_sum_lst = []

        for i in range(len(sorted_nums) - 2):
            target = 0 - sorted_nums[i]
            l = i + 1
            r = len(sorted_nums) - 1
            while l < r:
                if sorted_nums[l] + sorted_nums[r]== target:
                    if [sorted_nums[i], sorted_nums[l], sorted_nums[r]] not in three_sum_lst:
                        three_sum_lst.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return three_sum_lst

                
