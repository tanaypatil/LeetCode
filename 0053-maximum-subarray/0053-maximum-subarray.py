class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        ls = nums[0]
        gs = nums[0]
        for i, a in enumerate(nums[1:]):
            if ls < 0:
                ls = 0
            ls += a
            gs = max(gs, ls)
        return gs
        