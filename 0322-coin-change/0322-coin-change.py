class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for a in range(1, amount+1):
                if a >= coin:
                    dp[a] = min(1+dp[a-coin], dp[a])
        return dp[-1] if dp[-1] != float('inf') else -1