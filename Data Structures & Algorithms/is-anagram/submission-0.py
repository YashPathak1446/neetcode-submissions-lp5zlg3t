class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_list = list(s)
        for letter in t:
            if letter not in s_list: return False
            else: s_list.remove(letter)
        if len(s_list) != 0: return False
        return True
            
