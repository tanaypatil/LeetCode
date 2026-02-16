class Solution:
    @cache
    def dp(self, i, cs):
        if i < 0:
            return 1 if cs == self.target else 0
        positive = self.dp(i-1, cs+self.nums[i])
        negative = self.dp(i-1, cs-self.nums[i])
        return positive + negative
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target
        return self.dp(len(nums)-1, 0)