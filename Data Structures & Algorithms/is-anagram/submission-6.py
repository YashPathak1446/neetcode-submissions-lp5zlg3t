class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        dict_s = dict()
        dict_t = dict()

        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1
        
        for j in range(len(t)):
            if t[j] not in dict_t:
                dict_t[t[j]] = 1
            else:
                dict_t[t[j]] += 1
        

        for k in dict_s:
            if dict_t.get(k, 0) == 0 or dict_s[k] != dict_t[k]:
                return False
    
        return True