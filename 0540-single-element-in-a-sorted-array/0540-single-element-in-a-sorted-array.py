class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if m != 0 and nums[m] == nums[m-1]:
                m -= 2
                if m < 0:
                    l = m + 3
                elif (m-l+1) & 1:
                    r = m
                else:
                    l = m + 3
            elif m != len(nums)-1 and nums[m] == nums[m+1]:
                m += 2
                if m > len(nums)-1:
                    r = m - 3
                elif (r-m+1) & 1:
                    l = m
                else:
                    r = m - 3
            else:
                return nums[m]
        return -1
        