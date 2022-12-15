class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for i in range(len(prices) + 2)] for x in range(2)]
        
		# Bottom Up so start from last day to first
        for i in range(len(prices) - 1, -1, -1):
			# Use our DP Formulas !!!!!
            dp[0][i] = max(-prices[i] + dp[1][i + 1], dp[0][i + 1])
            dp[1][i] = max(prices[i] + dp[0][i + 2], dp[1][i + 1])
		# We want to return the max for BUYING at Day 0
		# We can't sell if we haven't bought a stock yet. (Requirement #2)
        return dp[0][0]
        