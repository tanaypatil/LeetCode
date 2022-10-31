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
        # print(heights, max_area)
        return max_area
    
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        n, m = len(mat), len(mat[0])
        # max_area = 0
        # for i in range(n):
        #     for j in range(n):
        #         arr = [0]*(m-j)
        #         # print(arr)
        #         # max_area = max(max_area, self.kadane(arr))
        #         for k in range(i, n):
        #             c = 0
        #             s = 0
        #             gs = 0
        #             for p in range(j, m):
        #                 # print(i, j, k, p)
        #                 arr[c] = 0 if (not int(mat[k][p]) or not arr[c]) and k != i else int(mat[k][p]) + arr[c]
        #                 s = 0 if not arr[c] else s+arr[c]
        #                 gs = max(gs, s)
        #                 c += 1
        #             max_area = max(max_area, gs)
        #             # print(i, j, k, arr)
        # return max_area
        max_area = 0
        height = [0]*(m)
        for row in mat:
            for j in range(m):
                height[j] = height[j]+1 if row[j] == "1" else 0
            max_area = max(max_area, self.largestRectangleArea(height))
        return max_area
            
        