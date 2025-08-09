class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, max_height = [], 0
        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1] >= height:
                pidx, h = stack.pop()
                max_height = max(max_height, h*(index-pidx))
                start = pidx
            stack.append((start, height))
        while stack:
            i, h = stack.pop()
            max_height = max(max_height, (len(heights)-i)*h)
        return max_height
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        curr_row = list(map(int, matrix[0]))
        max_area = self.largestRectangleArea(curr_row)
        for r in range(1, len(matrix)):
            for c in range(len(matrix[0])):
                curr_row[c] = curr_row[c] + int(matrix[r][c]) if int(matrix[r][c]) else 0
            max_area = max(max_area, self.largestRectangleArea(curr_row))
        return max_area