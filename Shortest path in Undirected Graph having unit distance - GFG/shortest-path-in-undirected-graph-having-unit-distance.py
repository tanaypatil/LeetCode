#User function Template for python3
from collections import deque, defaultdict


class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        q = deque({(src, 0)})
        ret = [float('inf')]*n
        ret[src] = 0
        visited = defaultdict(bool)
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        while q:
            node, dist = q.popleft()
            visited[node] = True
            for i in adj[node]:
                if not visited[i]:
                    ret[i] = min(ret[i], 1+dist)
                    q.append((i, ret[i]))
        for i in range(n):
            if ret[i] == float('inf'):
                ret[i] = -1
        return ret
                
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends