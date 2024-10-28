class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(None)
        def dfs(i, rem):
            if i >= n:
                return 1 if not rem else 0
            
            ans = 0
            for j in range(1, k+1):
                if j <= rem:
                    ans += dfs(i+1, rem-j)
            return ans
        
        return dfs(0, target) % (10**9+7)