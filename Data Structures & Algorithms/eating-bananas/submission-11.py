import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        if len(piles) == h:
            return r
        
        k = r
        while l <= r:
            mid = (l+r)//2
            current_hours = 0
            for i in range(len(piles)):
                current_hours += math.ceil(piles[i]/mid)
            
            if current_hours <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k