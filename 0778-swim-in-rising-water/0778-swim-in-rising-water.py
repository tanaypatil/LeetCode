class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        heap = [(grid[0][0], 0, 0)]
        
        ma = float('-inf')
        n = len(grid)
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited = defaultdict(bool)
        visited[(0, 0)] = True
        
        while heap:
            v, i, j = heappop(heap)
            if i == n-1 and j == n-1:
                ma = max(ma, v)
                return ma
            ma = max(ma, v)
            for x, y in moves:
                r, c = i+x, j+y
                if 0 <= r < n and 0 <= c < n and not visited[(r, c)]:
                    heappush(heap, (grid[r][c], r, c))
                    visited[(r, c)] = True
                    
        return ma if ma != float('-inf') else -1
        