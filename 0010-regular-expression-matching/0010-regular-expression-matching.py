class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]
        prev = [[False]*(m+1) for _ in range(2)]
        prev[1][0] = True
        p = " " + p
        s = " " + s
        dp[0][0] = True
        for i in range(1, n+1):
            dp = [False]*(m+1)
            dp[0] = prev[-1][0] or prev[-2][0] if p[i] == "*" else False
            for j in range(1, m+1):
                if p[i] == s[j] or p[i] == ".":
                    dp[j] = prev[-1][j-1]
                elif p[i] == "*":
                    dp[j] = prev[-1][j] or prev[-2][j] or ((prev[-1][j-1] or dp[j-1]) and (s[j] == p[i-1] or p[i-1] == "."))
            prev[0] = prev[1]
            prev[1] = dp
        return prev[-1][-1]