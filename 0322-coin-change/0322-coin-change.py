class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        dp = [0]*(amount+1)
        for i in range(1, amount+1):
            dp[i] = float('inf') if i%coins[0] else i//coins[0]
            
        for i in range(1, len(coins)):
            for j in range(1, amount+1):
                not_taken = dp[j]
                taken = float('inf')
                if not j%coins[i]:
                    taken = j//coins[i]
                if j >= coins[i]:
                    taken = min(taken, 1+dp[j-coins[i]])
                dp[j] = min(taken, not_taken)
            # print(dp)
        
        return -1 if dp[-1] == float('inf') else dp[-1]