class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)
        for k, v in adj.items():
            adj[k] = sorted(adj[k], reverse=True)
        ans = []
        
        def dfs(city):
            while adj[city]:
                j = adj[city].pop()
                dfs(j)
            ans.append(city)
            
        dfs("JFK")
        return ans[::-1]
                    