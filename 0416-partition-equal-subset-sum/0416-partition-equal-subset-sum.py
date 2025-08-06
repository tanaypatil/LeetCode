class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1:
            return False
        s //= 2

        prev = [False]*(s+1)
        prev[0] = True

        for num in nums:
            dp = [False]*(s+1)
            dp[0] = True
            for j in range(1, s+1):
                dp[j] = prev[j] if (j < num) else (prev[j] or prev[j-num])
            prev = dp
        return prev[-1]
        