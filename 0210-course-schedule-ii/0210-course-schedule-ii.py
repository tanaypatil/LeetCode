class Solution:
    visited = {}
    adj = {}
    ret = []
    
    def topo(self, node):
        Solution.visited[node] = True
        
        for i in Solution.adj[node]:
            if not Solution.visited[i]:
                self.topo(i)
        
        Solution.ret.append(node)
        
    def dfs(self, node):
        Solution.visited[node] = True
        Solution.recStack[node] = True
        
        for i in Solution.adj[node]:
            if not Solution.visited[i]:
                if self.dfs(i):
                    return True
            elif Solution.recStack[i]:
                return True
        Solution.recStack[node] = False
        return False
    
    def hasCycle(self, n):
        for i in range(n):
            if not Solution.visited[i]:
                if self.dfs(i):
                    return True
        return False
    
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        Solution.visited = defaultdict(bool)
        Solution.recStack = defaultdict(bool)
        Solution.adj = defaultdict(list)
        Solution.ret = []
        
        for p in pre:
            Solution.adj[p[0]].append(p[1])
        
        if self.hasCycle(numCourses):
            return []
        
        Solution.visited = defaultdict(bool)
        
        for i in range(numCourses):
            if not Solution.visited[i]:
                self.topo(i)
                
        return Solution.ret