class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        @lru_cache(None)
        def dp(i):
            if i >= n: return 0
            m = ans = float('-inf')
            for j in range(i, min(i+k, n)):
                m = max(m, arr[j])
                ans = max(ans, m*(j-i+1) + dp(j+1))
            return ans
        return dp(0)