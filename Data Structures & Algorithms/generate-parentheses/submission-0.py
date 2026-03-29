class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        curr_stack = []
        result_array = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                result_array.append("".join(curr_stack))
                return

            if openN < n:
                curr_stack.append("(")
                backtrack(openN + 1, closeN)
                curr_stack.pop()
            
            if closeN < openN:
                curr_stack.append(")")
                backtrack(openN, closeN + 1)
                curr_stack.pop()
        
        backtrack(0, 0)
        return result_array
