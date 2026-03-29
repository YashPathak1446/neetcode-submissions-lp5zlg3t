class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        elif len(s) == 1: return 1
        start = 0
        end = 1
        maxLen = 1
        currString = s[start:end]
        while end != len(s):
            if s[end] not in currString:
                end += 1
                try:
                    currString = s[start:end]
                except: 
                    pass
            else:
                maxLen = max(maxLen, len(currString))
                start += 1
                end = start + 1
                currString = s[start:end]
        maxLen = max(maxLen, len(currString))
        return maxLen