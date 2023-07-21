class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while j < len(nums):
            if not nums[j]:
                j += 1
            else:
                nums[i] = nums[j]
                i += 1
                j += 1
        while i < len(nums):
            nums[i] = 0
            i += 1
        