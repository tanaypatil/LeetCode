class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def next(i, j):
            moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            for di, dj in moves:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n and grid[r][c]:
                    yield r, c
                    
        def dfs(i, j):
            ans = grid[i][j]
            grid[i][j] = 0
            for r, c in next(i, j):
                ans += dfs(r, c)
            return ans
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans
        