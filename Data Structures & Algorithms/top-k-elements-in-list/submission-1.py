class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        values = []

        for v in hashmap.values():
            values.append(v)
        values.sort(reverse=True)
        values = values[:k]

        res_arr = []
        for k in hashmap:
            if hashmap[k] in values:
                res_arr.append(k)

        return res_arr