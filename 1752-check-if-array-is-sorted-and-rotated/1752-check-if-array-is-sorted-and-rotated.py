class Solution:
    def check(self, nums: List[int]) -> bool:
        i = f = 0
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                f = 1
                break
        if not f:
            return True
        for j in range(i+1, len(nums)-1):
            if nums[j+1] < nums[j]:
                return False
        return nums[0] >= nums[-1]
        