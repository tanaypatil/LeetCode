class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        csp = gsp = csn = gsn = 0
        for num in nums:
            csp += num
            csn += (-num)
            gsp = max(gsp, abs(csp))
            gsn = max(gsn, abs(csn))
            if csp < 0: csp = 0
            if csn < 0: csn = 0
        return max(gsn, gsp)
        