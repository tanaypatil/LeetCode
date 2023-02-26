class Solution:
    def is_possible(self, nums, s, k):
        c = 0
        for n in nums:
            c += n
            if c > s:
                k -= 1
                c = n
        return k > 0
    
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        
        while l < r:
            mid = l + (r-l)//2
            if self.is_possible(nums, mid, k):
                r = mid
            else:
                l = mid + 1
        return l
        