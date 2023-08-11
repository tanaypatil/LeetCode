class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n =  len(land), len(land[0])
        moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        visited = defaultdict(bool)
        
        def dfs(i, j, k):
            visited[(i, j)] = True
            k[0], k[1], k[2], k[3] = min(k[0], i), min(k[1], j), max(k[2], i), max(k[3], j)
            for di, dj in moves:
                r, c = i + di, j + dj
                if 0 <= r < m and 0 <= c < n and not visited[(r, c)] and land[r][c]:
                    dfs(r, c, k)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if not visited[(i, j)] and land[i][j]:
                    k = [float('inf'), float('inf'), float('-inf'), float('-inf')]
                    dfs(i, j, k)
                    ans.append(tuple(k))
        return ans
            
            
        