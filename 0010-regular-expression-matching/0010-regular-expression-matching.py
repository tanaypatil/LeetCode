class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]
        p = " " + p
        s = " " + s
        dp[0][0] = True
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] or dp[i-2][0] if p[i] == "*" else False
            for j in range(1, m+1):
                if p[i] == s[j] or p[i] == ".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i-2][j] or ((dp[i-1][j-1] or dp[i][j-1]) and (s[j] == p[i-1] or p[i-1] == "."))
        return dp[-1][-1]