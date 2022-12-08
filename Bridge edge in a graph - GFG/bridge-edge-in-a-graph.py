#User function Template for python3
from collections import defaultdict


class Solution:
    def dfs(self, u):
        Solution.visited[u] = True
        for v in Solution.adj[u]:
            if not Solution.visited[v]:
                self.dfs(v)
                
    
    #Function to find if the given edge is a bridge in graph.
    def isBridge(self, V, adjl, c, d):
        # code here
        adj = defaultdict(set)
        for i in range(len(adjl)):
            for j in adjl[i]:
                adj[i].add(j)
                adj[j].add(i)
        
        if d in adj[c]:
            adj[c].remove(d)
        if c in adj[d]:
            adj[d].remove(c)
        
        Solution.adj = adj
        Solution.visited = defaultdict(bool)
        
        both = 0
        
        for i in range(V):
            if not Solution.visited[i]:
                self.dfs(i)
                if Solution.visited[c] and Solution.visited[d]:
                    return 0
                elif Solution.visited[c] or Solution.visited[d]:
                    return 1
        return 0
        

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
            adj[b].append(a)
            
        for i in range(V):
            adj[i] = list(OrderedDict.fromkeys(adj[i])) 
            
        c,d=map(int,input().split())
        ob = Solution()
        
        print(ob.isBridge(V, adj, c,d))
# } Driver Code Ends