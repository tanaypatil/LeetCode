class Solution:
    def dfs(self, i, curr, arr, sarr):
        if i == len(arr):
            sarr.add(curr)
            return
        
        self.dfs(i+1, curr+arr[i], arr, sarr)
        self.dfs(i+1, curr, arr, sarr)
        
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        set1, set2 = set(), set()
        n = len(nums)
        self.dfs(0, 0, nums[:n//2], set1)
        self.dfs(0, 0, nums[n//2:], set2)
        
        set2 = sorted(set2)
        ans = float('inf')
        for s in set1:
            remaining = goal-s
            i = bisect_right(set2, remaining)
            if i < len(set2):
                ans = min(ans, abs(set2[i]-remaining))
            if i > 0:
                ans = min(ans, abs(set2[i-1]-remaining))
                
        return ans if ans != float('-inf') else -1
                