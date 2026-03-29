class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            if (ord(char.lower()) >= 97 and ord(char.lower()) <= 122) or (ord(char) >= 48 and ord(char) <= 57):
                new_str += char.lower()
    
        for i in range(int(len(new_str)/2)):
            if new_str[i] != new_str[len(new_str) - i - 1]:
                return False
    
        return True