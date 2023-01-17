class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        c = 0
        for i, a in enumerate(nums):
            if s-a-c == c:
                return i
            c += a
        return -1
        