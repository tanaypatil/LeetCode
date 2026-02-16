class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T(i, j) = max(T(i, j-1), prices[j]-prices[m]+T(i-1, m))
        
        n = len(prices)
        
        def kTransactionMax(k):
            prev = [0]*n    
            for i in range(k):
                max_diff = -prices[0]
                dp = [0]*n
                for j in range(1, n):
                    dp[j] = max(dp[j-1], prices[j] + max_diff)
                    max_diff = max(max_diff, prev[j]-prices[j])
                prev = dp
            return prev[-1]
        
        return kTransactionMax(2)
                    
        