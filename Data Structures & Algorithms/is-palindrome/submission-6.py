class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new_string += s[i].lower()
        
        for i in range(len(new_string)//2):
            if new_string[i] != new_string[len(new_string) - 1 - i]:
                return False
        
        return True