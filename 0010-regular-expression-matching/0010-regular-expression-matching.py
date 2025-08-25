class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        prev = [[False]*(n+1) for _ in range(2)]
        prev[-1][0] = True
        
        for i in range(m):
            dp = [False]*(n+1)
            dp[0] = prev[-1][0] or prev[-2][0] if p[i] == "*" else False
            for j in range(1, n+1):
                if p[i] == s[j-1] or p[i] == ".":
                    dp[j] = prev[-1][j-1]
                elif p[i] == "*":
                    dp[j] = prev[-1][j] or prev[-2][j]
                    if (p[i-1] == "." or p[i-1] == s[j-1]) and not dp[j]:
                        dp[j] = prev[-1][j-1] or dp[j-1]
            prev[-2] = prev[-1]
            prev[-1] = dp
        return prev[-1][-1]
                    
                
        