class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return True
            if nums[l] <= nums[m]:
                if nums[l] == nums[m]:
                    l += 1
                elif nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if nums[m] == nums[r]:
                    r -= 1
                elif nums[m] <= target <= nums[r]:
                    l = m
                else:
                    r = m - 1
        return False