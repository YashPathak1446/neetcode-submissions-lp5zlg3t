class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0): return 0
        if (len(nums) == 1): return 1
        mappings = {}
        for num in nums:
            if num not in mappings: mappings[num] = num + 1

        i = 0
        prev = nums[i]
        count = 1
        maxCount = 1
        while (i != len(nums)):
            if mappings[prev] in mappings.keys():
                prev = mappings[prev]
                count += 1

            else:
                maxCount = max(maxCount, count)
                count = 1
                i+=1
                try:
                    prev = nums[i]
                except:
                    pass
        return maxCount
