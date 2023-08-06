class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        adj = defaultdict(list)
        indegrees = [0]*n
        for pre, cur in relations:
            indegrees[cur-1] += 1
            adj[pre-1].append(cur-1)
            
        # print(indegrees, adj)
        # return 0
            
        @lru_cache(None)
        def dp(mask, indegs):
            if mask == (1<<n)-1: return 0
            
            nodes = [i for i in range(n) if not indegs[i] and not (mask & 1<<i)]
            
            ans = float('inf')
            for k_nodes in combinations(nodes, min(k, len(nodes))):
                new_mask, new_indegs = mask, list(indegs)
                
                for node in k_nodes:
                    new_mask ^= 1<<node
                    for j in adj[node]:
                        new_indegs[j] -= 1
                ans = min(ans, 1 + dp(new_mask, tuple(new_indegs)))
                
            return ans
        
        return dp(0, tuple(indegrees))