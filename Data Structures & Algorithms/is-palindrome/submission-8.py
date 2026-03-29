class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                alnum_string += s[i].lower()

        l = 0
        r = len(alnum_string) - 1
        while l < r:
            if alnum_string[l] != alnum_string[r]:
                return False
            l += 1
            r -= 1
        return True