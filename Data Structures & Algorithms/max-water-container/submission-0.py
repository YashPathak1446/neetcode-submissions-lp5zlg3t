class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while (l != r):
            minHeight = min(heights[l], heights[r])
            currArea = (r - l) * minHeight
            maxArea = max(currArea, maxArea)
            if minHeight == heights[r]:
                r = r-1
            else:
                l = l + 1

        return maxArea