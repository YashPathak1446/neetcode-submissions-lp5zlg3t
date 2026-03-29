class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = []

        anagram_dict = dict()

        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = [word]
            else:
                anagram_dict[sorted_word].append(word)
            
        
        for v in anagram_dict.values():
            anagram_list.append(v)
        
        return anagram_list