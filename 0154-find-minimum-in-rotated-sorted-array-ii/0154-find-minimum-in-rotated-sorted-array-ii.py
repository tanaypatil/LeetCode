class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            # print(l, m , r)
            if nums[l] <= nums[r]:
                if nums[l] == nums[r]:
                    l += 1
                else:
                    return nums[l]
            elif nums[l] == nums[m]:
                l += 1
            elif nums[l] < nums[m]:
                l = m + 1
            elif nums[m] == nums[r]:
                r -= 1
            else:
                r = m
        return nums[r]
                    
        