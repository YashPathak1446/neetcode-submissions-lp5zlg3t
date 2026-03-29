class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram_dict = dict()

        for word in strs:
            sorted_key = "".join(sorted(word))
            if sorted_key in group_anagram_dict:
                group_anagram_dict[sorted_key].append(word)
            else:
                group_anagram_dict[sorted_key] = [word]
            
        output_list = []
        for v in group_anagram_dict.values():
            output_list.append(list(v))
        return output_list