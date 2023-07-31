class Solution:
    def dfs(self, i, j, empty):
        if i == self.endr and j == self.endc:
            # print(empty, self.req, self.visited)
            if empty >= self.req:
                self.ans += 1
            return
        if self.visited[(i, j)]:
            return
        self.visited[(i, j)] = True
        for di, dj in self.moves:
            r, c = i+di, j+dj
            if 0 <= r < self.m and 0 <= c < self.n and self.grid[r][c] != -1:
                self.dfs(r, c, empty+1)
        self.visited[(i, j)] = False
        
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.m, self.n = len(grid), len(grid[0])
        start, end = None, None
        self.req = 1
        self.visited = defaultdict(bool)
        self.ans = 0
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == 0:
                    self.req += 1
                    
        self.grid = grid
        self.endr, self.endc = end
        self.dfs(start[0], start[1], 0)
        
        return self.ans
                    