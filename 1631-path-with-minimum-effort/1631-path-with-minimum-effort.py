class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        rows, cols = len(heights), len(heights[0])
        if rows == 1 and cols == 1:
            return 0
        
        # q = deque({(0, 0, -1)})
        # visited = defaultdict(bool)
        
        heap = [(0, 0, 0)]
        
        r = [-1, 1, 0, 0]
        c = [0, 0, -1, 1]
        # ans = float('inf')
        dist = [[float('inf')]*cols for _ in range(rows)]
        while heap:
            eff, row, col = heappop(heap)
            if row == rows-1 and col == cols-1:
                return eff
            for i in range(4):
                x, y = r[i] + row, c[i] + col
                if 0 <= x < rows and 0 <= y < cols:
                    diff = max(eff, abs(heights[x][y]-heights[row][col]))
                    if dist[x][y] > diff:
                        dist[x][y] = diff
                        heappush(heap, (diff, x, y))
                        
        return -1
            
            
#             s = len(q)
#             for _ in range(s):
#                 row, col, eff = q.popleft()
#                 if row == rows-1 and col == cols-1:
#                     ans = min(ans, eff)
#                     continue
#                 if visited[(row, col, eff)]: continue
#                 if eff >= ans: continue
#                 visited[(row, col, eff)] = True
                
#         return -1 if ans == float('inf') else ans