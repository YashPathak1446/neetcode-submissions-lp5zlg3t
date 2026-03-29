class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in ["+", "-", "*", "/"]:
                val = 0
                if tokens[i] == "+":
                    val = stack[-1] + stack[-2]
                elif tokens[i] == "-":
                    val = stack[-2] - stack[-1]
                elif tokens[i] == "*":
                    val = stack[-1] * stack[-2]
                elif tokens[i] == "/":
                    val =stack[-2] / stack[-1]
                stack.pop()
                stack.pop()
                stack.append(int(val))
                print(stack)
            else:
                stack.append(int(tokens[i]))
                print(stack)
        
        return stack[-1]