class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < (len(asteroids)):
            if len(stack) == 0:
                stack.append(asteroids[i])
            else:
                if stack[-1] > 0 and asteroids[i] > 0:
                    stack.append(asteroids[i])
                elif stack[-1] < 0 and asteroids[i] < 0:
                    stack.append(asteroids[i])
                else:
                    if stack[-1] < 0:
                        stack.append(asteroids[i])
                    elif abs(stack[-1]) == abs(asteroids[i]):
                        stack.pop()
                    elif abs(stack[-1]) < abs(asteroids[i]):
                        stack.pop()
                        i-=1
            i += 1
        return stack