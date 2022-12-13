class Solution:
    def dp(self, i, cs, target):
        if i < 0:
            return 1 if cs == target else 0
        
        if (i, cs) in Solution.mem:
            return Solution.mem[(i, cs)]
        
        positive = self.dp(i-1, cs+Solution.nums[i], target)
        negative = self.dp(i-1, cs-Solution.nums[i], target)
        
        Solution.mem[(i, cs)] = positive + negative
        
        return positive + negative
        
        
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        Solution.nums = nums
        Solution.mem = {}
        return self.dp(len(nums)-1, 0, target)