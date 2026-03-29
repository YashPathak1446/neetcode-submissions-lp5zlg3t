class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = [] # pair [temp, index]

        for i in range(len(temperatures)):
            count = i
            while(stack and temperatures[i] > stack[-1][0]):
                temp, index = stack.pop()
                output[index] = i - index
            
            stack.append([temperatures[i], i])
            
        return output
                