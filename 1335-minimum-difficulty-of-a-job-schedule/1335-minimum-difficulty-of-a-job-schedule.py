class Solution:
    def minDifficulty(self, nums: List[int], d: int) -> int:
        n = len(nums)
        if n < d: return -1
        
        @lru_cache(None)
        def dp(i, d):
            if i >= n: return 0 if not d else float('inf')
            if d == 1: return max(nums[i:])
            mx, ans = 0, float('inf')
            for j in range(i, n):
                mx = max(mx, nums[j])
                ans = min(ans, mx + dp(j+1, d-1))
            return ans
        
        ans = dp(0, d)
        return ans if ans != float('inf') else -1
        