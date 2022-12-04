from heapq import heapify, heappush, heappop
from collections import defaultdict


class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adjl, S):
        #code here
        pq = []
        
        ret = [float('inf')]*V
        
        adj = defaultdict(list)
        
        for i, edges in enumerate(adjl):
            for v, w in edges:
                adj[i].append((w, v))
                
        ret[S] = 0
        
        heappush(pq, (0, S))
        
        while pq:
            weight, vertex = heappop(pq)
            for w, v in adj[vertex]:
                if ret[v] > w + weight:
                    ret[v] = w + weight
                    heappush(pq, (ret[v], v))
                    
        for i in range(V):
            if ret[i] == float('inf'):
                ret[i] = -1
                
        return ret


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends