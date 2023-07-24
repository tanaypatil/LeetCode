class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m-1] < nums[m] > nums[m+1]:
                # print(m-1, m, m+1)
                # print(nums[m-1], nums[m], nums[m+1])
                return m-1
            elif nums[m] < nums[m-1]:
                r = m
            else:
                l = m + 1
        return -1