class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        smap = {}
        for i, num in enumerate(nums):
            if target-num in smap:
                return smap[target-num], i
            smap[num] = i
        return -1, -1
        