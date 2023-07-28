class Solution:
    def dfs(self, i, s, adj, visited):
        visited[i] = True
        children = ['', '']
        for j in adj[i]:
            if not visited[j]:
                child_path = self.dfs(j, s, adj, visited)
                if child_path[-1] != s[i]:
                    if len(child_path) > len(children[0]):
                        children[1] = children[0]
                        children[0] = child_path
                    elif len(child_path) > len(children[1]):
                        children[1] = child_path
        
        Solution.max_path = max(Solution.max_path, len(children[0]+children[1])+1)
        
        return children[0]+s[i]
                
        
    def longestPath(self, parent: List[int], s: str) -> int:
        adj = defaultdict(list)
        visited = defaultdict(bool)
        
        for u, v in enumerate(parent):
            if u != 0:
                adj[u].append(v)
                adj[v].append(u)
            
        Solution.max_path = 0
        
        self.dfs(0, s, adj, visited)
        
        return Solution.max_path
        
        