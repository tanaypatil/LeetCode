class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        ret = []
        for i, a in enumerate(nums):
            s += a
            ret.append(s)
        return ret