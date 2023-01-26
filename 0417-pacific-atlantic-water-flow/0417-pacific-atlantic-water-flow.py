class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, opt):
            visited[(r, c)] = True
            if opt == 1:
                nodes1.add((r, c))
            if opt == 2:
                nodes2.add((r, c))
            for dr, dc in steps:
                i, j = r+dr, c+dc
                if 0 <= i < n and 0 <= j < m and not visited[(i, j)] and heights[i][j] >= heights[r][c]:
                    dfs(i, j, opt)    
        
        if not heights:
            return []
        
        n, m = len(heights), len(heights[0])
        ans = set()
        mem = {}
        steps = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        nodes1, nodes2 = set(), set()
        visited = defaultdict(bool)
        
        for i in range(n):
            if not visited[(i, 0)]:
                dfs(i, 0, 1)
                
        for j in range(m):
            if not visited[(0, j)]:
                dfs(0, j, 1)
                
        # print(nodes1)
        
        visited = defaultdict(bool)
        for i in range(n):
            if not visited[(i, m-1)]:
                dfs(i, m-1, 2)

        for j in range(m):
            if not visited[(n-1, j)]:
                dfs(n-1, j, 2)
                
        # print(nodes2)
        
        return nodes1.intersection(nodes2)
        
                