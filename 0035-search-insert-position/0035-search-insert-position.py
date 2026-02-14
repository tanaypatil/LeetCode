class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def b_left(nums, target):
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            return l
        return b_left(nums, target)
        