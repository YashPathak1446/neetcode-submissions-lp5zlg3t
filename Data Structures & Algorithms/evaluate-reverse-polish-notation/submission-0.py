class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            else:
                num2 = int(stack[-1])
                num1 = int(stack[-2])
                stack.pop()
                stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1/num2))
        return int(stack[0])