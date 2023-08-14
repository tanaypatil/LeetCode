class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        visited = defaultdict(bool)
        rec = defaultdict(bool)
        n = len(colors)
        
        def is_cycle(i):
            visited[i] = True
            rec[i] = True
            for j in adj[i]:
                if not visited[j] and is_cycle(j):
                    return True
                elif rec[j]:
                    return True
            rec[i] = False
            return False
        
        @lru_cache(None)
        def dfs(i):
            visited[i] = True
            cv = Counter()
            for j in adj[i]:
                if not visited[j]:
                    child = dfs(j)
                    for k, v in child.items():
                        cv[k] = max(v, cv[k])
            visited[i] = False
            cv[colors[i]] += 1
            return cv.copy()
        
        ans = 0
        for i in range(n):
            if not visited[i]:
                if is_cycle(i):
                    return -1
        
        visited = defaultdict(bool)
        for i in range(n):
            if not visited[i]:
                cv = dfs(i)
                ans = max(ans, max(cv.values()))
        return ans
        
        