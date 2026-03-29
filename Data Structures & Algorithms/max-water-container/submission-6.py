class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        currArea = min(heights[l],heights[r])*(r-l)
        maxArea = currArea
        while l!=r:
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            # print("L:",heights[l], "R:", heights[r])
            currArea = min(heights[l],heights[r])*(r-l)
            maxArea = max(currArea, maxArea)
        return maxArea