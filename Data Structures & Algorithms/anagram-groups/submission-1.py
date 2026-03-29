class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_list = []
        anagram_dict = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        
        for v in anagram_dict.values():
            output_list.append(v)
        return output_list
