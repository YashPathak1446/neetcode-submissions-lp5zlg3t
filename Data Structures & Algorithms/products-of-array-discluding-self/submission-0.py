class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = [1] * len(nums)

        for i in range(len(nums)):
            for k in range(len(result_arr)):
                if i != k:
                    result_arr[i] *= nums[k]
        
        return result_arr
