class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        def dfs(i, j):
            grid[i][j] = 2
            for di, dj in moves:
                r, c = i+di, j+dj
                if 0 <= r < m and 0 <= c < n and not grid[r][c]:
                    dfs(r, c)
        
        for i in range(m):
            for j in [0, n-1]:
                if not grid[i][j]:
                    dfs(i, j)
                    
        for j in range(n):
            for i in [0, m-1]:
                if not grid[i][j]:
                    dfs(i, j)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    dfs(i, j)
                    ans += 1
                    
        return ans
        