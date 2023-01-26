class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs, gs = 0, float('-inf')
        for num in nums:
            cs += num
            gs = max(cs, gs)
            if cs < 0:
                cs = 0
        return gs
        