class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @lru_cache(None)
        def dp(l, r):
            if r-l == 1:
                return 0
            
            ans = float('inf')
            for cut in cuts:
                if l < cut < r:
                    ans = min(ans, (r-l) + dp(l, cut) + dp(cut, r))
            return ans if ans != float('inf') else 0
        
        return dp(0, n)