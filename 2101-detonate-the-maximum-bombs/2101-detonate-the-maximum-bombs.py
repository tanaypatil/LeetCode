class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(bombs)
        
        def get_dist(x1, y1, x2, y2):
            return ((x2-x1)**2 + (y2-y1)**2)
        
        def dfs(i):
            visited[i] = True
            v = 0
            for j in adj[i]:
                if not visited[j]:
                    v += dfs(j)
            return 1+v
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    if get_dist(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1]) <= bombs[i][2]**2:
                        adj[i].append(j)           
        ans = 0
        
        for i in range(n):
            visited = defaultdict(bool)
            ans = max(ans, dfs(i))
                
        return ans
        