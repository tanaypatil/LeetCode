class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, a in enumerate(nums):
            while (0 < nums[i] <= len(nums)) and nums[i] != nums[nums[i]-1]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
        for i, a in enumerate(nums):
            if a != i+1:
                return i+1
        return len(nums)+1
        