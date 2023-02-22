def bisect_left(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = l + (r-l)//2
        if x <= arr[m]:
            r = m
        else:
            l = m + 1
    return l


def bisect_right(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = l + (r-l)//2
        if x >= arr[m]:
            l = m + 1
        else:
            r = m
    return l-1
    

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l, r = bisect_left(nums, target), bisect_right(nums, target)
        # print(l, r)
        if l < len(nums):
            l = l if nums[l] == target else -1
        else:
            l = -1
        if r < len(nums):
            r = r if nums[r] == target else -1
        else:
            r = -1
        return [l, r]