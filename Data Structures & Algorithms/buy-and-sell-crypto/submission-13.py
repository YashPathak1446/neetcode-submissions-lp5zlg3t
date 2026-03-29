class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1
        while (r < len(prices)):
            if prices[r] >= prices[l]:
                if prices[r] - prices[l] > max_profit:
                    max_profit = prices[r] - prices[l]
                r += 1
            
            elif prices[l] > prices[r]:
                l += 1
                r = l + 1


            
        return max_profit