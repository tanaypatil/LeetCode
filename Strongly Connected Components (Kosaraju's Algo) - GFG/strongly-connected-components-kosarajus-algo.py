#User function Template for python3
from collections import defaultdict


class Solution:
    def dfs(self, u):
        Solution.visited[u] = True
        Solution.temp.append(u)
        for v in Solution.adjl[u]:
            if not Solution.visited[v]:
                self.dfs(v)
    
    def fill(self, u):
        Solution.visited[u] = True
        for v in Solution.adj[u]:
            if not Solution.visited[v]:
                self.fill(v)
        Solution.stack.append(u)

    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        Solution.visited = defaultdict(bool)
        Solution.adj = adj
        Solution.stack = []
        
        for i in range(V):
            if not Solution.visited[i]:
                self.fill(i)
                
        adjl = defaultdict(list)
        
        for i, vs in enumerate(adj):
            for v in vs:
                adjl[v].append(i)
                
        Solution.adjl = adjl
        
        Solution.visited = defaultdict(bool)
        ret = []
        while Solution.stack:
            i = Solution.stack.pop()
            if not Solution.visited[i]:
                Solution.temp = []
                self.dfs(i)
                ret.append(Solution.temp)
                
        return len(ret)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends