class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, ans = [], 0
        
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                ans = max(ans, h*(index-i))
                start = i
            stack.append((start, height))
        
        while stack:
            i, h = stack.pop()
            ans = max(ans, h*(len(heights)-i))
        return ans
                