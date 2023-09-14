class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        @lru_cache(None)
        def dp(i, k, curr_count, curr_sum):
            if i >= n:
                return 0
            if not k:
                return float('-inf') # if i < n else 0
            curr_avg = (curr_sum + nums[i])/(curr_count + 1)
            return max(curr_avg + dp(i+1, k-1, 0, 0), dp(i+1, k, (curr_count + 1), (curr_sum + nums[i])))
        
        return dp(0, k, 0, 0)
            
            
        