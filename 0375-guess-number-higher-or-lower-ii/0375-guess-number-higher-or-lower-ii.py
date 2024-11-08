class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        @lru_cache(None)
        def dp(start, end):
            if start >= end:
                return 0
            
            if end-start == 1:
                return start
            
            if end-start == 2:
                return start+1
            
            ans = float('inf')
            for i in range(start, end+1):
                m = max(i+dp(start, i-1), i+dp(i+1, end))
                ans = min(ans, m)
                
            return ans
        
        return dp(1, n)