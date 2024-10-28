class Solution:
    def minDifficulty(self, nums: List[int], d: int) -> int:
        n = len(nums)
        if n < d: return -1
        
        @lru_cache(None)
        def dp(i, d):
            if d == 1:
                return max(nums[i:])
            
            res = float('inf')
            maxd = 0
            
            for j in range(i, n-(d-1)):
                maxd = max(maxd, nums[j])
                res = min(res, maxd + dp(j+1, d-1))
            
            return res
        
        return dp(0, d)
        