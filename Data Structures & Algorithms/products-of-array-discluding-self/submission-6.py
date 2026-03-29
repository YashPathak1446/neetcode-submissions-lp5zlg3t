class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                total_prod *= nums[i]
        
        prod_array = []
        for i in range(len(nums)):
            if zero_count == 0:
                prod_array.append(total_prod//nums[i])
            elif zero_count == 1:
                if nums[i] == 0:
                    prod_array.append(total_prod)
                else:
                    prod_array.append(0)
            else:
                prod_array.append(0)
        
        return prod_array