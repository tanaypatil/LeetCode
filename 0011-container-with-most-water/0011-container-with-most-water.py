class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        n = len(height)
        l, r = 0, n-1
        
        while l < r:
            m = max(m, (r-l)*(min(height[l], height[r])))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m
        