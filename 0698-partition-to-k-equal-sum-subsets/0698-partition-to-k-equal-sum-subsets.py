class Solution:
    def canPartitionKSubsets(self, nums, k):
        s, n = sum(nums), len(nums)
        q, r = divmod(s, k)
        if r:
            return False
        
        def dp(k, mask=0, cs=0, j=0):
            if mask == (1<<n)-1:
                return True
            
            if cs == q:
                return dp(k-1, mask)
            
            for i in range(j, n):
                if not (mask & 1<<i) and cs + nums[i] <= q:
                    if dp(k, mask | 1<<i, cs+nums[i], i+1):
                        return True
                    if not cs:
                        break
            
            return False
        
        return dp(k, 0)