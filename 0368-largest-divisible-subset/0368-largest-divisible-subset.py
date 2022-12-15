class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        fr = [-1]*N
        dp = [1]*N
        mi = 0
        ml = 1
        nums.sort()
        for i in range(1, N):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and dp[i] < 1+dp[j]:
                    dp[i] = 1+dp[j]
                    fr[i] = j
            if dp[i] > ml:
                ml = dp[i]
                mi = i
        res = []
        # print(mi, ml)
        # print(dp)
        # print(fr)
        while mi != -1:
            res.append(nums[mi])
            mi = fr[mi]
        
        return res[::-1]
        