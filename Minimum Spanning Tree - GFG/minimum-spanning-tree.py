#User function Template for python3
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        visited = defaultdict(bool)
        ans = 0
        
        adjl = defaultdict(list)
        
        heap = [(0,0,-1)]
        edges = []
        
        while heap:
            wt, curr, parent = heappop(heap)
            if visited[curr]:
                continue
            ans += wt
            visited[curr] = True
            if parent != -1:
                edges.append((curr, parent))
            for j, w in adj[curr]:
                if j != curr and w and not visited[j]:
                    heappush(heap, (w, j, curr))
                    
        return ans
            
            
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends