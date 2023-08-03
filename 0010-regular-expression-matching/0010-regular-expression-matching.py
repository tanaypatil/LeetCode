class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        p, s = " " + p, " " + s
        
        prev = [[False]*(m+1) for _ in range(2)]
        prev[1][0] = True
        
        for i in range(1, n+1):
            
            dp = [False]*(m+1)
            dp[0] = prev[-1][0] or prev[-2][0] if p[i] == "*" else False
            
            for j in range(1, m+1):
                
                if p[i] == s[j] or p[i] == ".":
                    dp[j] = prev[-1][j-1]
                elif p[i] == "*":
                    dp[j] = prev[-1][j] or prev[-2][j]
                    if (s[j] == p[i-1] or p[i-1] == ".") and not dp[j]:
                        dp[j] = dp[j] or prev[-1][j-1] or dp[j-1]
                    
            prev[0] = prev[1]
            prev[1] = dp
        
        return prev[-1][-1]