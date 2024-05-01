class Solution:
    def integerBreak(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(i, p, s):
            # print(i, p, s)
            if i > (int(n**(0.5)) + 1) or s >= n:
                if s == n:
                    return p
                return float('-inf')
            return max(float('-inf'), dp(i, p*i, s+i), dp(i+1, p*i, s+i), dp(i+1, p, s))
        
        return max(dp(1, 1, 0), 1) if n > 2 else 1
            
        