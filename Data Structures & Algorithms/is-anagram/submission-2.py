class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = dict()
        for letter in s:
            if letter not in anagram_dict:
                anagram_dict[letter] = 1
            else:
                anagram_dict[letter] += 1
        for letter in t:
            if letter in anagram_dict:
                anagram_dict[letter] -= 1
            else:
                return False
        
        for value in anagram_dict.values():
            if value != 0:
                return False
        return True