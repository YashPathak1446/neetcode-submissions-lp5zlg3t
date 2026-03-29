class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        hashmap = dict()
        # key : key + 1
        for num in nums:
            hashmap[num] = num + 1
        
        curr_len = 1
        max_len = 1

        for i in range(len(nums)):
            curr = nums[i]
            while hashmap[curr] in hashmap:
                curr_len += 1
                curr = hashmap[curr]
            max_len = max(max_len, curr_len)
            curr_len = 1
        return max_len
                
