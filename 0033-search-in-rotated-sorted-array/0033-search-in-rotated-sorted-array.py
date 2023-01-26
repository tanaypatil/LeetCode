class Solution:
    def search(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l, r = 0, n-1
        
        while l <= r:
            m = l + (r-l)//2
            if arr[m] == k:
                return m
            elif arr[l] <= arr[m]:
                if arr[l] <= k <= arr[m]:
                    r = m
                else:
                    l = m+1
            else:
                if arr[m] <= k <= arr[r]:
                    l = m
                else:
                    r = m-1
        return -1
            
        