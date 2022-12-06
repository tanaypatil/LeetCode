class Solution:
    
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        if not roads:
            return 1
        
        adj = defaultdict(dict)
        
        for src, dest, time in roads:
            adj[src][dest] = time
            adj[dest][src] = time
        
        times = [float('inf')]*n
        times[0] = 0
        heap = [(0, 0)]
        min_time = float('inf')
        
        ways = [0]*n
        ways[0] = 1
        MOD = 10**9+7
        while heap:
            time, city = heappop(heap)
            for c, t in adj[city].items():
                if t + time < min_time and t+time < times[c]:
                    times[c] = t+time
                    heappush(heap, (times[c], c))
                    ways[c] = ways[city]%MOD
                elif times[c] == t+time:
                    ways[c] = (ways[c]%MOD + ways[city]%MOD)%MOD
                    
        return ways[n-1]%MOD
        
        
        
        