class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        @lru_cache(None)
        def dp(i, last):
            # print(i, last)
            if i >= len(stones)-1:
                # print("Returning True")
                return True
            
            for j in [last-1, last, last+1]:
                if stones[i]+j in exists and j > 0:
                    # print(f"From {stones[i]} to {stones[i]+j}")
                    if dp(exists[stones[i]+j], j):
                        return True
            return False
        
        exists = {}
        for i, stone in enumerate(stones):
            exists[stone] = i
        return dp(0, 0)