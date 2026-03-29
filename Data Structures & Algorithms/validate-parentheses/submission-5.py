class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        for char in s:
            if char == ")" or char == "}" or char == "]":
                if len(stack) == 0:
                    return False
                if char == "}" and stack[-1] == "{":
                    stack.pop()
                elif char == ")" and stack[-1] == "(":
                    stack.pop()
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(char)

        if len(stack) != 0:
            return False
        return True
