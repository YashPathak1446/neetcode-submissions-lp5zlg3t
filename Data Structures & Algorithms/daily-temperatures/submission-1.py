class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if (len(temperatures)) <= 1:
            return [0]
        l = 0
        r = 1
        result = []
        while l < len(temperatures) - 1:
            if r == len(temperatures):
                result.append(0)
                l += 1
                r = l + 1
            elif temperatures[l] < temperatures[r]:
                result.append(r-l)
                l += 1
                r = l + 1
            else:
                r += 1
        result.append(0)
        return result