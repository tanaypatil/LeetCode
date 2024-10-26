class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        
        @lru_cache(None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (k - 1):
                return inf
            
            if i == j:
                return 0 if m == 1 else float('inf')
            
            if m == 1:
                return dp(i, j, k) + prefix[j+1] - prefix[i]
            
            ans = float('inf')
            for t in range(i, j, k-1):
                ans = min(ans, dp(i, t, 1) + dp(t+1, j, m-1))
            return ans
        
        res = dp(0, n-1, 1)
        return res if res != float('inf') else -1
        