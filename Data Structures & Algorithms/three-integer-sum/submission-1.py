class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return_list = []
        for i in range(len(nums)):
            target = 0 - nums[i]
            hashmap = dict()
            for num in nums[i+1:]:
                value = target - num
                if value in hashmap:
                    new_arr = sorted([nums[i], num, value])
                    if new_arr not in return_list:
                        return_list.append(new_arr)
                hashmap[num] = value

        return return_list