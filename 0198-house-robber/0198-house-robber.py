class Solution:
    def rob(self, nums: List[int]) -> int:
        f = nums[0]
        if len(nums) == 1:
            return f
        s = max(nums[:2])
        for i in range(2, len(nums)):
            f, s = s, max(s, f+nums[i])
        return s
        