class Solution:
    def findMin(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        min_num = arr[0]
        while l <= r:
            m = l + (r-l)//2
            if arr[l] <= arr[m]:
                min_num = min(min_num, arr[l])
                l = m + 1
            else:
                min_num = min(min_num, arr[m+1])
                r = m
        return min_num