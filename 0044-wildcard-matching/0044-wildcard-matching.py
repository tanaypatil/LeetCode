class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        prev = [False]*(m+1)
        
        prev[0] = True
        
        for i in range(1, n+1):
            dp = [False]*(m+1)
            if p[i-1] == "*":
                dp[0] = prev[0]
            for j in range(1, m+1):
                if p[i-1] == "?" or p[i-1] == s[j-1]:
                    dp[j] = prev[j-1]
                elif p[i-1] == "*":
                    dp[j] = dp[j-1] or prev[j-1] or prev[j]
            prev = dp
            
        return prev[-1]
                    
        