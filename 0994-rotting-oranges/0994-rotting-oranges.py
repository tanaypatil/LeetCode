class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, q = 0, deque()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        def move(i, j):
            moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in moves:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                    yield r, c

        time = 0
        while q:
            s = len(q)
            for _ in range(s):
                i, j = q.popleft()
                grid[i][j] = 0
                for x, y in move(i, j):
                    fresh -= 1
                    grid[x][y] = 0
                    q.append((x, y))

            if q:
                time += 1

        return time if not fresh else -1