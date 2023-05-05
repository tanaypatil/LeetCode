class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs, gs = 0, float('-inf')
        for num in nums:
            cs += num
            gs = max(gs, cs)
            if cs < 0:
                cs = 0
        return gs
        