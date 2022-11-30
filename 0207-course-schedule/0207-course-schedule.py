class Solution:
    adjl = []
    visited = {}
    recStack = {}
    
    def dfs(self, node):
        Solution.visited[node] = True
        Solution.recStack[node] = True
        
        for i in Solution.adjl[node]:
            if not Solution.visited[i]:
                if self.dfs(i):
                    return True
            elif Solution.recStack[i]:
                return True
        Solution.recStack[node] = False
        return False
    
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        Solution.adjl = defaultdict(list)
        for p in prerequisites:
            Solution.adjl[p[0]].append(p[1])
            
        print(Solution.adjl)
        Solution.visited = defaultdict(bool)
        Solution.recStack = defaultdict(bool)
        
        for i in range(numCourses):
            if not Solution.visited[i]:
                if self.dfs(i):
                    return False
        return True