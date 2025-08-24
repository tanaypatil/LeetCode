class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        mid = (n+m+1)//2
        l, r = 0, n
        
        while l <= r:
            cut1 = l + (r-l)//2
            cut2 = mid - cut1
            l1 = nums1[cut1-1] if cut1 > 0 else float('-inf')
            l2 = nums2[cut2-1] if cut2 > 0 else float('-inf')
            r1 = nums1[cut1] if cut1 < n else float('inf')
            r2 = nums2[cut2] if cut2 < m else float('inf')
            
            if l1 > r2:
                r = cut1-1
            elif l2 > r1:
                l = cut1+1
            else:
                if (n+m) & 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
                
        return -1
                
        