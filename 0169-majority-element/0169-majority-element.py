class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        me, count = nums[0], 0
        for i, a in enumerate(nums):
            count = count + 1 if a == me else count - 1
            if count == 0:
                count = 1
                me = a
        return me
        