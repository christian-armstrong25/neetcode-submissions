class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window
        l, r, profit = 0, 0, 0
        for r in range(len(prices)):
            if prices[r] - prices[l] > 0:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
        return profit

