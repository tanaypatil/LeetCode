class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def maxProfitK(k, prices):
            n = len(prices)
            prev = [0]*n
            
            for i in range(k):
                dp = [0]*n
                maxDiff = -prices[0]
                for j in range(1, n):
                    dp[j] = max(dp[j-1], prices[j]+maxDiff)
                    maxDiff = max(maxDiff, prev[j]-prices[j])
                prev = dp
            return prev[-1]
        return maxProfitK(2, prices)
        