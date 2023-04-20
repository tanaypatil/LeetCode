class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = deque()
        
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                max_area = max(max_area, h*(index-i))
                start = i
            stack.append((start, height))
            
        while stack:
            start, height = stack.pop()
            max_area = max(max_area, (len(heights)-start)*height)
        return max_area