class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        n = len(ring)
        
        @lru_cache(None)
        def dp(i, j):
            if j == len(key):
                return 0
            
            ans = float('inf')
            c = 0
            for k in range(n):
                if ring[(i+k) % n] == key[j]:
                    ans = min(ans, k + 1 + dp((i+k) % n, j+1))
                # print(i, k, j)
                if ring[(i-k+n)%n] == key[j]:
                    ans = min(ans, k + 1 + dp((i-k+n) % n, j+1))
            return ans
        
        return dp(0, 0)
        