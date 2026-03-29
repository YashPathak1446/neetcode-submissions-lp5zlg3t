class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while(r < len(prices)):
            curr_profit = prices[r] - prices[l]
            if curr_profit > max_profit:
                max_profit = curr_profit
            elif prices[r] < prices[l]:
                l += 1
                r = l
            r += 1
        return max_profit