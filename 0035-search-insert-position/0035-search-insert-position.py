def bisect_left(arr, k):
    n = len(arr)
    l, r = 0, n
    while l < r:
        m = l + (r-l)//2
        if k <= arr[m]:
            r = m
        else:
            l = m + 1
    return l
    
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)