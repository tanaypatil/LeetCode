class Solution:
    def dfs(self, i):
        Solution.visited[i] = True
        children = ['', '']
        for j in Solution.adj[i]:
            if not Solution.visited[j]:
                child_path = self.dfs(j)
                if child_path[-1] != Solution.word[i]:
                    if len(child_path) > len(children[0]):
                        children[1] = children[0]
                        children[0] = child_path
                    elif len(child_path) > len(children[1]):
                        children[1] = child_path
        
        Solution.max_path = max(Solution.max_path, len(children[0]+children[1])+1)
        
        return children[0]+Solution.word[i]
                
        
    def longestPath(self, parent: List[int], s: str) -> int:
        Solution.word = s
        adj = defaultdict(list)
        Solution.visited = defaultdict(bool)
        
        for u, v in enumerate(parent):
            if u != 0:
                adj[u].append(v)
                adj[v].append(u)
            
        Solution.adj = adj
        Solution.max_path = 0
        
        self.dfs(0)
        
        return Solution.max_path
        
        