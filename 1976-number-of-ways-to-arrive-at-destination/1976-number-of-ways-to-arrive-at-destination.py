class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))
            
        heap = [(0, 0)]
        ways = [0]*n
        ways[0] = 1
        dist = [float('inf')]*n
        dist[0] = 0
        while heap:
            time, road = heappop(heap)
            for nex, t in adj[road]:
                if t + time < dist[nex]:
                    dist[nex] = t + time
                    ways[nex] = ways[road]
                    heappush(heap, (t+time, nex))
                elif t + time == dist[nex]:
                    ways[nex] += ways[road]
        return ways[n-1]%(10**9+7)
        