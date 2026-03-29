class Solution:
    def mySqrt(self, x: int) -> int:
        curr_sqrt = 0
        for i in range(x + 1):
            if i * i <= x:
                curr_sqrt = i
            else:
                break
        return curr_sqrt