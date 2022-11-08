class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        minSum = 0
        currSum = 0
        totalSum = 0
        n = len(nums)
        for i, a in enumerate(nums):
            totalSum += a
            currSum += a
            if i < n-k:
                minSum += a
            else:
                currSum -= nums[i-(n-k)]
                minSum = min(minSum, currSum)
        return totalSum-minSum
        