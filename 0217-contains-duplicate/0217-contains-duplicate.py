class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num, count in Counter(nums).items():
            if count > 1:
                return True
        return False
        