class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def move(i, j):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj] == 1:
                    yield i+di, j+dj
        
        def dfs(i, j):
            grid[i][j] = 2
            p = 0
            for r, c in move(i, j):
                p += dfs(r, c)
            return 1+p
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans