class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_counter = dict()

        for i in range(len(nums)):
            if nums[i] not in freq_counter:
                freq_counter[nums[i]] = 1
            else:
                freq_counter[nums[i]] += 1
        
        majority_elements = []

        for k in freq_counter:
            if freq_counter[k] > len(nums) // 3:
                majority_elements.append(k)
        
        return majority_elements