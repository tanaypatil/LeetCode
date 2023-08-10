class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = defaultdict(bool)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mod = 10**9+7
        
        @lru_cache(None)
        def dfs(i, j):
            visited[(i, j)] = True    
            paths = 1
            for di, dj in moves:
                r, c = i+di, j+dj
                if 0 <= r < m and 0 <= c < n and not visited[(r, c)] and grid[r][c] > grid[i][j]:
                    paths += dfs(r, c)
            visited[(i, j)] = False
            return paths%mod
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dfs(i, j)
        return ans%mod
        