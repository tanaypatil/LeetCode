class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        
        def dfs(i, j):
            grid[i][j] = 2
            q.append((i, j, 0))
            for di, dj in moves:
                r, c = i+di, j+dj
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    dfs(r, c)
        f = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    f = 1
                    break
            if f: break
        
        ans = float('inf')
        visited = defaultdict(bool)
        while q:
            i, j, d = q.popleft()
            visited[(i, j)] = True
            if grid[i][j] == 1:
                ans = min(ans, d)
                continue
            for di, dj in moves:
                r, c = i+di, j+dj
                if 0 <= r < m and 0 <= c < n and grid[r][c] != 2 and not visited[(r, c)]:
                    q.append((r, c, d+1 if not grid[r][c] else d))
                    visited[(r, c)] = True
        
        return ans
        
        
        
        