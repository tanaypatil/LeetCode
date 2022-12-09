#User function Template for python3
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

class Solution:
    def dfs(self, u):
        Solution.visited[u] = True
        Solution.disc[u] = Solution.low[u] = Solution.time
        Solution.time += 1
        children = 0
        for v in Solution.adj[u]:
            if not Solution.visited[v]:
                children += 1
                Solution.parent[v] = u
                self.dfs(v)
                Solution.low[u] = min(Solution.low[u], Solution.low[v])
                
                if (Solution.parent[u] != -1 and Solution.low[v] >= Solution.disc[u]) or (Solution.parent[u] == -1 and children > 1):
                    Solution.ret.add(u)
            elif v != Solution.parent[u]:
                Solution.low[u] = min(Solution.low[u], Solution.disc[v])
                

    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        Solution.visited = defaultdict(bool)
        Solution.ret = set()
        Solution.disc = [float('inf')]*V
        Solution.low = [float('inf')]*V
        Solution.parent = [-1]*V
        Solution.time = 0
        
        Solution.adj = adj
        
        for i in range(V):
            if not Solution.visited[i]:
                self.dfs(i)
                
        return sorted(list(Solution.ret)) if Solution.ret else [-1]
    
#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		ob = Solution()
		ans = ob.articulationPoints(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends