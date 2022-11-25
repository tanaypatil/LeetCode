from collections import defaultdict, deque

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
        if not V:
            return False
        if not adj:
            return False
        
        visited = defaultdict(bool)
        for i in range(V):
            if not visited[i]:
                q = deque({(i, -1)})
                while q:
                    vertex, parent = q.popleft()
                    visited[vertex] = True
                    for v in adj[vertex]:
                        if not visited[v]:
                            q.append((v, vertex))
                        elif v != parent:
                            return True
                        
        return False


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
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends