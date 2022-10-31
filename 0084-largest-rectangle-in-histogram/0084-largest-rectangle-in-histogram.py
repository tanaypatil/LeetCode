class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = deque()
        n = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[0][1] > h:
                index, height = stack.popleft()
                max_area = max(max_area, height*(i-index))
                start = index
            stack.appendleft((start, h))
        
        while stack:
            index, height = stack.popleft()
            max_area = max(max_area, height*(n-index))
            
        return max_area