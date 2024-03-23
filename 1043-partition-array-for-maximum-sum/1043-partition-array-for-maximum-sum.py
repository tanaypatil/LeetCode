class Solution: 
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            
            ans = float('-inf')
            max_in_subarr = float('-inf')
            for j in range(i, min(i+k, n)):
                max_in_subarr = max(max_in_subarr, nums[j])
                ans = max(ans, dp(j+1) + max_in_subarr*(j-i+1))
            return ans
        
        return dp(0)
        