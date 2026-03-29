class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left should be min and right should be  max
        l = 0
        r = 1
        maxProfit = 0
        if (len(prices) == 0 or len(prices) == 1): return 0
        while (r != len(prices)):
            if (prices[r] <= prices[l]):
                l = r
            else:
                currProfit = prices[r] - prices[l]
                maxProfit = max(currProfit, maxProfit)
            r += 1
        return maxProfit