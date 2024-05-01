class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def dp(i, p, s):
            return (p if s == n else float('-inf')) if (i > (int(n**(0.5)) + 1) or s >= n) else max(float('-inf'), dp(i, p*i, s+i), dp(i+1, p*i, s+i), dp(i+1, p, s))
        return dp(1, 1, 0) if n > 2 else 1
            
        