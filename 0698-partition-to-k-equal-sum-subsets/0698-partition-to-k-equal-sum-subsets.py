class Solution:
    def canPartitionKSubsets(self, nums, k):
        s, n = sum(nums), len(nums)
        q, r = divmod(sum(nums), k)
        nums.sort(reverse=True)
        if r or nums[0] > q: return False
        
        
        def dp(rest_k, mask, curr_sum=0, next_index=0):
            if rest_k == 1:
                return True
            
            if curr_sum == q:
                return dp(rest_k-1, mask)
            
            for i in range(next_index, n):
                if not (mask & (1<<i)) and curr_sum + nums[i] <= q:
                    if dp(rest_k, mask | (1<<i), curr_sum + nums[i], i+1):
                        return True
                    if not curr_sum: break
            return False
        
        return dp(k, 0)