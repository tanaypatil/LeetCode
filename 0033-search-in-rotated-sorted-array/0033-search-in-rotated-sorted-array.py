class Solution:
    def search(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)-1
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == k:
                return m
            if arr[l] <= arr[m]:
                if arr[l] <= k <= arr[m]:
                    r = m
                else:
                    l = m + 1
            else:
                if arr[m+1] <= k <= arr[r]:
                    l = m + 1
                else:
                    r = m
            
            
        return -1