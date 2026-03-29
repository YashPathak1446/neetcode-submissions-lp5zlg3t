class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        l = 0
        r = 1
        curr_set = set(s[l])
        max_len = 1
        curr_len = 1
        while r != len(s):
            if s[r] in curr_set:
                max_len = max(max_len, curr_len)
                curr_set.remove(s[l])
                l += 1
                curr_len -= 1
            else:
                curr_set.add(s[r])
                r += 1
                curr_len += 1
            
        return max(max_len, curr_len)
        
        return max_len
