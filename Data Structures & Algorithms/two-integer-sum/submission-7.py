class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = dict()

        for i in range(len(nums)):
            value = target - nums[i]
            if value in sum_dict:
                return [sum_dict[value][0], i]

            sum_dict[nums[i]] = [i, value]
