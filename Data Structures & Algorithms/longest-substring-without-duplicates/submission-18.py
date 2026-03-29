class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0 
        r = 1
        curr_substr = s[0]
        substr_set = set(s[0])
        max_len = 1

        while r < len(s):
            if s[r] not in substr_set:
                curr_substr += s[r]
                substr_set.add(s[r])
                r += 1
            else:
                max_len = max(r - l, max_len)
                substr_set.remove(s[l])
                l += 1
        max_len = max(r - l, max_len)
        return max_len