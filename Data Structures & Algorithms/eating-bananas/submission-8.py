import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        max_k = max(piles)
        
        l = 1
        r = max_k
        while l <= r:
            mid = (r+l)//2
            current_hours = 0
            for i in range(len(piles)):
                current_hours += math.ceil(piles[i]/mid)
            if current_hours > h:
                l = mid + 1
            else:
                max_k = mid
                r = mid - 1
        
        return max_k