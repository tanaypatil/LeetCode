class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        MOD = 10**9+7
        for i in range(n):
            dp[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 * dp[i+1][j-1]
                    l, r = i+1, j-1
                    while s[l] != s[i]:
                        l += 1
                    while s[r] != s[i]:
                        r -= 1
                        
                    if l == r:
                        dp[i][j] += 1
                    elif l > r:
                        dp[i][j] += 2
                    else:
                        dp[i][j] -= dp[l+1][r-1]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                dp[i][j] = (dp[i][j] + MOD) % MOD
        return dp[0][-1]