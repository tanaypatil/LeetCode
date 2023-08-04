class Solution:
    def canPartitionKSubsets(self, nums, k):
        N = len(nums)
        nums.sort(reverse = True)

        basket, rem = divmod(sum(nums), k)
        if rem or nums[0] > basket: return False

        dp = [-1] * (1<<N) 
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                neib = dp[mask ^ (1<<j)]
                if mask & (1<<j) and neib >= 0 and neib + nums[j] <= basket:
                    dp[mask] = (neib + nums[j]) % basket
                    break

        return dp[-1] == 0