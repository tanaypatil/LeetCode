class Solution:
    def check(self, left_sorted, right_sorted):
        l, r = 0, 0
        while l < len(left_sorted) and r < len(right_sorted):
            if abs(left_sorted[l][1] - right_sorted[r][1]) <= self.valueDiff:
                if right_sorted[r][0] - left_sorted[l][0] <= self.indexDiff:
                    self.ans = True
                    break
                else:
                    l += 1
            else:
                if left_sorted[l][1] < right_sorted[r][1]:
                    l += 1
                else:
                    r += 1
    
    def merge(self, left_sorted, right_sorted):
        l, r = 0, 0
        final_sorted = []
        while l < len(left_sorted) and r < len(right_sorted):
            if left_sorted[l][1] < right_sorted[r][1]:
                final_sorted.append(left_sorted[l])
                l += 1
            else:
                final_sorted.append(right_sorted[r])
                r += 1
                
        while l < len(left_sorted):
            final_sorted.append(left_sorted[l])
            l += 1
            
        while r < len(right_sorted):
            final_sorted.append(right_sorted[r])
            r += 1
            
        return final_sorted
    
    
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left_sorted = self.merge_sort(arr[:mid])
        right_sorted = self.merge_sort(arr[mid:])
        
        self.check(left_sorted, right_sorted)
        
        return self.merge(left_sorted, right_sorted)
        
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        self.ans = False
        self.valueDiff = valueDiff
        self.indexDiff = indexDiff
        self.merge_sort([*enumerate(nums)])
        return self.ans