class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        for c in coins:
            for j in range(1, amount+1):
                dp[j] = dp[j] + dp[j-c] if j >= c else dp[j]
        return dp[-1]
        