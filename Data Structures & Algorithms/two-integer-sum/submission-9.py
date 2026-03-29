class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_dict = dict()

        for i in range(len(nums)):
            other_num = target - nums[i]

            if other_num in nums_dict:
                return [nums_dict[other_num], i]
            
            nums_dict[nums[i]] = i
                