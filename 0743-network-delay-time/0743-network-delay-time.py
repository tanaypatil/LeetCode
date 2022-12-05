class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return -1
        
        dist = [float('inf')]*n
        dist[k-1] = 0
        
        heap = [(0, k-1)]
        adj = defaultdict(dict)
        for s, t, w in times:
            adj[s-1][t-1] = w
        while heap:
            we, p = heappop(heap)
            for t, w in adj[p].items():
                if dist[t] > w + we:
                    dist[t] = w + we
                    heappush(heap, (dist[t], t))
                    
        for i in range(n):
            if dist[i] == float('inf'):
                return -1
                
        return max(dist)
        