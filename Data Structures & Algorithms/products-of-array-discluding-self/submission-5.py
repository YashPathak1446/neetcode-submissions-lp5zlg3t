class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1
        
        prod_array = []

        if zero_count == 0:
            for num in nums:
                prod_array.append(total_product//num)
        elif zero_count > 1:
            prod_array = [0] * len(nums)
        else:
            for num in nums:
                if num != 0:
                    prod_array.append(0)
                else:
                    prod_array.append(total_product)
        
        return prod_array