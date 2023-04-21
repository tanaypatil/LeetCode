class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        s //= 2
        prev = [False]*(s+1)
        prev[0] = True
        for i in range(len(nums)):
            dp = [False]*(s+1)
            dp[0] = True
            for j in range(1, s+1):
                dp[j] = prev[j-nums[i]] or prev[j] if j >= nums[i] else prev[j]
            prev = dp
            # print(dp)
        return prev[-1]
        