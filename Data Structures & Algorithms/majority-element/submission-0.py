class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_criteria = len(nums) // 2
        nums_dict = dict()
        
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
        
        for k, v in nums_dict.items():
            if v >= majority_criteria:
                return k