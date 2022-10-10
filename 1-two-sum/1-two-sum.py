
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i, a in enumerate(nums):
            indexes[a] = i
        for i, a in enumerate(nums):
            if (target-a in indexes) and indexes[target-a] != i:
                return [i, indexes[target-a]]
        return -1