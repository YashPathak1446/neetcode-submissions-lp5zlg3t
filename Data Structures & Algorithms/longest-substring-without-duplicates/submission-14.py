class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        r = 1
        curr_substr = s[l]
        longest_length = 1
        curr_length = 1
        while (r < len(s)):
            if s[r] not in curr_substr:
                curr_substr += s[r]
                curr_length += 1
                r += 1
            else:
                longest_length = max(longest_length, curr_length)
                l += 1
                if len(curr_substr) == 1:
                    curr_substr = ""
                else:
                    curr_substr = curr_substr[1:]
                curr_length -= 1
        return max(longest_length, curr_length)