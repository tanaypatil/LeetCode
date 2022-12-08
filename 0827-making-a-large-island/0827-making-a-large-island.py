class Solution:
    def dfs(self, grid):
        if not grid:
            return 0
        
        visited = defaultdict(bool)
        
        q = deque()
        n = len(grid)
        index = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] and not visited[(i, j)]:
                    index += 1
                    q = deque({(i, j)})
                    co = 0
                    while q:
                        r, c = q.popleft()
                        if visited[(r, c)]: continue
                        grid[r][c] = index
                        co += 1
                        visited[(r, c)] = True
                        for a, b in self.move(r, c, n):
                            if not visited[(a, b)] and grid[a][b]:
                                q.append((a, b))
                    Solution.areas[index] = co
    
    def move(self, x, y, N):
        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= x + i < N and 0 <= y + j < N:
                yield x + i, y + j

    
    def largestIsland(self, grid: List[List[int]]) -> int:
        m = 0
        c = 0
        res = 0
        Solution.areas = defaultdict(int)
        self.dfs(grid)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if not grid[i][j]:
                    c += 1
                    possible = set(grid[x][y] for x, y in self.move(i, j, len(grid)))
                    res = max(res, sum(Solution.areas[index] for index in possible) + 1)
        return res if c else max(Solution.areas.values())
        