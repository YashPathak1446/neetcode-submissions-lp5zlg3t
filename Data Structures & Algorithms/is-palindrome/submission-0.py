class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        s = s.lower()
        for letter in s:
            if letter.isalnum(): newString += letter
        print(newString)
        
        index = 0
        while (index < len(newString)//2):
            if newString[index] == newString[-1 - index]: index += 1
            else: return False
        return True