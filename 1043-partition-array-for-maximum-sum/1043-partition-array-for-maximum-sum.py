class Solution: 
    def maxSumAfterPartitioning(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(l):
            if l >= n:
                return 0
            m = max_sum = 0
            for i in range(l, min(n, l+k)):
                m = max(m, nums[i])
                max_sum = max(max_sum, m*(i-l+1) + dp(i+1))
            return max_sum
        
        return dp(0)
        