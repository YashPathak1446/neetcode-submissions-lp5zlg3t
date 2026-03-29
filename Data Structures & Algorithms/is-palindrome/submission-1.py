class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        s = s.lower()
        for letter in s:
            if (letter.isalnum()): newString += letter
        
        letter_idx = 0
        while (letter_idx < len(newString)//2):
            if newString[letter_idx] != newString[len(newString) - letter_idx - 1]:
                return False
            letter_idx += 1
        return True


        