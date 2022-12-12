class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        s //= 2
        prev = [False]*(s+1)
        dp = [False]*(s+1)
        prev[0] = True
        for i in range(len(nums)):
            for j in range(s+1):
                if nums[i] > j: continue
                if nums[i] == j or prev[j] or prev[j-nums[i]]:
                    dp[j] = True
            prev = [dp[j] for j in range(s+1)]
        return dp[-1]
        
        