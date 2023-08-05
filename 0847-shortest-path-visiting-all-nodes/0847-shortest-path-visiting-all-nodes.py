class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        W = [[float("inf")] * n for _ in range(n)]
        #for i in range(n): W[i][i] = 0
        for i in range(n):
            for j in graph[i]:
                W[i][j] = 1
        
        for i,j,k in product(range(n), repeat = 3):
            W[i][j] = min(W[i][j], W[i][k] + W[k][j])
                    
        dp = [[float("inf")] * n for _ in range(1<<n)]
        for i in range(n): dp[1<<i][i] = 0
            
        for mask in range(1<<n):
            n_z_bits = [j for j in range(n) if mask&(1<<j)]
            
            for j, k in permutations(n_z_bits, 2):
                cand = dp[mask ^ (1<<j)][k] + W[k][j]
                dp[mask][j] = min(dp[mask][j], cand)

        return min(dp[-1])