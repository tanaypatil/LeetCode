class Solution:
    def merge(self, l, m, r):
        merged = []
        lo, hi = m+1, m+1
        for i in range(l, m+1):
            while lo <= r and Solution.nums[lo]-Solution.nums[i] < Solution.lower:
                lo += 1
            while hi <= r and Solution.nums[hi]-Solution.nums[i] <= Solution.upper:
                hi += 1
            Solution.count += hi-lo
        i, j = l, m+1
        while i <= m and j <= r:
            if Solution.nums[i] > Solution.nums[j]:
                merged.append(Solution.nums[j])
                j += 1
            else:
                merged.append(Solution.nums[i])
                i += 1
        
        while i <= m:
            merged.append(Solution.nums[i])
            i += 1
        
        while j <= r:
            merged.append(Solution.nums[j])
            j += 1
            
        Solution.nums[l:r+1] = merged
        
    def merge_sort(self, l, r):
        if l >= r:
            return
        m = l + (r-l)//2
        self.merge_sort(l, m)
        self.merge_sort(m+1, r)
        self.merge(l, m, r)
    
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        Solution.lower = lower
        Solution.upper = upper
        prefix = [0] + list(accumulate(nums))
        Solution.nums = prefix
        Solution.count = 0
        self.merge_sort(0, len(prefix)-1)
        return Solution.count
        