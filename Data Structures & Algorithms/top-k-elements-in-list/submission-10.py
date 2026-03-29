class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict()

        for i in range(len(nums)):
            if nums[i] not in freq_map:
                freq_map[nums[i]] = 1
            else:
                freq_map[nums[i]] += 1
        values_list = []
        for v in freq_map.values():
            values_list.append(v)
        values_list.sort()
        values_list = values_list[::-1][:k]

        top_k_lst = []

        for k in freq_map:
            if freq_map[k] in values_list:
                top_k_lst.append(k)

        return top_k_lst