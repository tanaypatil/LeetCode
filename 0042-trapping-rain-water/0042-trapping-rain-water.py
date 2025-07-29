class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = []
        water = 0
        for index, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                i = stack.pop()
                if not stack:
                    continue
                water += (min(heights[stack[-1]], height) - heights[i])  * (index-stack[-1]-1)
            stack.append(index)
        return water
        