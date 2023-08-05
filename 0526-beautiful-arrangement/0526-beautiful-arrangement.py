class Solution:
    def countArrangement(self, n: int) -> int:
        
        @lru_cache
        def dp(mask, pl):
            
            if pl == 0:
                return 1
            
            s = 0
            for i in range(n):
                if not (mask & (1 << i)) and (pl % (i+1) == 0 or (i+1) % pl == 0):
                    s += dp(mask | (1 << i), pl - 1)
            return s
        
        return dp(0, n)
        