from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        n = len(isConnected)
        edges = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    edges[i].append(j)
        
        visited = defaultdict(bool)
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                q = deque({i})
                while q:
                    v = q.popleft()
                    visited[v] = True
                    for j in edges[v]:
                        if not visited[j]:
                            q.append(j)
        return count