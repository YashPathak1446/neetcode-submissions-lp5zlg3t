class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = dict()
        num_set = set()
        for num in nums:
            num_set.add(num)
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        values_list = list(num_dict.values())
        top_k_freq_values = sorted(values_list)[::-1][0:k]
        num_list = []

        for num in num_set:
            if num_dict[num] in top_k_freq_values:
                num_list.append(num)

        return num_list