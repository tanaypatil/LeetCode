class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(i, last):
            if i >= len(stones)-1:
                return True
            
            for j in [last-1, last, last+1]:
                if stones[i]+j in exists and j > 0 and dp(exists[stones[i]+j], j):
                    return True
            return False
        
        exists = {stone:i for i, stone in enumerate(stones)}
        return dp(0, 0)