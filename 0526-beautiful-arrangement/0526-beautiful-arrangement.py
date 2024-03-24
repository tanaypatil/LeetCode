class Solution:
    def countArrangement(self, n: int) -> int:
        
        @lru_cache
        def dp(pos, mask=0):
            if not pos:
                return 1
        
            s = 0
            
            for i in range(n):
                if not (mask & 1<<i) and (not (pos % (i+1)) or not ((i+1) % pos)):
                    s += dp(pos-1, mask | 1<<i)
            
            return s
        
        return dp(n)