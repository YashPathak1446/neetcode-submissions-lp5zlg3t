class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        curr_substr = s2[l:r]
        while r <= len(s2):
            if sorted(curr_substr) == sorted(s1):
                return True
            else:
                l += 1
                r += 1
                curr_substr = s2[l:r]
        return False 