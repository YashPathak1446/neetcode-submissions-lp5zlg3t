class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = dict()
        for i in range(len(nums)):
            if nums[i] not in countDict:
                countDict[nums[i]] = 1
            else:
                countDict[nums[i]] += 1
            
        count = 0
        sorted_values = []
        for v in countDict.values():
            sorted_values.append(v)
        sorted_values.sort(reverse=True)
        sorted_values = sorted_values[:k]
        output_list = []
        for key in countDict:
            if countDict[key] in sorted_values:
                output_list.append(key)
        
        return output_list
