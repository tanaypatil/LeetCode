class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, n):
            dp.append(max(dp[i-1], nums[i]+dp[i-2]))
        return dp[-1]
        