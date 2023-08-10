class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]: 
        n = len(graph)
        paths = set()
        
        def dfs(i, path):
            if i == n-1:
                paths.add(tuple(path+[n-1]))
                return
            for j in graph[i]:
                dfs(j, path+[i])
                
        dfs(0, [])
        return paths