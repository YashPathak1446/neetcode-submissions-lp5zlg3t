class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1
        
        res_list = []
        for num in nums:
            if zero_count > 1:
                res_list.append(0)
            else:
                if zero_count == 1:
                    if num == 0:
                        res_list.append(total_product)
                    else:
                        res_list.append(0)
                else:
                    res_list.append(int(total_product/num))
        
        return res_list
