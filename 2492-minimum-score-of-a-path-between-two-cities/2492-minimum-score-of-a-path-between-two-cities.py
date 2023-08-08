class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(lambda: defaultdict(int))
        for u, v, w in roads:
            adj[u-1][v-1] = w
            adj[v-1][u-1] = w
        
        ans = float('inf')
        visited = defaultdict(bool)
        
        q = deque({(0, float('inf'))})
        
        while q:
            node, min_dist = q.popleft()
            visited[node] = True    
            ans = min(ans, min_dist)
            for j in adj[node]:
                if not visited[j]:
                    q.append((j, adj[node][j]))
                    
        return ans
                    
                