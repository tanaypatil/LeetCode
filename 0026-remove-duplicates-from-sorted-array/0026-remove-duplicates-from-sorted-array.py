class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = i+1
        last_num = nums[0]
        while i < len(nums)-1:
            while j < len(nums) and nums[j] == last_num:
                j += 1
            if j >= len(nums):
                break
            nums[i+1] = nums[j]
            i += 1
            last_num = nums[i]
        return i+1
        