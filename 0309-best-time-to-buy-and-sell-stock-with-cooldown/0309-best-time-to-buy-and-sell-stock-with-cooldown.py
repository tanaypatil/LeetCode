class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(day, last_action):
            if day >= len(prices): return 0
            profit = dp(day+1, last_action)
            if last_action == "sell":
                profit = max(profit, dp(day+1, "buy") - prices[day])
            else:
                profit = max(profit, dp(day+2, "sell") + prices[day])
            return profit
        
        return dp(0, "sell")
        