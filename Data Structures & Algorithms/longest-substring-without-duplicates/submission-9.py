class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        r = 0
        visited = set()
        curr_string = ""
        len_longest = 0
        while (r < len(s)):
            if s[r] in curr_string:
                len_longest = max(len_longest, len(curr_string))
                curr_string = curr_string[curr_string.index(s[r]) + 1:]
            curr_string += s[r]
            r += 1
            
        len_longest = max(len(curr_string), len_longest)
        return len_longest