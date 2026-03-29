class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alnum_string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                alnum_string += s[i]
        for i in range(len(alnum_string)//2):
            if alnum_string[i] != alnum_string[len(alnum_string) - 1 - i]:
                return False

        return True